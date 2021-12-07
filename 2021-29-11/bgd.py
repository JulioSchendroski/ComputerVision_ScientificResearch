import cv2 as cv
import numpy as np

img = cv.imread("3.jpeg")
#resized = cv.resize(img, (600,400))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thr = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

kernel = np.ones((3,3), np.uint8)
closing = cv.morphologyEx(thr, cv.MORPH_CLOSE, kernel, iterations=5)
bg = cv.dilate(closing, kernel, iterations=3)


#Criando máscara
mask = 255 - bg
result = cv.bitwise_and(img, img, mask=mask)

cv.imshow("Imagem", result)
cv.waitKey(0)
cv.destroyAllWindows()