from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import messagebox

def register():
    reg_p=Tk()
    reg_p.minsize(900,755)
    reg_p.maxsize(900,755)
    reg_p.title("CV-ANCIES")
    reg_p.iconbitmap('logo..ico')
    reg_p.config(bg="#545B5C")
   
    def form_page(): 
      #  from cv_vacancy import vacancy_btn 
      #  from cv_vacancy import cv_btn

       updated=form.get()


    #    if updated!= 1 or 2:
    #       win=Tk()
    #       win.title('Error')
    #       win.minsize(250,200)
    #       win.maxsize(250,200)
    #       Label(print("1 or 2 field is empty"))


          
       if updated==1:
         #  from cv_vacancy import vacancy_btn
          reg_p.destroy()
          import vacancy
         #  vacancy_btn["state"]=DISABLED
       elif updated==2:
          reg_p.destroy()
          import cvform
         #  cv_btn["state"]=DISABLED

    def login_page(): 
      #  from cv_vacancy import vacancy_btn 
      #  from cv_vacancy import cv_btn
          reg_p.destroy()
          import login
         #  cv_btn["state"]=DISABLED

    def agree():
       import terms 
       if terms.y==1:
          pass
       elif terms.n==2:
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
       f_entry.delete(0,END)
    def del2(event):
       l_entry.delete(0,END)
    def del3(event):
       u_entry.delete(0,END)
    def del4(event):
       email_try.delete(0,END)
    def del5(event):
       pw_entry.delete(0,END)
    def del6(event):
       cpw_try.delete(0,END)

    #show password functions 
    def show():
        if (yup.get()==1):
            pw_entry.config(show='')
        else:
            pw_entry.config(show='*')

    def show2():
        if  (yupp.get()==1):
            cpw_try.config(show='')
        else:
            cpw_try.config(show='*')

    f_name=Label(frame_r,text="First Name: ",font=my_font1,bg="black",fg="white")
    f_name.place(x=50,y=110)
    f_entry=Entry(frame_r,font=my_font1,bg="#E2E6E8",fg="black")
    f_entry.insert(0,"first name")
    f_entry.place(x=50,y=150)
    f_entry.bind("<FocusIn>",del1)

    l_name=Label(frame_r,text="Last Name: ",font=my_font1,bg="black",fg="white")
    l_name.place(x=355,y=110)
    l_entry=Entry(frame_r,font=my_font1,bg="#E2E6E8",fg="black")
    l_entry.insert(0,"last name")
    l_entry.place(x=355,y=150)
    l_entry.bind("<FocusIn>",del2)

    u_name=Label(frame_r,text="Username: ",font=my_font1,bg="black",fg="white")
    u_name.place(x=50,y=210)
    u_entry=Entry(frame_r,font=my_font1,bg="#E2E6E8",fg="black")
    u_entry.insert(0,"Username")
    u_entry.place(x=50,y=250)
    u_entry.bind("<FocusIn>",del3)

    email=Label(frame_r,text="Email: ",font=my_font1,bg="black",fg="white")
    email.place(x=355,y=210)
    email_try=Entry(frame_r,font=my_font1,bg="#E2E6E8",fg="black")
    email_try.insert(0,"email@")
    email_try.place(x=355,y=250)
    email_try.bind("<FocusIn>",del4)

    pw=Label(frame_r,text="Password: ",font=my_font1,bg="black",fg="white")
    pw.place(x=50,y=300)

    pw_entry=Entry(frame_r,font=my_font1,bg="#E2E6E8",fg="black",show="*")
    pw_entry.insert(0,"create password")
    pw_entry.place(x=50,y=340)
    pw_entry.bind("<FocusIn>",del5)
    yup=IntVar(value=1)
    Checkbutton(text='Show',offvalue=0,variable=yup,bg='#E2E6E8',command=show).place(x=365,y=442) 

    con_pw=Label(frame_r,text="Confirm Password: ",font=my_font1,bg="black",fg="white")
    con_pw.place(x=355,y=300)

    cpw_try=Entry(frame_r,font=my_font1,bg="#E2E6E8",fg="black",show="*")
    cpw_try.insert(0,"confirm password")
    cpw_try.place(x=355,y=340)
    cpw_try.bind("<FocusIn>",del6)
    yupp=IntVar(value=1)
    Checkbutton(text='Show',offvalue=0,variable=yupp,bg='#E2E6E8',command=show2).place(x=670,y=442) 

    #verification function 
    def verify():
        a=f_entry.get()
        b=l_entry.get()
        c=u_entry.get()
        d=email_try.get()
        e=pw_entry.get()
        f=cpw_try.get()
            
        if (a=="" or a=="first name") or (b=="" or b=="last name") or (c=="" or c=="Username") or (d=="" or d=="email@") or (e=="" or e=="create password") or (f=="" or f=="confirm password"):
            messagebox.showerror("Signup","One or More Fields Empty.")
        elif "@" and ".com" not in b:
            messagebox.showerror("Signup","Invalid Email")
        elif len(d)<7 or len(e)<7:
            messagebox.showerror("Signup","Password must be more than 7 characters")
        elif len(c)!=10:
            messagebox.showerror("Signup","Invalid Phone Number Length")
        elif e!=d:
            messagebox.showerror("Signup","Passwords not match")
    
    #terms and conditions 
    agree_btn=Button(frame_r,text="terms and conditions",font=my_font,bg="#2B2828",fg="#fCA311",command=agree)
    agree_btn.place(x=445,y=440)
    global sign_in
    sign_in=Button(frame_r,text="SIGN UP",font=my_font1,bg="#fCA311",fg="black",command=verify)
    sign_in.place(x=520,y=475)        
    global log_in
    log_in=Button(frame_r,text="GO TO LOGIN",font=my_font1,bg="#fCA311",fg="black",command=login_page)
    log_in.place(x=320,y=475)   
    
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
