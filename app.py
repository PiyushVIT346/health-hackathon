import os
import numpy as np
from flask import Flask, request, render_template, jsonify, redirect, url_for, flash, session
from tensorflow.keras.models import load_model
import sqlite3
import tensorflow as tf
import json
from dotenv import load_dotenv
import google.generativeai as genai
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message

import gdown
if not os.path.exists("braintumor.h5"):
    gdown.download("https://drive.google.com/drive/folders/1a689Slu-nRyqU9nflIMg7hK08Mz0mmis", "braintumor.h5", quiet=False)

if not os.path.exists("CT_scan_model_fixed.h5"):
    gdown.download("https://drive.google.com/drive/folders/1a689Slu-nRyqU9nflIMg7hK08Mz0mmis", "CT_scan_model_fixed.h5", quiet=False)

if not os.path.exists("XRay_model.h5"):
    gdown.download("https://drive.google.com/drive/folders/1a689Slu-nRyqU9nflIMg7hK08Mz0mmis", "XRay_model.h5", quiet=False)



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
app.secret_key = os.urandom(24)

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



@app.route('/')
def home():
    return render_template('page.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get('password')

        with sqlite3.connect('example.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users2 WHERE email = ? AND password = ?', (email, password))
            user = cursor.fetchone()

        if user:
            session['email'] = email
            flash('Login successful!', 'success')
            return redirect(url_for('success'))
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('login2.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if not name or not email or not password:
            flash('All fields are required.', 'danger')
            return redirect(url_for('register'))

        try:
            with sqlite3.connect('example.db') as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO users2 (name, email, password) VALUES (?, ?, ?)', (name, email, password))
                conn.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('home'))
        except sqlite3.IntegrityError:
            flash('This email is already registered.', 'danger')

    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('select.html')

#-------------------------------------------------------------------------------------------------------------------------------#
doctype_model = load_model("medical_image_classifier.h5",compile=False)
xray_model = load_model("XRay_model.h5",compile=False)
mri_model = load_model("braintumor.h5",compile=False)
ct_model = load_model("CT_scan_model_fixed.h5",compile=False)

# Define class labels for each model
#DOCTYPE_LABELS = ["X-ray", "MRI", "CT"]
DOCTYPE_LABELS = ["CT", "MRI", "X-ray"]
XRAY_LABELS = ["Fracture", "No Fracture"]
MRI_LABELS = ["glioma", "meningioma", "no tumor", "pituitary"]
CT_LABELS = ["squamous carcinoma left hilum", "normal","large carcinoma left hilum","adenocarcinoma left lower lobe"]

FIRST_AID_PRECAUTIONS = {
    # X-ray Labels
    "Fracture": "Immobilize the affected area, apply a splint if possible, and seek immediate medical attention.",
    "No Fracture": "No immediate intervention required. If pain persists, consult a doctor for further evaluation.",

    # MRI Labels
    "glioma": "Seek specialized medical evaluation immediately. Avoid strenuous activities until you consult a neurologist.",
    "meningioma": "Consult with a neurologist/neurosurgeon promptly for further evaluation and management.",
    "no tumor": "No immediate action required. Maintain a healthy lifestyle and schedule regular check-ups.",
    "pituitary": "Follow up with an endocrinologist or neurospecialist for detailed evaluation and management.",

    # CT Labels
    "squamous carcinoma left hilum": "Seek immediate care from an oncologist. Follow prescribed treatments and avoid smoking or irritants.",
    "normal": "No action required. Continue maintaining a healthy lifestyle and regular medical check-ups.",
    "large carcinoma left hilum": "Urgently consult with a pulmonologist or oncologist. Avoid strenuous activities and adhere strictly to medical advice.",
    "adenocarcinoma left lower lobe": "Consult an oncologist immediately. Follow the recommended treatment plan and monitor your condition closely."
}


def preprocess_image(img_path, target_size):
    img = image.load_img(img_path, target_size=target_size, color_mode="rgb")
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

@app.route("/predict")
def predict():
    return render_template("predict.html")

@app.route('/upload', methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        # Predict document type
        img_array = preprocess_image(file_path, (224, 224))
        doc_pred = doctype_model.predict(img_array)
        doc_class_idx = np.argmax(doc_pred)
        doc_class = DOCTYPE_LABELS[doc_class_idx]

        # Select the corresponding model
        if doc_class == "X-ray":
            selected_model = xray_model
            labels = XRAY_LABELS
        elif doc_class == "MRI":
            selected_model = mri_model
            labels = MRI_LABELS
        elif doc_class == "CT":
            selected_model = ct_model
            labels = CT_LABELS
        else:
            return jsonify({"error": "Unknown document type"}), 400

        target_size = (selected_model.input_shape[1], selected_model.input_shape[2])
        img_array = preprocess_image(file_path, target_size)

        final_pred = selected_model.predict(img_array)
        final_class_idx = np.argmax(final_pred)
        final_class = labels[final_class_idx]
        first_aid_precaution = FIRST_AID_PRECAUTIONS.get(final_class, "No specific precaution available.")

        # Update user history
        if 'email' in session:
            update_user_history(session['email'], doc_class, final_class)

        return jsonify({"document_type": doc_class, "classification": final_class, "first_aid": first_aid_precaution})

#---------------------------------------------------------------------------------------------------------------------------------#



@app.route('/feedback')
def feedback():
    return render_template('feedback.html')
#brze knkm ojqb wkmf

@app.route('/contact')
def contact():
    return render_template('contact.html')


def init_db():
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            history TEXT DEFAULT '[]'
        )
        ''')
        conn.commit()

init_db()
import datetime
def update_user_history(email, doc_type, prediction):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT history FROM users2 WHERE email = ?", (email,))
        result = cursor.fetchone()

        history = json.loads(result[0]) if result and result[0] else []
        history.insert(0, {"doc_type": doc_type, "prediction": prediction, "timestamp": timestamp})
        history = history[:10]

        cursor.execute("UPDATE users2 SET history = ? WHERE email = ?", (json.dumps(history), email))
        conn.commit()

@app.route('/history')
def view_history():
    if 'email' not in session:
        flash('You must be logged in to view your history.', 'danger')
        return redirect(url_for('login'))

    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT history FROM users2 WHERE email = ?", (session['email'],))
        result = cursor.fetchone()
        history = json.loads(result[0]) if result and result[0] else []
    return render_template('history.html', history=history)


@app.route('/assistant', methods=['GET', 'POST'])
def assistant():
    if 'history' not in session:
        session['history'] = []
    prompt="""You are a health hub chatbot. User will tell about the symptom he is facing. Answer like a doctor. provide the possible 
              solution to heal. provide the possible cause of the symptom. provide consultancy. act like doctor and also try to fetch more 
              data and symptomps related to disease.provide lines in form of points/bullet that will be easy to read and more attractive. 
    """
    
    if request.method == 'POST':
        question = request.form.get('message')
        if question:
            try:
                model = genai.GenerativeModel("gemini-pro")
                response = model.generate_content([prompt[0], question])
                session['history'].insert(0, {
                    'user': question,
                    'gem': response.text,
                    'user_color': 'blue',
                    'gem_color': '#f5f5f5'
                })
                session['history'] = session['history'][:10]
            except Exception as e:
                session['history'].insert(0, {
                    'user': question,
                    'gem': f'An error occurred: {e}',
                    'user_color': 'blue',
                    'gem_color': 'red'
                })

    return render_template('chat_index.html', history=session.get('history', []))


@app.route('/chartPlaner')
def chartPlaner():
    return render_template('chartPlaner.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    diseases = data.get("diseases", [])
    food_preference = data.get("food_preference", "Not Specified")
    disease_info=" "
    food_info=" "
    print("Diseases submitted by the user:", diseases)
    print("Food preference submitted:", food_preference)

    prompt_base = (
        "You are a health hub chatbot. The user has provided their health conditions and indian food preference. "
        "Answer like a doctor. Provide possible solutions, likely causes, and consultancy advice. "
        "Present your answer as a complete HTML snippet that includes a table. "
        "The table must have columns for each day of the week (Monday to Sunday) and rows for Breakfast, Lunch, Snack, and Dinner. "
        "Below the table, list possible causes, likely causes, and consultancy advice in different bullet points clearly and attractive taking much space needed separated. "
        "Now, based on the following details, please generate a personalized food planner chart."
        "Also show the food that are in table that how are they beneficaly for the disease that user is facing"
        "Strongly follow the Food Preference which user is giving."
    )
    disease_info = "Diseases: " + (", ".join(diseases) if diseases else "None specified")
    food_info = "Food Preference: " + food_preference
    final_prompt = f"{prompt_base}\n{disease_info}\n{food_info}\nPrefer food based on Food Preference only. Strongly follow food preferance type."
    print(final_prompt)
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content([final_prompt])
        print(response)
        food_chart = response.text
    except Exception as e:
        food_chart = f"<p>Error generating chart: {str(e)}</p>"
    print(food_chart)
    return jsonify({
        "message": "Data recorded and dynamic chart generated successfully!",
        "food_chart": food_chart
    })

if __name__ == '__main__':
    app.run(debug=True)
