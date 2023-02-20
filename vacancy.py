
from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
import tkinter as tk
import sqlite3
from tkinter import messagebox
import runpy

main = Tk()
main.minsize(1100, 710)
main.maxsize(1100, 710)
main.title("CV-ANCIES")
main.iconbitmap('logo..ico')
main.config(bg="#4A78A9")

global s
s = 0


# button commands---------------------------------------------
def exit_all():
    main.destroy()


def home():
    main.destroy()
    runpy.run_path("scratch.py")


my_font0 = Font(
    family='Lucida sans',
    size=11,
    weight='bold',
    slant='roman',
    overstrike=0)

my_font = Font(
    family='Lucida sans',
    size=13,
    weight='bold',
    slant='roman',
    overstrike=0)

my_font1 = Font(
    family='Lucida sans',
    size=15,
    weight='bold',
    slant='roman',
    overstrike=0)
my_font2 = Font(
    family='Lucida sans',
    size=25,
    weight='bold',
    slant='roman',
    overstrike=0)
my_font3 = Font(
    family='Lucida sans',
    size=14,
    weight='bold',
    slant='roman',
    overstrike=0)
my_font4 = Font(
    family='Lucida sans',
    size=20,
    weight='bold',
    slant='roman',
    overstrike=0)


def about_p():
    abt = Frame(main, bg="black", borderwidth=2)
    abt.place(x=230, y=47)
    for_place = Label(abt, text="REGISTER", font=my_font, padx=655, pady=700, bg="#2B2828", fg="#2B2828")
    for_place.grid()
    my_font5 = Font(
        family='Lucida sans',
        size=60,
        weight='bold',
        slant='roman',
        overstrike=0)
    Label(abt, text="KASP", font=my_font5, bg="#2B2828", fg="#fCA311").place(x=130, y=15)
    i1 = Image.open('abt.png')
    i2 = i1.resize((490, 525))
    i3 = ImageTk.PhotoImage(i2)
    i4 = Label(abt, image=i3, bg="#2B2828")
    i4.image = i3
    i4.place(x=10, y=105)
    img = Image.open('lg.png')
    img1 = img.resize((390, 310))
    logo = ImageTk.PhotoImage(img1)
    logo5 = Label(abt, image=logo, bg="#2B2828")
    logo5.image = logo
    logo5.place(x=480, y=20)


def datab():
    try:
        log = sqlite3.connect('Vacancy.db')
        log1 = log.cursor()
        log1.execute("""CREATE TABLE details(
            name text,
            address text,
            language text,
            field text,
            skills text,
            salary number,
            contact number,
            qualification varchar,
            anything_else varchar,
            email varchar,
            yearOfExperience varchar,
            )
                    """)
        log.commit()
        log.close()
    except:
        pass


# logo--------------------------------------------------
img = Image.open('lg.png')
img1 = img.resize((220, 180))
logo = ImageTk.PhotoImage(img1)

img2 = Image.open('help.png')
img3 = img2.resize((30, 30))
help_ico = ImageTk.PhotoImage(img3)

img4 = Image.open('settings.png')
img5 = img4.resize((30, 30))
settings_ico = ImageTk.PhotoImage(img5)

# bar frame-------------------------------------------
bar = Frame(main, bg="white", borderwidth=1)
bar.grid(sticky=W)
random = Label(bar, text='hello', fg="black", bg="black", pady=380, padx=97).grid()

# inserting logo------------------------------------------
logo1 = Label(bar, image=logo, bg="black").place(y=25)

# buttons--------------------------------------------

about_btn = Button(bar, text="ABOUT", bg="#213A5C", fg="white", padx=73.2, pady=4, font=my_font,
                   command=lambda: indicate(about_indicate, about_p))
about_btn.place(y=285, x=0)

cv_btn = Button(bar, text="CV FORM", bg="#213A5C", fg="white", padx=63.4, font=my_font, pady=4, state=DISABLED)
cv_btn.place(y=330, x=0)

vacancy_btn = Button(bar, text="VACANCY FORM", bg="#213A5C", fg="white", padx=31.4, font=my_font, pady=4,
                     command=lambda: indicate(vacancy_indicate, vacancy_page))
vacancy_btn.place(y=375, x=0)

profile_btn = Button(bar, text="PROFILE", bg="#213A5C", fg="white", padx=67, font=my_font, pady=4,
                     command=lambda: indicate(profile_indicate, profile))
profile_btn.place(y=420, x=0)

exit_btn = Button(bar, text="EXIT", bg="#213A5C", fg="white", padx=83.4, font=my_font, pady=4, command=exit_all)
exit_btn.place(y=465, x=0)

