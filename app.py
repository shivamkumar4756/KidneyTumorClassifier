import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing import image
import io

app = Flask(__name__)

# Load the trained model
MODEL_PATH = "artifacts/training/model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Class labels
class_names = ["No Tumor", "Tumor Detected"]

def preprocess_image(file):
    """Preprocess the uploaded image for model prediction."""
    img = image.load_img(io.BytesIO(file.read()), target_size=(224, 224))  # Resize to model input size
    img_array = image.img_to_array(img)  # Convert to array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Normalize
    return img_array

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Kidney Tumor Classification API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    img_array = preprocess_image(file)
    prediction = model.predict(img_array)

    predicted_class = class_names[np.argmax(prediction)]
    confidence = float(np.max(prediction))

    return jsonify({"prediction": predicted_class, "confidence": confidence})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
