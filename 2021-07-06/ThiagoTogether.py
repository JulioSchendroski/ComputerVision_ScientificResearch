import numpy as np #importa numpy
import cv2 as cv #importa cvopen

img = cv.imread('lotr.jpg',cv.IMREAD_COLOR)
#px = img[100, 100]
#print(px)

cv.namedWindow('Teste1')
cv.imshow('Teste1',img)
cv.resizeWindow('Teste1',1280,720)
cv.waitKey(0)

img2 = cv.imread('lotr.jpg', cv.IMREAD_GRAYSCALE)
px = img2[100, 100]
print(px)
cv.namedWindow('Teste2') #Comando para nomear a janela como 'teste cvOpen'
cv.imshow('Teste2', img2) #Exibir imagem 
cv.resizeWindow('Teste2',1280,720)
cv.waitKey() #Definir um tempo ou keyboard para fechar a janela
