from tkinter import *

class Calculator:
  def __init__(self, master):
    self.master = master
    master.title("Calculator")

    # Input field
    self.total_display = Entry(master, width=35, borderwidth=5)
    self.total_display.grid(row=0, columnspan=4, padx=10, pady=10)

    # Button functions
    button_1 = Button(master, text="1", command=lambda: self.button_click(1))
    button_1.grid(row=1, column=0, padx=5, pady=5)

    button_2 = Button(master, text="2", command=lambda: self.button_click(2))
    button_2.grid(row=1, column=1, padx=5, pady=5)

    # ... (similar button definitions for other numbers and operators)

    button_clear = Button(master, text="C", command=self.clear_all)
    button_clear.grid(row=4, column=0, padx=5, pady=5)

    button_equal = Button(master, text="=", command=self.calculate)
    button_equal.grid(row=4, column=3, padx=5, pady=5)

    # Internal variables
    self.num1 = None
    self.operation = None
    self.result = None

  def button_click(self, number):
    self.total_display.insert(END, str(number))

  def clear_all(self):
    self.total_display.delete(0, END)
    self.num1 = None
    self.operation = None
    self.result = None

  def calculate(self):
    try:
      self.num2 = int(self.total_display.get())
      if self.operation == "+":
        self.result = self.num1 + self.num2
      elif self.operation == "-":
        self.result = self.num1 - self.num2
      elif self.operation == "*":
        self.result = self.num1 * self.num2
      elif self.operation == "/":
        if self.num2 == 0:
          raise ZeroDivisionError("Division by zero")
        self.result = self.num1 / self.num2

      self.total_display.delete(0, END)
      self.total_display.insert(END, str(self.result))
      self.num1 = self.result
      self.operation = None
    except ValueError:
      pass  # Handle invalid input gracefully (optional)

if __name__ == "__main__":
  root = Tk()
  calculator = Calculator(root)
  root.mainloop()