
---

<h1 align="center"> 🚗 Vehicle Collision Prediction System 🚗 </h1>

<img align="right" height="160" src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3Bpa2R2enp3Y291MDJwY2tkejA0cnlkN3hmaXY3bmt5NjZqc2dhbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/s7LrWWLeWLumc/giphy.gif"/>

This project focuses on developing
a **Vehicle Collision Prediction System** 
using a YOLO model for vehicle detection and a depth estimation model
to calculate safe distances between vehicles. The system aims to prevent collisions
by analyzing object proximity and alerting drivers when the safe distance is breached.


 <br/>
  <br/>
  
---

## Table of Contents
1. [📖 Introduction](#-introduction)
2. [🔧 Methodology](#-methodology)
3. [🔍 Object Detection (YOLO)](#-object-detection-yolo)
4. [📏 Depth Estimation & Distance Calculation](#-depth-estimation-distance-calculation)
5. [🚨 Alert System](#-alert-system)
6. [▶️ How to Run](#-how-to-run)

## 📖 Introduction
This project utilizes machine learning models to predict potential vehicle collisions by:
- Detecting vehicles using a YOLO object detection model.
- Estimating the distance between vehicles using depth estimation.
- Alerting drivers when vehicles come too close, based on a predefined safe distance threshold.

## 🔧 Methodology
1. **Vehicle Detection**: A YOLO model is trained to detect vehicles in real-time video streams.
2. **Depth Estimation**: A depth estimation model calculates distances between the detected vehicles.
3. **Distance Calculation**: The depth map is sliced according to the bounding boxes detected by YOLO to measure the proximity between vehicles.
4. **Alert System**: Alerts are triggered if the distance between vehicles is less than the safe threshold.

## 🔍 Object Detection (YOLO)
The **YOLO (You Only Look Once)** model is used to detect vehicles. The process involves:
- Training the YOLO model with vehicle data.
- Bounding boxes are drawn around detected vehicles.
- Detection occurs in real-time with high accuracy.

## 📏 Depth Estimation & Distance Calculation
To measure the distance between vehicles:
- A depth map is generated for the scene.
- The bounding boxes detected by YOLO are overlaid on the depth map to extract the depth information for each vehicle.
- Distances are calculated by measuring the depth values within the bounding boxes.

## 🚨 Alert System
An alert system is integrated to notify drivers when vehicles are too close. The system:
- Continuously monitors distances.
- Alerts the driver visually or audibly if the distance falls below the safety threshold.
## 🤖 Demo
<img align="center" height="160" src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXYwZzY5bW5ia3FiY2NvczNka2xqbW40czlwNTQ1enB1aHUxb2h5MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NCoqnkC0kHOJ6g09Xn/giphy.gif"/>

## ▶️ How to Run
1. Open the project code in your environment.
2. Install the necessary dependencies for YOLO and depth estimation models.
3. Feed live video input or a video file to the system.
4. Run the detection and collision prediction.
5. The system will display vehicle detection and issue alerts based on safe distances.
