import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def BinarizaAdaptive (file,blurKernel, maxThreshhold, flag1,flag2,kernelThresh, C):
    src = cv.imread(file,cv.IMREAD_GRAYSCALE)
    suave = cv.GaussianBlur(src,(blurKernel,blurKernel),0) #É aplicdo uma suavização na imagem 
    bin1 = cv.adaptiveThreshold(suave,maxThreshhold,flag1,flag2,kernelThresh,C) #O treshold adaptativo é um método mais inteligente de limiarizar a imagem, já que ele não aplica o mesmo threshold para toda imagem, ele utiliza-se de valores diferentes para diferentes áreas

    imgs = [src,suave,bin1]
    titulos = ["Original", "Blur", "Adaptative Threshold"]

    for i in range(3):
        plt.subplot(1,3,i+1), plt.imshow(imgs[i],'gray')
        plt.title(titulos[i])
    plt.show()


BinarizaAdaptive("banana.jpg",7,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,5)
#Flags : cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY_INV, cv.THRESH_BINARY, cv.ADAPTIVE_THRESH_MEAN_C