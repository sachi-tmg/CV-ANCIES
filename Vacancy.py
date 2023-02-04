from tkinter import *
import tkinter as tk
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


def vacancy_page():
    vacancy_frame=Frame(main,bg="#7f9db9",width=865,height=655)
    vacancy_frame.place(x=230,y=45)

    vacancy_ttl=tk.Label(vacancy_frame,text="VACANCIES ENTRIES",font=my_font4,fg="white",bg="#7f9db9")
    vacancy_ttl.place(x=294,y=40)
    vacancy_ttl2=tk.Label(vacancy_frame,text="Please enter the following data",font=my_font ,fg="white",bg="#7f9db9")
    vacancy_ttl2.place(x=298,y=85)

    company_lbl=tk.Label(vacancy_frame,text="Company Name",font=my_font0,fg="white",bg="#7f9db9")
    company_lbl.place(x=20,y=150)
    company_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    company_entry.place(x=20,y=180)

    Fieldofjob_lbl=tk.Label(vacancy_frame,text="Field of Job",font=my_font0,fg="white",bg="#7f9db9")
    Fieldofjob_lbl.place(x=20,y=280)
    Fieldofjob_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    Fieldofjob_entry.place(x=20,y=310)

    contact_no_lbl=tk.Label(vacancy_frame,text="Contact Number",font=my_font0,fg="white",bg="#7f9db9")
    contact_no_lbl.place(x=20,y=410)
    contact_no_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    contact_no_entry.place(x=20,y=440)

    email_lbl=tk.Label(vacancy_frame,text="Contact Number",font=my_font0,fg="white",bg="#7f9db9")
    email_lbl.place(x=20,y=540)
    email_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    email_entry.place(x=20,y=570)

    address_lbl=tk.Label(vacancy_frame,text="Contact Number",font=my_font0,fg="white",bg="#7f9db9")
    address_lbl.place(x=305,y=150)
    address_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    address_entry.place(x=305,y=180)

    req_skill_lbl=tk.Label(vacancy_frame,text="Required Skill",font=my_font0,fg="white",bg="#7f9db9")
    req_skill_lbl.place(x=305,y=280)
    req_skill_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    req_skill_entry.place(x=305,y=310)

    req_qualification_lbl=tk.Label(vacancy_frame,text="Required Qualification",font=my_font0,fg="white",bg="#7f9db9")
    req_qualification_lbl.place(x=305,y=410)
    req_qualification_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    req_qualification_entry.place(x=305,y=440)

    yrsOFexperience_lbl=tk.Label(vacancy_frame,text="Years of experience required",font=my_font0,fg="white",bg="#7f9db9")
    yrsOFexperience_lbl.place(x=305,y=540)
    yrsOFexperience_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    yrsOFexperience_entry.place(x=305,y=570)

    reqLanguage_lbl=tk.Label(vacancy_frame,text="Required Proficient Language",font=my_font0,fg="white",bg="#7f9db9")
    reqLanguage_lbl.place(x=590,y=150)
    reqLanguage_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    reqLanguage_entry.place(x=590,y=180)

    salary_lbl=tk.Label(vacancy_frame,text="Salary",font=my_font0,fg="white",bg="#7f9db9")
    salary_lbl.place(x=590,y=280)
    salary_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    salary_entry.place(x=590,y=310)

    anythingElse_lbl=tk.Label(vacancy_frame,text="Anything Else",font=my_font0,fg="white",bg="#7f9db9")
    anythingElse_lbl.place(x=590,y=410)
    anythingElse_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    anythingElse_entry.place(x=590,y=440)

    submit_btn=Button(vacancy_frame,text="SUBMIT",font=my_font4,bg="#fCA311",fg="white")
    submit_btn.place(x=650,y=545)
main.mainloop()
