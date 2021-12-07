import cv2 as cv
import numpy as np

#Função, ler img
def captureImage(fileName,size=(0,0)):
    src = cv.resize(cv.imread(fileName),size)
    return src
    
#Função, tratamentos necessesários: trheshold, blur, (canny)
def processImage(src,blur):
  src = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
  srcEqualize = cv.equalizeHist(src)
  srcBlurred = cv.GaussianBlur(srcEqualize,(blur,blur),0)
  _,bin = cv.threshold(srcBlurred,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
  return bin

#Função mascara
def mask_image(src,range):
  range = 80
  hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
  lower = np.array([56 - range, 242 - range, 61 - range])
  higher = np.array([237 + range ,237 + range, 66 + range]) #range 10
  maskHsv = cv.inRange(hsv, lower, higher)
  mask = cv.bitwise_and(src,src,mask=maskHsv)
  return mask

#Função, contornos
def contourFinder(src,dst):
  conts,_ = cv.findContours(src,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
  cv.drawContours(dst,conts,-1,(0,255,255),2)
  cv.putText(dst,("Contornos : ")+str(len(conts)),(15,25),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv.LINE_AA)

#Função exibir e salvar src em disco
def outImage(src,outPutName):
    cv.imwrite(outPutName,src)
    cv.imshow("Image Process",src)
    cv.waitKey(0)

imgOriginal = captureImage('gato2.jpeg',(800,500))
ImgMask = mask_image(imgOriginal,80)

Result = processImage(ImgMask,5)
contourFinder(Result,imgOriginal)

outImage(imgOriginal,"gatoTeste.jpeg")


#cv.imshow("Imagem",imgOriginal)
#cv.waitKey(0)
