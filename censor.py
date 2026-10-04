import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

#Path to the local model downloaded from Google servers
MODEL_PATH = "blaze_face_short_range.tflite"

#Initialize the MediaPipe tasks API face detector
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.FaceDetectorOptions(base_options=base_options, min_detection_confidence=0.2)

detector = vision.FaceDetector.create_from_options(options)

def censor_faces(frame):
    """
    Detects faces using an ensemble of short-range and long-range detectors and censors them by drawing black rectangles over the detected faces.   
    """
    # Convert the frame to RGB for MediaPipe processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert OpenCV image to MediaPipe Image
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    #Execute face detection
    detection_result = detector.detect(mp_image)

    #Apply censorship (black rectangles) over detected faces
    if detection_result.detections:
        for detection in detection_result.detections:
            bbox = detection.bounding_box

            #Extract bounding box coordinates and dimensions
            x = int(bbox.origin_x)
            y = int(bbox.origin_y)
            width = int(bbox.width)
            height = int(bbox.height)
            
           # Add padding to the bounding box to ensure the entire face is covered
            pad_x = int(width * 0.35)
            pad_y = int(height * 0.35)
            
            # Add extra padding to the top of the bounding box to cover the forehead and hairline
            pad_top = int(height * 0.25) 
            
           # Calculate new coordinates and dimensions for the rectangle with padding
            new_x = max(0, x - pad_x)
            new_y = max(0, y - pad_y - pad_top)
            new_w = width + (pad_x * 2)
            new_h = height + (pad_y * 2) + pad_top
            
            # Draw a black rectangle over the detected face
            cv2.rectangle(frame, (new_x, new_y), (new_x + new_w, new_y + new_h), (0, 0, 0), -1)

    return frame