# logout__ icon-------------------------------------
ico101 = Image.open('lgicon.png')
ico102 = ico101.resize((90, 90))
ico103 = ImageTk.PhotoImage(ico102)

lo_btn = Button(bar, image=ico103, bg="black", padx=76.2, font=my_font, pady=4, command=home, borderwidth=0,
                activebackground="black")
lo_btn.place(y=520, x=70)

# top bar--------------------------------------------------
cvbar = Frame(main, bg="white", borderwidth=1)
cvbar.place(x=225, y=0)
spa = Label(cvbar, text="hello", bg="black", fg="black", padx=530, pady=10).grid()

help_btn = Button(main, image=help_ico, bg="white").place(x=1020, y=2)
settings_btn = Button(main, image=settings_ico, bg="white").place(x=1060, y=2)

# indicate_buttons
# home_indicate = tk.Label(bar, text=' ', bg="#fCA311")
# home_indicate.place(x=0, y=240, width=5, height=37)

about_indicate = tk.Label(bar, text=' ', bg="#fCA311")
about_indicate.place(x=0, y=285, width=5, height=37)

cv_indicate = tk.Label(bar, text=' ', bg="#fCA311")
cv_indicate.place(x=0, y=330, width=5, height=37)

vacancy_indicate = tk.Label(bar, text=' ', bg="#fCA311")
vacancy_indicate.place(x=0, y=375, width=5, height=37)

profile_indicate = tk.Label(bar, text=' ', bg="#fCA311")
profile_indicate.place(x=0, y=420, width=5, height=37)

exit_indicate = tk.Label(bar, text=' ', bg="#fCA311")
exit_indicate.place(x=0, y=465, width=5, height=37)


# hide_function-------
def hide_indicators(lb):
    # home_indicate.config(bg="#fCA311")
    about_indicate.config(bg="#fCA311")
    cv_indicate.config(bg="#fCA311")
    vacancy_indicate.config(bg="#fCA311")
    profile_indicate.config(bg="#fCA311")
    exit_indicate.config(bg="#fCA311")


# indicate_function---------------
def indicate(lb, page):
    hide_indicators(lb)
    lb.config(bg='#91ffff')
    page()


