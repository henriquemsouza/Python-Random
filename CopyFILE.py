import shutil
import os

import glob
#print("entre com  o caminho")
#caminho=input()
#source="\Users\souza\Documents\sng"
#source=Path('\Users\souza\Documents\sng')
#source=os.path.abspath("C:\Users\souza\Documents\sng")
#source=os.path.abspath(caminho)
source=glob.glob("C:\Users\souza\Documents\sng")
#src = "C:\Users\souza\Documents\sng"
destination="\Users\souza\Documents\Q0"
for files in source:
    if files.endswith(".txt"):
        shutil.copy(files,destination)
