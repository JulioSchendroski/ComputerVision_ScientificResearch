import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

src = cv.imread('fish.jpg')
imgBGR = src[::2,::2] #Redmensiona a imagem, utilizando slicing 
imgRGB = cv.cvtColor(imgBGR, cv.COLOR_BGR2RGB) #Converte-se a imagem BGR para RGB, devido o matplotlib utiliazr apenas RGB
blue,green,red = cv.split(imgBGR) #Realiza-se o split, para as três variáveis de cor, blue, gree, red

plt.subplot(2,3,1)  #Define a exbição com 2 linhas, 3 colunas e o indice na qual a imagem irá, no caso o primeiro indice
plt.title('Original BGR') #Titulo para a imagem
plt.imshow(imgBGR) #Plotagem da imagem "imgBGR"

plt.subplot(2,3,2)
plt.title('Original Convertida (RGB)')
plt.imshow(imgRGB)

plt.subplot(2,3,3)
plt.title('Blue HOT')
plt.imshow(blue,cmap="hot") #Utilizando de um color map "gray" para trabalhar com imagens na escala cinza
#Verificar outras opções de color map : https://matplotlib.org/stable/tutorials/colors/colormaps.html

plt.subplot(2,3,4)
plt.title('Green BWR')
plt.imshow(green, cmap="bwr")

plt.subplot(2,3,5)
plt.title('Red')
plt.imshow(red,cmap="gray")


plt.show()
