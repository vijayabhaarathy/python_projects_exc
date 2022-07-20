# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 17:42:27 2022

@author: vijay
"""

from tkinter import *
from datetime import date

master = Tk()
master.title('Calculate Age')
master.geometry('250x300')
s1 = Label(master)
age=0

def calc_age():
    global s1
    s1.destroy()
    today = date.today()
    dob = date(int(e2.get()), int(e3.get()), int(e4.get()))
    age = today.year - dob.year
    s1 = Label(text=f"{e1.get()}'s age is {age}!!")
    s1.grid(row=10, column=2, padx=20, pady=10)
    
l1 = Label(master, text = "Name")
l2 = Label(master, text = "Year")
l3 = Label(master, text = "Month")
l4 = Label(master, text = "Date")

name_input = StringVar()
year_input = StringVar()
month_input = StringVar()
day_input = StringVar()

e1 = Entry(master, textvariable=name_input)
e2 = Entry(master, textvariable=year_input)
e3 = Entry(master, textvariable=month_input)
e4 = Entry(master, textvariable=date_input)

b1 = Button(master, text = "Calculate Age", command = calc_age)

l1.grid(row=2, column = 1, padx=2, pady=10)
l2.grid(row=3, column = 1, padx=2, pady=10)
l3.grid(row=4, column = 1, padx=2, pady=10)
l4.grid(row=5, column = 1, padx=2, pady=10)

e1.grid(row=2, column=2, padx=10, pady=10)
e2.grid(row=3, column=2, padx=10, pady=10)
e3.grid(row=4, column=2, padx=10, pady=10)
e4.grid(row=5, column=2, padx=10, pady=10)

b1.grid(row=7, column = 2, padx=10, pady=10)

mainloop()
