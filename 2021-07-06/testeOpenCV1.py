import numpy as np #importa numpy
import cv2 as cv #importa cvopen

img = cv.imread('lotr.jpg')
px = img[100, 100]
print(px)

blue =  img[100,100,0]
print(blue)

print(img.size)


#cv.namedWindow('Teste')
#cv.imshow('Teste',img)
#cv.waitKey()