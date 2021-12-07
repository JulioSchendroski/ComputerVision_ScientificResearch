import cv2
import os
import numpy as np

#Processing images with threshold
def process_image(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((3,3), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=5)
    bg = cv2.dilate(closing, kernel, iterations=3)
    mask = 255 - bg
    result = cv2.bitwise_and(src, src, mask=mask)
    return result

def load_dataSet(folder):
    dirPath = folder
    Files = os.listdir(dirPath)
    for File in Files:
        imgPath = os.path.join(dirPath, File)
        img = cv2.imread(imgPath)
        result = process_image(img)
        resized = cv2.resize(result, (320,240))
        cv2.imwrite(f'/home/schn/Documentos/ifsp_ic_julio/2021-29-11/conict_imgs_result/mask_{File}', resized)

load_dataSet('/home/schn/Documentos/ifsp_ic_julio/2021-29-11/conict_imgs')