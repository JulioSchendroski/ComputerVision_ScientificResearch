import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

src = cv.imread("C:\\Codes\\ifsp_ic_julio\\2021-16-08\\Imagens\\gato1.jpeg",cv.IMREAD_GRAYSCALE) #Definindo a imagem a ser trabalhada, e também é selecionado uma flag para tal, no cas é escala cinza
src_redm = src[::2,::2] #Redmensionamento da imagem, utilizando slicing 
hist = cv.calcHist([src_redm],[0],None,[256],[0,255]) #Calculo do histograma, utilizando o redmensionamento da imagem original e definindo os intervalos
hist_eq = cv.equalizeHist(src_redm) #Função para equalizar o histograma, ou seja, uma melhor divisão dentre as intensidades de cor, na escala cinza, em toda a imagem

plt.plot(hist) #Plotagem do histograma original, sem equalizar
plt.hist(src_redm.ravel(),256,[0,256]) #Comando reavel() irá tranformar uma matriz bidimensional, em uma matriz unidimensional
plt.hist(hist_eq.ravel(),256,[0,256]) #Plotando o histograma equaliazdo, utilizando novamente o ravel()




plt.ylabel("Qtd Pixel"), plt.xlabel("Intensidade") #Definindo o significado de cada eixo
plt.show()


cv.imshow("Original",src_redm)
cv.imshow("Equalizado",hist_eq)
cv.waitKey(0)














#print(src.size)
#cv.imshow("Img", src)
#cv.waitKey(0)


