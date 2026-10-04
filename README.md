# C.O.V.E.R.T. Vision
**Censorship Operations & Video Encrypted Real-Time Tracking**

COVERT is a modular, Python-based computer vision tool designed for automated face anonymization (blackout censorship) in both real-time video streams and offline video files. 

## Features
The system operates via a Command Line Interface (CLI) offering three main operational modes:
1. **Live Camera Preview:** Real-time face detection and censorship via webcam.
2. **Video File Preview:** On-the-fly censorship of local video files.
3. **Export Censored Video:** Headless processing that reads an input video, applies blackout censorship to all detected faces, and exports the result to a new file.

## Technology Stack
* **Language:** Python 3.x
* **Computer Vision:** OpenCV (`cv2`)
* **Detection Model:** Haar Cascade Classifiers (Frontal Face)

## Roadmap (Future Improvements)
- [x] Core processing engine and CLI interface implementation.
- [x] Live camera and offline `.mp4` video file support.
- [x] Model upgrade: Replace Haar Cascades with a modern model(MediaPipe Tasks API) to accurately detect faces from multiples angles and profiles
- [x] Advanced detection model upgrade: Migrate to YOLOv8 for robust long-range and background face detection.
- [ ] Universal Format Support: Expand input/output compatibility beyond `.mp4` to `.avi`, `.mov`, and `.mkv`.
- [ ] Audio Obfuscation: Implement audio extraction, voice distortion (pitch shifting), and re-muxing to ensure total identity protection (tone/voice masking).
## Quick Start
1. **Clone the repository:**
```bash
git clone [https://github.com/AFForge/covert-vision.git](https://github.com/AFForge/covert-vision.git)
cd covert-vision
```
2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
3. **Run the system:**
```bash
python main.py
```

## Privacy Notice
This tool is designed with privacy in mind. All video processing is done locally on your machine. No video data or telemetry is sent to external servers.

## Acknowledgments & Third-Party Licenses
This project incorporates open-source models and libraries:
*YOLOv8 framework by Ultralytics (AGPL-3.0 License).
*YOLOv8-Face fine-tuned model hosted on Hugging Face.
*Early iterations utilized OpenCV Haar Cascades and Google MediaPipe Tasks API.
