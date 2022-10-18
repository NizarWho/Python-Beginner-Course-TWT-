# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:24:45 2022

@author: nza7
"""
# Tutorial #7 - while Loops
# need to understand for loops and conditions

#while condition == True:
    #do this

loop = True

while loop:
    name = input('Insert something:')
    if name == 'stop':
        loop = False
        break

# 
loop = True
while loop:
    password = input('Password:')
    if password == 'stop':
        loop = False
        break
# keep aksing until given as opposed to for loop that knows the ammount of times it will run
# while loop do not know how long it will take!