import cv2 as cv
import os

#Processing images with threshold
def process_image(src):
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    _, trhs = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
    canny = cv.Canny(trhs, 127,200)
    return trhs

def load_dataSet(folder):
    dirPath = folder
    Files = os.listdir(dirPath)
    for File in Files:
        imgPath = os.path.join(dirPath, File)
        img = cv.imread(imgPath)
        result = process_image(img)
        resized = cv.resize(result, (320,240))
        cv.imwrite(f'C:\\CodesPy\\ifsp_ic_julio\\2021-16-11\\result\\gray_{File}', resized)

load_dataSet('C:\\CodesPy\\ifsp_ic_julio\\2021-16-11\\Srcs')
