from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
# from tkinter import messagebox
# import sqlite3

cvtemp=Tk()
cvtemp.minsize(600,690)
cvtemp.maxsize(600,690)
cvtemp.title("CV-ANCIES")
# cvtemp.iconbitmap('logo..ico')
cvtemp.config(bg="white")

my_font0 = Font(
    family = 'Lucida sans',
    size = 12,
    weight='bold',
    slant = 'roman',
    overstrike = 0)
my_font = Font(
    family = 'Lucida sans',
    size = 14,
    weight='bold',
    slant = 'roman',
    overstrike = 0)
my_font1 = Font(
        family = 'Lucida sans',
        size = 17,
        weight='bold',
        slant = 'roman',
        overstrike = 0)
my_font2 = Font(
        family = 'Lucida sans',
        size = 19,
        weight='bold',
        slant = 'roman',
        overstrike = 0)
my_font3 = Font(
        family = 'Lucida sans',
        size = 40,
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

b=id_entry.get()
id_entry.delete(0,END)

r1='Kiyo Tamang'                        #f_name 
r2='IT'                                 # Field_of_job t
r3='9841123456'                         # contact number,
r4='ki123@gmail.com'                    # email1 varchar,
r5='Kyoto'                              # address1 varchar,
r6='I am a blah blah blah.....'         # aboutMe text,
r7='Sketching'                          # extra_skill1 text,
r8='Sleeping'                           # extra_skill2 text,
r9='5'                                  # yearsOf_expereience1 number,
r10='I used to work blah blah blah....' # about_experience text,
r11='Chinese'                           # proficient_Language1 text,
r12='English'                           # proficient_Language2 text,
r13='+2 in cs'                          # qualification1 varchar,
r14='bsc in computing'                  # qualification2 varchar,
r15='Sachi'                             # reference text,
r16="Rather not say"                    # anything_else1

#template frame------------------------------------
cvtime=Frame(cvtemp,bg="black",borderwidth=1)
cvtime.place(x=0,y=120)
log_ttle=Label(cvtemp,text="cv",fg="white",bg="white",padx=316,pady=310)
log_ttle.place(x=0,y=50)

cvt=Frame(cvtemp,bg="white",borderwidth=1)
cvt.place(x=0,y=150)
log_ttle=Label(cvt,text="cv",fg="#98C1D9",bg="#98C1D9",padx=90,pady=380)
log_ttle.grid()

Profile=Label(cvtemp,text=r1,font=my_font3,fg='black',bg='white')
Profile.place(x=310,y=90,anchor=CENTER)
Contact=Label(cvt,text='CONTACT',font=my_font1,fg='white',bg='#98C1D9')
Contact.place(x=35,y=5)

#lines----------------------------------------------------------------
my_canvas=Canvas(cvt,width=192,height=0.1,bg='white',borderwidth=0)
my_canvas.place(x=0,y=35)

Numberlb=Label(cvt,text="Phone no:",font=my_font,fg='#213A5C',bg='#98C1D9')
Numberlb.place(x=0,y=40)
Number=Label(cvt,text=r3,font=my_font0,fg='#213A5C',bg='#98C1D9')
Number.place(x=0,y=70)

Emailb=Label(cvt,text="Email:",font=my_font,fg='#213A5C',bg='#98C1D9')
Emailb.place(x=0,y=95)
Email=Label(cvt,text=r4,font=my_font0,fg='#213A5C',bg='#98C1D9')
Email.place(x=0,y=120)

Addresslb=Label(cvt,text="Address:",font=my_font,fg='#213A5C',bg='#98C1D9')
Addresslb.place(x=0,y=145)
Address=Label(cvt,text=r5,font=my_font0,fg='#213A5C',bg='#98C1D9')
Address.place(x=0,y=170)

#ed---------------

Education=Label(cvt,text='EDUCATION',font=my_font1,fg='white',bg='#98C1D9')
Education.place(x=25,y=200)

my_canvas=Canvas(cvt,width=192,height=0.1,bg='white',borderwidth=0)
my_canvas.place(x=0,y=230)

Quali1=Label(cvt,text="Qualifications:",font=my_font,fg='#213A5C',bg='#98C1D9')
Quali1.place(x=0,y=235)
Quali1=Label(cvt,text=r13,font=my_font0,fg='#213A5C',bg='#98C1D9')
Quali1.place(x=0,y=255)

Quali2=Label(cvt,text=r14,font=my_font0,fg='#213A5C',bg='#98C1D9')
Quali2.place(x=0,y=275)

#skills--------------------------
Skills=Label(cvt,text='SKILLS',font=my_font1,fg='white',bg='#98C1D9')
Skills.place(x=55,y=310)

my_canvas=Canvas(cvt,width=192,height=0.1,bg='white',borderwidth=0)
my_canvas.place(x=0,y=340)

skill1=Label(cvt,text=r7,font=my_font0,fg='#213A5C',bg='#98C1D9')
skill1.place(x=0,y=350)
skill2=Label(cvt,text=r8,font=my_font0,fg='#213A5C',bg='#98C1D9')
skill2.place(x=0,y=370)

#languages---------
Language=Label(cvt,text='LANGUAGE',font=my_font1,fg='white',bg='#98C1D9')
Language.place(x=30,y=410)

my_canvas=Canvas(cvt,width=192,height=0.1,bg='white',borderwidth=0)
my_canvas.place(x=0,y=440)

lang1=Label(cvt,text=r11,font=my_font0,fg='#213A5C',bg='#98C1D9')
lang1.place(x=0,y=450)
lang2=Label(cvt,text=r12,font=my_font0,fg='#213A5C',bg='#98C1D9')
lang2.place(x=0,y=470)

#p------------------
Profile=Label(cvtemp,text='PROFILE',font=my_font2,fg='#213A5C',bg='white')
Profile.place(x=210,y=155)
Profile=Label(cvtemp,text=r6,font=my_font0,fg='black',bg='white')
Profile.place(x=210,y=190)
Experience=Label(cvtemp,text='EXPERIENCE',font=my_font2,fg='#213A5C',bg='white')
Experience.place(x=210,y=270)
Experience=Label(cvtemp,text=r9,font=my_font0,fg='black',bg='white')
Experience.place(x=210,y=300)
Experience=Label(cvtemp,text=r10,font=my_font0,fg='black',bg='white')
Experience.place(x=210,y=320)
FOJ=Label(cvtemp,text='Field of Job',font=my_font2,fg='#213A5C',bg='white')
FOJ.place(x=210,y=380)
FOJ=Label(cvtemp,text=r2,font=my_font0,fg='black',bg='white')
FOJ.place(x=210,y=415)
Reference=Label(cvtemp,text='REFERENCE',font=my_font2,fg='#213A5C',bg='white')
Reference.place(x=210,y=460)
Reference=Label(cvtemp,text=r15,font=my_font0,fg='black',bg='white')
Reference.place(x=210,y=495)
if r16=="":
    pass
else:
    Anything_Else=Label(cvtemp,text='ANYTHING ELSE',font=my_font2,fg='#213A5C',bg='white')
    Anything_Else.place(x=210,y=560)
    Anything_Else=Label(cvtemp,text=r16,font=my_font0,fg='black',bg='white')
    Anything_Else.place(x=210,y=595)

#edit button-------------------------------------------------------------
edit_btn=Button(cvtemp,bg="#3D5A80",fg='white',text="Edit")
edit_btn.place(x=550,y=0)
submit_btn=Button(cvtemp,bg="#3D5A80",fg='white',text="Submit")
submit_btn.place(x=130,y=0)

cvtemp.mainloop()
