import numpy as np #Importa biblioteca numpy
import cv2 #Importa biblioteca do opencv

img = cv2.imread('color.jpg') #Lê a imagem através do caminho, ou do nome com formato
img2 = cv2.imread('ottis.jpg')
img3 = cv2.imread('logoCV.png')

img = cv2.resize(img, (540,600)) #Redefine a imagem específicada, passando como parametro os dimensões
img2 = cv2.resize(img2, (540,600))
img3 = cv2.resize(img3, (540,600))

#////////////////////////////////////

#reflect = cv2.copyMakeBorder(img3,20,20,20,20,cv2.BORDER_REFLECT) #Adiciona efeito de reflexo nas bordas, passando como parâmetro as distâncias das borda e o tipo de borda desejado
#cv2.imshow('Borda Refletida',reflect) #Exibe imagem refletida


#////////////////////////////////////
#infos image

print(img.shape) #Retorna o numero de colunas, fileiras e os canais de cores
print(img.size)  #Total de pixels da imagem
print(img2.shape)
print(img2.size)

#////////////////////////////////////

#Splitting 

#blue = img[:, :, 0] #É chamado de Split, esse método de fazer split define como 0 as cores de não interesse, e através do BGR, sendo BLUE = 0, GREEN = 1 , RED = 2
#green = img[:, :, 1]
#red = img[:, :, 2]
#blue, green, red = cv2.split(img) #Outro método de utilizar split, é com a função própria cv2.splt() passando como parâmetro a imagem que se deseja fazer split

#merge_imagem = cv2.merge((blue, green, red)) #Merged realiza o inverso de split, é capaz de reverter o split e voltar com as cores originais
#merge_imagem = cv2.merge((red, green, blue)) #Invertendo R e B, resultado torna-se diferente
#cv2.imshow('Blue',blue) #Exibe imagem com split, definido com a cor de interesse
#cv2.imshow('Green',green)
#cv2.imshow('Red',red)
#cv2.imshow('Merged', merge_imagem)

#////////////////////////////////////////////////////////////////////////

#resized = cv2.resize(img, None, fx=2,fy=2, interpolation= cv2.INTER_AREA) #A função "resize" redefine o tamanho da imagem, no entanto dessa maneira como foi passada, é com parametros de x e y, é com uma flag pré-definida 
#cv2.imshow('Resize', resized) #Exibe a imagem com o tamanho redefinido

#////////////////////////////////////////////////////////////////////////

#Blending
#blend1 =  cv2.add(img, img2, img3) #A função "add", faz de forma bem simplificada a adição de duas imagens, no entanto é NECESSÁRIO as imagens serem de mesmas dimensões
#blend2 = cv2.addWeighted(img, 0.5,img2, 0.5, 0) #Outra função de add, é "addWeighted" capaz de mudar a opacidade entre as imagens misturdas, definindo com constantes entre 0.0 e 1.0
#cv2.imshow('Original1',blend1)


cv2.selectROI(img)
cv2.imshow('Original1',img)

#////////////////////////////////////////////////////////////////////////

#bitwise
#bit = cv2.bitwise_and(img,img2) #AND, OR, NOT, XOR são os parâmetros possiveis para realizar bitwise na imagem

#////////////////////////////////////////////////////////////////////////

#cv2.imshow('Original1', img)
#cv2.imshow('Original2',img2)
#cv2.imshow('Original3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()