def vacancy_page():
    vacancy_frame=Frame(main,bg="#3D5A80",width=865,height=655)
    vacancy_frame.place(x=230,y=47)

    vacancy_ttl=tk.Label(vacancy_frame,text="VACANCIES ENTRIES",font=my_font4,fg="white",bg="#3D5A80")
    vacancy_ttl.place(x=294,y=40)
    vacancy_ttl2=tk.Label(vacancy_frame,text="Please enter the following data (* Required)",font=my_font ,fg="white",bg="#3D5A80")
    vacancy_ttl2.place(x=298,y=85)

    company_lbl=tk.Label(vacancy_frame,text="Company Name *",font=my_font0,fg="white",bg="#3D5A80")
    company_lbl.place(x=20,y=150)
    company_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    company_entry.place(x=20,y=180)

    Fieldofjob_lbl=tk.Label(vacancy_frame,text="Field of Job *",font=my_font0,fg="white",bg="#3D5A80")
    Fieldofjob_lbl.place(x=20,y=280)
    Fieldofjob_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    Fieldofjob_entry.place(x=20,y=310)

    contact_no_lbl=tk.Label(vacancy_frame,text="Contact Number *",font=my_font0,fg="white",bg="#3D5A80")
    contact_no_lbl.place(x=20,y=410)
    contact_no_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    contact_no_entry.place(x=20,y=440)

    email_lbl=tk.Label(vacancy_frame,text="E-mail *",font=my_font0,fg="white",bg="#3D5A80")
    email_lbl.place(x=20,y=540)
    email_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    email_entry.place(x=20,y=570)

    address_lbl=tk.Label(vacancy_frame,text="Address *",font=my_font0,fg="white",bg="#3D5A80")
    address_lbl.place(x=305,y=150)
    address_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    address_entry.place(x=305,y=180)

    req_skill_lbl=tk.Label(vacancy_frame,text="Required Skill *",font=my_font0,fg="white",bg="#3D5A80")
    req_skill_lbl.place(x=305,y=280)
    req_skill_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    req_skill_entry.place(x=305,y=310)

    req_qualification_lbl=tk.Label(vacancy_frame,text="Required Qualification *",font=my_font0,fg="white",bg="#3D5A80")
    req_qualification_lbl.place(x=305,y=410)
    req_qualification_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    req_qualification_entry.place(x=305,y=440)

    yrsOFexperience_lbl=tk.Label(vacancy_frame,text="Years of experience required *",font=my_font0,fg="white",bg="#3D5A80")
    yrsOFexperience_lbl.place(x=305,y=540)
    yrsOFexperience_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    yrsOFexperience_entry.place(x=305,y=570)

    reqLanguage_lbl=tk.Label(vacancy_frame,text="Required Proficient Language *",font=my_font0,fg="white",bg="#3D5A80")
    reqLanguage_lbl.place(x=590,y=150)
    reqLanguage_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    reqLanguage_entry.place(x=590,y=180)

    salary_lbl=tk.Label(vacancy_frame,text="Salary *",font=my_font0,fg="white",bg="#3D5A80")
    salary_lbl.place(x=590,y=280)
    salary_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    salary_entry.place(x=590,y=310)

    anythingElse_lbl=tk.Label(vacancy_frame,text="Anything Else",font=my_font0,fg="white",bg="#3D5A80")
    anythingElse_lbl.place(x=590,y=410)
    anythingElse_entry=tk.Entry(vacancy_frame,bg="white",fg="black",font=my_font3)
    anythingElse_entry.place(x=590,y=440)



    def verify():
        a = company_entry.get()
        b = address_entry.get()
        c = reqLanguage_entry.get()
        d = Fieldofjob_entry.get()
        e = req_skill_entry.get()
        f = salary_entry.get()
        g = contact_no_entry.get()
        h = req_qualification_entry.get()
        i = email_entry.get()
        j = yrsOFexperience_entry.get()

        if (a == "") or (b == "") or (c == "") or (d == "") or (e == "") or (f == "") or (g == "")  or (h == "") or (i == "") or (j == ""):
            messagebox.showerror("ERROR", "One or More Fields Empty.")
        elif (len(g)<10) or (len(g)>10):
            messagebox.showerror("ERROR", "Invalid Contact!")
        else:
            datab()
            submit()

    submit_btn = Button(vacancy_frame, text="SUBMIT", font=my_font4, bg="#213A5C", fg="white", command=verify)
    submit_btn.place(x=650, y=545)

    def submit():
        global s
        s = s + 1
        log = sqlite3.connect('Vacancy.db')

        # create cursor
        log1 = log.cursor()

        # insert into tables
        log1.execute(
            "INSERT INTO details VALUES(:name, :address, :language, :field, :skills, :salary, :contact, :qualification, :anything_else, :email, :yearOfExperience)",
            {
                'name': company_entry.get(),
                'address': address_entry.get(),
                'language': reqLanguage_entry.get(),
                'field': Fieldofjob_entry.get(),
                'skills': req_skill_entry.get(),
                'salary': salary_entry.get(),
                'contact': contact_no_entry.get(),
                'qualification': req_qualification_entry.get(),
                'anything_else': anythingElse_entry.get(),
                'email': email_entry.get(),
                'yearOfExperience': yrsOFexperience_entry.get(),

            })
        messagebox.showinfo("Vacancy Number!",f" {s} ,The vacancy number is needed for editing and updating!" )


        log.commit()
        log.close()




        # clear entries
        company_entry.delete(0, END)
        address_entry.delete(0, END)
        reqLanguage_entry.delete(0, END)
        req_skill_entry.delete(0, END)
        Fieldofjob_entry.delete(0,END)
        salary_entry.delete(0, END)
        contact_no_entry.delete(0, END)
        req_qualification_entry.delete(0, END)
        anythingElse_entry.delete(0, END)
        email_entry.delete(0, END)
        yrsOFexperience_entry.delete(0, END)
        messagebox.showinfo('Vacancy', 'Your data has been saved! ')



def profile():
    profile_p = Frame(main, bg="#4A78A9", width=865, height=655)
    profile_p.place(x=230, y=47)
    for_place = Label(profile_p, text="AVAILABLE VACANCIES", font=my_font2, bg="#4A78A9", fg="white")
    for_place.place(x=260, y=20)
    board = Frame(profile_p, bg="#3D5A80", borderwidth=1, width=300)
    board.place(x=130, y=530)
    # ignore this-----
    for_space = Label(board, text="profile", pady=30, padx=200, bg="#3D5A80", fg="#2B2828")
    for_space.grid()
    #importing username------


    #for username----
    # us = sqlite3.connect('CVAN.db')
    # usr = us.cursor()
    # usr.execute("SELECT * FROM vancy")
    # uname = usr.fetchall()
    # i = len(uname) - 1
    # while i >= 0:
    #     bb = uname[i][3]
    #     if bb == aa:
    #         dis_nam = aa
    #         print(dis_nam)
    #         break
    #     i = i - 1


    # us.commit()
    # us.close()

