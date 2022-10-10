from cmath import rect
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
kernel = np.ones((3, 3), dtype = np.uint8)

while True:
    rect, frame = cap.read()
    if rect:
        # frame = cv2.filp(frame, 0)
        # frame = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)

        cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()