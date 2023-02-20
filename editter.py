from tkinter import * 
import sqlite3
from tkinter import messagebox

root = Tk()
root.title('Upadate Vacancy')
root.iconbitmap('logo..ico')
# databases

# create a databases or connect to one
conn = sqlite3.connect('Vacancy.db')

# create cursor
c = conn.cursor()



def delete():
    # create database
    conn = sqlite3.connect('Vacancy.db')

    # create cursor
    c = conn.cursor()
    c.execute("SELECT * FROM details")

    dataa = c.fetchall()
    aa = len(dataa)
    # delete record
    c.execute("DELETE from details WHERE oid=" + delete_box.get())
    print("DELETED SUCCESSFULLY")
    conn.commit()
    conn.close()

    # create database
    conn = sqlite3.connect('Vacancy.db')

    # create cursor
    c = conn.cursor()
    c.execute("SELECT * FROM details")
    plate = c.fetchall()
    bb = len(plate)
    if bb < aa:
        messagebox.showinfo('Update data', 'Your data has been deleted!')
    else:
        messagebox.showerror('Error', 'No Data Found!')

    conn.commit()
    conn.close()


delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

delete_label = Label(root, text='Vacancy number:')
delete_label.grid(row=9, column=0)

delete_btn = Button(root, text='Delete', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=120)


# create update Button
def edit():
    global editor


    # create database
    conn = sqlite3.connect('Vacancy.db')

    # create cursor
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute('SELECT * FROM details WHERE oid= ' + record_id)
    records = c.fetchall()
    if records == []:
        messagebox.showerror("ERROR", "No Data Found!")
    else:
        editor = Tk()
        editor.title("Update Data")
        editor.iconbitmap('logo..ico')
        editor.geometry("300x480")

        global c_name
        global adderesss
        global lang
        global fieldd
        global skillss
        global salaryy
        global con
        global quali
        global anye
        global emaill
        global yoe

        c_name = Entry(editor, width=30)
        c_name.grid(row=0, column=1, padx=20, pady=(10, 0))

        adderesss = Entry(editor, width=30)
        adderesss.grid(row=1, column=1)

        lang = Entry(editor, width=30)
        lang.grid(row=2, column=1)

        fieldd = Entry(editor, width=30)
        fieldd.grid(row=3, column=1)

        skillss = Entry(editor, width=30)
        skillss.grid(row=4, column=1)

        salaryy = Entry(editor, width=30)
        salaryy.grid(row=5, column=1)

        con = Entry(editor, width=30)
        con.grid(row=6, column=1)

        quali = Entry(editor, width=30)
        quali.grid(row=7, column=1)

        anye = Entry(editor, width=30)
        anye.grid(row=8, column=1)

        emaill = Entry(editor, width=30)
        emaill.grid(row=9, column=1)

        yoe = Entry(editor, width=30)
        yoe.grid(row=10, column=1)

        # create textbox Label

        c_name_label = Label(editor, text="Comapany name")
        c_name_label.grid(row=0, column=0, pady=(10, 0))

        adderesss_label = Label(editor, text="address")
        adderesss_label.grid(row=1, column=0)

        lang_label = Label(editor, text="language")
        lang_label.grid(row=2, column=0)

        fieldd_label = Label(editor, text="field of work")
        fieldd_label.grid(row=3, column=0)

        skillss_label = Label(editor, text="skill")
        skillss_label.grid(row=4, column=0)

        salaryy_label = Label(editor, text="salary")
        salaryy_label.grid(row=5, column=0)

        con_label = Label(editor, text="contact")
        con_label.grid(row=6, column=0)

        quali_label = Label(editor, text="qualification")
        quali_label.grid(row=7, column=0)

        anye_label = Label(editor, text="anything else")
        anye_label.grid(row=8, column=0)

        emaill_label = Label(editor, text="email")
        emaill_label.grid(row=9, column=0)

        yoe_label = Label(editor, text="experience")
        yoe_label.grid(row=10, column=0)

        for record in records:
            c_name.insert(0, record[0])
            adderesss.insert(0, record[1])
            lang.insert(0, record[2])
            fieldd.insert(0, record[3])
            skillss.insert(0, record[4])
            salaryy.insert(0, record[5])
            con.insert(0, record[6])
            quali.insert(0, record[7])
            anye.insert(0, record[8])
            emaill.insert(0, record[9])
            yoe.insert(0, record[10])

        save_btn = Button(editor, text='save', command=update)
        save_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=120)


# creating an update function
def update():
    # create a databases or connect to one
    conn = sqlite3.connect('Vacancy.db')

    # create cursor
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE details SET
    name = :name,
    address = :address,
    language = :language,
    field =:field,
    skills=:skills,
    salary = :salary,
    contact=:contact,
    qualification=:qualification,
    anything_else=:anything_else,
    email=:email,
    yearOfExperience=:yearOfExperience
    WHERE oid = :oid""",
              {'name': c_name.get(),
               'address': adderesss.get(),
               'language': lang.get(),
               'field': fieldd.get(),
               'skills': skillss.get(),
               'salary': salaryy.get(),
               'contact': con.get(),
               'qualification': quali.get(),
               'anything_else': anye.get(),
               'email': emaill.get(),
               'yearOfExperience': yoe.get(),
               'oid': record_id

               }
              )
    messagebox.showinfo("UPDATED","Your data has been updated!")
    conn.commit()
    conn.close()

    # destroying all the data and closing window
    editor.destroy()


edit_btn = Button(root, text='Update', command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=120)
# commit change
conn.commit()

# close connection
conn.close()

root.mainloop()