#     try:
#         # fetching data----
#         log = sqlite3.connect('Vacancy.db')
#
#     # create cursor----
#         log1 = log.cursor()
#
#         log1.execute("SELECT * FROM details")
#
# #data for post 1---
#         fet = log1.fetchone()
#         cname = fet[0]
#         rq = fet[7]
#         fw = fet[3]
#         rs = fet[4]
#         log.commit()
#         log.close()
#     except:
#         messagebox.showinfo("ERROR", "The company doesn't have enough vacancies! Atleast 2 DATA required.")




    try:
        #connecting
        log = sqlite3.connect('Vacancy.db')

        # create cursor----
        log1 = log.cursor()

        log1.execute("SELECT * FROM details")
        # data for post 2 ----
        po = log1.fetchall()
        po1 = tuple(po)
        # po2 = po1[1]
        first_tup = po1[0]
        second_tup =po1[1]
        cn = first_tup[0]
        cn1 = second_tup[0]
        rq1 = first_tup[7]
        rq = second_tup[7]
        fw1 = first_tup[3]
        fw = second_tup[3]
        rs1 = first_tup[4]
        rs = second_tup[4]
    except:
        messagebox.showinfo("ERROR", "The company doesn't have enough vacancies! Atleast 2 DATA required for edit.")

    log.commit()
    log.close()

    # labels----
    coname_l = Label(board,
        text="""CLICK ON the EDIT button 
    to delete or update existing Vacancies. Thankyou!""", font=my_font0, bg="#3D5A80", fg="white")
    coname_l.place(x=8, y=10)

    # usern_l = Label(board, text=f"User name:", font=my_font1, bg="#2B2828", fg="white")
    # usern_l.place(x=8, y=40)

    # posts
    post1 = Frame(profile_p, bg="#3D5A80", height=400, width=260, highlightbackground="white", highlightthickness=1)
    post1.place(x=55, y=100)
    conm = Label(post1, text=f"Company Name:", font=my_font1, bg="#3D5A80", fg="white")
    conm.place(x=10, y=20)
    conm1 = Label(post1, text=f"{cn}", font=my_font1, bg="#3D5A80", fg="white")
    conm1.place(x=10, y=60)
    co_de = Label(post1, text=f"Field of work:", font=my_font1, bg="#3D5A80", fg="white")
    co_de.place(x=10, y =100)
    co_de1 = Label(post1, text=f"{fw}", font=my_font1, bg="#3D5A80", fg="white")
    co_de1.place(x=10, y=140)
    co_de2 = Label(post1, text=f"Required skills:", font=my_font1, bg="#3D5A80", fg="white")
    co_de2.place(x=10, y=180)
    co_de3 = Label(post1, text=f"{rs}", font=my_font1, bg="#3D5A80", fg="white")
    co_de3.place(x=10, y=220)
    co_de4 = Label(post1, text=f"Required qualification:", font=my_font1, bg="#3D5A80", fg="white")
    co_de4.place(x=10, y=260)
    co_de5 = Label(post1, text=f"{rq}", font=my_font1, bg="#3D5A80", fg="white")
    co_de5.place(x=10, y=300)


    post2 = Frame(profile_p, bg="#3D5A80", height=400, width=260, highlightbackground="white", highlightthickness=1)
    post2.place(x=340, y=100)
    conm = Label(post2, text=f"Company Name:", font=my_font1, bg="#3D5A80", fg="white")
    conm.place(x=10, y=20)
    conm1 = Label(post2, text=f"{cn1}", font=my_font1, bg="#3D5A80", fg="white")
    conm1.place(x=10, y=60)
    co_de = Label(post2, text=f"Field of work:", font=my_font1, bg="#3D5A80", fg="white")
    co_de.place(x=10, y=100)
    co_de1 = Label(post2, text=f"{fw1}", font=my_font1, bg="#3D5A80", fg="white")
    co_de1.place(x=10, y=140)
    co_de2 = Label(post2, text=f"Required skills:", font=my_font1, bg="#3D5A80", fg="white")
    co_de2.place(x=10, y=180)
    co_de3 = Label(post2, text=f"{rs1}", font=my_font1, bg="#3D5A80", fg="white")
    co_de3.place(x=10, y=220)
    co_de4 = Label(post2, text=f"Required qualification:", font=my_font1, bg="#3D5A80", fg="white")
    co_de4.place(x=10, y=260)
    co_de5 = Label(post2, text=f"{rq1}", font=my_font1, bg="#3D5A80", fg="white")
    co_de5.place(x=10, y=300)

    # edit button
    edit_btn = Button(profile_p, text='EDIT', font=my_font1, bg="#213A5C", fg="white", command=edit)
    edit_btn.place(x=700, y=100)

def edit():
    runpy.run_path("editter.py")


vacancy_page()
main.mainloop()