import cv2 as cv
import numpy as np

img = cv.imread('C:\\Codes\\ifsp_ic_julio\\2021-16-08\\Imagens\\quadrado.jpg',cv.IMREAD_GRAYSCALE)
blur = cv.GaussianBlur(img,(5,5),0)
_,bin = cv.threshold(blur,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

conts,_ = cv.findContours(bin,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
for cont in conts:
    area = cv.contourArea(cont)
    perimeter = cv.arcLength(cont,True)

print(area)
print(perimeter)

cv.imshow('Image',bin)
cv.waitKey(0)
cv.destroyAllWindows()