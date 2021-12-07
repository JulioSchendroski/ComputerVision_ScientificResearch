import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def CannyMetodo(fileName,size,blurKernel, threshValue1,threshValue2): #Método para reconhecimento de bordas com Canny
    img = cv.imread(fileName,cv.IMREAD_GRAYSCALE)[::size,::size] #Leitura da imagem com escala cinza e possibilidade de redmensionar a imagem com slicing de uma tupla
    img = cv.GaussianBlur(img,(blurKernel,blurKernel),0) #Aplica O filtro Gaussiano
    imgCanny  = cv.Canny(img, threshValue1,threshValue2) #Detecção de bordas com o método Canny
    return imgCanny #Retorno da imagem que foi reconhecido as bordas


def Blend(Src1,alpha,Src2,beta,gamma): #Método para juntar imagens
    dst = cv.addWeighted(Src1,alpha,Src2,beta,gamma) #Função de adicionar imagem e sobrepor, é possível adicionar apenas 2 elementos no máximo, passando como parâmetro as imagens "Source" e o nível de opacidade, definido entre 0 e 1
    cv.imshow("Blend Images", dst)
    cv.waitKey(0)

img = CannyMetodo("plantas.jpg",1,5,80,200) #Atribui para um objeto o método Canny para detectar bordas
img2 = CannyMetodo("plantas.jpg",1,5,150,220)
Blend(img,1,img2,1,0) #Adicionar imagens sobrepostas


#cv.imshow("Imagem Canny", img)
#cv.waitKey(0)

#A escolha dos valores do Canny,não podem ser valores distântes um de outro, e há uma convesão de T2 > T1 para uma melhor otimização dos valores
#É com base em estimativas em relação a ruídos.