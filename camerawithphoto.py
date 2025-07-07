import cv2

cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    if not ret:
        print("FAILED TO GRAB FRAME")
        break
    cv2.imshow("press 's' to Save", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite("sd.jpg", frame)
        print("sd.jpg saved")
        break
    elif key == ord('q'):
        print("EXIT WITHOUT SAVING")
        break

cap.release()
cv2.destroyAllWindows()