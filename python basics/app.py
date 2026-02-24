from tkinter import *

root= Tk()
root.geometry("600x600")
frame_one= Frame(root)
frame_one.pack()

def Yaayyy():
    print("Yay dadddy")
button_one= Button(frame_one,text= "touch me daddy", command=Yaayyy)
button_one.pack()

root.mainloop()


