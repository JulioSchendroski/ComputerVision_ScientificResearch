import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def CannyMetodo(fileName,size,blurKernel, cannyValue1,cannyValue2):
    img = cv.imread(fileName)[::size,::size]
    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #Conversão de cor para a escala cinza
    img = cv.GaussianBlur(img,(blurKernel,blurKernel),0) #Aplica O filtro Gaussiano

    imgCanny  = cv.Canny(img, cannyValue1,cannyValue2)

    resultado = np.vstack([np.hstack([img,imgCanny])]) #Exibir imagem em uma unica janela, através de pilhas de numpy

    cv.imshow("Cannys",resultado)
    cv.waitKey(0)



CannyMetodo("deserto.jpg",2,5,70,220)
CannyMetodo("deserto.jpg",2,5,70,70) #Inclui chão e montanha além da arvore
CannyMetodo("deserto.jpg",2,5,300,40)

#Aplicação do canny, canny é outro método de detecção de bordas ou contornos, passado como parâmetro a imagem com gaussianBlur
#O canny utiliza-se de dois parâmetros para definir as bordas da imagem, para isso é passado dois valores de thresholding para o método
#A respeito do calculo do calculo dos gradientes e como funciona a detecção das bordas, com gráficos :  https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html

#Canny é o método inteligente de se detectar bordas de uma imagem, faz o uso de aproximações do vetor gradiente, chamado de "supressão não-máxima" ou seja
#reduz as bordas o máximo possível com ruídos, por isso se faz necessário o uso de Gaussian Blur, o lado ruim da aplicação do Canny é a omissão de bordas com
#valores não precisos.

#A escolha dos valores do Canny para a detecção é considerado complexo, não podem ser valores distântes um de outro, e há uma convesão de T2 > T1 para uma melhor
#otimização dos valores

#A escolha é com base em estimativas em relação a ruídos.
