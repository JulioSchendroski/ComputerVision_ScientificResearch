import cv2 as cv
import numpy as np

img = cv.imread("jardim.jpg")

#-------------------------cortando coordeanada específica imagem-------------------------
#cut =  img[33:106,506:675] #Variável que recebe uma determinada regição do source definido

#-------------------------Redimensionamento imagem (resize)-------------------------
#width = img.shape[1] # É declarado uma variável chamada "width" para receber a largura, representada pelo .shape[1]
#height = img.shape[0] # É declarado uma variável chamada "height" para receber a altura, representada pelo .shape[0]
#prop = float(height/width) # Econtra-se uma proporção entre os tamanhos originais da imagem
#new_widht = 200 # Multiplicador para a nova proporção desejada
#new_height = int(new_widht*prop) # é criado uma nova variável, representando a nova largura(height) para ser multiplicada pela nova altura(width)
#new_size = (new_widht, new_height) # Novo tamanho da imagem
#img_resize = cv.resize(img,new_size,interpolation=cv.INTER_AREA) # É possivel represenar um novo tamanho da imagem apenas pela função .resize()
#print(width)
#print(height)
#print(prop)
#cv.imshow('Window', img_resize) #Função para mosrar a imagem redimensionada
#img_redmensionada = img[::5,::5] # Realiza uma interpolação das linhas e colunas, pegando coluna sim e coluna não, o mesmo vale para linhas, e depois uma proporção desejada
#cv.imshow('Dimensões', img_redmensionada)

#-------------------------Flip/Reflect-------------------------
#flipped = cv.flip(img, 1) #usando função "flip", com parâmetros do source desejado, e o código do flip desejado, nesse caso 1, espelhando a imagem
#flipped2 = cv.flip(img,0) #usando função "flip", com parâmetros do source desejado, e o código do flip desejado, nesse caso 0, invertendo a imagem de cabeça para baixo
#flip_horizontal = img[::-1, : ] # Outro método de espelhar a imagem, dessa vez com slicing, selecionando todo o eixo y, e invertendo usando -1
#cv.imshow('Horizontal', flip_horizontal)
#flip_vertical = img[::-1, :] # Outro método de espelhar a imagem, dessa vez com slicing, selecionando todo o eixo x, e invertendo usando -1
#cv.imshow('Vertical', flip_vertical)

#-------------------------Rotating-------------------------
#(width, heigth) = img.shape[:2] #Atribui os dois primeiros elementos do .shape para as variáveis width e height
#center = (width // 2, heigth // 2) #Determina-se o centro da imagem, para rotacionar apenas ele
#m = cv.getRotationMatrix2D(center, 20,1.0) #Definie-se uma variável "m" para receber a função de rotação, cmo parâmetros de centro, angulo e escala, essa variável "m" recebe uma conversão desses valores para uma matrix 2x3
#rotated = cv.warpAffine(img,m,(width,heigth)) # A função affine recebe um source (img), a matriz definida por "m" e o pontos que será rotacionado, sendo eles widith = y e height = x
#cv.imshow('IC', rotated )

#-------------------------Masking-------------------------
#mascara = np.zeros(img.shape[:2], dtype= "uint8") # A variável mascara recebe uma função do numpy que define todos os pontos da imagem como zero, definindo a imagem com a cor preta (0,0,0), utilizando de slicing e manipulando inteiros de 8 bits
#cv.rectangle(mascara,(260,0),(338,433),255,-1) # Define-se um retânculo na imagem, utilizando a mascara criada, com as coodernadas desejadas, a cor específica e a espessura (por ser -1, entende-se como sem espessura)
#cv.imshow('Mascara', mascara)
#img_mask = cv.bitwise_not(img,img,mask=mascara) # A variável img_mask, cria a mascara para a imagem original, e utiliza-se o operador .bitwise_not para acrescentar na imagem original uma mascara negativa
#cv.imshow('IMG MASK', img_mask)



cv.imshow('Original', img)
cv.waitKey(0)


# OBS : Affine, significa uma alterações entre espaços sem perder a proporção original da imagem
