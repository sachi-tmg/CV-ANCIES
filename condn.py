from tkinter import *
import tkinter as tk


con=Tk()
con.minsize(450,450)
con.maxsize(450,450)
con.title("CV-ANCIES")
con.iconbitmap('logo..ico')
con.config(bg="#2B2828")

def click_agree():
    global y
    y=1
    con.destroy()
def click_no():
    global n
    n=2
    con.destroy()




T=Text(con, height = 18, width = 43,bg="#2B2828",fg='#fCA311')
T.place(x=50,y=50)
terms='''Hello There! WELCOME TO CV-ANCIES. 
Oh Looks like You need to stop here for a 
moment.
Actually There is a need for you to confirmsomething.
These are some terms you need to agree so 
that you can proceed to next step:

1.[For Job Seekers] We are only letting youguys to get opportunity to know about the  job's vacancies you are eligible to. So,   for further process you yourself are 
responsible if anything happens.

2.[For Company Users] This apllication onlyprovides you the eligible candidates for   the vacancies you have uploaded to. For    further processing and all, you yourself   are responsible if anything does happens.

3.[For BOTH] We will not take responsibility if you guys met and are deceived by next party. So be careful when you guys decide  to meet.

     That's all!'''
T.insert(tk.END,terms)

    
yes=Button(con,text="I AGREE",bg="#2B2828",fg="#fCA311",borderwidth=2,padx=50,command=click_agree)
yes.place(x=50,y=350)
no=Button(con,text="NO I DONOT AGREE",bg="#2B2828",fg="#fCA311",borderwidth=2,command=click_no,padx=17)
no.place(x=50,y=380)

con.mainloop()