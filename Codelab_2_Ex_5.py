import tkinter as tk
from tkinter import font

class MovieDetailsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Details")
        self.root.geometry("600x500")
        self.root.configure(bg='#E9A654')
        
        # Create main frame with padding
        main_frame = tk.Frame(root, bg='#E9A654', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title section with blue background
        title_frame = tk.Frame(main_frame, bg='#8B0000', height=60)
        title_frame.pack(fill=tk.X, pady=(0, 20))
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame, 
            text="Chainsaw Man - The Movie: Reze Arc",
            font=('Times New Roman', 20, 'bold'),
            bg="#8B0000",
            fg='white',
            pady=15
        )
        title_label.pack()
        
        # Movie details section
        details_frame = tk.Frame(main_frame, bg="#E9A654")
        details_frame.pack(fill=tk.BOTH, expand=True)
        
        # Define font styles
        label_font = font.Font(family='Arial', size=11, weight='bold')
        value_font = font.Font(family='Arial', size=11)
        
        # Movie information
        movie_info = [
            ("Release Date:", "23 October 2025"),
            ("Director:", "Tatsuya Yoshihara"),
            ("Main Cast:", "Kikunosuke Toya, Tomori Kusunoki,, Reina Ueda"),
            ("Genre:", "Action, Adventure, Sci-Fi, Seinen, Thriller"),
            ("Runtime:", "100 minutes"),
        ]
        
        # Create labels for each piece of information
        for label_text, value_text in movie_info:
            row_frame = tk.Frame(details_frame, bg='#E9A654')
            row_frame.pack(anchor='w', pady=5)
            
            label = tk.Label(
                row_frame,
                text=label_text,
                font=label_font,
                bg='#E9A654',
                width=15,
                anchor='w'
            )
            label.pack(side=tk.LEFT)
            
            value = tk.Label(
                row_frame,
                text=value_text,
                font=value_font,
                bg='#E9A654',
                anchor='w'
            )
            value.pack(side=tk.LEFT)
        
        # Synopsis section
        synopsis_label = tk.Label(
            details_frame,
            text="Synopsis:",
            font=label_font,
            bg='#E9A654',
            anchor='w'
        )
        synopsis_label.pack(anchor='w', pady=(1, 1))
        
        synopsis_text = (
            "For the first time, Chainsaw Man slashes his way onto the big screen in an epic, action-fueled adventure that continues the hugely popular anime series. "
            "Denji worked as a Devil Hunter for the yakuza, trying to pay off the debt he inherited from his parents, until the yakuza betrayed him and had him killed. "
            "As he was losing consciousness, Denji’s beloved chainsaw-powered devil-dog, Pochita, made a deal with Denji and saved his life. "
            "This fused the two together, creating the unstoppable Chainsaw Man. "
            "Now, in a brutal war between devils, hunters, and secret enemies, a mysterious girl named Reze has stepped into his world, and Denji faces his deadliest battle yet, fueled by love in a world where survival knows no rules."
        )
        
        synopsis_value = tk.Label(
            details_frame,
            text=synopsis_text,
            font=value_font,
            bg='#E9A654',
            wraplength=500,
            justify=tk.LEFT,
            anchor='w'
        )
        synopsis_value.pack(anchor='w', pady=(0, 20))
        
        # Close button
        close_button = tk.Button(
            main_frame,
            text="Close",
            command=root.quit,
            font=('Arial', 10),
            bg='#ADD8E6',
            width=10,
            relief=tk.RAISED,
            bd=2
        )
        close_button.pack(pady=10)

def main():
    root = tk.Tk()
    app = MovieDetailsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()