import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def contornos(fileName,kernelValue,cannyValue1,cannyValue2,contType,color=(0,0,0)): #Méotodo para realizar todos processos necessários na imagem para encontrar os contornos
    img = cv.imread(fileName)
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #conversão da imagem para escala cinza
    imgSmooth = cv.GaussianBlur(imgGray,(kernelValue,kernelValue),0) #Aplicação do filtro Gaussiano com kernel de passado como parâmetro
    _,thresh = cv.threshold(imgSmooth,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU) #threshold da imagem com o método OTSU, para uma binarização mais precisa
    edges = cv.Canny(thresh,cannyValue1,cannyValue2) #Detecção de bordas com Canny, utilizando novamente os parâmetros como valor
    contours,_ = cv.findContours(edges,contType,cv.CHAIN_APPROX_NONE) #Localiza os contornos, passado como parâmetros o tipo de contorno que o método deve econtrar, em forma de flag
    cv.drawContours(img,contours, -1,color ,3) #Desenha os contornos na imagem orgiginal, utilizando dos contornos previamentes determinados e aplicado na imagem original
    cv.putText(img,("Quantiade de contorno : ")+str(len(contours)),(10,15),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1,cv.LINE_AA) #Adiciona uma texto na tela com um contador da quantidade de bordas encontradas durante o processo
    cv.imwrite("Contornos.jpg",img)

def exibir(fileName):
    cv.imshow("Cont ",cv.imread(fileName))
    cv.waitKey(0)

    
#contornos("Objetos.jpg",5,127,200,cv.RETR_TREE, (0,255,255))
contornos("dice.jpg",5,127,200,cv.RETR_TREE,(255,0,0))
exibir("Contornos.jpg")

#O objeto deve ser sempre branco e o fundo preto, para uma melhor definição dos contornos

#Realizar o desafio proposto pelo livro.

#flags de contornos : cv.RETR_EXTERNAL (Seleciona apenas os extremos da imagem)
# cv.RETR_LIST (Seleciona todos os contornos, estabelecendo uma hierarquia)
# cv.RETR_CCOMP (Seleciona em duas hierarquias, os extremos, e a segunda hierarquia é os furos e buracos na imagem)
# cv.RETR_TREE (Seleciona todos os contornos e estebelece uma hierarquia apenas dos contornos)
