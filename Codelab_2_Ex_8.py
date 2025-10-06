import tkinter as tk

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

tk.Canvas.create_circle = _create_circle

root = tk.Tk()
root.title("Flag of Japan")

# Canvas dimensions (3:2 ratio)
width = 1200
height = 800

canvas = tk.Canvas(root, width=width, height=height, borderwidth=0, 
                   highlightthickness=0, bg="white")
canvas.pack()

# Draw the red circle (Hinomaru - circle of the sun)
# Center of the flag
center_x = width / 2
center_y = height / 2

# Radius is 3/5 of the height divided by 2
radius = (3 * height) / 10

canvas.create_circle(center_x, center_y, radius, fill="#BC002D", outline="")

root.mainloop()