import numpy as np
import cv2 as cv

img = cv.imread("jardim.jpg")

#------------------------- Infos Imagem-------------------------
#(b, g, r) = img[0, 0] # As variáveis b, g, r recebem a imagem com altura = 0 e largura = 0
#print('O pixel (0,0) tem suas seguintes cores : ') #Comando de output 
#print(f'Vermelho :{r}, verde : {g}, azul :{b} ') # formatador de strings para mostrar quais cores estão presentes no ponto (0,0) da imagem, sendo o canto superior esquerdo
#print(img.shape) # Mostra quantidade de colunas, linhas e por ser uma imagem colorida, apresenta 3 canais de cores

#------------------------- Varrendo Pixels-------------------------
#for y in range (0,img.shape[0]): #Comando de repetição para acessar a linha y(altura), utilizando img.shape[0], sendo 0 para altura
    #for x in range (0, img.shape[1]): #Comando de repetição para acessar a linha x(largura), utilizando img.shape[1], sendo 1 para largura
        #img [y, x] = (0, 255, 255) #img nos pontos y e x recebem uma listas com os canais de cores da imagem

#for y in range(0,img.shape[0]):
    #for x in range(0,img.shape[1]):
        #img[y, x] = (0, y % 256, x % 256) # Img recebe nos pontos x e y o resto da divisão de x por 256 (sendo uma unidade a mais, garantindo que a cor será maior que 0), assim como o y


#for y in range(0,img.shape[0],100): # No comando range, é determinado os "steps", funcionando como um pulo entre cada parâmetro definido (15)
    #for x in range(0,img.shape[1],100): # Assim como nesse, seus "steps" são definidos como 10
        #img[y:y+7, x:x+7] = (255,0,255) #Img recebe os pontos com alterações eu seu valores, sendo y + 2, determinando assim a "espessura" das alterações definidas

#for y in range(0,img.shape[0]):
    #for x in range(0,img.shape[1]):
        #img[y, x] = (x**2 % 256 , 0 , y**2 % 256) # Neste caso, img recebe x elevado ao quadrado, seguido de um resto de divisão pelo valor da cor azul, o mesmo vale pale o eixo y

#for y in range (0,img.shape[0]):
    #for x in range(0,img.shape[1],10):
        #img [y,x:y*2] = (0, 0, 255) #Img recebe o todo o x como y elevado ao quadrado, obetendo uma faixa dividindo a metade da imagem com a cor desejada

#-------------------------Drawing-------------------------
#img[100:150, 50:100 ] = (0,255,0) #Utilizando da técnica de slicing, é definido 2 pontos com o operado ":" na qual a imagem irá receber desenhos
#cv.arrowedLine(img,(300,300),(80,380),(255,0,0),2) #Desenha-se uma seta, passado como parâmetro a source (img), pontos de origem e ponto final, as cores desejadas, e a espessura da seta (2)
#cv.ellipse(img,(300,300),(170,80),0,0,360,(0,0,250),2) # é desenhado uma elipse, no entanto é necessário definir o source, centro, eixos x e y, angulo em graus, a cor e a espessura da elipse 
#fonte = cv.FONT_HERSHEY_DUPLEX # Uma variável que irá receber uma fonte, e define-se para ela o tipo de fonte desejada
#cv.putText(img,'Julio',(150,75),fonte,3,(0,255,0),2,cv.LINE_AA) # Com a função cv.putText() é possivel definir a mensagem, tipo de fonte, espessura e a cor

#cv.imshow('Imagem Escrita',img)  
cv.imshow('Original',img)
cv.waitKey(0)

# Outras formas a serem desenhadas https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga1ea127ffbbb7e0bfc4fd6fd2eb64263c
