import os
import numpy as np
from flask import Flask, request, render_template
from keras.preprocessing import image
from keras.models import load_model

# Initialize Flask app 
app = Flask(__name__)

# Load your trained Keras model
model = load_model("model.h5", compile=False)

# List of class labels (ensure it matches your model's output order)
labels = [
    'anadenanthera', 'arecaceae', 'arrabidaea', 'cecropia', 'chromolaena',
    'combretum', 'croton', 'dipteryx', 'eucalipto', 'faramea', 'hyptis',
    'mabea', 'matayba', 'mimosa', 'myrcia', 'protium', 'qualea', 'schinus',
    'senegalia', 'serjania', 'syagrus', 'tridax', 'urochloa'
]

# Home route
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']
        if not file:
            return render_template('predict.html', prediction=None, image_path=None, confidence=None)

        # Save uploaded file to static/uploads directory
        basepath = os.path.dirname(__file__)
        upload_folder = os.path.join(basepath, 'static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        upload_path = os.path.join(upload_folder, file.filename)
        file.save(upload_path)

        # Preprocess the image
        img = image.load_img(upload_path, target_size=(128, 128))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        # Predict
        probs = model.predict(x)[0]
        pred = np.argmax(probs)
        predicted_label = labels[pred]
        confidence = float(probs[pred] * 100)

        return render_template('predict.html',
                               prediction=predicted_label,
                               image_path=file.filename,
                               confidence=confidence)

    return render_template('predict.html', prediction=None, image_path=None, confidence=None)

# Logout route
@app.route('/logout.html')
def logout():
    return render_template('logout.html')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
