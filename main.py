import cv2
import sys
from censor import censor_faces

def process_live_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    print("[INFO] Camera opened. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        censored_frame = censor_faces(frame)

        cv2.imshow('C.O.V.E.R.T. = Censorship Operations & Video Encrypted Real-Time Tracking', censored_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    while True:
        print("\n" + "="*30)
        print("C.O.V.E.R.T. = Censorship Operations & Video Encrypted Real-Time Tracking")
        print("="*30)
        print("1. Process live camera feed")
        print("2.Process video file [Still in development]")
        print("3. Export video file to .mp4 [Still in development]")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            process_live_camera()
        elif choice == '2':
            print("Video file processing is still in development.")
        elif choice == '3':
            print("Exporting video file to .mp4 is still in development.")
        elif choice == '4':
            print("Exiting the program.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    
if __name__ == "__main__":
    main()

