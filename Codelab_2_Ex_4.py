from tkinter import *
root = Tk()
label1 = Label(root, bg='red')
label2 = Label(root, bg='green')
label3 = Label(root, bg='blue') 
# Absolute positioning
label1.place(x = 10, y = 20)
label2.place(x= 20, y= 40)
label3.place(x= 40, y= 60)
root.mainloop()
