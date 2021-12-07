import numpy as np
import cv2 as cv
from matplotlib import cm, pyplot as plt


def binOTSU(FileName,KernelValue, binFlag, coordinateY,coordinateX, outputName): #Defini-se o método para realizar binarização com o modo OTSU
    img = cv.imread(FileName,cv.IMREAD_GRAYSCALE) #Leitura da imagem com a aplicação de escala cinza
    blur = cv.GaussianBlur(img,(KernelValue,KernelValue),0) #Aplicação de blur na imagem, através de um kernel definido por parâmetro.

    _,otsu = cv.threshold(blur, 0,255,binFlag+cv.THRESH_OTSU) #Declaração do método OTSU, com dois objetos, sendo "otsu" como o nosso output, e o segundo o valor pré-definido para o threshold
    #é definido também uma flag para binarizar e é acrescentado a flag OTSU.

    print(f"O valor de limiarização definido pelo método OTSU é : {_}") #Mostra o valor de limar definido pelo OTSU

    limiar = blur[coordinateY,coordinateX] #Captura de um valor de intensidade de determinado pixel, através das coordenadas
    print(f"Valor de intensidade de cinza do pixel escolhido  : {limiar}")
    cv.imwrite(outputName,otsu) #Comando para escrever no disco do computador o resultado de OTSU
    
def exibir(fileName):
    cv.imshow("Imagem OTSU",cv.imread(fileName))
    cv.waitKey(0)


binOTSU("Cranio.jpg",5,cv.THRESH_BINARY,532,415,"CranioOTSU.jpg") #Chamada do método
exibir("CranioOTSU.jpg")

#A conclusão é que por o método OTSU definir automáticamente os valores de limiar de modo otmimizado, ou seja, o que se enquadra melhor para aquela
#imagem, então não é possível alterar os valores de threshold do mesmo, recomaneda-se fazer uso de adaptative threshold para situações na qual o OTSU
#Não limiariza de forma correta. O método não funciona de forma correta em situações na qual a área a ser segmentada é menor que seu fundo, com muitos ruídos
#e objetos ou regiões com grande constrastes também pode causar problema com OTSU.