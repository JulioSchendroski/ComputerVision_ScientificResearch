import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("textura.jpg")
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

kernelBlur = np.ones((3,3),np.float32)/9 #O kernel é o "bloco" de pixels que circundam o pixel a ser trabalhado, em forma de matriz
ImgSmooth = cv.filter2D(img, -1, kernelBlur) # O método de blur smooth, faz uso que uma pre-definição de um kernel, ou seja, é necessário construir um kernal antes de utiliza-lo
imgGauss = cv.GaussianBlur(img, (3,3),0) #Blur Gaussiano, tem seus parâmetros o source, tamanho do kernel, ou seja uma matriz Y x Y, e o desvio padrão 
imgBilat = cv.bilateralFilter(img,3,77,77) #Blue bilateral, Utiliza-se do filtro Gaussiano, O bilateral utilizxa-se de pixels com instensidades semelhantes para eralizar o blue, por isso mantem as bordas mais definidas
imgMedian = cv.medianBlur(img,3) #Fz a media do kernel, e substitui os pixels com a média, é utilizado principalmente com imagens "Salt and pepper", traduzindo para o Portugês, seria algo como a estática de TV que vemos em canais abertos

plt.subplot(2,3,1), plt.title("Original"), plt.imshow(img) #Plotagem das imagens com matplotlib
plt.subplot(2,3,2), plt.title("Smooth"), plt.imshow(ImgSmooth)
plt.subplot(2,3,3), plt.title("Gaussiano"), plt.imshow(imgGauss)
plt.subplot(2,3,4), plt.title("Bilateral"), plt.imshow(imgBilat)
plt.subplot(2,3,5), plt.title("Mediana Box"), plt.imshow(imgMedian)

plt.show()

#Para mais informações e filtos, é recomendável acessar e ler a respeito nas documentações :  https://docs.opencv.org/4.5.2/d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1

