import urllib.request

from tkinter import *


top = Tk()
top.geometry("100x100")

def ReadCFandWrite():
   x = urllib.request.urlopen('http://www.w3ii.com/pt/python3/python_networking.html')
   saveFile = open('SalveContent.txt','w')
   saveFile.write(str(x.read()))
   saveFile.close()

B = Button(top, text = "Hello", command = ReadCFandWrite)
B.place(x = 50,y = 50)
top.mainloop()
