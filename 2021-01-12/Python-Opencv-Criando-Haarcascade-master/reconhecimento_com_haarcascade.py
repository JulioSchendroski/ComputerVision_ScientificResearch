import numpy as np
import cv2


cascade = cv2.CascadeClassifier('haarcascade_martelo.xml')
img = cv2.imread('images/martelo2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hammers = cascade.detectMultiScale(gray, scaleFactor=1.08, minNeighbors=4)


for(x, y, w, h) in hammers:
    detectada = cv2.rectangle(img, (x, y), (x + w, y + h), (116, 90, 53), 2, cv2.LINE_AA)

cv2.imshow('Img', detectada)
cv2.waitKey()
cv2.destroyAllWindows()
