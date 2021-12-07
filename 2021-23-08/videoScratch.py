import cv2 as cv
import numpy as np

cap = cv.VideoCapture('http://192.168.15.87:8080/video')
count = 0

while True:
    #Image Capture
    _,frame = cap.read()

    #Image Process
    resized = cv.resize(frame,(600,400))
    gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(5,5),0)
    _,bin = cv.threshold(blur,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

    #Mask
    hsv = cv.cvtColor(resized,cv.COLOR_BGR2HSV)
    upper_blue = np.array([121,255,255]) # --> V S H
    lower_blue = np.array([38,86,0])
    mask = cv.inRange(hsv,lower_blue,upper_blue)

    #Contour
    conts,_ = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    if mask.any():
        cv.drawContours(resized,conts,-1,(0,255,0),3)
        #cv.imwrite("CaptureObject.jpg",resized)

    #Image Exit/Shot
    key = cv.waitKey(1)
    if key == ord("e"): # e == exit
        break
    elif key == ord("s"): # s == 'shot'
        shot = "Foto{}.jpg".format(count)
        cv.imwrite(shot,resized)
        count += 1

 
    cv.imshow("Frame",resized)
    cv.imshow("Mask",mask)
cap.release()


#Referências
#Incluir todos estudos ja realizados