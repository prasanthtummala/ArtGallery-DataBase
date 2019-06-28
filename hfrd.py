from tkinter import *
import pymysql

root = Tk()
root.geometry('500x500')
root.title("artist Form")

name1 = StringVar()
birthplace1 = StringVar()
age1 = IntVar()
style1 = StringVar()


def database():
    name = name1.get()
    birthplace = birthplace1.get()
    style = style1.get()
    age = age1.get()
    conn = pymysql.connect("localhost","root","123456","artgallery")
    with conn:
        cursor = conn.cursor()

    cursor.execute('INSERT INTO artist (name,birthplace,age,style) VALUES(?,?,?,?,?)',
                   (name, birthplace, style, age))
    conn.commit()


label_0 = Label(root, text="artist form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=name1)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="birthplace", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(root, textvar=birthplace1)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="age", width=20, font=("bold", 10))
label_3.place(x=70, y=230)

entry_3 = Entry(root, textvar=age1)
entry_3.place(x=235, y=230)


label_4 = Label(root, text="style", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

entry_4 = Entry(root, textvar=style1)
entry_4.place(x=230, y=280)

Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=180, y=380)

root.mainloop()