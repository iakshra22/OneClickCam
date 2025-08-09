import cv2
import datetime

# Start capturing from default camera (0)
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        print("Unable to grab video frame. Please try again")
        break

    cv2.imshow("Live Feed - Press 's' to Save | 'q' to Quit", frame)

    key_pressed = cv2.waitKey(1) & 0xFF

    if key_pressed == ord('s'):
        # Generate a unique filename with timestamp
        timestamp = datetime.datetime.now().strftime("image_%Y%m%d_%H%M%S.jpg")
        cv2.imwrite(timestamp, frame)
        print(f"Image saved as {timestamp}")
        break

    elif key_pressed == ord('q'):
        print("Exited without saving the image.")
        break

# Release the webcam and destroy OpenCV windows
cap.release()
cv2.destroyAllWindows()
