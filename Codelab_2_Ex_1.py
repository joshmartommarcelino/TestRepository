import tkinter as tk
from tkinter import ttk, scrolledtext
from collections import Counter

class LetterCounterShapeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Letter Counter & Shape Printer")
        self.root.geometry("700x600")
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_letter_counter_tab()
        self.create_shape_printer_tab()
    
    def create_letter_counter_tab(self):
        # Letter Counter Tab
        self.letter_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.letter_frame, text="Letter Counter")
        
        # Input section
        ttk.Label(self.letter_frame, text="Enter a sentence:", font=("Arial", 12)).pack(pady=10)
        
        self.text_entry = tk.Text(self.letter_frame, height=4, width=60, wrap=tk.WORD)
        self.text_entry.pack(pady=5)
        
        # Buttons
        button_frame = ttk.Frame(self.letter_frame)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Count Letters", command=self.count_letters).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_letter_counter).pack(side=tk.LEFT, padx=5)
        
        # Results section
        ttk.Label(self.letter_frame, text="Results:", font=("Arial", 12, "bold")).pack(pady=(20,5))
        
        # Frame for results
        results_frame = ttk.Frame(self.letter_frame)
        results_frame.pack(fill='both', expand=True, padx=10)
        
        # Total count
        self.total_label = ttk.Label(results_frame, text="Total letters: 0", font=("Arial", 10))
        self.total_label.pack(anchor='w', pady=5)
        
        # Individual letter counts
        self.results_text = scrolledtext.ScrolledText(results_frame, height=15, width=70, state='disabled')
        self.results_text.pack(fill='both', expand=True)
    
    def create_shape_printer_tab(self):
        # Shape Printer Tab
        self.shape_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.shape_frame, text="Shape Printer")
        
        # Controls section
        controls_frame = ttk.Frame(self.shape_frame)
        controls_frame.pack(pady=10)
        
        ttk.Label(controls_frame, text="Select Shape:", font=("Arial", 12)).grid(row=0, column=0, padx=5, sticky='w')
        
        self.shape_var = tk.StringVar(value="triangle")
        shapes = [("Triangle", "triangle"), ("Rectangle", "rectangle"), ("Diamond", "diamond"), ("Heart", "heart")]
        
        for i, (text, value) in enumerate(shapes):
            ttk.Radiobutton(controls_frame, text=text, variable=self.shape_var, value=value).grid(row=0, column=i+1, padx=5)
        
        # Size input - centered in frame
        size_frame = ttk.Frame(self.shape_frame)
        size_frame.pack(pady=10)
        
        # Create a sub-frame to center the size controls
        size_center_frame = ttk.Frame(size_frame)
        size_center_frame.pack()
        
        ttk.Label(size_center_frame, text="Size:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.size_var = tk.StringVar(value="5")
        size_spinbox = ttk.Spinbox(size_center_frame, from_=1, to=30, textvariable=self.size_var, width=8)
        size_spinbox.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(size_center_frame, text="(Note: Heart shape ignores size)", font=("Arial", 8), foreground="gray").pack(pady=5)
        
        # Buttons
        button_frame = ttk.Frame(self.shape_frame)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Generate Shape", command=self.generate_shape).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_shape_display).pack(side=tk.LEFT, padx=5)
        
        # Shape display
        ttk.Label(self.shape_frame, text="Generated Shape:", font=("Arial", 12, "bold")).pack(pady=(20,5))
        
        self.shape_display = scrolledtext.ScrolledText(self.shape_frame, height=20, width=70, 
                                                      font=("Courier", 10), state='disabled')
        self.shape_display.pack(fill='both', expand=True, padx=10)
    
    def count_letters(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        if not text:
            return
        
        # Count only alphabetic characters (case insensitive)
        letters_only = ''.join(char.lower() for char in text if char.isalpha())
        letter_counts = Counter(letters_only)
        total_letters = sum(letter_counts.values())
        
        # Update total count
        self.total_label.config(text=f"Total letters: {total_letters}")
        
        # Display individual letter counts
        self.results_text.config(state='normal')
        self.results_text.delete("1.0", tk.END)
        
        if letter_counts:
            self.results_text.insert(tk.END, "Letter frequencies (case-insensitive):\n")
            self.results_text.insert(tk.END, "="*50 + "\n\n")
            
            # Sort alphabetically
            for letter in sorted(letter_counts.keys()):
                count = letter_counts[letter]
                percentage = (count / total_letters) * 100
                bar = "█" * min(count, 30)  # Visual bar representation
                self.results_text.insert(tk.END, f"{letter.upper()}: {count:3d} ({percentage:5.1f}%) {bar}\n")
            
            self.results_text.insert(tk.END, f"\n{'-'*50}\n")
            self.results_text.insert(tk.END, f"Unique letters: {len(letter_counts)}\n")
            self.results_text.insert(tk.END, f"Total characters: {len(text)}\n")
            self.results_text.insert(tk.END, f"Total letters: {total_letters}\n")
        
        self.results_text.config(state='disabled')
    
    def clear_letter_counter(self):
        self.text_entry.delete("1.0", tk.END)
        self.total_label.config(text="Total letters: 0")
        self.results_text.config(state='normal')
        self.results_text.delete("1.0", tk.END)
        self.results_text.config(state='disabled')
    
    def generate_shape(self):
        shape_type = self.shape_var.get()
        try:
            size = int(self.size_var.get())
        except ValueError:
            size = 5
        
        # Generate the shape
        shape_output = ""
        
        if shape_type == "triangle":
            shape_output = self.create_triangle(size)
        elif shape_type == "rectangle":
            shape_output = self.create_rectangle(size)
        elif shape_type == "diamond":
            shape_output = self.create_diamond(size)
        elif shape_type == "heart":
            shape_output = self.create_heart()
        
        # Display the shape
        self.shape_display.config(state='normal')
        self.shape_display.delete("1.0", tk.END)
        self.shape_display.insert(tk.END, shape_output)
        self.shape_display.config(state='disabled')
    
    def create_triangle(self, height):
        lines = []
        for i in range(1, height + 1):
            spaces = " " * (height - i)
            stars = "*" * (2 * i - 1)
            lines.append(spaces + stars)
        return "\n".join(lines)
    
    def create_rectangle(self, size):
        lines = []
        for i in range(size):
            if i == 0 or i == size - 1:
                lines.append("*" * size)
            else:
                lines.append("*" + " " * (size - 2) + "*")
        return "\n".join(lines)
    
    def create_diamond(self, size):
        lines = []
        # Upper half (including middle)
        for i in range(size):
            spaces = " " * (size - i - 1)
            stars = "*" * (2 * i + 1)
            lines.append(spaces + stars)
        
        # Lower half
        for i in range(size - 2, -1, -1):
            spaces = " " * (size - i - 1)
            stars = "*" * (2 * i + 1)
            lines.append(spaces + stars)
        
        return "\n".join(lines)
    
    def create_heart(self):
        heart_lines = [
            "  **   **  ",
            " **** **** ",
            "***********",
            " ********* ",
            "  *******  ",
            "   *****   ",
            "    ***    ",
            "     *     "
        ]
        return "\n".join(heart_lines)
    
    def clear_shape_display(self):
        self.shape_display.config(state='normal')
        self.shape_display.delete("1.0", tk.END)
        self.shape_display.config(state='disabled')

def main():
    root = tk.Tk()
    app = LetterCounterShapeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()