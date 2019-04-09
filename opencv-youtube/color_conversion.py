import cv2
import numpy as np
video_capture = cv2.VideoCapture(0)

while True:
    _,frame = video_capture.read()

    frame = cv2.resize(frame, (440, 440), interpolation = cv2.INTER_LINEAR) 

    # Color Conversions 
    gray=cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    xyz = cv2.cvtColor(frame, cv2.COLOR_RGB2XYZ)
    ycc = cv2.cvtColor(frame, cv2.COLOR_RGB2YCrCb)
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    hls = cv2.cvtColor(frame, cv2.COLOR_RGB2HLS)
    lab = cv2.cvtColor(frame, cv2.COLOR_RGB2Lab)
    luv = cv2.cvtColor(frame, cv2.COLOR_RGB2Luv)

    # Making into single frame row
    row1 = np.hstack((frame,xyz,ycc))
    row2 = np.hstack((hsv,hls,lab,luv))
    
    cv2.imshow("frame,xyz,ycc",row1)
    cv2.imshow("gray",gray)
    cv2.imshow("hsv,hls,lab,luv",row2)
   

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()