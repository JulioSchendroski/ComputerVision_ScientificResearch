import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def Laplacian(fileName, blurValue):
    img = cv.imread(fileName,cv.IMREAD_GRAYSCALE)
    img = cv.GaussianBlur(img,(blurValue,blurValue),0) #Aplicação de blur através da média do kernel

    lap_blur = cv.Laplacian(img, cv.CV_64F) #Laplacian é um dos métodos de blur, utliza-se de derivdadas parciais do método Sobel, de um kernel 3x3
    lap_blur = np.uint8(np.abs(lap_blur)) #Conversão de 64F para uint8
    cv.imshow("Imagem with Laplacian Filter", lap_blur)
    cv.waitKey(0)


def Sobel(fileName,blurValue):
    img = cv.imread(fileName,cv.IMREAD_GRAYSCALE)
    img = cv.GaussianBlur(img,(blurValue,blurValue),0)
    SobelX = cv.Sobel(img,cv.CV_64F,1,0) #O método de Sobel para detectar bordas, faz uso de derivdas em um determinado eixo de um kernel 3x3, é preciso específicar o eixo a ser tratado com um vetor unitário do eixo, para a derivada diercional
    SobelX = np.uint8(np.abs(SobelX)) #Novamente a conversão do tipo de dados trabalhados
    SobelY = cv.Sobel(img,cv.CV_64F,0,1) # Dessa vez definindo o eixo Y como verdadeiro, através do vetor unitário em Y
    SobelY = np.uint8(np.abs(SobelY))
    Mask = cv.bitwise_or(SobelX, SobelY) #Aplicando uma mascara com operadores lógicos "bitwise_or" para unir os dois eixos de sobel.
    imagens = [img,SobelX,SobelY,Mask]
    tlt = ["Original","Sobel X", "Sobel Y", "Mascara X+Y"]
    for i in range(4):
        plt.subplot(2,2,i+1), plt.imshow(imagens[i],'gray')
        plt.title(tlt[i])
    plt.show()    
    

#Sobel("brigadeiros.jpg",5)
Sobel("sudoku.jpg",5)
#Laplacian("brigadeiros.jpg",5)


#Informação importante, A transição do preto para o branco, as derivadas parciais assumem uma taxa de inclinação positivas, sendo possiveis utiliazar o escopo de inteiros de 1 byte (8 bits) que tem um range de 0 - 255
#quando se tranforma de branco para o preto, na binarização, o coeficiente angular torna-se negativo, fugindo do tipo de uint8, então é necessário utilizar o tipo de 64F, e depois, utilizando 
#a biblioteca numpy, utiliaz-se do método np.abs() ou np.absolute() para converter novamente em uint8, para escara de cor padrão de 0 - 255.

#A definição de borda é nada mais que uma região na qual há um limite entre duas regiões com níveis de cinza muito diferentes entre sí, e encontra-se essa região com um vetor gradiente, que indica a maior variação
#de um determinado valor, que nos nossos estudos é a intensidade de cinza em uma região, e a sua direção. Se houver uma variação rápida nas abicissas, quer dizer que existe uma borda vertical nauqlea região, o mesmo se aplica
#caso a variação nas abicissas seja de forma lenta, em nas ordenadas de forma rápida, o resutado é uma borda no sentido vertical, mesmo sentido do vetor gradiente da função.

#É importante ressaltar que o método Laplaciado faz uso de derivada de segunda ordem com o operador gradiente, dessa maneira, é muito sensível em relações a ruídos, necessitando de uma mascara maior, no entanto faz com que
#o brilho da imagem decaída. Sendo assim, é muito pouco utilizado, e normalmente não é muito prático e eficaz.