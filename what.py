import tkinter as tk
from tkinter import * # While generally discouraged, let's keep it for this example

# 1. ROOT WINDOW: Use Tk() for the main window (main)
main = tk.Tk()
main.title('Main Window - Using pack()')
main.geometry("400x300") # Set size to make it visible

# Widgets for the main window
Button(main, text="A").pack(side=LEFT, expand=YES, fill=Y)
Button(main, text="B").pack(side=TOP, expand=YES, fill=BOTH)
Button(main, text="C").pack(side=RIGHT, expand=YES, fill=NONE, anchor=NE, pady=6)
Button(main, text="D").pack(side=BOTTOM, expand=NO, fill=Y, pady=6)

def open_second_window():
    # 2. SECOND WINDOW: Use Toplevel() for any additional window
    # Pass 'main' as the parent
    secondary = tk.Toplevel(main)
    secondary.title('User Login')
    secondary.geometry("300x150+500+100") # Position it away from the main window

    # Widgets for the secondary window using grid layout
    Label(secondary, text="Username").grid(row=0, sticky=W, padx=5, pady=5)
    Label(secondary, text="Password").grid(row=1, sticky=W, padx=5, pady=5)
    
    Entry(secondary).grid(row=0, column=1, sticky=E, padx=5, pady=5)
    Entry(secondary, show="*").grid(row=1, column=1, sticky=E, padx=5, pady=5)
    
    Button(secondary, text="Login").grid(row=2, column=1, sticky=E, padx=5, pady=5)

def open_third_window():
    # 3. THIRD WINDOW: Use Toplevel() for any additional window
    # Pass 'main' as the parent
    tertiary = tk.Toplevel(main)
    tertiary.title('User Login')
    tertiary.geometry("600x250+600+200") # Position it away from the main window

    # Widgets for the secondary window using grid layout
    Label(tertiary, text="Username").grid(row=0, sticky=W, padx=5, pady=5)
    Label(tertiary, text="Password").grid(row=1, sticky=W, padx=5, pady=5)
    
    Entry(tertiary).grid(row=0, column=1, sticky=E, padx=5, pady=5)
    Entry(tertiary, show="*").grid(row=1, column=1, sticky=E, padx=5, pady=5)
    
    Button(tertiary, text="Login").grid(row=2, column=1, sticky=E, padx=5, pady=5)

def open_fourth_window():
    # 4. FOURTH WINDOW: You know the drill at this point.
    fourth = tk.Toplevel(main)
    fourth.title('Fourth Window (Toplevel)')
    fourth.geometry("400x200+100+500") # Adding a unique geometry is helpful
    label1 = Label(fourth, bg='red', width=10, height=2)
    label2 = Label(fourth, bg='green', width=10, height=2)
    label3 = Label(fourth, bg='blue', width=10, height=2) 
    # Relative positioning
    label1.place(relx=0.5, rely=0.2, anchor='center')
    label2.place(relx=0.5, rely=0.5, anchor='center')
    label3.place(relx=0.5, rely=0.8, anchor='center') 

    # 5. CRITICAL: Do NOT call mainloop() here. The main.mainloop() handles it.

# Now, call the function to create the second window
# The three windows are now created and ready to be displayed.
open_second_window()
open_third_window()
open_fourth_window()


# 4. START LOOP: The ONE AND ONLY mainloop() for the entire application.
main.mainloop()