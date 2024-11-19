#Python Functions: Exercises with Solutions
#Exercise 1: Greet a User
#Objective: Write a function that greets a user by their name.

#Code:

def greet_user(name):
    """Greets the user with their name."""
    return f"Hello, {name}! Welcome to Python programming."

# Example
print(greet_user("Usman"))

#Exercise 2: Add Two Numbers
#Objective: Write a function to add two numbers.

#Code:

def add_numbers(num1, num2):
    """Adds two numbers and returns the result."""
    return num1 + num2

# Example
print(add_numbers(5, 10))

#Exercise 3: Check Even or Odd
#Objective: Write a function to check whether a number is even or odd.

#Code:

def check_even_odd(number):
    """Checks if a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"

# Example
print(check_even_odd(7))
print(check_even_odd(8))

#Exercise 4: Find the Largest Number
#Objective: Write a function to find the largest of three numbers.

#Code:

def find_largest(num1, num2, num3):
    """Finds and returns the largest of three numbers."""
    return max(num1, num2, num3)

# Example
print(find_largest(10, 20, 15))

#Exercise 5: Calculate Factorial
#Objective: Write a function to calculate the factorial of a number.

#Code:

def calculate_factorial(n):
    """Calculates the factorial of a number."""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Example
print(calculate_factorial(5))

#Exercise 6: Reverse a String
#Objective: Write a function to reverse a string.

#Code:

def reverse_string(text):
    """Reverses the input string."""
    return text[::-1]

# Example
print(reverse_string("Python"))

#Exercise 7: Check Prime Number
#Objective: Write a function to check whether a number is prime.

#Code:

def is_prime(number):
    """Checks if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example
print(is_prime(7))
print(is_prime(10))

#Exercise 8: Count Vowels in a String
#Objective: Write a function to count the number of vowels in a string.

#Code:

def count_vowels(text):
    """Counts the number of vowels in the input string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Example
#print(count_vowels("I love Python programming."))

#Exercise 9: Find the Maximum in a List
#Objective: Write a function to find the maximum number in a list.

#Code:

def find_max_in_list(numbers):
    """Finds the maximum number in a list."""
    return max(numbers)

# Example
print(find_max_in_list([3, 5, 2, 9, 1]))

#Exercise 10: Convert Temperature
#Objective: Write a function to convert temperatures between Celsius and Fahrenheit.

#Code:

def convert_temperature(temperature, scale):
    """Converts temperature between Celsius and Fahrenheit."""
    if scale == "C":
        return (temperature * 9/5) + 32  # Celsius to Fahrenheit
    elif scale == "F":
        return (temperature - 32) * 5/9  # Fahrenheit to Celsius
    else:
        return "Invalid scale"

# Example
print(convert_temperature(0, "C"))  # Celsius to Fahrenheit
print(convert_temperature(32, "F"))  # Fahrenheit to Celsius

def calculate_average():
  """Calculates the average of 4 subjects out of 100."""

  total_marks = 0
  for i in range(1, 5):
    while True:
      try:
        marks = float(input(f"Enter marks for subject {i} (out of 100): "))
        if 0 <= marks <= 100:
          total_marks += marks
          break
        else:
          print("Marks must be between 0 and 100. Please try again.")
      except ValueError:
        print("Invalid input. Please enter a number.")

  average = total_marks / 4
  return average

if __name__ == "__main__":
  average_marks = calculate_average()
  print(f"The average marks are: {average_marks:.2f}")

def calculate_average():  # This is like asking your friend for the scores
  total_marks = 0  # Imagine a box to store the total score, initially empty
  for i in range(1, 5):  # This is like asking for each test score, one by one
    marks = float(input(f"Enter marks for subject {i} (out of 100): "))  # Ask for the score
    total_marks += marks  # Add the score to the box
  average = total_marks / 4  # Divide the total score by 4
  return average  # Give the average score back

if __name__ == "__main__":  # This part just runs the code
  average_marks = calculate_average()  # Get the average
  print(f"The average marks are: {average_marks:.2f}")  # Show the average