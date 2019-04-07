import cv2

eye_cascade = cv2.CascadeClassifier("eye.xml") 

video_capture = cv2.VideoCapture(0)

while True:
    _,frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    eye_detect =  eye_cascade.detectMultiScale(
        gray,scaleFactor=1.3,minNeighbors=20,flags =cv2.CASCADE_SCALE_IMAGE,
        minSize=(30,30)
    )
    

 
    for (x,y,w,h) in eye_detect:
        x_center = int((x+(x+w))/2)
        y_center = int((y+(y+h))/2)
        cv2.circle(frame,(x_center,y_center),20,(0,0,255),5)

    cv2.imshow('Webcam',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()