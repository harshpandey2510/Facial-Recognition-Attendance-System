# Facial-Recognition-Attendance-System
Face Recognition Attendance System
This repository contains a Python script for a face recognition-based attendance system. The script utilizes the face_recognition library along with OpenCV for real-time face recognition from a webcam feed.

Features
Face Recognition: The script can recognize faces of known individuals in real-time using pre-trained face recognition models.

Attendance Tracking: It tracks the attendance of recognized individuals by recording their names and timestamps in a CSV file.

Requirements
Python 3.x
face_recognition library
OpenCV (cv2)
NumPy
CSV module
Setup
Clone the repository to your local machine.
Ensure you have Python 3.x installed along with the required libraries (face_recognition, OpenCV, NumPy).
Place the images of known individuals in the faces directory.
Update the script with the filenames of the images and their corresponding names.
Run the script.
Usage
Run the script using Python (python script.py).
The webcam feed will start, and faces will be recognized in real-time.
Recognized faces will have their attendance recorded in a CSV file named with the current date.
Customization
Adding Known Faces: Add images of known individuals to the faces directory and update the script with their filenames and names.

Customizing Output: You can customize the output format, such as changing the CSV file name format or adjusting the text displayed for recognized individuals.

Note
Ensure proper lighting conditions and clear images of known individuals for better recognition accuracy.
This script is for educational purposes and can be further extended or modified based on specific requirements.
