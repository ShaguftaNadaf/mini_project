# importing modules

from tkinter import *
from tkinter import Entry, Label, Spinbox, ttk
from tkinter.constants import BOTTOM
import random, string

#----initialize window----
# ----instead to root u write win, window etc----

root = Tk()
root.title(" DataFlair  -  password generator")
root.geometry('100x200')

# creating labels 
# ----there are 2 labels----
label_name = Label(root, text= "PASSWORD GENERATOR", font='arial 15 bold').pack()
label_name1 = Label(root, text ='DataFlair', font ='arial 15 bold').pack(side= BOTTOM)

# password length create
# 1--again craete1 label for pass_length
# 2---pass_length assign strng or intvar
# 3---create a spingbox for length adjustment

pass_label = Label(root, text = 'password length', font='arial 10 bold').pack()
pass_var = IntVar()
pass_length = Spinbox(root,from_ = 7, to_ = 15, width=18, textvariable= pass_var).pack()

# define a func which generate password
# 1--def fun
# 2--create 

pass_str= StringVar()
def generator():

    password = ''
    for j in range(0,5):
        password = random.choice(string.ascii_letters) + random.choice(string.digits) + random.choice(string.punctuation)
    for i in range(pass_var.get()- 5):
        password = password+random.choice(string.ascii_letters + string.digits + string.punctuation)
    pass_str.set(password)
    



button = Button(root, text = 'generate password', command = generator).pack(pady=40)

pass_entrybox = Entry(root, textvariable= pass_str).pack()

root.mainloop()