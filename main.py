import cv2
import cvzone
cap = cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
filter=input("which filter do you want from following options:sunglass.png,beard.png,""cool.png,pirate.png,star.png:")
overlay=cv2.imread(filter,cv2.IMREAD_UNCHANGED)
while True:
    _,frame = cap.read()
    faces=cascade.detectMultiScale(frame)
    for (x,y,w,h) in faces:
        frame=cvzone.overlayPNG(frame,overlay)
    cv2.imshow('snapit', frame)
    if cv2.waitKey(10) == ord('q'):
        break

