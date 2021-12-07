import cv2 as cv
import os

def load_dataSet(folder):
    dirPath = folder
    Files = os.listdir(dirPath)
    for File in Files:
        imgPath = os.path.join(dirPath, File)
        img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
        print(imgPath)
        resized = cv.resize(img, (320,240))
        cv.imwrite(f'/home/schendroski/Documentos/ifsp_ic_julio/2021-07-12/dataset_positivo_processado/p_{File}', resized)

load_dataSet('/home/schendroski/Documentos/ifsp_ic_julio/2021-07-12/dataset_positivo')
