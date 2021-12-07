import cv2 as cv
import numpy as np

def show(fileName,thresh,percent):
    img = cv.imread(fileName)

    resized = cv.resize(img,(600,400))
    gray = cv.cvtColor(resized,cv.COLOR_RGB2GRAY)
    _,bin = cv.threshold(gray,thresh,255,cv.THRESH_BINARY)

    kernel = np.ones((3,3),np.uint8)

    closing = cv.morphologyEx(bin,cv.MORPH_CLOSE,kernel, iterations = 1)

    bg = cv.dilate(closing,kernel,iterations=3)

    dist = cv.distanceTransform(bg,cv.DIST_L2,3)

    _,fg = cv.threshold(dist,percent*dist.max(),255,0)
    fg = np.uint8(fg)
    unknown = cv.subtract(bg,fg)

    _, marker = cv.connectedComponents(fg)
    marker = marker+1
    marker[unknown == 255] = 0

    marker = cv.watershed(resized,marker)
    resized[marker == -1] = [0,0,255]

    cv.imshow("imagem"+fileName,fg)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    print(f"{dist.max()} ::::  {dist.max()*percent}" )

show('1.jpeg',15,0.1)
show('2.jpeg',40,0.2)
show('3.jpeg',40,0.1)
show('4.jpeg',50,0.3)
show('5.jpeg',40,0.3)
show('6.jpeg',50,0.1)
show('7.jpeg',68,0.1)
show('8.jpeg',30,0.2)
show('9.jpeg',80,0.4)
show('10.jpeg',47,0.2)


