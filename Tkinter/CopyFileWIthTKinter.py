import os
import shutil
from tkinter import *

top = Tk()
top.geometry("500x100")

L1 = Label(top, text="Entre com  o caminho do Binario")
L1.pack( side = LEFT)
srcEntry = Entry(top, bd =1)
srcEntry.pack(side = RIGHT)
srcEntry["width"]=100

srcEntry.get()
src=srcEntry




def CallCopyFile():
    src_files = os.listdir(src)
    for file_name in src_files:
     full_file_name = os.path.join(src, file_name)
     if (os.path.isfile(full_file_name)and full_file_name.endswith(".txt")):
        shutil.copy(full_file_name, 'H:\COPP')
        
B = Button(top, text ="Baixar", command = src and CallCopyFile)
B.place(x=80,y=70)





top.mainloop()
