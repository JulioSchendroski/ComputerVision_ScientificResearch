import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt



def binOTSU (file, resize, blurKernel, flag):
    src = cv.imread(file,cv.IMREAD_GRAYSCALE)
    src = src[::resize,::resize] #Redmensionamento da imagem
    blur = cv.GaussianBlur(src,(blurKernel,blurKernel),0)

    _, otsu = cv.threshold(blur,0,255,flag+cv.THRESH_OTSU) #O método de OTSU, determina a melhor binarização para a imagem, é passado como uma flag como uma flag adicional, a flag determina a melhor otimização entre os dois retornos passados, de forma global
    print( "{}".format(_) )
    resultado = np.vstack([np.hstack([blur,otsu])]) #Utiliza-se do método de vizualização com pilhas.
    cv.imshow("Original e OTSU", resultado)
    cv.waitKey(0)
    

#binOTSU("banana.jpg",2,7,cv.THRESH_BINARY)
binOTSU("cana.png",1,5,cv.THRESH_BINARY)
#binOTSU("plantas.jpg",1,7,cv.THRESH_BINARY_INV)

#Flags : cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY_INV, cv.THRESH_BINARY, cv.ADAPTIVE_THRESH_MEAN_C

#Verificar o ajuste de limiar, para não ficar apenas preto e branco.

