import cv2
import datetime

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        print("FAILED TO GRAB FRAME")
        break

    cv2.imshow("Live Feed - Press 's' to Save | 'q' to Quit", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        filename = datetime.datetime.now().strftime("image_%Y%m%d_%H%M%S.jpg")
        cv2.imwrite(filename, frame)
        print(f"{filename} saved")
        break
    elif key == ord('q'):
        print("EXIT WITHOUT SAVING")
        break

cap.release()
cv2.destroyAllWindows()

