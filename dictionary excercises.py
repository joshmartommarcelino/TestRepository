student = {
    'name' : 'Alice',
    'age' : 20,
    'courses' : ['Math', 'Physics']
}
print(student)

Product = {
    'Title' : 'Guitar',
    'price' : 250,
    'Quantity' :1,
}
print(Product)

student_info = {
    'name' : 'Bob',
    'age' : 21,
    'major' : 'Computer Science',
}

student_info_2 = dict(name ="Emma",age=22,major="Biology")

print(student_info)
print(student_info_2)

student_4 = {
    "name" : "Charlie",
    "age" : 19,
    "major" : "Physics"
}

print(student_4['name'])

print(student.get("GPA", "Not Available"))

student_5 = {
    "name" : "Dave",
    "age" : 20,
    "major" : "Chemistry"
}

student_5["GPA"] = 3.8

student_5["age"] = 21

student_5.pop("major")

print(student_5)