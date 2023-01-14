from tkinter import *
from PIL import Image, ImageTk
r=Tk()
r.title("LOGIN".center(300))

r.config(bg='#E2E6E8')
r.minsize(width=1000,height=650)
r.maxsize(width=1400,height=700)
img=Image.open("D:\Documents\Python\CV-ANCIES\LO.png")
img1=img.resize((220,220))
img2=ImageTk.PhotoImage(img1)
Label(image=img2,borderwidth=0,bg='#E2E6E8').pack(side=TOP,padx=30,pady=30)
# img=PhotoImage(file="D:\Documents\Python\CV-ANCIES\LO.png")

fra=LabelFrame(r, padx=10,pady=10)
fra.pack(padx=70)
fra.configure(bg='#E2E6E8',borderwidth=0)

#...........
def cur(e):
    un.delete(0,END)

Label(fra,text='Username',font=('Perpetua',17),bg='#E2E6E8',fg='#0C4160').place(x=6,y=0)
un=Entry(fra, width=30,borderwidth=2,font=("Perpetua",17),fg='#545B5C')
un.insert(0,'Username')
un.pack(padx=5,pady=30)
un.bind("<FocusIn>",cur)

#.............
def put(e):
    pw.delete(0,END)

Label(fra,text='Password',font=("Perpetua",17),bg='#E2E6E8',fg='#0C4160').place(x=6,y=85)
pw=Entry(fra, width=30,borderwidth=2,font=('Perpetua',17),fg='#545B5C')
pw.insert(0,'Password')
pw.pack(padx=5,pady=25)
pw.bind("<FocusIn>",put)

Label(fra,text='New to CVancies?',font=('Perpetua',12),bg='#E2E6E8',fg='#0C4160').place(x=230,y=170)

fra1=LabelFrame(r, padx=10,pady=10)
fra1.pack(padx=70)
fra1.configure(bg='#E2E6E8',borderwidth=0)





Log=Button(fra1,text='Login',bg='#0C4160',fg='white',font=('Perpetua',15),width=7).pack(side=LEFT,padx=80)
Reg=Button(fra1,text='Register',fg='#ffffff',bg='#0C4160',font=('Perpetua',15)).pack(side=RIGHT,padx=80)


fra.mainloop()