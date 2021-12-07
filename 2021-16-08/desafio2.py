import numpy as np
import cv2 as cv

img = cv.imread("DadosTeste.jpg") #Leitura da imagem
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #Conversão de BGR para GRAY scale
blur = cv.GaussianBlur(imgGray,(5,5),0) #Aplicação de filtro Gaussiano com kernel de 5 x 5
ret, bin = cv.threshold(blur,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU) #Threshold da imagem com a flag OTSU

conts,_ = cv.findContours(bin,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) #Identificando todos os contornos da imagem

pipe = 0 #Inicializa os numeros de pipes do dado como 0
countPipe = 0 #Inicializa o contador de pipe dos dados

for cont in conts: #Laço para utilizar um auxiliar, denominado de cont, em conts
    curvas = cv.arcLength(cont,True) #Atribui a um objeto o método de calculos de curva dos contornos previamente determinados (linha 9)
    if(curvas<200):  #caso o comprimento de curva for menor que 100, ou seja, isso garante que apenas circulos devem ser identificados 
        if(countPipe == 0): 
            pipe += 1 #Adição da quantidade de pipes dentro da imagem

print(f"A o resultado da soma dos dados é {pipe}")

cv.drawContours(img,conts,-1,(0,255,0),2)   
cv.imshow("Dados",img)
cv.waitKey(0)          