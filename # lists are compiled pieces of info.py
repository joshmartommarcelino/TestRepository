# lists are compiled pieces of info

integers = [2, 4, 6, 8, 10]
print(integers)

strings = ["Josh", "Allen", "Jheirom", "Denson", "Aniel"]
print(strings)

float = [ "Miku", 39, 1.01]
print(float)

marks=[2,45,67,89,25]

print(marks[-2])

print(len(marks))

print(marks + float)

print(marks[:2])

fruits=["apple","banana","cherry"]
print(fruits)

numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])

animals=["cat","dog","bird"]
animals[1] = "hamster"
animals[2] = "hedgehog"
print(animals)

colors=[]
colors.append("red")
colors.append("green")
colors.append("blue")
colors.remove("red")
print(colors)

names=["alice","bob","diana"]
print("Length of the list:", len(names))

numbers = [4, 7, 1, 8, 5]
total_sum = sum(numbers)
print("Sum of elements:", total_sum)

age=[23, 45, 28, 34, 60]
print("Maximum age:", max(age))
print("minimum age:", min(age))

scores=[88,56,92,78,61]
scores.sort()
print("Sorted list:", scores)

numbers=[1,3,5,7,9]
if 5 in numbers:
    print("Found)")
else: 
    print("Not Found")

items=[1,2,2,3,4,4,4,5]
count_of_4 = items.count(4)
print("count of 4:", count_of_4)

list_1=[2,4,6,2,7,3,63,3]
list_2=[5,7,5,12,3,5,44,6]

print(list_1 + list_2)

list_1.extend(list_2)
print(list_1)

list_1.reverse()
print(list_1)