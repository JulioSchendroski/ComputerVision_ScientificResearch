import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread("campoColorido.jpg")
img = cv.cvtColor(img,cv.COLOR_BGR2RGB) #Conversão da imagem para RGB

img_reduzida_metade = cv.resize(img,(600,375)) #Redução das dimensões da imagem pela metade
img_ampliada_dobro = cv.resize(img,(2400,1500)) #Ampliação das dimensões da imagem em dobro


print(img.size) #Mostra quantidade de pixels presents na imagem
print(img_reduzida_metade.size)
print(img_ampliada_dobro.size)


colors = ("b","g","r") #Cria-se uma tupla com cada cor dos canais
channels = cv.split(img) #Realiza-se um split da imagem original, ou seja, divide-se o canal de cor [3] em três variáveis
channelsRedz = cv.split(img_reduzida_metade)
channelsAmpl = cv.split(img_ampliada_dobro)

for (channel, color) in zip (channels, colors): #Loop para acessar tanto os canais do split, e tanto o que cada variável irá receber, utilizando de dois auxiliares
    hist = cv.calcHist([channel],[0],None,[256],[0,256]) #Usa-se um método de calculo de histograma, acessando a tupla de canais, de um intervalo de 0 - 256
    plt.subplot(2,3,1), plt.title("Original") #Plot das imagens com titulo específico
    plt.plot(hist,color=color) #Plot do histograma colorido

for (channel, color) in zip (channelsRedz, colors):
    hist = cv.calcHist([channel],[0],None,[256],[0,256])
    plt.subplot(2,3,2), plt.title("Reduzido")
    plt.plot(hist,color=color)

for (channel, color) in zip (channelsAmpl, colors):
    hist = cv.calcHist([channel],[0],None,[256],[0,256])
    plt.subplot(2,3,3), plt.title("Ampliada")
    plt.plot(hist,color=color)

plt.subplot(2,3,4),plt.imshow(img)
plt.subplot(2,3,5),plt.imshow(img_reduzida_metade)
plt.subplot(2,3,6),plt.imshow(img_ampliada_dobro)

plt.show()

