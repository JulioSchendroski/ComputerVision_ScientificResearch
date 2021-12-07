import cv2 as cv
import os
import random
import numpy as np

files = os.listdir('/home/schn/Documentos/ifsp_ic_julio/2021-29-11/positive_image_test')
cascade = cv.CascadeClassifier('cascade_mask.xml')

for index, file in enumerate(files):
    imgPath = os.path.join('/home/schn/Documentos/ifsp_ic_julio/2021-29-11/positive_image_test', file)
    img = cv.imread(imgPath)
    resized = cv.resize(img, (320,240))
    
    heifers = cascade.detectMultiScale(resized, 1.05, 5)

    for (x,y,w,h) in heifers:
        xMin = np.min(heifers)
        yMin = np.min(heifers)
        hMax = np.max(heifers)
        wMax = np.max(heifers)
        cv.rectangle(resized, (x,y), (w ,h), (0,255,255), 3)
        cv.rectangle(resized, (xMin,yMin), (wMax ,hMax), (255,0,0), 3)


    cv.imshow("Imagens", resized)
    cv.waitKey(0)
    cv.destroyAllWindows()

