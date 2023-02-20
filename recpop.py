from tkinter import *
from tkinter.font import Font
import sqlite3



root = Tk()
root.title('Available Vacancies')
root.config(bg="#4A78A9")
root.iconbitmap('logo..ico')
my_font0 = Font(
    family='Lucida sans',
    size=8,
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
# databases

# create a databases or connect to one
conn = sqlite3.connect('Vacancy.db')

# create cursor
c = conn.cursor()
c.execute("SELECT * FROM details")

dataa = c.fetchall()
dis1 = Label(root, text=f'Following are the Available Vacancies for you. All THE BEST!', font=my_font, padx=30, pady=30, bg="#4A78A9")
dis1.grid(row=0, column=0)
y = 0
for z in dataa:
    y = y + 1
    a,b,c,d,e,f,g,h,i,j,k = z
    dis = Label(root, text=f'{y}: Company: {a}, Address:  {b},  Language:  {c},  Field:  {d},  Skills:  {e},  Salary:  {f}, Contact:  {g},  Qualification:  {h},  Anything Else:  {i},  Email:  {j},  Year of Experience:  {k}', font=my_font0, bg = "#4A78A9", pady=10, padx=5)
    dis.grid(row=y, column=0)




conn.commit()
conn.close()
root.mainloop()
