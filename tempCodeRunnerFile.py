import face_recognition
import cv2

# Test the camera feed
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Camera feed not available.")
        break

    cv2.imshow("Testing Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

