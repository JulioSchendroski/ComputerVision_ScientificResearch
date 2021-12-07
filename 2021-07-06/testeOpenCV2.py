import numpy
import cv2 as cv

img = cv.imread('C:\Codes\Thiago\ottis.jpg')
cv.namedWindow('teste')
cv.imshow('teste', img)
cv.waitKey(0)