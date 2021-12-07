import cv2 as cv
import numpy as np


img = cv.imread('9.jpeg')
resized = cv.resize(img,(600,400))

gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(9,9),0)
_,bin = cv.threshold(blur,90,255,cv.THRESH_BINARY_INV)
edges = cv.Canny(bin,170,240)
hist = cv.equalizeHist(gray)



cv.imshow('Edge',edges)
cv.imshow('Imagem',img)
cv.imshow('Bin',bin)
#cv.imshow('Hist',hist)
#cv.imshow('Gray',gray)


#cv.imwrite("Contorno3.jpeg",edges)

#Como pegar um contorno dentre a lista de contornos? Como selecionar o melhor contorno?
#273,50, por exemplo o contorno que tem esse pixel?

cv.waitKey(0)