import urllib.request

from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def helloCallBack():
   x = urllib.request.urlopen('http://www.w3ii.com/pt/python3/python_networking.html')
   print(x.read())

B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()
