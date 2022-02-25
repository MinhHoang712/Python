# Import Module
from tkinter import *
import pyodbc
# Information List
datas = []

# Cập nhật thông tin sách
def update_books():
    select.delete(0,END)
    for n,a,d in datas:
        select.insert(END, n)
        
# Thêm thông tin sách đã nhập
def add():
    global datas
    datas.append([Name.get(),Author.get(),Description.get(1.0, "end-1c")])
    update_books()
  
# xem thông tin sách
def view():
    Name.set(datas[int(select.curselection()[0])][0])
    Author.set(datas[int(select.curselection()[0])][1])
    Description.delete(1.0,"end")
    Description.insert(1.0, datas[int(select.curselection()[0])][2])
  
#Xóa sách
def delete():
    del datas[int(select.curselection()[0])]
    update_books()
  
def reset():
    Name.set('')
    Author.set('')
    Description.delete(1.0,"end")

def save():
    Ten= datas[int(select.curselection()[0])][0]
    TacGia= datas[int(select.curselection()[0])][1]
    MoTa= datas[int(select.curselection()[0])][2]
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                          'Server=MSI\SQLEXPRESS;'
                          'Database=books;'
                          'Trusted_Connection=yes;'
                          )
    cursor = conn.cursor()
    cursor.execute(
                'INSERT INTO product (Name,Author,Description) VALUES(?,?,?)',(Ten,TacGia,MoTa)
                )
    conn.commit()
  
# Create Object
root = Tk()
root.title("Quản lý sách điện tử")
# Tạo kích thước cửa sổ
root.geometry('800x800')
    
# Thêm các Buttons, Label, ListBox
Name = StringVar()
Author = StringVar()
Description = StringVar()
  
  
frame1 = Frame()
frame1.pack(pady=10)
  
frame2 = Frame()
frame2.pack(pady=10)

frame3 = Frame()
frame3.pack(pady=10)

Label(frame1, text = 'Name:', font='arial 12 bold').pack(side=LEFT)
Entry(frame1, textvariable = Name,width=50).pack()

Label(frame2, text = 'Author:', font='arial 12 bold').pack(side=LEFT)
Entry(frame2, textvariable = Author,width=50).pack()

Label(frame3, text = 'Description:', font='arial 12 bold').pack(side=LEFT)
Description = Text(frame3,width=50,height=10)
Description.pack()

Button(root, text="Add", font="arial 12 bold", command= add).place(x= 300, y= 310)
Button(root, text="View", font="arial 12 bold", command= view).place(x= 300, y= 350)
Button(root, text="Delete", font="arial 12 bold", command= delete).place(x= 300, y= 390)
Button(root, text="Reset", font="arial 12 bold", command= reset).place(x= 300, y= 430)
Button(root, text="Save", font="arial 12 bold", command= save).place(x= 300, y= 470)
  
scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x= 400, y= 300)

# Execute Tkinter
root.mainloop()