import cv2

# Load the pre-trained Haar Cascade classifier for frontal face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def censor_faces(frame):
    """
    Censors faces in the given frame by detecting them and drawing black rectangles over them.
    """
    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30)
    )
    # Censor each detected face by drawing a black rectangle over it
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), -1)
    
    return frame