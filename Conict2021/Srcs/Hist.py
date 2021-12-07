import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("5.jpeg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
equalized = cv.equalizeHist(gray)
cv.calcHist([gray],[0],None,[256],[0,255]) 



plt.hist(gray.ravel(),256,[0,256])
plt.hist(equalized.ravel(),256,[0,256])

plt.ylabel("Qtd Pixel"), plt.xlabel("Intensidade") #Definindo o significado de cada eixo

plt.show()



#cv.calcHist([src_redm],[0],None,[256],[0,255]) 