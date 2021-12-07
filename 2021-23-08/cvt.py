import cv2 as cv
import numpy as np

cor = np.uint8([[[10,10,10]]])
hsv = cv.cvtColor(cor,cv.COLOR_BGR2HSV)
print(hsv)