# getting a user in put:

var1 = input("Enter the varaiable: ")
print(var1)

# Program to check input
# type in Python

num1 = input("Enter the num: ")
print(num1)
print("Type of num1: ",type(num1))

name1 = input("Enter the name: ")
print(name1)
print("Type of name1: ",type(name1))

# printing the sum in integer


num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

print("The sum of num1 and num2 : ",num1 + num2)

# printing the sum in float

num1 = float(input("Enter the float num1: "))
num2 = float(input("Enter the float num1: "))

print("The sum of float num1 and float num2: ",num1 + num2)

# string input

string = str(input("Enter the strg: "))
print("Given strg is: ",string)

# multiple input using spli

# taking two inputs at a time

x, y = input("Enter a two value: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

# taking three inputs at a time

x, y, z = input("Enter a three value: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()

# taking two inputs at a time

a, b = input("Enter a two value: ").split()
print("First number is {} and second number is {}".format(a, b))
print()

# taking multiple inputs at a time
# and type casting using list() function

x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x)