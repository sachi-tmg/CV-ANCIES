from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import messagebox
import sqlite3
 
#button commands---------------------------------------
def registration():
       loginp.destroy()
       import register

def categ():
    if records[i][5]=='Company':
        loginp.destroy()
        import vacancy
    else:
        loginp.destroy()
        import cvform


def check():
    a=user_entry.get()
    b=pw_entry.get()
    try:
        conn=sqlite3.connect('Check.db')
        c=conn.cursor()

        c.execute("SELECT * from vancy")
        global records
        records=c.fetchall()
        global i
        i=len(records)-1
        while i>=0:
            if records[i][2]!=a or records[i][4]!=b:
                i=i-1
                if i==-1:
                    messagebox.showerror("Login","Invalid Credentials")
                    break
                conn.commit()
                messagebox.showinfo("Login","Logged in Successfully")
                categ()
                break           
        conn.commit()
        conn.close()
    except:
        messagebox.showerror("Login","Sign Up First")

loginp=Tk()
loginp.minsize(1000,655)
loginp.maxsize(1000,655)
loginp.title("CV-ANCIES")
loginp.iconbitmap('logo..ico')
loginp.config(bg="black")
#fonst------------------------------------------------
my_font0 = Font(
    family = 'Lucida sans',
    size = 11,
    weight='bold',
    slant = 'roman',
    overstrike = 0)
my_font = Font(
    family = 'Lucida sans',
    size = 13,
    weight='bold',
    slant = 'roman',
    overstrike = 0)
my_font1 = Font(
        family = 'Lucida sans',
        size = 16,
        weight='bold',
        slant = 'roman',
        overstrike = 0)
my_font2 = Font(
        family = 'Lucida sans',
        size = 28,
        weight='bold',
        slant = 'roman',
        overstrike = 0)

#logo------------------------------------------
img=Image.open('lg.png')
img1=img.resize((400,320))
logo=ImageTk.PhotoImage(img1)
logo_p=Label(loginp,image=logo,bg="black")
logo_p.place(x=550,y=150)

#login frame------------------------------------
log=Frame(loginp,bg="white",borderwidth=1)
log.place(x=150,y=135)
log_ttle=Label(log,text="LOGIN",fg="#545B5C",bg="#545B5C",font=my_font2,padx=100,pady=165)
log_ttle.grid()

#event-entries--------------------------------
def del1(event):
       user_entry.delete(0,END)
def del2(e):
       pw_entry.delete(0,END)

#show-password-----------------------------
def show():
        if (shw.get()==1):
            pw_entry.config(show='')
        else:
            pw_entry.config(show='*')

       
#labels and entry 
login_lb=Label(log,text="LOGIN",font=my_font2,bg="#545B5C",fg="black")
login_lb.place(x=100,y=35)

user=Label(log,text="Username:",font=my_font1,bg="#545B5C",fg="black")
user.place(y=98,x=25)

user_entry=Entry(log,bg="#14213D",font=my_font1,fg="white",width=20,borderwidth=2,relief=GROOVE)
user_entry.insert(0,"Username")
user_entry.place(x=27,y=130)
user_entry.bind("<FocusIn>",del1)

pw=Label(log,text="Password:",font=my_font1,bg="#545B5C",fg="black")
pw.place(y=175,x=25)

pw_entry=Entry(log,bg="#14213D",font=my_font1,fg="white",width=20,borderwidth=2,relief=GROOVE)
pw_entry.insert(0,"Password")
pw_entry.place(x=27,y=205)
pw_entry.bind("<FocusIn>",del2)
shw=IntVar(value=1)
Checkbutton(log,text='Show',offvalue=0,variable=shw,bg='#14213D',command=show).place(x=227,y=207) 

def verify():
        a=user_entry.get()
        b=pw_entry.get()
        if (a=="" or a=="Username:") or (b=="" or b=="Password"):
            messagebox.showerror("Login","One or More Fields Empty.")
        elif len(b)<6:
            messagebox.showerror("Password Reset","Password must be more than 6 characters")
        else:
            check()    

log_btn=Button(log,bg="#fCA311",fg='black',text="LOGIN",padx=95,font=my_font, command=verify)
log_btn.place(x=27,y=255)

new=Label(log,bg="#545B5C",text="New to vancies?",fg="white",font=my_font0)
new.place(x=94,y=300)

register_btn=Button(log,bg="#14213D",fg='white',text="REGISTER",font=my_font0,command=registration)
register_btn.place(x=110,y=329)

img2=Image.open('help.png')
img3=img2.resize((20,20))
help_ico=ImageTk.PhotoImage(img3)
help_btn=Button(loginp,image=help_ico,bg="#fCA311").place(x=1050,y=2)

loginp.mainloop()









