import cv2 as cv
import numpy as np
from matplotlib import image, pyplot as plt
from numpy.lib.arraypad import pad

def capture_image(fileName,size=(0,0)):  #Método para captura da imagem
    src = cv.resize(cv.imread(fileName),size)
    rgb = cv.cvtColor(src,cv.COLOR_BGR2RGB)
    return rgb  #Retorna imagem no sistema RGB

def gray_image(src): #Método de conversão da imagem em cinza
  gray = cv.cvtColor(src,cv.COLOR_RGB2GRAY)
  return gray

def threshold_image(src,thresh): #Thresh hold da imagem para o métodod Watarshed, utilizando THRESH_BINARY
    _,bin = cv.threshold(src,thresh,255,cv.THRESH_BINARY)
    return bin

def threshold_image_inv(src,thresh): #Thresh hold da imagem para o métodod Canny, utilizando THRESH_BINARY_INV
    _,bin = cv.threshold(src,thresh,255,cv.THRESH_BINARY_INV)
    return bin    

def process_image(src,percent): #Método de processamento da imagem para Watershed
    kernel = np.ones((3,3),np.uint8) #Kernel 3X3
    closing = cv.morphologyEx(src,cv.MORPH_CLOSE,kernel, iterations = 6) #Utilizado para fechar os possíveis buracos da imagem
    bg = cv.dilate(closing,kernel,iterations=3) #Dilatar os objetos para identificar o background
    dist = cv.distanceTransform(bg,cv.DIST_L2,3) #Calcula a distância de cada pixel até o pixel preto mais próximo e retorna uma matriz com essas distâncias.
    _,fg = cv.threshold(dist,percent*dist.max(),255,0) #Threshold utilizando porcentagem da distância maxima identificada na matriz "dist".
    fg = np.uint8(fg) #Truncamento de fg para uint8
    unknown = cv.subtract(bg,fg) #Subtração do background com o foreground para obter apenas o contorno desejado
    _, marker = cv.connectedComponents(fg) #Cria-se um markador (matriz do mesmo tamanho que a imagem original), o método connectedComponentes, define o background como 0 e os outros objetos são definidos como números maiores ou iguais a 1.
    marker = marker+1 #Aplica para todos marcadores 1 unidade, para garantir que não sejam interpretados como background.
    marker[unknown == 255] = 0 #Definindo toda região desconhecida (resultado da subtração) como 0.
    return marker
  
def water(src,dst):
  marker = cv.watershed(dst,src)
  dst[marker == -1] = [255,0,0] #-1 é código do método de watershed para aplicar para todos cortornos.
  return dst

def image_edge(src,cannyValue1,cannyValue2): #Método das bordas em Canny
    srcBlurred = cv.medianBlur(src,7) #Blur para definir as bordas
    edge = cv.Canny(srcBlurred,cannyValue1,cannyValue2) #Aplicação do Canny com os valores parametrizados
    return edge

raw = [capture_image(f"{i+1}.jpeg",(600,400)) for i in range(10)]

rawWatershed = [capture_image(f"{i+1}.jpeg",(600,400)) for i in range(10)] #Lista parar ler as imagens na pasta

gray = [gray_image(img) for img in raw] #Lista de aplicação de escala cinza

thresh = [15,40,30,50,40,50,68,30,80,47] #Valores do threshold.

percentList = [0.2,0.2,0.1,0.3,0.22,0.1,0.1,0.2,0.4,0.2] #Por ser a porcentagem da distância máxima dos pixels 0 para os não zero, quanto maior a porcentagem, menos contorno haverá.

bin = [threshold_image(img, thresh[index]) for index, img in enumerate(gray)] #Lista para aplicar os valores de threshold nas imagens cinza.

bin_inv = [threshold_image_inv(img, thresh[index]) for index, img in enumerate(gray)] #Aplicação de threshold invertido nas imagens cinza

process = [process_image(img, percentList[index]) for index, img in enumerate(bin)] #Processamento das imagens para os objetos da lista "bin"

waterShade = [water(process[index], img) for index, img in enumerate(rawWatershed)] #Aplicação de watershed nas imagens processadas.

edges = [image_edge(img,120,200)for img in bin_inv] #Lista de Canny

titles = ['Original','Cinza','Limiar','Contorno','Segmentação']
 
for imageIndex, _ in enumerate(raw): #Iteração para o plot das imagens
  plt.subplot(10,5,imageIndex*5+1) #Subplot com valores para plotagem dos lugares desejados
  plt.axis(False) #Retirando os eixos
  if imageIndex == 0: #Definir que os titulos sejam postos apenas na primeira posição de acada coluna
    plt.title(titles[0])
  plt.imshow(raw[imageIndex],cmap='gray') #Plotagem com color map gray.

  plt.subplot(10,5,imageIndex*5+2)
  plt.axis(False)
  if imageIndex == 0:
    plt.title(titles[1])
  plt.imshow(gray[imageIndex],cmap='gray')

  plt.subplot(10,5,imageIndex*5+3)
  plt.axis(False)
  if imageIndex == 0:
    plt.title(titles[2])
  plt.imshow(bin_inv[imageIndex],cmap='gray')

  plt.subplot(10,5,imageIndex*5+4)
  plt.axis(False)
  if imageIndex == 0:
    plt.title(titles[3])
  plt.imshow(edges[imageIndex], cmap='gray')

  plt.subplot(10,5,imageIndex*5+5)
  plt.axis(False)
  if imageIndex == 0:
    plt.title(titles[4])
  plt.imshow(process[imageIndex], cmap='binary')

plt.show()  



