import cv2 as cv
import numpy as np
from matplotlib import image, pyplot as plt
from numpy.lib.arraypad import pad

#Original
def capture_image(fileName,size=(0,0)):
    src = cv.resize(cv.imread(fileName),size)
    rgb = cv.cvtColor(src,cv.COLOR_BGR2RGB)
    return rgb 

#Process
def process_image(src,blur):
  src = cv.cvtColor(src,cv.COLOR_RGB2GRAY)
  srcBlurred = cv.GaussianBlur(src,(blur,blur),0)
  srcEqualize = cv.equalizeHist(srcBlurred)
  return srcEqualize

#Bin
def threshold_image(src,flag):
    _,bin = cv.threshold(src,0,255,flag+cv.THRESH_OTSU)
    return bin

#Canny
def image_edge(src,cannyValue1,cannyValue2):
    edge = cv.Canny(src,cannyValue1,cannyValue2)
    return edge

raw = [capture_image(f"{i+1}.jpeg",(600,400)) for i in range(10)]
process = [process_image(img,5) for img in raw]
bin = [threshold_image(img,cv.THRESH_BINARY) for img in process]
edges = [image_edge(img,70,120) for img in bin]
titles = ['Original','Process','Threshold','Edges']



for imageIndex, _ in enumerate(raw):
  plt.subplot(10,4,imageIndex*4+1)
  plt.axis(False)
  if imageIndex == 0:
    plt.title(titles[0])
  plt.imshow(raw[imageIndex],cmap='gray')

  plt.subplot(10,4,imageIndex*4+2)
  plt.axis(False)
  if imageIndex == 0:
    plt.title(titles[1])
  plt.imshow(process[imageIndex],cmap='gray')

  plt.subplot(10,4,imageIndex*4+3)
  plt.axis(False)
  if imageIndex == 0:
    plt.title(titles[2])
  plt.imshow(bin[imageIndex],cmap='gray')

  plt.subplot(10,4,imageIndex*4+4)
  plt.axis(False)
  if imageIndex == 0:
    plt.title(titles[3])
  plt.imshow(edges[imageIndex],cmap='gray')



plt.show()  

#Inveter os eixos, e retirar os valores de eixos do subplot (conferir documentação) OK

#Estudar os histogramas e distribuições de colormap OK
#Atentar-se a conversão de cores (RGB2BGR) OK

#Imagem 1,2,3,4,6,10 (Talvez, desconsiderar a imagem 6)
#Histogramas 1,2,3 similares: Utilizar parâmetros parecidos nos processamentos de imagem (edge 32)

#Imagem 10: Mudança para 70,120 nos valores de canny, melhores que 120,200, explicar o por que!

# Imagens 5,6,7,8,9 (Talvez excluir a 6)

#Limiar OTSU, com os valores da linhas 21 não dá bons resultados para as imagens 
#imagem 4: Necessidade de inversão preto e branco
#Imagem 6 : Aplicar blur mais rigoroso
#Imagens 7,8,9 : Confusão do objetos e suas vizinhanças

#Variar os parâmetros para saber se melhoraram ou pioraram em cada imagem, e quais valores podem ser usados

