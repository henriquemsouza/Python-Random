from tkinter import *



class BuckyButtons:
    def __init__(self, master):
        frame=Frame(master)

        self.printButton= Button(frame, text="print message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton(frame, text="quit", command=frame.quit())
        self.quitButton.pack(side=LEFT)
    def printMessage(self):
        print("supplise mother f")




root = Tk()
b= BuckyButtons(root)
root.mainloop()
