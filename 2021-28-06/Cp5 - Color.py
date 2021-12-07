import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

src = cv.imread("montanha.jpg") 
org = cv.cvtColor(src,cv.COLOR_BGR2RGB) #Converte as cores de BGR para RGB
hsv = cv.cvtColor(src,cv.COLOR_BGR2HSV) #Aqui realiz-se a conversão de BGR para HSV
hsl = cv.cvtColor(src,cv.COLOR_BGR2HLS) #De BGR para HSL

plt.subplot(1,3,1) #Define a exbição com 1 linhas, 3 colunas e o indice na qual a imagem irá, no caso o primeiro indice
plt.title("Original") #Titulo para cada plot
plt.imshow(org) #plot desejado

plt.subplot(1,3,2)
plt.title("HSV")
plt.imshow(hsv)

plt.subplot(1,3,3)
plt.title("HSL")
plt.imshow(hsl)

plt.show()
















