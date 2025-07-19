pollen_classification
🌾 Pollen Profiling - Automated Classification of Pollen Grains Welcome to Pollen Profiling, a deep learning-based project for classifying pollen grains from microscopic images using TensorFlow and Keras.

🚀 Project Overview This project aims to automatically classify pollen grain species using a Convolutional Neural Network (CNN) trained on high-resolution microscopic images.

Key Features:

✅ Custom-trained Keras model (model.h5)

✅ Preprocessed pollen dataset (excluded from Git)

✅ Flask-based interactive web application

✅ Label encoder for decoding model predictions

📁 Directory Structure graphql Copy Edit Pollen-Profiling/ │ ├── app.py # Flask backend ├── model.h5 # Trained CNN model (excluded from Git) ├── label_encoder.pkl # Encodes/decodes labels (excluded from Git) ├── dataset/ # Pollen images (excluded from Git) ├── static/ # CSS and uploaded images ├── templates/ # HTML templates for Flask ├── pollen_grain_classification.ipynb # Jupyter notebook for model training ├── requirements.txt # Python dependencies ├── .gitignore └── README.md 🚫 Files & Git Ignore Policy The following files and folders are excluded to reduce repo size and comply with GitHub's upload limits:

gitignore Copy Edit dataset/ *.h5 *.pkl pycache/ *.pyc python-.exe ⚠ Note: You must download or generate the model and dataset files before running the project locally.

📊 Model Details Model Type: Convolutional Neural Network (CNN)

Framework: TensorFlow & Keras

Accuracy: ~99%

Trained Model: model.h5

Label Encoder: label_encoder.pkl

🌐 Web Application (Flask) Features include:

📤 Upload a microscopic pollen image

🧠 Predict the pollen species

📈 Display prediction and confidence score

🔁 Simple user interface and logout navigation

▶ How to Run Locally 1️⃣ Install Dependencies bash Copy Edit pip install -r requirements.txt 2️⃣ Start the Flask App bash Copy Edit set FLASK_APP=app.py set FLASK_ENV=development flask run (Use export instead of set on Linux/macOS)

3️⃣ Open in Browser Go to: http://127.0.0.1:5000

📽 Demo Video 🎥 https://drive.google.com/file/d/13DKMSDH7BKhYfMu2kUQBBZeC5TXz6lG9/view?usp=sharing

(Replace the link above with your actual video once it's ready.)

📄 Project Notes Files like model.h5, label_encoder.pkl, and the dataset/ folder are excluded from Git due to size limits.

You can generate these locally using the notebook, or request them from the author.

📧 Contact Sivapuram gayatri GitHub: https://github.com/gayatri9553/pollen-s-profiling-automated-classification-of-pollen-grain
