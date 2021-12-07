import numpy as np #Importando a biblioteca numpy (numpy = np)
import cv2 as cv #Biblioteca  openCV, adicionada como cv2 = cv

img = cv.imread('LogoTeste.png', cv.IMREAD_GRAYSCALE)
#Define a variável img, com a função de ler uma imagem com seu diretório ou nome, em seguida é declarado a maneira em que será exibida
cv.namedWindow('Ola') #Comando para nomear a janela como 'teste cvOpen'
cv.imshow('Ola', img) #Exibir imagem 
cv.waitKey() #Definir um tempo ou keyboard para fechar a janela
