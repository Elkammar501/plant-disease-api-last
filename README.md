# 🌿 Plant Disease API

API لتصنيف أمراض النباتات باستخدام MobileNetV2

---

## 🚀 تشغيل محلياً

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 📡 الـ Endpoint الوحيد المهم

### `POST /predict`

بتبعت صورة، بترجعلك اسم المرض ونسبة الثقة.

**URL:**
```
POST https://your-app.onrender.com/predict
```

**الـ Request:**
- نوع البيانات: `multipart/form-data`
- الحقل: `file` (صورة jpg أو png)

**الـ Response:**
```json
{
  "disease": "Tomato - Early Blight",
  "confidence": 94.3,
  "is_healthy": false,
  "class_index": 29
}
```

---

## 📱 كود Flutter جاهز

```dart
import 'dart:io';
import 'package:http/http.dart' as http;
import 'dart:convert';

Future<Map<String, dynamic>> predictDisease(File imageFile) async {
  final url = Uri.parse('https://your-app.onrender.com/predict');
  
  final request = http.MultipartRequest('POST', url);
  request.files.add(
    await http.MultipartFile.fromPath('file', imageFile.path),
  );

  final response = await request.send();
  final body = await response.stream.bytesToString();
  return jsonDecode(body);
}

// استخدام الدالة:
// final result = await predictDisease(imageFile);
// print(result['disease']);      // "Tomato - Early Blight"
// print(result['confidence']);   // 94.3
// print(result['is_healthy']);   // false
```

---

## ☁️ خطوات الـ Deployment على Render

1. ارفع الملفات على **GitHub** (مع النموذج `final_mobilenet_model.h5`)
2. اتفضل على [render.com](https://render.com) وسجل دخول
3. اضغط **New Web Service**
4. اربط الـ GitHub repo
5. Render هيقرأ `render.yaml` تلقائياً ويعمل كل حاجة
6. بعد الـ deploy، هتاخد رابط زي: `https://plant-disease-api.onrender.com`

---

## 📂 هيكل الملفات

```
plant-disease-api/
├── main.py                    ← كود الـ API
├── requirements.txt           ← المكتبات
├── render.yaml                ← إعدادات الـ deployment
└── final_mobilenet_model.h5   ← النموذج (هتحطه هنا)
```
