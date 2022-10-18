# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:14:15 2022

@author: nza7
"""
# Python Programming Tutorial #5 - Chained Conditionals and Nested Statements

# and keyword both conditions met
x = 2 
y = 3

if y  == 3 and x + y == 5:
    print('ran')
    
# or keyword only one condition has to be true

x = 2 
y = 3

if y  == 3 or x + y == 5:
    print('ran')
    
# using not- reverse inside brackets

x = 2 
y = 3

if not ( y  == x and x + y == 6):
    print('ran')
else:
    print(' :( ')
    
# nested if statements

x = 1
y = 4

if x == 2:
    if y == 3:
        print('x = 2, y = 3 ')
    else:
        print('x = 2, y != 3')
else:
    print('x != 2')
