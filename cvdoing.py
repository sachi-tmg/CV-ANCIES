from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import messagebox
import sqlite3

cvtemp=Tk()
cvtemp.minsize(650,690)
cvtemp.maxsize(650,690)
cvtemp.title("CV-ANCIES")
cvtemp.iconbitmap('logo..ico')
cvtemp.config(bg="white")



#fonts------------------------------------------------
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




def del1(event):
    a=id_entry.get()
    if a=='Insert User_Id':
       id_entry.delete(0,END)

id_entry=Entry(cvtemp,font=my_font,relief=GROOVE)
id_entry.insert(0,'Insert User_Id')
id_entry.place(x=0,y=0)
id_entry.bind("<FocusIn>",del1)



def load_cv_values():
    try:

        b=id_entry.get()
        id_entry.delete(0,END)
        # Connect to the database
        conn = sqlite3.connect("cv_detail.db")
        c=conn.cursor()
        # Retrieve the CV information
        c.execute("SELECT * FROM cv_placement")
        # global records
        records=c.fetchall()
        counter=1
        for i in records:
            for j in i:
                if counter==1:
                    if j!=b:
                        print("Sachi")
                        if b=="" or b=="Insert User_Id":
                            messagebox.showerror('Error',"Please Insert User_Id")
                        else:
                            messagebox.showerror("Error","Invalid User_Id")
                            break
                    elif j==b:
                        r1=str(i[1])    #f_name 
                        r2=str(i[2])    # Field_of_job t
                        r3=str(i[3])    # contact number,
                        r4=str(i[4])    # email1 varchar,
                        r5=str(i[5])    # address1 varchar,
                        r6=str(i[6])    # aboutMe text,
                        r7=str(i[7])    # extra_skill1 text,
                        r8=str(i[8])    # extra_skill2 text,
                        r9=str(i[9])    # yearsOf_expereience1 number,
                        r10=str(i[10])    # about_experience text,
                        r11=str(i[11])    # proficient_Language1 text,
                        r12=str(i[12])    # proficient_Language2 text,
                        r13=str(i[13])    # qualification1 varchar,
                        r14=str(i[14])    # qualification2 varchar,
                        r15=str(i[15])    # reference text,
                        r16=str(i[16])    # anything_else1
                    
                        
                        #template frame------------------------------------
                        cvtime=Frame(cvtemp,bg="white",borderwidth=1)
                        cvtime.place(x=0,y=120)
                        log_ttle=Label(cvtemp,text="cv",fg="white",bg="white",padx=316,pady=310)
                        log_ttle.place(x=0,y=50)

                        cvt=Frame(cvtemp,bg="white",borderwidth=1)
                        cvt.place(x=0,y=150)
                        log_ttle=Label(cvt,text="cv",fg="#4A78A9",bg="#4A78A9",padx=80,pady=330)
                        log_ttle.grid()
                
                        Profile=Label(cvtemp,text=r1,font=my_font2,fg='black',bg='white')
                        Profile.place(x=310,y=105,anchor=CENTER)
                        Contact=Label(cvt,text='CONTACT',font=my_font1,fg='white',bg='#4A78A9')
                        Contact.place(x=0,y=0)
                        Number=Label(cvt,text=r3,font=my_font0,fg='white',bg='#4A78A9')
                        Number.place(x=0,y=25)
                        Email=Label(cvt,text=r4,font=my_font0,fg='white',bg='#4A78A9')
                        Email.place(x=0,y=50)
                        Address=Label(cvt,text=r5,font=my_font0,fg='white',bg='#4A78A9')
                        Address.place(x=0,y=75)
                        Education=Label(cvt,text='EDUCATION',font=my_font1,fg='white',bg='#4A78A9')
                        Education.place(x=0,y=120)
                        Quali1=Label(cvt,text=r13,font=my_font0,fg='white',bg='#4A78A9')
                        Quali1.place(x=0,y=145)
                        Quali2=Label(cvt,text=r14,font=my_font0,fg='white',bg='#4A78A9')
                        Quali2.place(x=0,y=170)
                        Skills=Label(cvt,text='SKILLS',font=my_font1,fg='white',bg='#4A78A9')
                        Skills.place(x=0,y=215)
                        skill1=Label(cvt,text=r7,font=my_font0,fg='white',bg='#4A78A9')
                        skill1.place(x=0,y=240)
                        skill2=Label(cvt,text=r8,font=my_font0,fg='white',bg='#4A78A9')
                        skill2.place(x=0,y=265)
                        Language=Label(cvt,text='LANGUAGE',font=my_font1,fg='white',bg='#4A78A9')
                        Language.place(x=0,y=310)
                        lang1=Label(cvt,text=r11,font=my_font0,fg='white',bg='#4A78A9')
                        lang1.place(x=0,y=335)
                        lang2=Label(cvt,text=r12,font=my_font0,fg='white',bg='#4A78A9')
                        lang2.place(x=0,y=360)
                        Profile=Label(cvtemp,text='PROFILE',font=my_font1,fg='black',bg='white')
                        Profile.place(x=190,y=150)
                        Profile=Label(cvtemp,text=r6,font=my_font0,fg='black',bg='white')
                        Profile.place(x=190,y=175)
                        Experience=Label(cvtemp,text='EXPERIENCE',font=my_font1,fg='black',bg='white')
                        Experience.place(x=190,y=270)
                        Experience=Label(cvtemp,text=r9,font=my_font0,fg='black',bg='white')
                        Experience.place(x=190,y=295)
                        Experience=Label(cvtemp,text=r10,font=my_font0,fg='black',bg='white')
                        Experience.place(x=190,y=320)
                        FOJ=Label(cvtemp,text='Field of Job',font=my_font1,fg='black',bg='white')
                        FOJ.place(x=190,y=365)
                        FOJ=Label(cvtemp,text=r2,font=my_font0,fg='black',bg='white')
                        FOJ.place(x=190,y=390)
                        Reference=Label(cvtemp,text='REFERENCE',font=my_font1,fg='black',bg='white')
                        Reference.place(x=190,y=460)
                        Reference=Label(cvtemp,text=r15,font=my_font0,fg='black',bg='white')
                        Reference.place(x=190,y=485)
                        if r16=="":
                            pass
                        else:
                            Anything_Else=Label(cvtemp,text='ANYTHING ELSE',font=my_font1,fg='black',bg='white')
                            Anything_Else.place(x=190,y=545)
                            Anything_Else=Label(cvtemp,text=r16,font=my_font0,fg='black',bg='white')
                            Anything_Else.place(x=190,y=570)

                        #edit button-------------------------------------------------------------
                        edit_btn=Button(cvtemp,bg="#3D5A80",fg='white',text="Edit",command=edit)
                        edit_btn.place(x=550,y=0)
                conn.commit()
                conn.close() 
                counter+=1
    except:
        pass
            
        

def edit():
    cvtemp.destroy()
    import cvform

#submit button-------------------------------------------------------------
submit_btn=Button(cvtemp,bg="#3D5A80",fg='white',text="Submit",command=load_cv_values)
submit_btn.place(x=130,y=0)


# Display the window
cvtemp.mainloop()

