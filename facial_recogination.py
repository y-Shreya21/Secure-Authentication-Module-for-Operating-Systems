import cv2
import face_recognition

# Initialize the camera
camera = cv2.VideoCapture(0)

# Load the known face
known_face = face_recognition.load_image_file("C:\Users\dell\Downloads\WhatsApp Image 2025-03-26 at 10.03.50 AM.jpeg")
known_encoding = face_recognition.face_encodings(known_face)[0]

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()
    if not ret:
        break

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([known_encoding], face_encoding)
        if True in matches:
            print("Face recognized!")
            camera.release()
            cv2.destroyAllWindows()
            exit()

    # Display the resulting frame
    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
camera.release()
cv2.destroyAllWindows()