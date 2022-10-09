# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:14:01 2022

@author: nza7
"""

# Tutorial #2 - Basic Operators and Input

name = 'Niz'
print() # takes an argunment in the brackets usally string

# get user input

print ('Hello,What is your name?')
name = input()
print(name)

# The program would do something like this
# What is your name: Niz
# Niz

name = input("What is your name: ")
print("Well hello there", name) 

# The program would do something like this
What is your name: Niz
Well hello there Niz

+  # addition 
-  # subtraction
/  # division
*  # multiplication 
** # exponential
// # integer division (removes decimal portion)
%  # modulus (gives remainder of division) 

x = 5 
y = 6

d = 12 % 5
print(d)

z = x + y   #z is 11
print(z)

w = x - y      # w is -1
print (w)

q = 5 * 6      # q is 30
print (q)

u = 10 / x     # u is 2.0
print(u)

p = 10 * 2.0   # p is 20.0
print(p)

t = x ** 3     # t is 125 Exponents
print(t)

c = 28 // y    # c is 5 integer division rounds down and drops rem.
print(c)

j = x % 2
print(j)        # this gives you the remeiander not the decimal


# BEMDAS
x = (1+3) / 2  # x is 2.0
print(x)

y = 4 + 5 * 7  # y is 39
print(y)


# more stuff!!

num1 = 45
num2 = 4
num3 =num1/num2
print (num3)


# now opperate

print ('pick number: ')
num1 = input ()
print ('pick another number')
num2 = input()

SUM = int(num1) + (num2) # put int and () around num to make sure it recoginzes it is an int
str(3) = '3'
print(SUM)
print(type(num2))


# when we get input of something it gives us a type of a string

