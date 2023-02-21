from tkinter import *
from PIL import Image,ImageTk
from tkinter.font import Font

main=Tk()
main.minsize(1100,710)
main.maxsize(1100,710)
main.title("CV-ANCIES")
main.iconbitmap('logo..ico')
main.config(bg="black")
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
my_font2 = Font(
        family = 'Lucida sans',
        size = 25,
        weight='bold',
        slant = 'roman',
        overstrike = 0)

#logo--------------------------------------------------
img=Image.open('lg.png')
img1=img.resize((220,180))
logo=ImageTk.PhotoImage(img1)

img2=Image.open('help.png')
img3=img2.resize((30,30))
help_ico=ImageTk.PhotoImage(img3)

img4=Image.open('settings.png')
img5=img4.resize((30,30))
settings_ico=ImageTk.PhotoImage(img5)

#bar frame-------------------------------------------
bar=Frame(main,bg="white",borderwidth=1)
bar.grid(sticky=W)
random=Label(bar,text='hello',fg="black",bg="black",pady=380,padx=97).grid()

#inserting logo------------------------------------------
logo1=Label(bar,image=logo,bg="black").place(y=25)

#buttons--------------------------------------------
home_btn=Button(bar,text="HOME",bg="#fCA311",fg="black",padx=76.2,font=my_font,pady=4)
home_btn.place(y=240,x=0)

about_btn=Button(bar,text="ABOUT",bg="#fCA311",fg="black",padx=73.2,pady=4,font=my_font)
about_btn.place(y=285,x=0)

cv_btn=Button(bar,text="CV FORM",bg="#fCA311",fg="black",padx=63.4,font=my_font,pady=4)
cv_btn.place(y=330,x=0)

vacancy_btn=Button(bar,text="VACANCY FORM",bg="#fCA311",fg="black",padx=31.4,font=my_font,pady=4)
vacancy_btn.place(y=375,x=0)

back_btn=Button(bar,text="BACK",bg="#fCA311",fg="black",padx=80.4,font=my_font,pady=4)
back_btn.place(y=420,x=0)

exit_btn=Button(bar,text="EXIT",bg="#fCA311",fg="black",padx=83.4,font=my_font,pady=4)
exit_btn.place(y=465,x=0)

#top bar--------------------------------------------------
cvbar=Frame(main,bg="white",borderwidth=1)
cvbar.place(x=225,y=0)
spa=Label(cvbar,text="hello",bg="black",fg="black",padx=530,pady=10).grid()

help_btn=Button(main,image=help_ico,bg="#fCA311").place(x=1020,y=2)
settings_btn=Button(main,image=settings_ico ,bg="#fCA311").place(x=1060,y=2)


def profile():
    profile_p=Frame(main,bg="#2B2828",width=865,height=655)
    profile_p.place(x=230,y=47)
    for_place=Label(profile_p,text="COMPANY PROFILE",font=my_font2,bg="#2B2828",fg="white")
    for_place.place(x=260,y=20)
    board=Frame(profile_p,bg="black",borderwidth=1)
    board.place(x=55,y=85)
    #ignore this-----
    for_space=Label(board,text="profile",pady=30,padx=200,bg="#2B2828",fg="#2B2828")
    for_space.grid()

    #labels
    coname_l=Label(board,text="Company name:",font=my_font1,bg="#2B2828",fg="white")
    coname_l.place(x=8,y=10)

    usern_l=Label(board,text="User name:",font=my_font1,bg="#2B2828",fg="white")
    usern_l.place(x=8,y=40)
    
    #posts
    post1=Frame(profile_p,bg="#14213D",height=400,width=260,highlightbackground="white", highlightthickness=1)
    post1.place(x=55,y=200)
    post2=Frame(profile_p,bg="#14213D",height=400,width=260,highlightbackground="white", highlightthickness=1)
    post2.place(x=340,y=200)

    #edit button 
    edit_btn=Button(profile_p,text='EDIT',font=my_font1,bg="#FCA311",fg="black")
    edit_btn.place(x=700,y=100)
    

profile()
main.mainloop()