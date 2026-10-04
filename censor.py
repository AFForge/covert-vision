import cv2
import os
import urllib.request
from ultralytics import YOLO


#Path to the local model downloaded from Hugging Face.
MODEL_PATH = "yolov8n-face.pt"
MODEL_URL = "https://huggingface.co/deepghs/yolo-face/resolve/main/yolov8n-face/model.pt"

# Check if the model file exists, if not, download it from Hugging Face
if not os.path.exists(MODEL_PATH):
    print("[INFO] Downloading YOLOv8-Face weights from Hugging Face...")
    try:
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("[SUCCESS] YOLOv8-Face weights downloaded successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to download model weights: {e}")

# Load the YOLOv8-Face model
model = YOLO(MODEL_PATH)

def censor_faces(frame):
    """
    Detects faces using YOLOv8-Face and censors them by drawing black rectangles over the detected faces. 
    """
    # Convert the frame to RGB format as YOLOv8 expects RGB images
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model.predict(frame, conf=0.35, verbose=False)
    
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # Get the coordinates of the bounding box
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
            
            # Ensure the coordinates are within the frame boundaries
            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = max(0, x2)
            y2 = max(0, y2)
            
            # Draw a black rectangle over the detected face
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), -1)
            
    return frame