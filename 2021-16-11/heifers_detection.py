import cv2
import random

def haarCascade(filename, scale, neighbors):
    cascade = cv2.CascadeClassifier('heifers_edges_classfier_171111h.xml')
    img = cv2.imread(filename)
    resized = cv2.resize(img, (320,240))
    heifers = cascade.detectMultiScale(resized, scale, neighbors, minSize= (30,30))
    
    for (x,y,w,h) in heifers:
        randomColorB = random.randint(0,255)
        randomColorG = random.randint(0,255)
        randomColorR = random.randint(0,255)
        cv2.rectangle(resized, (x,y), (w , h), (randomColorB,randomColorG,randomColorR), 5)
    cv2.imshow('Imagens', resized)
    cv2.waitKey(0)

haarCascade('pessoa1.jpeg', 1.05, 5)
#haarCascade('carro.jpg', 1.05, 3)