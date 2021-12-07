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
  return srcBlurred

#Bin
def threshold_image(src,thresh):
    _,bin = cv.threshold(src,thresh,255,cv.THRESH_BINARY_INV)
    return bin

#Canny
def image_edge(src,cannyValue1,cannyValue2):
    edge = cv.Canny(src,cannyValue1,cannyValue2)
    return edge

raw = [capture_image(f"{i+1}.jpeg",(600,400)) for i in range(10)]
thresh = [15,40,30,50,40,50,68,30,80,40]
process = [process_image(img,5) for img in raw]
bin = [threshold_image(img,thresh[img_index]) for img_index, img in enumerate(process)]
edges = [image_edge(img,120,200) for img in bin]
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



