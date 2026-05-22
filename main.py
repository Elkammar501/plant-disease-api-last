from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI(title="Plant Disease API")

# السماح لأي تطبيق يتصل بالـ API (مهم للموبايل)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# تحميل النموذج مرة واحدة عند بدء الـ API
model = tf.keras.models.load_model("final_mobilenet_model.h5")

# أسماء الفئات بالترتيب
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
    """تحويل الصورة لشكل يقبله النموذج"""
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    return np.expand_dims(image_array, axis=0)  # إضافة batch dimension


@app.get("/")
def root():
    return {"message": "Plant Disease API is running ✅"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    استقبال صورة ورقة نبات وإرجاع اسم المرض ونسبة الثقة
    """
    # قراءة الصورة
    image_bytes = await file.read()

    # معالجة الصورة
    image_array = preprocess_image(image_bytes)

    # التنبؤ
    predictions = model.predict(image_array)
    predicted_index = int(np.argmax(predictions[0]))
    confidence = float(np.max(predictions[0]))

    # إرجاع النتيجة
    return {
        "disease": CLASS_NAMES[predicted_index],
        "confidence": round(confidence * 100, 2),
        "is_healthy": "Healthy" in CLASS_NAMES[predicted_index],
        "class_index": predicted_index,
    }
