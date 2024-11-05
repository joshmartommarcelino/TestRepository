colors = ('red', 'green', 'blue')
color1, color2, color3 = colors
print(color1)
print(color2)
print(color3)

numbers1 = (1,2,3)
numbers2 = (4,5,6)
numbers_combined = numbers1 + numbers2
print(numbers_combined)

alphabet = ('a','b','c','d','e','f','g')
print(alphabet[:3])
print(alphabet[-3])
print(alphabet[::2])

numbers = (1,2,2,3,4,4,4,5)
print(numbers.count(4))
print(numbers.index(2))

nested = (1,2,(3,4),5)
print(nested[2][1])

colors = ('red','green','blue')
print('yellow' in colors)
print('blue' in colors)