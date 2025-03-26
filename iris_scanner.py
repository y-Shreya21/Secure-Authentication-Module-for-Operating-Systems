import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Download from dlib repo

def get_eye_region(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)
        x1, y1 = landmarks.part(36).x, landmarks.part(36).y  # Left eye
        x2, y2 = landmarks.part(39).x, landmarks.part(39).y
        return gray[y1-10:y2+10, x1-10:x2+10]  # Crop the eye region

    return None

camera = cv2.VideoCapture(0)
while True:
    ret, frame = camera.read()
    if not ret:
        break

    eye_region = get_eye_region(frame)
    if eye_region is not None:
        cv2.imshow("Iris", eye_region)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
