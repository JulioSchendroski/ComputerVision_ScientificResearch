import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

src = cv.imread("fish.jpg")
srcRGB = cv.cvtColor(src,cv.COLOR_BGR2RGB) #Conversão da imagem "src" de BGR para RGB
srcREDM = srcRGB[::2,::2]

colors = ("b","g","r") #Definimos para a variável "colors" uma lista que irá receber para cada cor
channels = cv.split(srcREDM) #Cria-se uma variável "channels" para dividir as cores da imagem original, através do split

for (channel, color) in zip(channels, colors): #Loop para acessar cada um dos três canais de cores, que definimos através da lista "colors"
    hist = cv.calcHist([channel],[0],None,[256],[0,256]) #Função para calcular o histograma de cada canal de cor da imagem "srcRGB" , e defindo os parâmetros 
    plt.plot(hist,color = color) #Plotagem pela matplolib
    plt.xlabel("Intensidade") #Denominação para o eixo x
    plt.ylabel("Qtd Pixel") #Denominação para o eixo y

plt.show()
cv.imshow("img", src)
cv.waitKey(0)

print(srcRGB.size)