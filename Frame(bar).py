#bar frame-------------------------------------------
bar=Frame(main,bg="white",borderwidth=1)
bar.grid(sticky=W)
random=Label(bar,text='hello',fg="black",bg="black",pady=380,padx=97).grid()

#inserting logo------------------------------------------
logo1=Label(bar,image=logo,bg="black").place(y=25)

#buttons--------------------------------------------
home_btn=Button(bar,text="HOME",bg="#bac2ff",fg="black",padx=76.2,font=my_font,pady=4,command=lambda:indicate(home_indicate))
home_btn.place(y=240,x=0)

about_btn=Button(bar,text="ABOUT",bg="#bac2ff",fg="black",padx=73.2,pady=4,font=my_font,command=lambda:indicate(about_indicate,about_p))
about_btn.place(y=285,x=0)

cv_btn=Button(bar,text="CV FORM",bg="#bac2ff",fg="black",padx=63.4,font=my_font,pady=4,command=lambda:indicate(cv_indicate,cv_page))
cv_btn.place(y=330,x=0)

vacancy_btn=Button(bar,text="VACANCY FORM",bg="#bac2ff",fg="black",padx=31.4,font=my_font,pady=4,command=lambda:indicate(vacancy_indicate,vacancy_page))
vacancy_btn.place(y=375,x=0)

back_btn=Button(bar,text="BACK",bg="#bac2ff",fg="black",padx=80.4,font=my_font,pady=4,command=lambda:indicate(back_indicate))
back_btn.place(y=420,x=0)

exit_btn=Button(bar,text="EXIT",bg="#bac2ff",fg="black",padx=83.4,font=my_font,pady=4,command=lambda:indicate(exit_indicate))
exit_btn.place(y=465,x=0)

