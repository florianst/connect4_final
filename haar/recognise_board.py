import numpy as np
import cv2
board_cascade = cv2.CascadeClassifier('lbp/cascade.xml')
img = cv2.imread('test/0061_0038_0014_0159_0159.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = board_cascade.detectMultiScale(gray)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()