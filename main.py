import cv2
import sys
import os
from censor import censor_faces

def process_live_camera():
    """
    (Option 1)
    Processes the live camera feed and censors detected faces.
    """
    cap = cv2.VideoCapture(0)
    # Check if the camera opened successfully
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

def process_video_preview():
    """
    (Option 2)
    Processes a video file and censors detected faces in a preview window.
    """
    filepath = input("Enter the path to the video file: ")

    # Check if the file exists
    if not os.path.isfile(filepath):
        print("Error: File does not exist.")
        return
    
    cap = cv2.VideoCapture(filepath)
    print("[INFO] Video file opened. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[INFO] End of video file reached.")
            break

        censored_frame = censor_faces(frame)
        cv2.imshow('C.O.V.E.R.T. = Censorship Operations & Video Encrypted Real-Time Tracking', censored_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def process_video_export():
    """
    (Option 3)
    Exports a video file to .mp4 format. 
    """
    filepath = input("Enter the path to the video file: ")

    if not os.path.isfile(filepath):
        print("Error: File does not exist.")
        return
    output_filepath = input("Enter the output path for the .mp4 file: ")

    cap = cv2.VideoCapture(filepath)

    #Retrieve the original video's properties needed for VideoWriter
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
    out = cv2.VideoWriter(output_filepath, fourcc, fps, (width, height))

    print("[INFO] Exporting video to .mp4.(please be patient, this may take some time depending on the video length)")

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[INFO] End of video file reached.")
            break

        censored_frame = censor_faces(frame)
        out.write(censored_frame)

        frame_count += 1
        # Print progress every 30 frames
        if frame_count % 30 == 0:  
            print(f"[INFO] Processed {frame_count} frames.")

    cap.release()
    out.release()
    print(f"[INFO] Video exported to {output_filepath} successfully.")


def main():
    while True:
        print("\n" + "="*30)
        print("C.O.V.E.R.T. = Censorship Operations & Video Encrypted Real-Time Tracking")
        print("="*30)
        print("1. Process live camera feed")
        print("2. Process video file")
        print("3. Export video file to .mp4 [Note: This feature is still in development]")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            process_live_camera()
        elif choice == '2':
            process_video_preview()
        elif choice == '3':
            process_video_export()
        elif choice == '4':
            print("Exiting the program.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    
if __name__ == "__main__":
    main()

