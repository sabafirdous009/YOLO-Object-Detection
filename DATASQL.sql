CREATE DATABASE yolo_detection;

USE yolo_detection;

CREATE TABLE detections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    detected_class VARCHAR(255) NOT NULL,
    confidence FLOAT NOT NULL,
    image_path VARCHAR(255) NOT NULL
);