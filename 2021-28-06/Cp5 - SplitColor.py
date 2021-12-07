import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

src = cv.imread("montanha.jpg")
img = cv.cvtColor(src, cv.COLOR_BGR2RGB) #Converte a imagem de BGR para RGB já que o matplotlib utiliza o sistems RGB

blue_channel, green_channel, red_channel = cv.split(src) #Defini-se três variáveis para receber cada canal de cor, devido a função spliit, blue green e red respectivamente
result = cv.merge((blue_channel,green_channel,red_channel)) #Variável para realizar o merge e mostrar os três canais juntos
zero = np.zeros(src.shape[:2],dtype = "uint8") #imagem com a cor preta, zerando os canais de cores até o index 2, [0], [1]



plt.subplot(3,3,1), plt.title("Original"), plt.imshow(img) #Define a exbição com 3 linhas, 3 colunas e o indice na qual a imagem irá, no caso o primeiro indice
plt.subplot(3,3,2), plt.title("Split Blue"), plt.imshow(blue_channel,cmap='gray') #Utiliza-se do color map "gray" 
plt.subplot(3,3,3), plt.title("Split grenn"), plt.imshow(green_channel,cmap='gray')
plt.subplot(3,3,4), plt.title("Split Red"), plt.imshow(red_channel,cmap='gray')
plt.subplot(3,3,5), plt.title("Result"), plt.imshow(cv.cvtColor(result,cv.COLOR_BGR2RGB)) #Plota-se a conversão do "result" convertendo o mesmo para RGB, devido o matplotlib 
plt.subplot(3,3,6), plt.title("BLUE SOURCE"), plt.imshow(cv.merge([zero,zero,blue_channel])) #É definido como zero os canais de cores Red e Green, deixando apenas o canal de cor azul
plt.subplot(3,3,7), plt.title("GREEN SOURCE"), plt.imshow(cv.merge([zero,green_channel,zero])) #É definido como zero os canais de cores Red e Blue, deixando apenas o canal de cor azul
plt.subplot(3,3,8), plt.title("RED SOURCE"), plt.imshow(cv.merge([red_channel,zero,zero])) #É definido como zero os canais de cores Green e Blue, deixando apenas o canal de cor azul



plt.show()