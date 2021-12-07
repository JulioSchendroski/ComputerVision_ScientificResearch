import cv2 as cv #Importa biblioteca do opencv
import numpy as np # Importa biblioteca numpy
from matplotlib import pyplot as plt # Importa da biblioteca matplotlib apenas a função pyplot


img = cv.imread('color.jpg') # Definde uma imagem com seu respectivo nome e formato para uma variável "img"
blue = img[:, :, 0] #Utilizando de slicing, presente na biblioteca numpy, para selecionar todos pixels das coordenadas Y e X, sendo altura e largura respectivamente
green = img[:, :, 1] # Define-se no final o código que representa o canal desejado, sendo 0 = Blue, 1 = Green, 2 = Red
red = img[:, :, 2]
img = cv.cvtColor(img, cv.COLOR_BGR2RGB) # O openCV utuliza-se de BGR invés de RGB, causando imcompatibilidade que a bilbioteca matplotlib, que utiliza-se RGB

plt.subplot(221) # Utiliza-se da função subplot, que recebe como parâmetro as linhas e colunas a serem dispostos
plt.title('ORIGINAL') # Comando para nomear cada plot da imagem
plt.imshow(img) # Função para plotar a variável "img"

plt.subplot(222) # A disposição como parâmetro é linhas, colunas e o quadrante a ser posto a imagem trabalhada
plt.title('BLUE') # Intitula o gráfico como "BLUE"
plt.imshow(blue,cmap='gray') # Usa a imagem "blue" e utiliza-se da função "cmap=" para trabalhar com a escala cinza, usando a string "gray" como a cor definida

plt.subplot(223)
plt.title('GREEN')
plt.imshow(green,cmap='gray')

plt.subplot(224)
plt.title('RED')
plt.imshow(red,cmap='gray')

plt.show() # Função para dispor todas as imagens construidas em uma unica janela