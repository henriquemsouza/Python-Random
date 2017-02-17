from tkinter import *

#basic frame
root= Tk()

#make one frame in the top
topFrame = Frame(root)
topFrame.pack()
#make one frame in the bottom
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

buttom1 = Button(topFrame, text="button 1", fg="red")
buttom2 = Button(topFrame, text="button 2", fg="black")
buttom3 = Button(topFrame, text="button 3", fg="green")
buttom4 = Button(bottomFrame, text="button 4", fg="purple")

# .pack to display widget
buttom1.pack(side=LEFT)
buttom2.pack(side=LEFT)
buttom3.pack(side=LEFT)
buttom4.pack(side=BOTTOM)

#basic frame  make  one  loop  of the frame
root.mainloop()
