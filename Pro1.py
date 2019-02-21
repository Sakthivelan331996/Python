import tkinter as tk
from tkinter import *
def show():
        username=text1.get()
        password=text2.get()
        if username=="admin" and password =="root":
            print("LOGIN SUCCESSFULL")
        else:
            print("Invalid login")
a=Tk()
a.title("STC")
a.geometry("300x300")
a.configure(background='green')
Label(a,text="username",font=60,fg="white",bg="black").grid(row=1,column=1)
Label(a,text="Password",font=25,fg="red",bg="black").grid(row=2,column=1)
text1=Entry(a,width=20,bg="white")
text1.grid(row=1,column=2)
text2=Entry(a,width=20,bg="white")
text2.grid(row=2,column=2)
e=Button(a,width=10,text='Submit',bg='black',fg='white',font=20,command=show).grid(row=5,column=3)
