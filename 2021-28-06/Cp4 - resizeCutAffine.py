import cv2 as cv
import numpy as np

src = cv.imread('campo.jpg') #Leitura da imagem existente no sistema

resized = src[::2, ::2] #Método de modificar as dimensões da imagem, utilizando slice interpolado

cut = resized[145:269, 112:234] #Seleciona uma área específica da imagem e recorta ele, novamente utilizando slicing

cut_flip = cv.flip(cut, 1) # Função para rotacionar a umagem, no caso foi rotacionado o corte realizado anteriormente, e o código do flip é -1, ou seja, irá inverter as coodenadas x e y

center = (62,61) #Determinando o centro do corte realizado "cut"

matrix = cv.getRotationMatrix2D(center,90,1.0) #Função responsável por transformar uma imagem em uma matriz  2 x 3, utilizando como parâmetro o centro da imagem, a rotação em graus e a escala

cut_flip = cv.warpAffine(cut_flip,matrix,(123,126)) #Aqui finalmente é a rotoção da imagem e torno do próprio centro, utilizando o affine.


cv.imshow("Original", resized)
cv.imshow("Mod", cut_flip)
cv.imwrite("Modified.jpg",cut_flip) #Gera uma imagem no sistema modificada
cv.waitKey(0)
