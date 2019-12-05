#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:47:19 2019

@author: hala
"""

import sqlite3
conn = sqlite3.connect('OrgDB.db')
from tkinter import *
from tkinter import Tk
from tkinter import scrolledtext
from tkinter import messagebox
import functools
root=Tk()
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
w="500x500+"+str(int((screen_width-500)/2))+"+"+str(int((screen_height-500)/2))
root.geometry(w)

# =============================================================================
# Create DataBase with tabel
# =============================================================================
# c = conn.cursor()
# c.execute('''CREATE TABLE employee
#           (number int, name text, gender text, nationality text, dateofbirth text,address text,deparment text,salary real)''')
# conn.commit()
# conn.close()
# =============================================================================


# =============================================================================
# add function
# =============================================================================
def add():
    def save():
        c = conn.cursor()
        c.execute("INSERT INTO employee VALUES(?,?,?,?,?,?,?,?)",(val1.get(),val2.get(),val3.get(),val4.get(),val5.get(),val6.get(),val7.get(),val8.get()))
        conn.commit()

        
    StdWin=Toplevel(root)
    StdWin.title(' window')
    StdWin.geometry('400x250')
    number=Label(StdWin,text="Number").place(x=30,y=50)
    name=Label(StdWin,text="Name").place(x=30,y=90)
    gender=Label(StdWin,text="gender").place(x=30,y=120)
    nationality=Label(StdWin,text="nationality").place(x=30,y=150)
    dateofbirth=Label(StdWin,text="dateofbirth").place(x=30,y=170)
    address=Label(StdWin,text="address").place(x=30,y=200)
    deparment=Label(StdWin,text="deparment").place(x=30,y=220)
    salary=Label(StdWin,text="salary").place(x=30,y=240)
    button=Button(StdWin,text="Save",command=save).place(x=150,y=260)
    val1=IntVar()
    val2=StringVar()
    val3=StringVar()
    val4=StringVar()
    val5=StringVar()
    val6=StringVar() 
    val7=StringVar()
    val8=IntVar()
    e1=Entry(StdWin,textvariable=val1).place(x=100,y=60)
    e2=Entry(StdWin,textvariable=val2).place(x=100,y=90)
    e3=Entry(StdWin,textvariable=val3).place(x=100,y=120)
    e4=Entry(StdWin,textvariable=val4).place(x=100,y=150)
    e5=Entry(StdWin,textvariable=val5).place(x=100,y=170)
    e6=Entry(StdWin,textvariable=val6).place(x=100,y=200)
    e7=Entry(StdWin,textvariable=val7).place(x=100,y=220)
    e8=Entry(StdWin,textvariable=val8).place(x=100,y=240)

# =============================================================================
# view function
# =============================================================================
def view():
    c = conn.cursor()
    c.execute("SELECT * FROM employee")
    
    StdWin=Toplevel(root)
    StdWin.title(' window')
    StdWin.geometry('400x250')
    txt = scrolledtext.ScrolledText(StdWin, width=200, height=200, wrap=WORD)
    for row in c:
        txt.insert(END,row)
        txt.insert(END,"\n")
    
    txt.yview(END)
    txt.pack()
    conn.commit() 



# =============================================================================
# Main view
# =============================================================================
top=Menu(root)
root.config(menu=top)
file=Menu(top,tearoff=0)
file.add_command(label='Add employee',command=add)
file.add_command(label='view employee',command=view)
file.add_separator()
file.add_command(label='Quit',command=root.destroy)
top.add_cascade(label='File',menu=file)
root.mainloop()