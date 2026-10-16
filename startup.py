import subprocess
import sys
import os
import urllib.request

# List of required packages
required_packages = [
    "opencv-python",
    "ultralytics",
    "moviepy",
    "soundfile",
    "pedalboard",
]


# Using official identificators of YOLOv8-Face models
models = {
    "1":{
        "name": "YOLOv8 Nano",
        "filename": "yolov8n-face.pt",
        "url": "https://drive.google.com/uc?id=1ZD_CEsbo3p3_dd8eAtRfRxHDV44M0djK"
    },

    "2":{
        "name": "YOLOv8 Medium",
        "filename": "yolov8m-face.pt",
        "url": "https://drive.google.com/uc?id=1IJZBcyMHGhzAi0G4aZLcqryqZSjPsps-"
    }
}

def install_dependencies():
    print("[INFO] Checking and installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], stdout=subprocess.DEVNULL)
        subprocess.check_call([sys.executable, "-m", "pip", "install"] + required_packages)
        print("[SUCCESS] Packages have been installed.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Error while installing packages: {e}")
        input("\n Press Enter to stop the process...")
        sys.exit(1)

def download_file_from_gdrive(file_id, destination):

    URL = "https://docs.google.com/uc?export=download"
    session = urllib.request.urlopen(urllib.request.Request(f"{URL}&id={file_id}"))

    token = None
    for key, value in session.headers.items():
        if key.lower() == "set-cookie" and "download_warning" in value:
            token = value.split("download_warning=")[1].split(';')[0]
            break

    if token:
        params = f"?export=download&confirm={token}&id={file_id}"
        session = urllib.request.urlopen(urllib.request.Request(URL + params))

    print(f"[INFO] Installing to {destination}...")
    with open(destination, "wb") as f:
        f.write(session.read())

def setup_yolo_model():
    print("\n--- Choose AI model (YOLOv8-Face) ---")
    print("1. YOLOv8 Nano")
    print("2. Medium")
    
    choice = input("Choose [1/2] to install (default 1): ").strip()
    if choice not in models:
        choice = "1"
        
    selected = models[choice]
    model_path = selected["filename"]
    
    target_path = "yolov8n-face.pt"
    
    if not os.path.exists(target_path):
        print(f"[INFO] Choosen: {selected['name']}")
        try:
            download_file_from_gdrive(selected["gdrive_id"], target_path)
            print("[SUCCESS] Model was succesfully downloaded.")
        except Exception as e:
            print(f"[ERROR] The model could not be installed: {e}")
            print("[TIP] You can try to download yourself, if the problem will still exist.")
            input("\n Press Enter to continue...")
    else:
        print("[INFO] Model Yolo is in directory.")

def launch_main():
    main_script = "main.py"
    if os.path.exists(main_script):
        print("\n[INFO] Enviroment is ready, main script will run soon...\n")
        subprocess.run([sys.executable, main_script])
    else:
        print(f"[ERROR] Couldn't find {main_script}. Be sure they are in the same directory.")

if __name__ == "__main__":
    print("=" * 55)
    print(" C.O.V.E.R.T. - Turned on main script ")
    print("=" * 55)
    
    install_dependencies()
    setup_yolo_model()
    launch_main()