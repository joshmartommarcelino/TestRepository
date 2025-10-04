# Import Module
from tkinter import *
main = Tk() #Defines the buttons
main.title('Using pack()') #label
'''fill expands depending on the x or y axis, and it won't work without saying yes in expand'''
Button(main, text="A").pack(side=LEFT, expand=YES, fill=Y) #left vertical
Button(main, text="B").pack(side=TOP, expand=YES, fill=BOTH) #top left horizontal
Button(main, text="C").pack(side=RIGHT, expand=YES, fill=NONE, anchor=NE,pady=6) #bottom right small
Button(main, text="D").pack(side=BOTTOM, expand=NO, fill=Y,pady=6) #bottom left near center small
main.mainloop()#mainloop()  indicates your application is ready to run
# and it tells the code to keep displaying
def open_second_window():
    root = Tk()
    root.title('User Login()') #label
    Label(root, text="Username").grid(row=0, sticky=W)
    Label(root, text="Password").grid(row=1, sticky=W)
    Entry(root).grid(row=0, column=1, sticky=E)
    Entry(root).grid(row=1, column=1, sticky=E)
    Button(root, text="Login").grid(row=2, column=1, sticky=E)
    open_second_window()
    root.mainloop()
