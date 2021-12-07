import numpy as np
import cv2 as cv

def image_process(src, GauBlur, threshValue, flag): #Processamento da imagem para retirar apenas as infromações necessárias, como os pontos do dado, ou apenas seu contorno externo
    imgGray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    equalized = cv.equalizeHist(imgGray)
    blur = cv.GaussianBlur(equalized, (GauBlur,GauBlur),0)
    _,bin = cv.threshold(blur, threshValue, 255, flag)
    return bin #Retorna a imagem binarizada

def mask_image(src):
    hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    lower = np.array([38, 86, 0])
    higher = np.array([121 ,255, 255])
    maskHsv = cv.inRange(hsv, lower, higher)
    #mask = cv.bitwise_and(src,src,mask=maskHsv)
    return maskHsv

def contour_finder(src, dst, measure):
    conts,_ = cv.findContours(src, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    for cont in conts:
        area = cv.contourArea(cont)
        if (area > measure):
            cv.drawContours(dst, conts, -1, (0, 255, 255), 2)
    cv.putText(dst,"Area: {0:2.0f}".format(area), (30,35), cv.FONT_HERSHEY_SIMPLEX, 1, (232, 60, 37), 3)
             

cap = cv.VideoCapture('http://192.168.15.65:8080/video')
count = 0

while True:
    _,frame = cap.read()
    resized = cv.resize(frame, (600, 400))

    imgTest = image_process(resized, 13,123,cv.THRESH_BINARY)
    ImgTestMask = mask_image(resized)
    contour_finder(imgTest,ImgTestMask,200)
    
    key = cv.waitKey(1)
    if key == 27: # esc == exit
        break
    elif key == 32: # space == shot
        shot = "Foto{}.jpg".format(count)
        cv.imwrite(shot,resized)
        count += 1

    cv.imshow("Frame",resized)
cap.release()


#https://pysource.com/2018/03/01/find-and-draw-contours-opencv-3-4-with-python-3-tutorial-19/
#https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv