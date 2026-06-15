# Plant Disease Detection System

An AI-powered computer vision project designed to detect plant diseases from leaf images using deep learning.

This project demonstrates how artificial intelligence can support smart agriculture by helping users identify plant health conditions quickly and efficiently through image-based disease classification.

---

## Project Summary

**Plant Disease Detection System** is a deep learning-based solution that classifies plant leaf images into healthy or diseased categories.

The project uses a trained convolutional neural network model based on **MobileNetV2**, a lightweight and efficient architecture suitable for real-time prediction and mobile-friendly AI applications.

The system is supported by a **FastAPI backend**, allowing the trained model to receive image inputs and return prediction results in a structured format.

---

## Problem Statement

Plant diseases can significantly affect crop quality and productivity. Early detection is important to help farmers and agricultural specialists take timely action.

Traditional disease diagnosis often requires manual inspection or expert knowledge, which may not always be available. This project addresses that challenge by using artificial intelligence to analyze plant leaf images and predict the most likely disease class.

---

## Project Objective

The main objective of this project is to build an intelligent plant disease classification system that can:

- Identify plant diseases from leaf images.
- Distinguish between healthy and diseased leaves.
- Support multiple crop categories.
- Provide fast and reliable prediction results.
- Serve as a foundation for mobile or web-based smart agriculture applications.

---

## Dataset

The model was trained using the **PlantVillage Dataset** from Kaggle.

Dataset source:  
https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset

The dataset contains labeled images of plant leaves organized into disease and healthy categories. It includes multiple crops such as apple, corn, grape, potato, tomato, strawberry, peach, cherry, and others.

---

## Supported Plant Categories

The system supports disease classification for several plant types, including:

- Apple
- Blueberry
- Cherry
- Corn
- Grape
- Orange
- Peach
- Pepper Bell
- Potato
- Raspberry
- Soybean
- Squash
- Strawberry
- Tomato

---

## Classification Coverage

The model supports **38 output classes**, covering both healthy and diseased plant leaves.

Examples of detectable conditions include:

- Apple Scab
- Apple Black Rot
- Cedar Apple Rust
- Corn Common Rust
- Corn Northern Leaf Blight
- Grape Black Rot
- Grape Esca
- Potato Early Blight
- Potato Late Blight
- Tomato Bacterial Spot
- Tomato Early Blight
- Tomato Late Blight
- Tomato Leaf Mold
- Tomato Mosaic Virus
- Tomato Yellow Leaf Curl Virus
- Healthy leaf classes for multiple crops

---

## Machine Learning Approach

This project applies **transfer learning** using MobileNetV2.

MobileNetV2 was selected because it is:

- Lightweight
- Efficient
- Suitable for image classification
- Appropriate for deployment-focused applications
- A strong choice for mobile and real-time AI systems

The model was adapted to classify plant leaf images across multiple disease categories by adding custom classification layers on top of the pretrained base model.

---

## Backend Overview

The backend is built using **FastAPI**, providing a clean and efficient interface for image-based prediction.

The backend handles:

- Receiving uploaded leaf images.
- Preprocessing images before prediction.
- Passing images to the trained model.
- Returning the predicted class.
- Returning the confidence score.
- Identifying whether the prediction represents a healthy plant or a diseased one.

---

## Key Features

- AI-powered plant disease detection.
- Image-based prediction.
- Deep learning model based on MobileNetV2.
- FastAPI backend integration.
- Supports 38 plant disease and healthy classes.
- Lightweight architecture suitable for real-time use.
- Clear prediction response including disease name and confidence score.
- Can be integrated with mobile applications, web applications, or agricultural platforms.

---

## Project Workflow

The project follows a complete AI development workflow:

1. Dataset preparation and organization.
2. Image preprocessing.
3. Transfer learning using MobileNetV2.
4. Model training and validation.
5. Model evaluation.
6. Model saving.
7. Backend API development.
8. Prediction serving through FastAPI.

---

## Prediction Output

For each uploaded plant leaf image, the system returns:

- Predicted disease or healthy class.
- Confidence score.
- Health status indicator.
- Class index.

This makes the output easy to use in external applications such as mobile apps, dashboards, or farmer assistant tools.

---

## Strengths of the Project

- Practical computer vision use case.
- Suitable for smart agriculture applications.
- Uses a lightweight model architecture.
- Supports many plant and disease categories.
- Backend is ready for integration with other systems.
- Clear separation between model training and deployment.
- Simple and scalable project structure.

---

## Possible Use Cases

This project can be used as a foundation for:

- Smart farming applications.
- Plant disease diagnosis tools.
- Agricultural assistant mobile apps.
- Educational AI and computer vision demos.
- Crop monitoring platforms.
- Farmer support systems.
- Research prototypes in applied machine learning.

---

## Limitations

Although the model can perform well on dataset images, real-world performance may vary depending on:

- Image quality.
- Lighting conditions.
- Background complexity.
- Leaf position and clarity.
- Similarity between different plant diseases.
- Diseases not included in the training dataset.

For best results, the system should be tested further using real-world mobile images captured under different conditions.

---

## Future Enhancements

Future improvements may include:

- Adding Arabic disease names.
- Adding disease treatment recommendations.
- Returning the top predicted classes.
- Adding confidence-based warnings for uncertain predictions.
- Improving real-world generalization using field images.
- Converting the model to TensorFlow Lite for mobile deployment.
- Adding a complete frontend interface.
- Deploying the API on a cloud server.
- Adding logging and monitoring.
- Expanding the dataset with more crops and diseases.

---

## Project Value

This project shows how deep learning can be applied to solve a real agricultural problem. It combines computer vision, transfer learning, and backend deployment into a practical AI solution that can support early plant disease detection and help improve agricultural decision-making.
