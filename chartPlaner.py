from dotenv import load_dotenv
import google.generativeai as genai
import os
from flask import Flask, request, render_template, jsonify

# Load environment variables and configure the Gemini API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)
app.secret_key = "p1i2y3u4s5h6"

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

    # Prepare the dynamic prompt for the Gemini model
    prompt_base = (
        "You are a health hub chatbot. The user has provided their health conditions and food preference. "
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
    # Dynamically generate the food planner chart using Gemini
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
