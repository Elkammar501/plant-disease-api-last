from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
from PIL import Image
import io
from fastapi.responses import HTMLResponse
app = FastAPI(title="Plant Disease API")

# Allow any application to connect to the API
app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"],
 allow_methods=["*"],
 allow_headers=["*"],
)

# Load the trained model once when the API starts
model = tf.keras.models.load_model("final_mobilenet_model.h5")

# Class names in the same order used during model training
CLASS_NAMES = [
 "Apple - Apple Scab",
 "Apple - Black Rot",
 "Apple - Cedar Apple Rust",
 "Apple - Healthy",
 "Blueberry - Healthy",
 "Cherry - Powdery Mildew",
 "Cherry - Healthy",
 "Corn - Cercospora / Gray Leaf Spot",
 "Corn - Common Rust",
 "Corn - Northern Leaf Blight",
 "Corn - Healthy",
 "Grape - Black Rot",
 "Grape - Esca (Black Measles)",
 "Grape - Leaf Blight",
 "Grape - Healthy",
 "Orange - Haunglongbing (Citrus Greening)",
 "Peach - Bacterial Spot",
 "Peach - Healthy",
 "Pepper Bell - Bacterial Spot",
 "Pepper Bell - Healthy",
 "Potato - Early Blight",
 "Potato - Late Blight",
 "Potato - Healthy",
 "Raspberry - Healthy",
 "Soybean - Healthy",
 "Squash - Powdery Mildew",
 "Strawberry - Leaf Scorch",
 "Strawberry - Healthy",
 "Tomato - Bacterial Spot",
 "Tomato - Early Blight",
 "Tomato - Late Blight",
 "Tomato - Leaf Mold",
 "Tomato - Septoria Leaf Spot",
 "Tomato - Spider Mites",
 "Tomato - Target Spot",
 "Tomato - Yellow Leaf Curl Virus",
 "Tomato - Mosaic Virus",
 "Tomato - Healthy",
]


def preprocess_image(image_bytes: bytes) -> np.ndarray:
 """Convert the uploaded image into a format accepted by the model."""
 image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
 image = image.resize((224, 224))
 image_array = np.array(image) / 255.0
 return np.expand_dims(image_array, axis=0) # إضافة batch dimension


@app.get("/", response_class=HTMLResponse)
def home():
 with open("plant_disease_ui.html", "r", encoding="utf-8") as f:
 return f.read()


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
 """
 Receive a plant leaf image and return the predicted disease name and confidence score.
 """
 # Read the uploaded image
 image_bytes = await file.read()

 # Preprocess the image
 image_array = preprocess_image(image_bytes)

 # Make prediction
 predictions = model.predict(image_array)
 predicted_index = int(np.argmax(predictions[0]))
 confidence = float(np.max(predictions[0]))

 # Return the prediction result
 return {
 "disease": CLASS_NAMES[predicted_index],
 "confidence": round(confidence * 100, 2),
 "is_healthy": "Healthy" in CLASS_NAMES[predicted_index],
 "class_index": predicted_index,
 }
