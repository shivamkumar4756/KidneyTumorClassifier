from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.pipeline.prediction import PredictionPipeline

app = Flask(__name__)
CORS(app)

# Initialize ClientApp class
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

clApp = ClientApp()

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        # ✅ Save file properly
        file_path = os.path.join("inputImage.jpg")
        file.save(file_path)
        
        # ✅ Check if file is saved correctly
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not saved correctly.")

        # ✅ Update filename and predict
        clApp.classifier.filename = file_path
        
        # ✅ Log for debugging
        print(f"🔥 File saved at: {file_path}")

        # ✅ Predict using pipeline
        result = clApp.classifier.predict()

        if 'error' in result[0]:
            raise Exception(result[0]['error'])

        prediction_text = result[0]["image"]
        print(f"✅ Prediction Result: {prediction_text}")

        # ✅ Return successful JSON response
        return jsonify({"prediction": prediction_text})

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
