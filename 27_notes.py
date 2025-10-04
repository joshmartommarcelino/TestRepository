'''this is a refresher for while and for loops'''
#printing a list of 1-10 using loops

print("=== WHILE LOOPS ===")

# While loop example
print("While loop:")
i = 1
while i <= 10:
    print(i)
    i += 1

print("\n=== FOR LOOPS ===")

# For loop with range
print("For loop with range:")
for i in range(1, 11):
    print(i)

# printing even numbers 1-10

print("WHILE EVEN LOOP:")
i = 2
while i <= 10:
    print(i)
    i += 2

print("\nFOR EVEN LOOP:")
for i in range(2, 11, 2):
    print(i)

# printing odd number 1-10
print("WHILE ODD LOOP:")
i = 1
while i <= 10:
    print(i)
    i += 2

print("\nFOR ODD LOOP:")
for i in range(1, 11, 2):
    print(i)

# Import Module
from tkinter import *
# create root window
root = Tk()
root.title('First App')
# Creates a title in the output
root.geometry('350x600')
# Creates a output Window of size 350 x 600
root.resizable(0, 0)# Output Window size is fixed
#mainloop()  indicates your application is ready to run
# and it tells the code to keep displaying
l = Label(root, text="Hello !",
      	fg="Blue",
      	bg="#FFFFFF",
      	font=('Roboto',25))
l.pack()
l1 = Label(root, text ="My name is Josh",
       	fg="Blue",
      	bg="#FFFFFF",
      	font=('Arial',10))
l1.pack()
l2 = Label(root, text ="I am studying in Bath Spa University Academic center RAK \n I am enrolled in BSc CC Year 2, Group - 2", fg="Blue", bg="#FFFFFF", font=('Arial',8))
l2.pack()
l3 = Label(root,text="Josh Martom Marcelino",fg="Blue", bg="#FFFFFF", font=('Arial',7))
l3.pack()
l1 = Label(root, text ="Hobbies",
       	fg="Blue",
      	bg="#FFFFFF",
      	font=('Arial',10))
l1.pack(anchor = W )
'''This part is for check buttons, west anchoring, radio buttons'''
Label(root, text="Check Buttons to select multiple options").pack(anchor = W) 
C1 = Checkbutton(root, text = "Gaming")
C2 = Checkbutton(root, text = "Guitar")
C1.pack(anchor = W )
C2.pack(anchor = W )
Label(root, text="Radio Buttons to select one option from multiple options").pack(anchor = W)
R1 = Radiobutton(root, text="Web Developer",value=1)
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Data Analyst",value=2)
R2.pack( anchor = W )
R3 = Radiobutton(root, text="Backend Developer",value=3)
R3.pack( anchor = W)

root.mainloop() 