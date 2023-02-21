from tkinter import *
from PIL import Image,ImageTk
from tkinter.font import Font

main=Tk()
main.minsize(1100,710)
main.maxsize(1100,710)
main.title("CV-ANCIES")
main.iconbitmap('logo..ico')
main.config(bg="#4A78A9")

#button commands---------------------------------------------
def exit_all():
    main.destroy()
def home():
    main.destroy()
    import login

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
my_font3 = Font(
        family = 'Lucida sans',
        size = 14,
        weight='bold',
        slant = 'roman',
        overstrike = 0)
my_font4 = Font(
        family = 'Lucida sans',
        size = 20,
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
about_btn=Button(bar,text="ABOUT",bg="#213A5C",fg="white",padx=73.2,pady=4,font=my_font)
about_btn.place(y=285,x=0)

cv_btn=Button(bar,text="CV FORM",bg="#213A5C",fg="white",padx=63.4,font=my_font,pady=4)
cv_btn.place(y=330,x=0)

vacancy_btn=Button(bar,text="VACANCY FORM",bg="#213A5C",fg="white",padx=31.4,font=my_font,pady=4)
vacancy_btn.place(y=375,x=0)

profile_btn=Button(bar,text="PROFILE",bg="#213A5C",fg="white",padx=67,font=my_font,pady=4)
profile_btn.place(y=420,x=0)

exit_btn=Button(bar,text="EXIT",bg="#213A5C",fg="white",padx=83.4,font=my_font,pady=4,command=exit_all)
exit_btn.place(y=465,x=0)

#logout__ icon-------------------------------------
ico101=Image.open('lgicon.png')
ico102=ico101.resize((90,90))
ico103=ImageTk.PhotoImage(ico102)

lo_btn=Button(bar,image=ico103,bg="black",padx=76.2,font=my_font,pady=4,command=home,borderwidth=0,activebackground="black")
lo_btn.place(y=520,x=70)

#top bar--------------------------------------------------
cvbar=Frame(main,bg="white",borderwidth=1)
cvbar.place(x=225,y=0)
spa=Label(cvbar,text="hello",bg="black",fg="black",padx=530,pady=10).grid()

help_btn=Button(main,image=help_ico,bg="white").place(x=1020,y=2)
settings_btn=Button(main,image=settings_ico ,bg="white").place(x=1060,y=2)

main.mainloop()