#1 The If Statement
import string


if 4 < 5:
    print("true")
#2 The Importance of Indentation
number = int(input("Please type a number: "))
if number < 5:
    print("the number is less than 5")
print("I always run")

# If the number is less than 5 both print statements will execute. 
# Otherwise just "I always run" will be printed to the screen

#3 The Else Statement
number = int(input("Please type a number: "))
if number < 5:
    print("the number is less than 5")
else:
    print("the number is NOT less than 5")

# 4 The Elif Statement: allows multiple conditions after if
number = int(input("Please type a number: "))

if number < 5:
    print("the number is less than 5")
elif number < 10:
    print("the number is greater than or 5 and less than 10")
elif number < 15:
    print("the number is greater than or 10 and less than 15")
else:
    print("the number is NOT less than 15")


if number == 10:
    print("The number is 10")
elif number == 15:
    print("The number is 15")

# Notice it is not necessary to include an else


#5 sandbox

color_string = string(input('Pick a color:red / blue / green))
if color == 'red':
    print('You are cool 😎')
elif color == 'blue':
    print('You are blue 💙')
elif color == 'green':
    print('That is my favorite color 💚')
    



