Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>
>>> from tkinter import *
>>> a=Tk()
>>> main.title("STC")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    main.title("STC")
NameError: name 'main' is not defined
>>> a.title("STC")
''
>>> a.geometry("300x300")
''
>>> a.configure(background='green')
>>> label(a,text="username",font=60,fg="white",bg="black").grid(row=1,column=1)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    label(a,text="username",font=60,fg="white",bg="black").grid(row=1,column=1)
NameError: name 'label' is not defined
>>> Label(a,text="username",font=60,fg="white",bg="black").grid(row=1,column=1)

>>> Label(a,text="Password",font=25,fg="red",bg="black").grid(row=1,column=1)

>>> Label(a,text="username",font=60,fg="white",bg="black").grid(row=1,column=1)
>>> Label(a,text="Password",font=25,fg="red",bg="black").grid(row=2,column=1)
>>> 
>>> 
>>> text1=Entry(a,width=20,bg="white")
>>> text1.grid(row=1,column=2)
>>> text2=Entry(a,width=20,bg="white")
>>> text2.grid(row=2,column=2)
>>> e=Button(b,width=10,text='Submit',bg='black',fg='white',font=20)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    e=Button(b,width=10,text='Submit',bg='black',fg='white',font=20)
NameError: name 'b' is not defined
>>> >>> e=Button(a,width=10,text='Submit',bg='black',fg='white',font=20)
SyntaxError: invalid syntax
>>> e=Button(a,width=10,text='Submit',bg='black',fg='white',font=20)
>>> e.grid(row=5,column=3)
>>> 
