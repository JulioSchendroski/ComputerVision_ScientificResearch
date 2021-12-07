import cv2 as cv
import numpy as np

img = cv.imread('C:\\Codes\\ifsp_ic_julio\\2021-16-08\\Imagens\\Planta.jpg')
lower_green = np.array([27,53,37])
upper_green = np.array([37,105,77])
mask = cv.inRange(img,lower_green,upper_green)

conts,_ = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
for cnt in conts:
    cv.drawContours(img,conts,-1,(0,0,255),3)
    if upper_green.any():
        print("Deu certo?")
    else:
        print("Deu errado?")

cv.imshow("Imagem",img)
cv.imshow("Mask",mask)
cv.waitKey(0)