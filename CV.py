from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter.font import Font
main=tk.Tk()
main.minsize(1100,770)
main.maxsize(1100,770)
main.title("CV-ANCIES")
main.iconbitmap('logo..ico')
main.config(bg="#bac2ff")

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
        size = 15,
        weight='bold',
        slant = 'roman',
        overstrike = 0)

my_font3 = Font(
        family = 'Lucida sans',
        size = 14,
        weight='bold',
        slant = 'roman',
        overstrike = 0)

my_font2 = Font(
        family = 'Lucida sans',
        size = 25,
        weight='bold',
        slant = 'roman',
        overstrike = 0)

my_font4 = Font(
        family = 'Lucida sans',
        size = 20,
        weight='bold',
        slant = 'roman',
        overstrike = 0)


#cv_form_frame------------------------------------
def cv_page():
    cv_frame=Frame(main,bg="#2B2828",width=865,height=655)
    cv_frame.place(x=230,y=45)
    cv_ttl=tk.Label(cv_frame,text="CV ENTRIES",font=my_font4,fg="white",bg="#2B2828")
    cv_ttl.place(x=20,y=40)
    cv_ttl2=tk.Label(cv_frame,text="Please enter the following data",font=my_font0,fg="white",bg="#2B2828")
    cv_ttl2.place(x=20,y=85)

    Fname_lbl=tk.Label(cv_frame,text="First Name",font=my_font0,fg="white",bg="#2B2828")
    Fname_lbl.place(x=20,y=130)

    Field_of_job_lbl=tk.Label(cv_frame,text="Field of Job",font=my_font0,fg="white",bg="#2B2828")
    Field_of_job_lbl.place(x=20,y=220)

    contact_lbl=tk.Label(cv_frame,text="Contact Number",font=my_font0,fg="white",bg="#2B2828")
    contact_lbl.place(x=20,y=310)

    email1_lbl=tk.Label(cv_frame,text="Email",font=my_font0,fg="white",bg="#2B2828")
    email1_lbl.place(x=20,y=400)

    address1_lbl=tk.Label(cv_frame,text="Address",font=my_font0,fg="white",bg="#2B2828")
    address1_lbl.place(x=20,y=490)

    aboutMe_lbl=tk.Label(cv_frame,text="Email",font=my_font0,fg="white",bg="#2B2828")
    aboutMe_lbl.place(x=20,y=580)

    extra_skill1_lbl=tk.Label(cv_frame,text="Extra Skill 1",font=my_font0,fg="white",bg="#2B2828")
    extra_skill1_lbl.place(x=305,y=130)

    extra_skill2_lbl=tk.Label(cv_frame,text="Extra Skill 2",font=my_font0,fg="white",bg="#2B2828")
    extra_skill2_lbl.place(x=305,y=220)

    yearsOf_expereience1_lbl=tk.Label(cv_frame,text="Years of Expereience",font=my_font0,fg="white",bg="#2B2828")
    yearsOf_expereience1_lbl.place(x=305,y=310)

    about_experience_lbl=tk.Label(cv_frame,text="About the Experience",font=my_font0,fg="white",bg="#2B2828")
    about_experience_lbl.place(x=305,y=400)

    proficient_Language1_lbl=tk.Label(cv_frame,text="Proficient Language 1",font=my_font0,fg="white",bg="#2B2828")
    proficient_Language1_lbl.place(x=305,y=490)

    proficient_Language2_lbl=tk.Label(cv_frame,text="Proficient Language 2",font=my_font0,fg="white",bg="#2B2828")
    proficient_Language2_lbl.place(x=305,y=580)

    qualification1_lbl=tk.Label(cv_frame,text="Qualification 1",font=my_font0,fg="white",bg="#2B2828")
    qualification1_lbl.place(x=590,y=130)

    qualification2_lbl=tk.Label(cv_frame,text="Qualification 2",font=my_font0,fg="white",bg="#2B2828")
    qualification2_lbl.place(x=590,y=220)

    reference_lbl=tk.Label(cv_frame,text="Reference",font=my_font0,fg="white",bg="#2B2828")
    reference_lbl.place(x=590,y=310)
    
    anything_else1_lbl=tk.Label(cv_frame,text="Anything Else",font=my_font0,fg="white",bg="#2B2828")
    anything_else1_lbl.place(x=590,y=400)

    submit_btn1=Button(cv_frame,text="SUBMIT",font=my_font4,bg="#fCA311",fg="white")
    submit_btn1.place(x=590,y=575)

main.mainloop()

