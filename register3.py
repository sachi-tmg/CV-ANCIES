from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import messagebox


    #creating a database table

def datab():
    try:
        conn=sqlite3.connect("Cvancies.db")
        c=conn.cursor()
        c.execute("""CREATE TABLE vancy(
            fname TEXT(10),
            lname TEXT(10),
            usrname TEXT,
            email TEXT(30),
            epasswd_entry TEXT(10),
            cpasswd_entry TEXT(10)
            )
        """)
        conn.commit()
        conn.close()
        print("Table created")
    except:
        pass

def register():
    reg_p=Tk()
    reg_p.minsize(900,755)
    reg_p.maxsize(900,755)
    reg_p.title("CV-ANCIES")
    reg_p.iconbitmap('logo..ico')
    reg_p.config(bg="#545B5C")


    
    
      #  from cv_vacancy import vacancy_btn 
      #  from cv_vacancy import cv_btn

    #    updated=form.get()


    #    if updated!= 1 or 2:
    #       win=Tk()
    #       win.title('Error')
    #       win.minsize(250,200)
    #       win.maxsize(250,200)
    #       Label(print("1 or 2 field is empty"))


          
    #    if updated==1:
    #      #  from cv_vacancy import vacancy_btn
    #       reg_p.destroy()
    #       import vacancy
    #      #  vacancy_btn["state"]=DISABLED
    #    elif updated==2:
    #       reg_p.destroy()
    #       import cvform
    #      #  cv_btn["state"]=DISABLED

    def login_page(): 
      #  from cv_vacancy import vacancy_btn 
      #  from cv_vacancy import cv_btn
          reg_p.destroy()
          import login
         #  cv_btn["state"]=DISABLED

    def agree():
        import condn 
        if condn.y==1:
                datab()
                submit()
        elif condn.n==2:
            sign_in.destroy()

