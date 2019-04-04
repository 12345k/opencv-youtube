import cv2

face_cascade = cv2.CascadeClassifier("face.xml")

video_capture = cv2.VideoCapture(0)

while True:
    _,frame = video_capture.read()

   

    face_detect =  face_cascade.detectMultiScale(
        frame,scaleFactor=1.1,minNeighbors=5,flags =cv2.CASCADE_SCALE_IMAGE,
        minSize=(30,30)
    )
    

    for (x,y,w,h) in face_detect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)


    cv2.imshow('Webcam',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()