import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

src = cv.imread("brinde.jpg") 
src = cv.cvtColor(src, cv.COLOR_BGR2RGB) #Reliza-se uma conversão da imagem de BGR para RGB, devido a biblioteca matplotlib utilizar apenas RGB 

mask = np.zeros(src.shape[:2], dtype = "uint8") #Transforma a imagem selecionada na cor preta, definindo todos os canais como "zero"
#Outros tipos de dados a ser trabalhados : https://scikit-image.org/docs/dev/user_guide/data_types.html
cv.ellipse(mask,(300,200),(100,175),0,0,360,255,-1) #Desenha uma elipse, passando os parâmetros necessários
src_mask = cv.bitwise_and(src,src, mask= mask) #Sobrepõe o desenho realizado, elipse, em cima da mascara criada, utiliza-se o operador lógico "bitwise" "and" para sobrepor

plt.subplot(1,3,1) #Define a exbição com 1 linhas, 3 colunas e o indice na qual a imagem irá, no caso o primeiro indice
plt.title("Original") #Titulo para cada plot
plt.imshow(src) #plot desejado

plt.subplot(1,3,2)
plt.title("Máscara binária")
plt.imshow(mask,'gray') #Defini-se um color map para a imgame, assim sendo possivel trabalhar com as escalas cinzas na imagem

plt.subplot(1,3,3)
plt.title("Imagem com máscara")
plt.imshow(src_mask)

plt.show() #Plota-se todas as imagens definidas











