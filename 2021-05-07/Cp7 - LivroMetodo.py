import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("textura.jpg")
img = img[::2, ::2]
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

suave =  np.vstack([np.hstack([img,cv.blur(img,(9,9))])]) #O livro cria uma coluna, o numpy interpreta como uma pilha, na vertical, e passa como parâmetros pilhas horizontais dentro da vertical
#Em relação a praticidade, é mais facil, no entanto é apenas a vizualizção das imagens em apenas um "cv.imshow()" e não é possivel fazer analises mais detalhadas

cv.imshow("Blur", suave)
cv.waitKey(0)