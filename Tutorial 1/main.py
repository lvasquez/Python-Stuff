# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

a = 1
c = "Hello there"
print(a)
print(c)
print("Hello World")

v1 = "first string"
v2 = "second string"
print(v1, v2)

temp1 = v1
v1 = v2
v2 = temp1
print(v1, v2)

num1 = 5
num2 = 5
if num1 < num2:
    print("num1 is less than b")
    print("part of de IF")
elif num1 == num2:
    print("num1 is equal to num2")
else:
    print("not less than b")


def function1():
    print("arith")
    print("arith 2")


print("out of the function")
print(function1())


def function2(x):
    return 2*x


f = function2(3)
print(f)

myList = [1, 4, 3, 6]
print(myList)
myList.append(19)
print(myList)
myList.append('hello')
myList.append([2, 6])
print(myList)


fruits = ["banana", "apple", "pear"]
temp = fruits[0]
fruits[0] = fruits[2]
fruits[2] = temp
print(fruits)

for f in fruits:
    print(f)

myNumbers = [2, 10, 55]
total = 0
for n in myNumbers:
    total = total + n

print(total)


list_while = [5, 4, 4, 3, 1, -2, -3, -5]
total2 = 0
j = 0
while list_while[j] > 0:
    total2 += list_while[j]
    j += 1

print(total2)

total3 = 0
for element in list_while:
    if element <= 0:
        break
    total3 += element

print(total3)

for i in range(len(list_while)):
    print(list_while[i])


print(list(range(1, 100)))

total = 0
for i in range(1, 100):
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i
print(total)


total = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

list_tutorial6 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

total2 = 0
lenList = len(list_tutorial6) - 1

while list_tutorial6[lenList] < 0:
    total2 += list_tutorial6[lenList]
    lenList -= 1
print(total2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
