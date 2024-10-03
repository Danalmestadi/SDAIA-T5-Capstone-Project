import streamlit as st
import cv2
import torch
import numpy as np
from ultralytics import YOLO
from PIL import Image
import io

# Streamlit title
st.title("YOLO Object Detection App")

# Sidebar for input options
st.sidebar.title("Input Options")
uploaded_file = st.sidebar.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

# Load the YOLO model (you can replace 'yolov8' with your custom-trained model if needed)
model = YOLO('yolov8n.pt')  # Load pre-trained model

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert the image to a format suitable for YOLO
    image_np = np.array(image)

    # Perform object detection
    results = model(image_np)

    # Draw bounding boxes on the image
    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0]  # Coordinates of the bounding box
        cv2.rectangle(image_np, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)

    # Convert the image back to display
    st.image(image_np, caption="Detected Image", use_column_width=True)

    # Option to download the processed image
    st.sidebar.download_button("Download Result Image", data=image_np, file_name="detected_image.png", mime="image/png")

else:
    st.write("Please upload an image to detect objects.")

