# 🏥 Health Hub AI

> **AI-powered healthcare assistance platform for medical image analysis, symptom assistance, personalized food planning, and health-history tracking.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?logo=tensorflow)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-Generative%20AI-4285F4?logo=google)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![Gunicorn](https://img.shields.io/badge/Gunicorn-WSGI-green)
![Render](https://img.shields.io/badge/Deployment-Render-purple)

---

## 📌 Overview

**Health Hub AI** is an AI-powered healthcare web application designed to provide users with a centralized platform for preliminary health analysis and assistance.

The application combines **deep-learning-based medical image classification** with **Generative AI** to provide several healthcare-oriented capabilities through a single web interface.
## 🏥 Health Hub AI

![Health Hub AI](https://github.com/PiyushVIT346/health-hackathon/blob/main/health.jpg)
The platform can automatically identify the type of uploaded medical image and route it to the appropriate specialized deep-learning model. It currently supports:

* 🩻 X-ray analysis
* 🧠 MRI brain-tumor classification
* 🫁 CT-scan classification
* 🤖 AI-powered health assistant
* 🍱 Personalized food and diet planner
* 📜 Prediction-history tracking
* 👤 User registration and login
* 💬 AI-generated health guidance

The backend is implemented using **Flask**, while **TensorFlow/Keras** powers the image-classification models and **Google Gemini** provides generative-AI functionality.

---

# 🎯 Problem Statement

Medical information and preliminary health analysis can be difficult to access quickly, especially when users need to understand different types of medical reports, symptoms, or basic health recommendations.

Traditional healthcare workflows may require users to consult different tools for medical-image analysis, symptom-related information, dietary planning, and maintaining previous prediction records.

**Health Hub AI aims to bring these capabilities together into one web-based platform**, providing fast preliminary insights from medical images, AI-assisted symptom conversations, personalized food-planning suggestions, and a history of previous predictions.

> ⚠️ **Important:** This project is intended for educational, research, and preliminary-assistance purposes. Its predictions and AI-generated responses should **not** be considered a medical diagnosis or a replacement for a qualified healthcare professional.

---

# 💡 Why Health Hub AI?

The project was developed to explore how **Artificial Intelligence, Deep Learning, and Generative AI** can be integrated into a healthcare-oriented application.

### Key motivations

* Provide preliminary analysis of medical images.
* Automatically identify the uploaded medical-image type.
* Reduce the need for manually selecting the appropriate prediction model.
* Provide an AI-powered conversational health assistant.
* Generate personalized food-planning suggestions.
* Maintain a history of previous image-analysis results.
* Build a complete end-to-end AI healthcare application.
* Demonstrate deployment of an AI-powered Flask application.

---

# 🚀 Key Features

## 1. 🩺 Medical Image Classification

Users can upload a medical image through the application.

The system first determines whether the uploaded image is:

* X-ray
* MRI
* CT scan

It then automatically selects the corresponding specialized model.

### Pipeline

```text
Uploaded Medical Image
          │
          ▼
┌─────────────────────────┐
│ Medical Image Classifier│
└────────────┬────────────┘
             │
      ┌──────┼───────┐
      ▼      ▼       ▼
     X-ray   MRI     CT
      │      │       │
      ▼      ▼       ▼
 X-ray ML  MRI ML  CT ML
   Model    Model   Model
      │      │       │
      └──────┼───────┘
             ▼
      Final Prediction
             │
             ▼
     Precaution / Guidance
```

---

## 2. 🦴 X-ray Fracture Detection

The X-ray model classifies uploaded X-ray images into:

* `Fracture`
* `No Fracture`

The application also provides a corresponding precautionary message based on the predicted class.

---

## 3. 🧠 MRI Brain-Tumor Classification

The MRI model classifies brain MRI images into:

* `glioma`
* `meningioma`
* `no tumor`
* `pituitary`

The system then provides a corresponding preliminary precaution or recommendation.

---

## 4. 🫁 CT Scan Classification

The CT model supports classification into categories including:

* Squamous carcinoma of the left hilum
* Normal
* Large carcinoma of the left hilum
* Adenocarcinoma of the left lower lobe

The application maps the predicted category to a corresponding preliminary precaution.

---

## 5. 🤖 AI Health Assistant

Health Hub includes a conversational AI assistant powered by **Google Gemini**.

Users can describe symptoms or ask health-related questions.

The assistant is designed to provide:

* Possible causes
* General health information
* Potential solutions
* Consultation suggestions
* Easy-to-read bullet-point responses

The application also maintains a limited conversation history within the user session.

---

## 6. 🍱 Personalized Food Planner

The platform provides an AI-powered food-planning feature.

Users can provide:

* Health conditions/diseases
* Food preferences

The system sends these details to the Generative AI model and generates a personalized weekly food chart.

The generated plan includes:

| Meal         | Schedule        |
| ------------ | --------------- |
| 🍳 Breakfast | Monday → Sunday |
| 🍛 Lunch     | Monday → Sunday |
| 🍎 Snack     | Monday → Sunday |
| 🍽️ Dinner   | Monday → Sunday |

The generated response also contains explanations about how suggested foods may relate to the provided health conditions.

---

## 7. 👤 User Authentication

The application provides basic user authentication using:

* Registration
* Login
* Session management
* SQLite database

User records include:

```text
ID
Name
Email
Password
Prediction History
```

---

## 8. 📜 Prediction History

For authenticated users, the application stores recent medical-image predictions.

Each history entry contains:

```text
Document Type
Prediction
Timestamp
```

The application keeps the latest **10 predictions** for each user.

Example:

```text
MRI
→ glioma
→ 2026-08-19 10:30:45

X-ray
→ Fracture
→ 2026-08-18 15:42:10
```

---

# 🧠 AI/ML Architecture

The project uses a **multi-model classification architecture**.

Instead of using one model for every medical image, a document-type classifier first determines the category of the uploaded image.

```text
                    ┌─────────────────────┐
                    │      User Upload    │
                    └──────────┬──────────┘
                               │
                               ▼
                  ┌────────────────────────┐
                  │ Document Type Classifier│
                  └───────────┬────────────┘
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
          X-Ray              MRI              CT
             │                │                │
             ▼                ▼                ▼
      X-Ray Classifier  MRI Tumor Model  CT Scan Model
             │                │                │
             └────────────────┼────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ Final Prediction │
                    └─────────┬────────┘
                              │
                              ▼
                    First-Aid / Guidance
```

---

# 🔄 Application Workflow

```text
                    ┌───────────────┐
                    │     User      │
                    └───────┬───────┘
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       ▼
           Register/Login          AI Assistant
                │                       │
                ▼                       ▼
          Health Dashboard        Gemini AI
                │
       ┌────────┼─────────┐
       │        │         │
       ▼        ▼         ▼
    Medical   History   Food Planner
     Image       │         │
       │         │         │
       ▼         │         ▼
  Type Detection│      Gemini AI
       │         │         │
       ▼         │         ▼
 Specialized    │    Weekly Food Plan
    Model       │
       │        │
       ▼        │
 Prediction ────┘
```

---

# 🛠️ Tech Stack

## Backend

* **Python**
* **Flask**
* **Gunicorn**

## Machine Learning / Deep Learning

* **TensorFlow**
* **Keras**
* **NumPy**
* **Pillow**

## Generative AI

* **Google Gemini API**
* `google-generativeai`

## Database

* **SQLite**

## Authentication & Sessions

* Flask sessions
* SQLite

## Frontend

* HTML5
* CSS3
* JavaScript
* Jinja2 Templates

## Deployment

* **Render**
* **Gunicorn**

## Model Management

* **gdown**
* Google Drive-hosted model files

The repository's dependency configuration includes Flask, TensorFlow, NumPy, Pillow, Gunicorn, python-dotenv, flask-mail, gdown, and Google's Generative AI SDK.

---

# 📂 Project Structure

```text
health-hackathon/
│
├── app.py
├── requirements.txt
├── Procfile
├── ProcFile
├── render.yaml
├── .gitignore
│
├── templates/
│   ├── page.html
│   ├── index.html
│   ├── login2.html
│   ├── register.html
│   ├── select.html
│   ├── predict.html
│   ├── result.html
│   ├── history.html
│   ├── chat_index.html
│   ├── chartPlaner.html
│   ├── feedback.html
│   └── contact.html
│
└── static/
    ├── CSS files
    ├── JavaScript files
    ├── medical images
    ├── UI assets
    └── application images
```

The repository currently contains dedicated templates for authentication, prediction, history, AI chat, and food planning, along with CSS/JavaScript and image assets in the `static` directory.

---

# 🧩 Core Components

## 1. Flask Application

`app.py` acts as the main backend entry point.

It handles:

* HTTP routes
* Authentication
* File uploads
* Model loading
* Image preprocessing
* Model prediction
* Prediction history
* Gemini API requests
* Food-plan generation
* HTML rendering
* JSON responses

---

## 2. Image Preprocessing

Uploaded images are processed before being passed to the TensorFlow models.

The preprocessing pipeline includes:

```text
Input Image
     │
     ▼
Resize
     │
     ▼
RGB Conversion
     │
     ▼
Convert to NumPy Array
     │
     ▼
Add Batch Dimension
     │
     ▼
Normalize Pixel Values
     │
     ▼
Model Prediction
```

Pixel values are normalized to the range:

```text
0 → 1
```

by dividing the image array by `255`.

---

# 🤖 Model Routing

The application uses the following model-routing logic:

```text
Document Type
│
├── X-ray
│      └── XRay_model.h5
│
├── MRI
│      └── braintumor.h5
│
└── CT
       └── CT_scan_model_fixed.h5
```

An additional model:

```text
medical_image_classifier.h5
```

is used to determine the type of uploaded medical image.

The models are automatically downloaded through `gdown` if they are not present locally.

---

# 🔐 Authentication Flow

```text
User
 │
 ├── Register
 │      │
 │      ▼
 │   SQLite
 │
 └── Login
        │
        ▼
     Validate
        │
        ▼
   Create Session
        │
        ▼
   Health Dashboard
```

The application stores user information in a SQLite table called `users2`.

---

# 📊 Prediction History Architecture

```text
Prediction
     │
     ▼
Current User Session
     │
     ▼
SQLite Database
     │
     ▼
JSON History
     │
     ▼
Latest 10 Records
     │
     ▼
History Page
```

Each prediction is stored with its document type, prediction result, and timestamp.

---

# 🌐 Application Routes

The Flask backend exposes several routes.

| Route          | Method   | Purpose                           |
| -------------- | -------- | --------------------------------- |
| `/`            | GET      | Home page                         |
| `/login`       | GET/POST | User login                        |
| `/register`    | GET/POST | User registration                 |
| `/success`     | GET      | User dashboard/selection          |
| `/predict`     | GET      | Medical-image prediction page     |
| `/upload`      | POST     | Upload and classify medical image |
| `/history`     | GET      | View prediction history           |
| `/assistant`   | GET/POST | Gemini-powered health assistant   |
| `/chartPlaner` | GET      | Food planner page                 |
| `/submit`      | POST     | Generate personalized food chart  |
| `/feedback`    | GET      | Feedback page                     |
| `/contact`     | GET      | Contact page                      |

These routes are implemented in the main Flask application.

---

# 📡 API Example

## Medical Image Prediction

### Request

```http
POST /upload
Content-Type: multipart/form-data
```

Upload:

```text
file = medical_image.jpg
```

### Response

```json
{
  "document_type": "MRI",
  "classification": "glioma",
  "first_aid": "Seek specialized medical evaluation immediately..."
}
```

---

# 🍱 Food Planner API

### Request

```http
POST /submit
Content-Type: application/json
```

Example:

```json
{
  "diseases": [
    "Diabetes"
  ],
  "food_preference": "Indian Vegetarian"
}
```

### Response

```json
{
  "message": "Data recorded and dynamic chart generated successfully!",
  "food_chart": "<generated HTML>"
}
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/PiyushVIT346/health-hackathon.git
```

```bash
cd health-hackathon
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

The application loads the API key using `python-dotenv` and configures the Google Generative AI client from the environment.

### ⚠️ Security Recommendation

**Never commit API keys to GitHub.**

Use:

```text
.env
```

locally and configure the environment variable through your deployment platform.

If an API key has already been committed to a public repository, **revoke/rotate it immediately** and replace it with a new secret.

---

# ▶️ Running the Application

Start the Flask application with:

```bash
python app.py
```

The application will start locally.

Open:

```text
http://127.0.0.1:5000
```

---

# 🚀 Deployment

The project is configured for deployment using **Gunicorn**.

The repository includes a `Procfile` containing:

```text
web: gunicorn app:app
```

and a Render configuration using:

```text
gunicorn app:app
```

as the start command.

## Render Deployment

### Step 1 — Create a Render Web Service

Connect the GitHub repository:

```text
PiyushVIT346/health-hackathon
```

### Step 2 — Configure Environment

Set:

```text
GOOGLE_API_KEY=your_new_api_key
```

as a secret environment variable.

### Step 3 — Build Command

```bash
pip install -r requirements.txt
```

### Step 4 — Start Command

```bash
gunicorn app:app
```

### Step 5 — Deploy

Render will install the dependencies and launch the Flask application through Gunicorn.

---

# 🧠 Generative AI Workflow

The Gemini-powered components follow this architecture:

```text
User Input
    │
    ▼
Flask Backend
    │
    ▼
Prompt Construction
    │
    ▼
Google Gemini
    │
    ▼
Generated Response
    │
    ├───────────────┐
    ▼               ▼
Health Assistant   Food Planner
    │               │
    ▼               ▼
Chat Response     Weekly Food Plan
```

---

# 📈 Advantages

## Unified Healthcare Platform

Instead of building separate applications for different healthcare tasks, Health Hub combines multiple AI capabilities into one platform.

## Automated Model Selection

Users do not need to manually choose between X-ray, MRI, and CT models.

The application first identifies the document type and automatically routes the image.

## Multi-Modal AI Approach

The project combines:

```text
Computer Vision
       +
Deep Learning
       +
Generative AI
       +
Web Application
       +
Database
```

## Personalized Assistance

The platform can generate responses based on user-provided symptoms, health conditions, and food preferences.

## History Tracking

Users can revisit recent medical-image prediction results.

---

# 🧪 Example Use Cases

### Use Case 1 — X-ray

```text
User uploads X-ray
        ↓
Document classifier
        ↓
X-ray detected
        ↓
Fracture model
        ↓
Fracture / No Fracture
        ↓
Preliminary precaution
```

### Use Case 2 — MRI

```text
User uploads MRI
        ↓
Document classifier
        ↓
MRI detected
        ↓
Brain-tumor classifier
        ↓
Tumor classification
        ↓
Preliminary guidance
```

### Use Case 3 — Health Assistant

```text
User:
"I have been experiencing persistent headaches."

        ↓

Gemini-powered assistant

        ↓

Possible causes
General information
Suggested consultation
Health guidance
```

### Use Case 4 — Food Planner

```text
Health Condition
       +
Food Preference
       ↓
Gemini
       ↓
Personalized Weekly Plan
       ↓
Breakfast
Lunch
Snack
Dinner
```

---

# 🔒 Security Considerations

The application should be improved before being used with real patient data.

Recommended improvements include:

* Hash passwords using a secure password-hashing algorithm.
* Add CSRF protection.
* Validate uploaded file types.
* Restrict maximum upload size.
* Store uploaded files securely.
* Avoid exposing medical images publicly.
* Encrypt sensitive healthcare information.
* Use secure session configuration.
* Store API keys exclusively in environment variables.
* Add authentication/authorization controls.
* Avoid storing personally identifiable medical information unnecessarily.
* Add HTTPS in production.
* Add rate limiting to AI endpoints.
* Validate and sanitize AI-generated HTML before rendering it.

---

# ⚠️ Medical Disclaimer

This project is an **AI/ML educational and hackathon project**.

Predictions generated by the machine-learning models are preliminary and should **not be interpreted as a definitive medical diagnosis**.

Similarly, responses generated by the AI assistant and food planner are not substitutes for professional medical advice.

Users should consult a qualified healthcare professional for:

* Diagnosis
* Treatment
* Medication
* Emergency conditions
* Medical-image interpretation
* Personalized dietary recommendations

---

# 🔮 Future Improvements

The project can be extended with:

### AI/ML

* Improve model accuracy through transfer learning.
* Add confidence scores to predictions.
* Add explainable AI using Grad-CAM.
* Support additional medical-image categories.
* Add skin-disease classification.
* Add pneumonia detection.
* Add diabetic-retinopathy detection.
* Add ECG analysis.

### Generative AI

* Upgrade to newer Gemini models.
* Add Retrieval-Augmented Generation for trusted medical resources.
* Add medical knowledge-base integration.
* Add conversation memory.
* Add multilingual healthcare assistance.

### Backend

* Replace SQLite with PostgreSQL for production.
* Implement proper authentication.
* Add JWT/OAuth authentication.
* Add API versioning.
* Add request validation with Pydantic.
* Add logging and monitoring.

### Security

* Password hashing.
* Secure file storage.
* Role-based access control.
* Encryption of sensitive data.
* HTTPS.
* Rate limiting.
* Input sanitization.

### Deployment

* Dockerize the application.
* Add CI/CD using GitHub Actions.
* Use cloud object storage for uploaded images.
* Use managed databases.
* Add application monitoring.

---

# 🏗️ Future Production Architecture

```text
                         ┌─────────────────────┐
                         │       Frontend      │
                         │ HTML/CSS/JavaScript │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Flask API      │
                         └──────────┬──────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
      │ ML Inference │      │ Gemini API   │      │ PostgreSQL   │
      │   Service    │      │              │      │   Database   │
      └──────┬───────┘      └──────────────┘      └──────────────┘
             │
       ┌─────┼─────┐
       ▼     ▼     ▼
     X-Ray   MRI   CT
     Model  Model Model
```

---

# 📊 Technology Summary

| Component            | Technology            |
| -------------------- | --------------------- |
| Programming Language | Python                |
| Web Framework        | Flask                 |
| ML Framework         | TensorFlow / Keras    |
| Image Processing     | Pillow / NumPy        |
| Generative AI        | Google Gemini         |
| Database             | SQLite                |
| Authentication       | Flask Session         |
| Model Download       | gdown                 |
| WSGI Server          | Gunicorn              |
| Deployment           | Render                |
| Frontend             | HTML, CSS, JavaScript |
| Templating           | Jinja2                |

---

# 📁 Important Files

| File               | Purpose                                           |
| ------------------ | ------------------------------------------------- |
| `app.py`           | Main Flask application and AI/ML backend          |
| `requirements.txt` | Python dependencies                               |
| `Procfile`         | Gunicorn deployment command                       |
| `render.yaml`      | Render deployment configuration                   |
| `templates/`       | HTML/Jinja2 application pages                     |
| `static/`          | CSS, JavaScript, images, and frontend assets      |
| `example.db`       | SQLite database generated/used by the application |
| `.env`             | Local environment variables                       |

---

# 👨‍💻 Development Workflow

```text
Idea
  ↓
Healthcare Problem
  ↓
ML Model Development
  ↓
Flask Integration
  ↓
Medical Image Upload
  ↓
Model Routing
  ↓
Prediction
  ↓
Gemini Integration
  ↓
User History
  ↓
Food Planner
  ↓
Deployment
```

---

# 🎯 Project Outcome

Health Hub AI demonstrates how **Deep Learning and Generative AI can be integrated into a full-stack healthcare application**.

The final system combines medical-image classification, automated model selection, AI-powered health assistance, personalized food planning, authentication, and prediction history into a unified Flask application.

The project provides a practical demonstration of building an end-to-end AI application where machine-learning inference and Generative AI services work together to provide healthcare-oriented assistance.

---

# ⭐ Highlights

```text
✅ Multi-model medical image classification
✅ Automatic X-ray / MRI / CT detection
✅ X-ray fracture classification
✅ MRI brain-tumor classification
✅ CT scan classification
✅ Gemini-powered AI health assistant
✅ Personalized AI food planner
✅ User registration and login
✅ Prediction history
✅ Flask backend
✅ TensorFlow/Keras models
✅ SQLite database
✅ Render deployment configuration
```

---

# 🤝 Contributing

Contributions are welcome!

### 1. Fork the repository

```bash
git fork https://github.com/PiyushVIT346/health-hackathon
```

### 2. Clone your fork

```bash
git clone <your-fork-url>
```

### 3. Create a feature branch

```bash
git checkout -b feature/new-feature
```

### 4. Make your changes

Implement and test your feature.

### 5. Commit your changes

```bash
git add .
git commit -m "Add new healthcare feature"
```

### 6. Push your branch

```bash
git push origin feature/new-feature
```

### 7. Open a Pull Request

Create a pull request describing your changes.

---

# 📜 License

This project is currently provided as an educational/hackathon project.

If you intend to distribute or commercialize the project, add an appropriate open-source license such as MIT, Apache-2.0, or another license that matches your intended usage.

---

# 👨‍💻 Author

**Piyush Singh**

B.Tech CSE | Applied Machine Learning

### Connect

* GitHub: [@PiyushVIT346](https://github.com/PiyushVIT346)
* Repository: [Health Hub AI](https://github.com/PiyushVIT346/health-hackathon)

---

# ⭐ Support

If you find this project useful or interesting:

⭐ Star the repository
🍴 Fork the repository
🐛 Report issues
💡 Suggest improvements
🤝 Contribute to the project

---

## 🏥 Health Hub AI

**Bringing Computer Vision, Deep Learning, and Generative AI together for smarter healthcare assistance.**

> *AI can assist healthcare — but human medical expertise remains essential.*
