import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def Binariza(file, threshold, kernel):
    src = cv.imread(file, cv.IMREAD_GRAYSCALE)
    src = cv.cvtColor(src,cv.COLOR_BGR2RGB)
    srcBlur = cv.GaussianBlur(src,(kernel,kernel),0) #Aplicação do filtro Gaussiano de blur
    _, bin = cv.threshold(srcBlur,threshold,255,cv.THRESH_BINARY) # O método retorna dois valores, o primeiro é o valor do threshold e o segundo o output da imagem.
    _, bin2 = cv.threshold(srcBlur,threshold,255,cv.THRESH_BINARY_INV) #Mesma ideia do threshold ja apresentado, no entanto é aplicado um thresh invertido.
    imgs = [src,srcBlur,bin, bin2]
    titulos = ["Original", "Suave", "Binarização", "Binarização invertida","Histograma Original"]

    for i in range(4):
        plt.subplot(3,3,i+1), plt.imshow(imgs[i])
        plt.title(titulos[i])
        plt.subplot(3,3,5),plt.hist(src.ravel(),255,[0,256]),plt.title("Histograma Original")

    plt.show()

Binariza ("recHidr.jpg",50,7) 
Binariza ("recHidr.jpg",50,11)
