import os

path = 'C:\\CodesPy\\ifsp_ic_julio\\2021-13-10\\Srcs'
files = os.listdir(path)
index=1
        
for index, file in enumerate(files):
    os.rename(os.path.join(path,file), os.path.join(path, ''.join([str(index),'.jpg'])))

#Programa para renomear os arquivos por code ou manual
#diminuir minimal hit -> 0.98
#aumentar 10% no stage (22)
