import cv2

img = cv2.imread("test.jpeg");
model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

faces = model.detectMultiScale(img);

for x,y,width,height in faces:
    cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,0),10)
cv2.imshow("Face",img);
cv2.waitKey(0)
cv2.destroyAllWindows()