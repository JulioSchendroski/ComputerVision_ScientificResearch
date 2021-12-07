#import numpy as np
import cv2
import random

def haarCascade(filename, scale, neighbors):
    cascade = cv2.CascadeClassifier('heifers111020h.xml')
    img = cv2.imread(filename)
    resized = cv2.resize(img, (320,240))
    heifers = cascade.detectMultiScale(resized, scale, neighbors)
    
    for (x,y,w,h) in heifers:
        randomColorB = random.randint(0,255)
        randomColorG = random.randint(0,255)
        randomColorR = random.randint(0,255)
        cv2.rectangle(resized, (x,y), (w , h), (randomColorB,randomColorG,randomColorR), 5)
        print(x,y)  
    cv2.imshow('Imagens', resized)
    cv2.waitKey(0)

haarCascade('cow.jpg', 1.03, 5)
#haarCascade('carro.jpg', 1.05, 3)