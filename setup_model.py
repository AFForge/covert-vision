import os
import urllib.request

# Configuration for the MediaPipe face detection model
MODEL_FILENAME = "blaze_face_short_range.tflite"
MODEL_URL = "https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/blaze_face_short_range.tflite"

def download_model():
    """Downloads the required MediaPipe model if it doesn't exist locally."""
    if not os.path.exists(MODEL_FILENAME):
        print(f"[INFO] Downloading {MODEL_FILENAME} from Google servers...")
        try:
            urllib.request.urlretrieve(MODEL_URL, MODEL_FILENAME)
            print("[SUCCESS] Model downloaded successfully.")
        except Exception as e:
            print(f"[ERROR] Failed to download the model: {e}")
    else:
        print(f"[INFO] {MODEL_FILENAME} is already present.")

if __name__ == "__main__":
    download_model()