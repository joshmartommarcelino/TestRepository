# addition input
A = int(input("First: "))
B = int(input("Second: "))

sum = A + B

print(sum)

# elif age wrong
age = int(input("Enter your age: "))
if age < 18:
      print("You are a minor")
elif age > 18:
      print("you are an adult")

# elif score wrong
score = int(input("What was your score? "))
if score > 59: print('You passed!')
elif score < 59: print('Skill issue')

# else correct age
age = int(input("Enter your age: "))

if age >= 21:
      print("You can drink")
else:
      print("you cannot drink")

# salary else correct
salary = int(input("Enter your salary: "))
if salary >= 10000:
      print("You are a rich")
else:
      print("You are Poor")

# if-elif-else

marks = int(input("Enter your marks: "))

if marks >= 90:
      print ("Grade: A")
elif marks >= 75:
      print("Grade: B")
elif marks >= 60:
      print("Grade: C")   
else:
      print("Grade: F") 

# multiple conditions with "and" & "or"
 
num =int(input("enter a number: "))

if num > 0 and num < 10:
      print(" THe number is a single-digit positive number")
else:
      print("The number is either negative or has more than one digit")

# checking if even or odd

number = int(input("Enter your number: "))

if number % 2 == 0:
      print(f"(number) is an even number.")
else:
      print(f"(number) is an odd number.")

# nested if-else

num =int(input("enter a new number: "))

if num >= 0:
      if num == 0: 
        print("The number is 0")
      else: 
        print("the number is positive")
else:
      print("The Number is negative")






