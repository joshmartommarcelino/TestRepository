# Creating the dictionary
student = {
    "Name": "Alice",
    "Age": 24,
    "Major": "Computer Science"
}

# Accessing and printing values
print("Name:", student["Name"])
print("Major:", student["Major"])

# Adding a new key-value pair
student["GPA"] = 3.8

# Updating the Age
student["Age"] = 25

# Printing the updated dictionary
print(student)

for key, value in student.items():
    print(f"{key}: {value}")

def check_key(dictionary, key):
    if key in dictionary:
        return "Key exists"
    else:
        return "Key does not exist"

# Testing the function
print(check_key(student, "Name"))  # Output: Key exists
print(check_key(student, "Hobbies"))  # Output: Key does not exist

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Merging dictionaries
merged_dict = {**dict1, **dict2}
print(merged_dict)

# Removing a key
student.pop("Age", None)  # Using pop with a default value to avoid KeyError if the key doesn't exist

# Printing the updated dictionary
print(student)

classroom = {
    "Student1": {"Name": "John", "Age": 20},
    "Student2": {"Name": "Emma", "Age": 22}
}

# Accessing values
print("Student2 Name:", classroom["Student2"]["Name"])
print("Student1 Age:", classroom["Student1"]["Age"])

classroom = {
    "Student1": {"Name": "John", "Age": 20},
    "Student2": {"Name": "Emma", "Age": 22}
}

# Accessing values
print("Student2 Name:", classroom["Student2"]["Name"])
print("Student1 Age:", classroom["Student1"]["Age"])

squares = {x: x**2 for x in range(1, 6)}
print(squares)