#Example of if statement.
num = 7
if num > 0:
    print(num, "this is positive number.")
num = -5
if num < 0:
    print(num,"this is negative number")

# Example of if...else statement.
num = int(input("Enter the number: "))
if num > 0:
    print(num,"this number is postive.")
else:
    print(num,"this number is negative")

# Example of if...elif...else.

num = int(input("Enter the number: "))
if num > 0:
    print(num,"this number is positive")
elif num == 0:
    print("Zero")
else:
    print(num,"this num is negative")


#Python Nested if Example

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
