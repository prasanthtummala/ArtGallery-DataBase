from tkinter import *
import pymysql

root = Tk()
root.geometry('500x500')
root.title("Customer Form")

cid1 = IntVar()
cname1 = StringVar()
amount1 = IntVar()
address1 = StringVar()


def database():
    cname = cname1.get()
    cid = cid1.get()
    address = address1.get()
    amount = amount1.get()
    conn = pymysql.connect("localhost","root","123456","artgallery")
    with conn:
        cursor = conn.cursor()

    cursor.execute('INSERT INTO customer (cid,cname,address,amount) VALUES(?,?,?,?,?)',
                   (cid,cname,address,amount))
    conn.commit()


label_0 = Label(root, text="customer form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="cid", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=cid1)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="cname", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(root, textvar=cname1)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="address", width=20, font=("bold", 10))
label_3.place(x=70, y=230)

entry_3 = Entry(root, textvar=address1)
entry_3.place(x=235, y=230)


label_4 = Label(root, text="amount", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

entry_4 = Entry(root, textvar=amount1)
entry_4.place(x=230, y=280)

Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=180, y=380)

root.mainloop()