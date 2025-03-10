from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import io

app = Flask(__name__)

# Load the trained model
MODEL_PATH = "artifacts/training/model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        # Convert the file to a BytesIO stream
        file_bytes = io.BytesIO(file.read())

        # Load image from BytesIO
        img = image.load_img(file_bytes, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize

        # Make prediction
        prediction = model.predict(img_array)
        prediction_list = prediction.tolist()  # Convert numpy array to list

        print("🔥 Prediction Output:", prediction_list)  # Debugging

        return jsonify({"prediction": prediction_list})  # Send JSON response

    except Exception as e:
        print("❌ Error:", str(e))  # Print error in terminal
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8080)
