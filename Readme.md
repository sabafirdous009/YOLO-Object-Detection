# Object Detection Using YOLO Model
This project uses the YOLO (You Only Look Once) model for real-time object detection with a webcam feed. Detected objects are annotated on the video, saved as images, and logged into a MySQL database for further analysis.

# Features
Real-time object detection using YOLO.
Saves detected objects' details, including class, confidence score, and image, into a MySQL database.
Captures annotated video with detections and saves it locally.
Supports saving detected frames as individual images.

# Setup Instructions
1. Install the required libraries by running `pip install -r requirements.txt` in your terminal
2. Install the YOLO model using the following command: `python -m pip
3. Install the MySQL connector using the following command: `pip install mysql-connector-python`
4. Configure the MySQL database connection settings in the `config.py` file
5. Run the script using `python main.py`

### Prerequisites
Python 3.12 (recommended to use Conda environment).
MySQL installed and configured.
Webcam or external camera for real-time detection.


# Environment Setup
### Create Conda Environment:

#### bash
conda create --name yolo_env python=3.12 -y
conda activate yolo_env
Install Required Packages: Use the following command to install the dependencies:

#### bash
pip install ipykernel ultralytics opencv-python mysql-connector-python
Verify Installation:

#### bash
python -c "import cv2, mysql.connector, ultralytics; print('All packages are installed!')"
Database Setup
Create Database: Open MySQL and run:

#### sql
CREATE DATABASE yolo_detection;
USE yolo_detection;
Create Table:

#### sql
CREATE TABLE detections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    detected_class VARCHAR(255) NOT NULL,
    confidence FLOAT NOT NULL,
    image_path VARCHAR(255) NOT NULL
);
YOLO Model
Model Used: YOLOv8
Custom Model: yolo11m.pt
Place the model file in the project directory.
Update the file path in the script:

model = YOLO("yolo11m.pt")
Running the Project
Start the Application: Run the script using:

#### bash
python app.py
Output:

Annotated video is saved in the format: output_YYYY-MM-DD_HH-MM-SS.mp4.
Detected images are saved in the detected_images/ directory.
Detected objects are logged in the detections table in the yolo_detection database.
Terminate the Application:

Press q to stop the application gracefully.
Project Structure
plaintext

project/
│
├── app.py                  # Main application script
├── requirements.txt        # List of Python dependencies
├── detected_images/        # Directory for saving detected frames
├── yolo11m.pt              # YOLO custom model file
└── README.md               # Project documentation

## Requirements
The following Python packages are required:

ipykernel
ultralytics
opencv-python
mysql-connector-python
datetime
Key Features
Real-Time Detection: Uses YOLOv8 to detect objects in the video stream.

Database Integration: Stores detection details (timestamp, detected_class, confidence, image_path) into a MySQL database.

Annotated Output: Annotates detected objects directly on the video frames.

# Contributions
Contributions to improve the code or add new features are welcome! Fork this repository and create a pull request with your changes.

# License
This project is licensed under the MIT License.

Let me know if you'd like any further changes or additions to the README!






