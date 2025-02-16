from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf

# Load Model
model = tf.keras.models.load_model("artifacts/training/model.h5")

# Load & Preprocess Image
img_path = "artifacts/data_ingestion/kidney-ct-scan-images/tumor/kidney-tumor-0001.jpg"  # <-- Change this to any sample image
img = image.load_img(img_path, target_size=(224, 224))  # Change size if needed
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0  # Normalize

# Predict
prediction = model.predict(img_array)
print("✅ Prediction Output:", prediction)
