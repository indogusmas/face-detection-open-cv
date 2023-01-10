import cv2
import numpy as numpy

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
camera  = cv2.VideoCapture(0);
#camera = cv2.imread('test.jpg');

while(True):
    ret,img = camera.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Face",img);
    if(cv2.waitKey(1) == ord('q')):
        break;
camera.release()
cv2.destroyAllWindows()