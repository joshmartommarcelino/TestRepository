from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer

# Initialize pygame mixer for MP3 support
mixer.init()

root = Tk()
root.geometry("2560x1440") 
root.title("Working with images") 

def play_sound():
    mixer.music.load("moka-cinnamon.mp3")
    mixer.music.play()

# Main frame with blue background
main_frame = Frame(root, bg="#5479E9", padx=20, pady=20)
main_frame.pack(fill=BOTH, expand=True)

# Title section with yellow background
title_frame = Frame(main_frame, bg="#FFEF16", height=60)
title_frame.pack(fill=X, pady=(0, 20))
title_frame.pack_propagate(False)

title_label = Label(    
    title_frame, 
    text="Cinammoroll Button",
    font=('Arial', 20, 'bold'),  # Changed from 'Selecta' to 'Arial'
    bg="#FFEF16",
    fg='white',
    pady=15)
title_label.pack()

# Load and resize image
img = Image.open("cinammoroll.png")
resized_image = img.resize((600, 400))
new_image = ImageTk.PhotoImage(resized_image)

# Create button with image
button = Button(main_frame, image=new_image, command=play_sound, border=0)
button.pack(pady=20)

root.mainloop()