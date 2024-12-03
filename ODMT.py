
import cv2
import datetime
import os
import mysql.connector
from ultralytics import YOLO  # For YOLO, install with `pip install ultralytics`
from ultralytics.utils.plotting import Annotator

# Load YOLO model
model = YOLO("yolov8x.pt")  # Replace with your model file path

# Initialize webcam
cap = cv2.VideoCapture(0)  # Change index if you have multiple cameras

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30

# Create VideoWriter with date-time-stamped filename
date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"output_{date_time}.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

# Directory to save detected images
save_dir = "detected_images"
os.makedirs(save_dir, exist_ok=True)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",       # Replace with your MySQL username
    password="9717367529",   # Replace with your MySQL password
    database="yolo_detection",  # Ensure the database exists
    port="3306"
)
cursor = db.cursor()

print(f"Recording started: {output_file}")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video frame is empty or video processing has been successfully completed.")
            break

        # Perform object detection
        results = model.predict(frame, conf=0.5)  # Adjust confidence threshold
        boxes = results[0].boxes  # Get bounding boxes

        # Only proceed if objects are detected
        if len(boxes) > 0:
            # Annotate detected objects on the frame
            annotated_frame = results[0].plot()  # Annotated frame

            
            for box in boxes:
                class_name = model.names[int(box.cls)]  # Get class name
                confidence = float(box.conf)  # Confidence score

                # Save the frame as an image with a timestamp
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Corrected timestamp format
                image_filename = f"{save_dir}/detected_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')}.jpg"
                cv2.imwrite(image_filename, frame)  # Save the frame as an image
                print(f"Image saved: {image_filename}")

                # Insert detection data into the database
                insert_query = """
                INSERT INTO detections (timestamp, detected_class, confidence, image_path)
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_query, (timestamp, class_name, confidence, image_filename))
                db.commit()
                print(f"Detection saved to database: {class_name} ({confidence:.2f})")


            # Write the annotated frame to the video output
            out.write(annotated_frame)

            # Display the annotated frame
            cv2.imshow("YOLO Object Detection", annotated_frame)
        else:
            # If no objects are detected, display the original frame
            cv2.imshow("YOLO Object Detection", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    cursor.close()
    db.close()
    print(f"Recording saved as {output_file}")



