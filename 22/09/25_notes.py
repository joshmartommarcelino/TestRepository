"""We shall learn the basics of python programming
this section is about comments"""
print("Hello Students") #single line comments
print("Welcome to python programming")

'''A variable is a name that refers to a value.

Variable names are case-sensitive, meaning that spam, SPAM, Spam, and sPaM are 4 different variables.'''

#Initialising variable directly
message= "Good morning"
x = 17
pi = 3.14
a,b = 100, 200 #multiple assignment of variables
MAX_CONNECTIONS = 500 # Constants - UPPERCASE
year_of_study = "Level 5" #String
Age = 18 #Integer
Address = "\nTokyo Tower, Japan"

print('My name is "Josh Martom Marcelino"') #using single quote to be able to use double quote
print("I am", Age, "years old.")
print("I am at", year_of_study)
print("Hatsune\nMiku") #Breaks the line in-between
# The combined print statement using a single f-string with newlines (\n)
print(f'My name is "Josh Martom Marcelino"\nI am {Age} years old.\nI am at {year_of_study}')

'''Simple If Statements
The simplest kind of if statement has one test and one action.'''

voting_age = 19
   #Executes if true
if voting_age >= 18:
    print('You are old enough to vote.')
        #No brackets to open block-indentation does the job.
else:
    #Executes if false
    print("Sorry you are too young to vote.")