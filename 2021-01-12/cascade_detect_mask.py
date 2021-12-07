import cv2 as cv
import numpy as np

cascade = cv.CascadeClassifier("cascade.xml")
img = cv.imread("vaca.jpg")
resized = cv.resize(img, (320,240))
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

heifers = cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3)
for (x, y, w, h) in heifers:
    cv.rectangle(resized, (x, y), (x + w, y + h), (0,255,255), 2, cv.LINE_AA)

#print((w,h))

cv.imshow("Img", resized)
cv.waitKey(0)
cv.destroyAllWindows()

#24 altura, 32 largura