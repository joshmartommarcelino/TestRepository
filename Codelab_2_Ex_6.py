from tkinter import *
root = Tk()

leftframe=Frame(root,bg='red',width=250)
leftframe.pack(side=LEFT,fill =Y)

topframe = Frame(root, bg='green',width=400,height=200)
topframe.pack(fill=BOTH ,expand=YES)

centreframe = Frame(root, bg='white',width=400,height=200)
centreframe.pack( fill=BOTH,expand=YES )

bottomframe = Frame(root, bg='black',width=400,height=200)
bottomframe.pack( fill=BOTH,expand=YES) 
root.mainloop()
