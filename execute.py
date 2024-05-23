import os
import subprocess
import time
list = []
executeTime = {}
path = './'
pvFile = []
for file_name in os.listdir(path):
    if '.pv' in file_name:
        pvFile.append(file_name)
for file in pvFile:
    print(file)
    start = time.time()
    p = subprocess.Popen('proverif ../' + file, shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,encoding='utf-8',cwd = './proverif/')
    #list.append(p.communicate()[0])
    print(p.communicate()[0])
    end = time.time()
    executeTime[file] = end - start
for i,j in executeTime.items():
    print(i,j)