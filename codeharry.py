# --------------------chapter 1---------------
# modules
# module is a file containing code written by somebody else which can be impoetrd and used in our program
'''types of modules'''
# 1)Built in module----pre installed in python
# 2)External module-----need to install using pip
'''import os
import flask'''

# pyhton as a calculator use
'''open terminal--type python---REPL lunch READ EVALUATE PRINT LOOP---then
6+5 = 11 OR print('hello world')
for quick execution repl use ----for exit() use'''

# comment---three qoute are work as a comment
'''hello world
----it not execute---'''

# pip
# pip is a package manager for python/ u can use pip to install a module in our system
'''pip install tkinter'''

# print 
# for multiple lines printing
# ('''in this print function if u have to write a poem and have to print then 
# in paranthesis simply you have to write a poem in three qoutes''') 
from tkinter import BooleanVar, StringVar


print("Hello world")
print('''Twinkle Twinkle Little Star
how i wonder what u are
up above the world soo high
like a diamond in the sky''')

# import a module playsound 
'''pip install playsound
from playsound import playsound
playsound(---full_path write---) '''

'''import os
print(os.listdir())
this print the all folders in this '''

# --------------------chapter 2----------------------
# variables and data type 
'''a = 'ashar'--------string data type
b = 342  -------integer data type
c = 34.6 -------float data type
----------------BooleanVar
-----------------None'''
# for type of class 
# print(type(a))=----give thr result type of class is string 

'''assignment operator             comparision operator            logical operator
a = 23                             <                                True
a += 34                             >                                 False       
a -= 2                              ==                                  and
a *= 3                              !=                               or/ not'''

'''input function---
always input fun take input in string only
a = input('enter your name :')
b = input('enter a number :')----
print(type(b))'''

a=2
b=4
print(a+b)
print('the sum of a and b is', 2+4)

a = 45
b = 15
print('the remainder is ', a%b)

user = int(input('enter a number:'))
user1 = int(input('enter secnd number:'))
average = (user + user1)/2
print('average is', average)

# ---------------chapter 3-----------
#                 string                                        methods/ function of string
'''string is a data type and string is immutable                length      .endswith(anything u write at the end)
u write string in a single qoute                                .upper()   .count()    .find()  .replace()
double qoute or three qoute                                     .lower()   .title()'''
'''concatinate string ---means to join the string with +
a = 'good morning'
print(a + name)

name = a s h a r            print(name(4))
    #  0 1 2 3 4                r
    #   -5-4-3-2-1
len(name)-------4 give length of a String
slicing  start argument   stop argument  step argument
      [1:2:1]''' 

# escape sequence
# \t, \n, \\, \', 
# tab, new line,bakslash, single qoute.
# zxxxxx 






