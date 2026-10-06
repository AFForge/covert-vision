import cv2
import sys
import os
from censor import censor_faces

def get_optimal_format(output_filepath):
    """
    Determines the optimal format code based on the output file extension.
    """
    base_name, ext = os.path.splitext(output_filepath)
    ext = ext.lower()

    if ext == '.mp4':
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MPEG-4
        return fourcc, output_filepath
    elif ext == '.mkv':
        fourcc = cv2.VideoWriter_fourcc(*'X264')  # H.264
        return fourcc, output_filepath
    
    else:
        print(f"[WARNING] Unsupported output format '{ext}'. Defaulting to .mp4.")
        output_filepath = base_name + '.mp4'
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MPEG-4
        return fourcc, output_filepath
    

def process_live_camera(style):
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

        censored_frame = censor_faces(frame, style)

        cv2.imshow('C.O.V.E.R.T. = Censorship Operations & Video Encrypted Real-Time Tracking', censored_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def process_video_preview(style):
    """
    (Option 2)
    Processes a video file and censors detected faces in a preview window.
    """
    filepath = input("Enter the path to the video file: ").strip()

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

        censored_frame = censor_faces(frame, style)
        cv2.imshow('C.O.V.E.R.T. = Censorship Operations & Video Encrypted Real-Time Tracking', censored_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def process_video_export(style):
    """
    (Option 3)
    Exports a video file to the format specified by the user's output extension.
    """
    filepath = input("Enter the path to the input video file: ").strip()

    if not os.path.isfile(filepath):
        print("Error: File does not exist.")
        return
    output_filepath = input("Enter the output path for the file: ").strip()

    cap = cv2.VideoCapture(filepath)

    #Retrieve the original video's properties needed for VideoWriter
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #Define the codec and create VideoWriter object
    fourcc, output_filepath = get_optimal_format(output_filepath)
    out = cv2.VideoWriter(output_filepath, fourcc, fps, (width, height))

    print(f"[INFO] Exporting video to {output_filepath}.(please be patient, this may take some time depending on the video length)")

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[INFO] End of video file reached.")
            break

        censored_frame = censor_faces(frame, style)
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


        while True:
            print("Select a censorship style:")
            print("1. Blackout")
            print("2. Pixelate")
            censorship_style = input("Enter your choice (1-2): ").strip()
            if censorship_style == '1':
                style = "blackout"
                break
            elif censorship_style == '2':
                style = "pixelate"
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
                
        while True:
            print("Select an option:")
            print("1. Process live camera feed")
            print("2. Process video file")
            print("3. Export video file to choosen extension")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == '1':
                process_live_camera(style)
            elif choice == '2':
                process_video_preview(style)
            elif choice == '3':
                process_video_export(style)
            elif choice == '4':
                print("Exiting the program.")
                sys.exit(0)
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
    
if __name__ == "__main__":
    main()