#company name---------------------------------------------------------
    def c_name():
        """Company name's entry box appears if the radiobutton "HERE TO UPLOAD VACANCIES" is clicked """
        updated1=form.get()
        def del7(e):
            company_name.delete(0,END)
        if updated1==1:
           company_name=Entry(frame_r,font=my_font1,bg="#E2E6E8",fg="black",width=17)
           company_name.insert(0,"Company name")
           company_name.place(x=50,y=450)
           company_name.bind("<FocusIn>",del7)
           pass
        else: 
           pass
           
    #fonts------------------------------------------------
    my_font = Font(
        family = 'Lucida sans',
        size = 11,
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

    #frame-1---------------------------------------
    frame_r=Frame(reg_p,bg="#fCA311",borderwidth=1)
    frame_r.place(x=110,y=100)
    
    space=Label(frame_r,text="REGISTER",pady=260,padx=310,bg="black",fg="black")
    space.grid()
    
    #labels and entry-----------------------------------------
    r=Label(frame_r,text="REGISTRATION",font=my_font2,bg="black",fg="white")
    r.place(x=200,y=30)

    #deleet funcs----------------------------------------------
    def del1(event):
        x=f_ent.get()
        if x=='first name':
            f_ent.delete(0,END)
    def del2(event):
        x=l_ent.get()
        if x=='last name':
            l_ent.delete(0,END)
    def del3(event):
        x=u_ent.get()
        if x=='Username':
            u_ent.delete(0,END)
    def del4(event):
        x=email_try.get()
        if x=='email@':
            email_try.delete(0,END)
    def del5(event):
        x=pw_ent.get()
        if x=='password':
            pw_ent.delete(0,END)
    def del6(event):
        x=cpw_ent.get()
        if x=='re-enter':
            cpw_ent.delete(0,END)

    #show password functions 
    def show():
        if (yup.get()==1):
            pw_ent.config(show='')
        else:
            pw_ent.config(show='*')

    def show2():
        if  (yupp.get()==1):
            cpw_ent.config(show='')
        else:
            cpw_ent.config(show='*')

    f_name=Label(frame_r,text="First Name: ",font=my_font1,bg="black",fg="white")
    f_name.place(x=50,y=110)
    f_ent=Entry(frame_r,font=my_font1,bg="#E2E6E8",fg="black")
    f_ent.insert(0,"first name")
    f_ent.place(x=50,y=150)
    f_ent.bind("<FocusIn>",del1)

    l_name=Label(frame_r,text="Last Name: ",font=my_font1,bg="black",fg="white")
    l_name.place(x=355,y=110)
    l_ent=Entry(frame_r,font=my_font1,bg="#E2E6E8",fg="black")
    l_ent.insert(0,"last name")
    l_ent.place(x=355,y=150)
    l_ent.bind("<FocusIn>",del2)

    u_name=Label(frame_r,text="Username: ",font=my_font1,bg="black",fg="white")
    u_name.place(x=50,y=210)
    u_ent=Entry(frame_r,font=my_font1,bg="#E2E6E8",fg="black")
    u_ent.insert(0,"Username")
    u_ent.place(x=50,y=250)
    u_ent.bind("<FocusIn>",del3)

    email=Label(frame_r,text="Email: ",font=my_font1,bg="black",fg="white")
    email.place(x=355,y=210)
    email_try=Entry(frame_r,font=my_font1,bg="#E2E6E8",fg="black")
    email_try.insert(0,"email@")
    email_try.place(x=355,y=250)
    email_try.bind("<FocusIn>",del4)

    pw=Label(frame_r,text="Password: ",font=my_font1,bg="black",fg="white")
    pw.place(x=50,y=300)

    pw_ent=Entry(frame_r,font=my_font1,bg="#E2E6E8",fg="black",show="*")
    pw_ent.insert(0,"password")
    pw_ent.place(x=50,y=340)
    pw_ent.bind("<FocusIn>",del5)
    yup=IntVar(value=1)
    Checkbutton(text='Show',offvalue=0,variable=yup,bg='#E2E6E8',command=show).place(x=365,y=442) 

    con_pw=Label(frame_r,text="Confirm Password: ",font=my_font1,bg="black",fg="white")
    con_pw.place(x=355,y=300)

    cpw_ent=Entry(frame_r,font=my_font1,bg="#E2E6E8",fg="black",show="*")
    cpw_ent.insert(0,"re-enter")
    cpw_ent.place(x=355,y=340)
    cpw_ent.bind("<FocusIn>",del6)
    yupp=IntVar(value=1)
    Checkbutton(text='Show',offvalue=0,variable=yupp,bg='#E2E6E8',command=show2).place(x=670,y=442) 

    #verification function 
    def verify():
        global a
        a=f_ent.get()
        global b
        b=l_ent.get()
        global c
        c=u_ent.get()
        global d
        d=email_try.get()
        global e
        e=pw_ent.get()
        global f
        f=cpw_ent.get()
            
        if (a=="" or a=="first name") or (b=="" or b=="last name") or (c=="" or c=="Username") or (d=="" or d=="email@") or (e=="" or e=="password") or (f=="" or f=="re-enter"):
            messagebox.showerror("Signup","One or More Fields Empty.")
        elif "@" and ".com" not in d:
            messagebox.showerror("Signup","Invalid Email")
        elif len(e)<7 or len(e)<7:
            messagebox.showerror("Signup","Password must be more than 7 characters")
        elif f!=e:
            messagebox.showerror("Signup","Passwords not match")
        else:
            agree()

    #terms and conditions 
    # agree_btn=Button(frame_r,text="terms and conditions",font=my_font,bg="#2B2828",fg="#fCA311",command=agree)
    # agree_btn.place(x=445,y=440)
    global sign_in
    sign_in=Button(frame_r,text="NEXT",font=my_font1,bg="#fCA311",fg="black",command=verify)
    sign_in.place(x=520,y=475)        
    global log_in
    log_in=Button(frame_r,text="GO TO LOGIN",font=my_font1,bg="#fCA311",fg="black",command=login_page)
    log_in.place(x=320,y=475)   

    def submit():
        conn= sqlite3.connect('Cvancies.db')

    #create cursor
        c= conn.cursor() 
    
    #insert into tables
        c.execute("INSERT INTO vancy VALUES(:fname, :lname, :usrname, :email, :epasswd_entry, :cpasswd_entry)", {"fname":f_ent.get(),"lname":l_ent.get(), "usrname":u_ent.get(), "email":email_try.get(), "epasswd_entry":pw_ent.get(), "cpasswd_entry":cpw_ent.get()})
        conn.commit()
        conn.close()

    form=IntVar()
   #  form.set("vacancy")
    company=Radiobutton(frame_r,indicatoron=0,
                        state=NORMAL,text="HERE TO UPLOAD VACANCIES",padx=15,
                        variable=form,value=1,
                        font=my_font,bg="#fCA311",fg="black",command=c_name)
    company.place(x=50,y=400)
    employee=Radiobutton(frame_r,indicatoron=0,
                         state=NORMAL,
                         text="HERE TO MAKE CV & FIND JOBS",bg="#fCA311",fg="black",
                         variable=form,value=2,font=my_font,padx=10)
    employee.place(x=355,y=400)
    
    reg_p.mainloop()

register()
