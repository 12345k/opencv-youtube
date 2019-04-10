import cv2
import numpy as np
video_capture = cv2.VideoCapture(0)

while True:
    _,frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray,100, 200)

    cv2.imshow("edge",edged)
    cv2.imshow("frame",frame)
   

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()