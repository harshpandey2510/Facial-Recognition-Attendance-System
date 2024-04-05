import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Load known faces and their encodings
yourname_image = face_recognition.load_image_file("faces/yourname.jpeg")
yourname_encoding = face_recognition.face_encodings(yourname_image)[0]

yourfriend1_image = face_recognition.load_image_file("faces/yourfriend1.jpeg")
yourfriend1_encoding = face_recognition.face_encodings(yourfriend1_image)[0]

# Load images and encodings for additional individuals
yourfriend2_image = face_recognition.load_image_file("faces/yourfriend2.jpeg")
yourfriend2_encoding = face_recognition.face_encodings(yourfriend2_image)[0]

yourfriend3_image = face_recognition.load_image_file("faces/yourfriend3.jpeg")
yourfriend3_encoding = face_recognition.face_encodings(yourfriend3_image)[0]

# Update known face encodings and names lists
known_face_encodings = [yourname_encoding, yourfriend1_encoding, yourfriend2_encoding, yourfriend3_encoding]
known_faces_names = ["YourName", "YourFriend1", "YourFriend2", "YourFriend3"]

# List of expected students
students = known_faces_names.copy()

# Initialize CSV file
now = datetime.now()
current_date = now.strftime("%d-%m-%y")
f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

# Main loop for face recognition
while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_faces_names[best_match_index]

            # Add text if the person is present
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_COMPLEX_SMALL
                topLeftCornerOfText = (20, 50)
                fontScale = 1
                fontColor = (0, 255, 0)  # Green color
                thickness = 2
                lineType = 2

                # Add shadow effect
                cv2.putText(frame, name + " - Present", (topLeftCornerOfText[0] + 2, topLeftCornerOfText[1] + 2),
                            font, fontScale, (0, 0, 0), thickness, lineType)

                # Add the text
                cv2.putText(frame, name + " - Present", topLeftCornerOfText, font, fontScale, fontColor, thickness,
                            lineType)

            # If the student is recognized, remove from the list and record attendance
            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])

    # Display frame
    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release video capture and close CSV file
video_capture.release()
cv2.destroyAllWindows()
f.close()
