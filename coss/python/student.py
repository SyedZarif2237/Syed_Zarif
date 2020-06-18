from tkinter import *
import sqlite3
import tkinter.messagebox
from PIL import Image,ImageTk

root = Tk()
root.geometry('500x650')
root.title("Registration Form")
#root.config(background="white")


def exitt():
    exit()


imge=Image.open("Team Male.png")
photo=ImageTk.PhotoImage(imge)

lab=Label(image=photo)
lab.pack()

fn=StringVar()
ln=StringVar()
dob=StringVar()
var=StringVar()
var_c1= "Java" #checkbox 1
var_c2 = "python" #checkbox 2
radio_var=StringVar() #radio var

# def abt():
#     tkinter.messagebox.showinfo("Welcome","Menu Options")

def ext_1():
    exit()


def database(arg=None):
   name1=fn.get() #first name
   last1=ln.get() #last name
   date=dob.get() #dob
   country=var.get() #country
   prog=var_c2 #prog lang
   gender=radio_var.get() #gender radio button
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Name TEXT,Last TEXT,DOB TEXT,country TEXT,Programming TEXT,Gender Text)')
   cursor.execute('INSERT INTO Student (Name,Last,DOB,country,Programming,Gender) VALUES(?,?,?,?,?,?)',(name1,last1,date,country,prog,gender,))
   conn.commit()
     

label_0 = Label(root, text="Registration form",relief="solid",width=20,font=("arial", 19,"bold"))
label_0.place(x=90,y=150)


label_1 = Label(root, text="FirstName :",width=20,font=("bold", 10))
label_1.place(x=80,y=240)

entry_1 = Entry(root,textvar=fn)
entry_1.place(x=240,y=242)


label_2 = Label(root, text="LastName :",width=20,font=("bold", 10))
label_2.place(x=80,y=280)

entry_2 = Entry(root,textvar=ln)
entry_2.place(x=240,y=282)

label_3 = Label(root, text="DOB :",width=20,font=("bold", 10))
label_3.place(x=80,y=320)

entry_3 = Entry(root,textvar=dob)
entry_3.place(x=240,y=320)

label_3 = Label(root, text="Country :",width=20,font=("bold", 10))
label_3.place(x=75,y=370)

var=StringVar()

list1=["Nepal","India",'America','China',"Canada",'Japan','South Africa']
droplist=OptionMenu(root,var,*list1)
var.set("Select Country")
droplist.config(width=15)
 
droplist.place(x=238,y=370)

label_4 = Label(root, text="Prog Language :",width=20,font=("bold", 10))
label_4.place(x=95,y=420)


c1 = Checkbutton(root, text="java", variable=var_c1).place(x=235,y=420)   #check box 1

c2 = Checkbutton(root, text="python", variable=var_c2).place(x=290,y=420)  #check box 2

label_4 = Label(root, text="Gender :",width=20,font=("bold", 10))
label_4.place(x=73,y=459)

#radio_var=StringVar()
r1=Radiobutton(root, text="Male", variable=radio_var, value="Male").place(x=230,y=460)  #radio 1
r2=Radiobutton(root, text="Female", variable=radio_var, value="Female").place(x=290,y=460)  #radio 2


label_0 = Label(root, text="DOB :",width=20,font=("bold",10))
label_0.place(x=65,y=320)


but_login=Button(root, text='Signup',width=12,bg='brown',fg='white',command=database).place(x=130,y=515)
root.bind("<Return>",database)

but_quit=Button(root, text='Quit',width=12,bg='brown',fg='white',command=exitt).place(x=280,y=515)
#but_login=Button(root,text="login",width=12,bg='brown',fg='white',command=second_win).place(x=208,y=560)

root.mainloop()
