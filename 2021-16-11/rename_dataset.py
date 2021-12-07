import os

path = 'C:\\CodesPy\\ifsp_ic_julio\\2021-16-11\\Srcs'
files = os.listdir(path)
index=1
        
for index, file in enumerate(files):
    os.rename(os.path.join(path,file), os.path.join(path, ''.join([str(index),'.jpg'])))
