from tkinter import *

#basic frame
root= Tk()

#Simple label bg=background color,fg= color of the text 
one=Label(root,text="one",bg="black",fg="white")
one.pack()

two=Label(root,text="two",bg="white",fg="black")
#Fill the entire shaft X
two.pack(fill=X)

ONEE=Label(root,text="ONEE",bg="blue",fg="white")
ONEE.pack(fill=Y)

#basic frame
root.mainloop()
