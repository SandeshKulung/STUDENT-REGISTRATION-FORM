from tkinter import*
from tkinter import messagebox
def participation1():
    import pymysql
    dbms1=pymysql.connect("localhost","root","SUJATA3322","eventsandsportsclub")
    cursor=dbms1.cursor()
    lsql="SELECT count(FullName) FROM student WHERE FullName=%s"
    cursor.execute(lsql,value)
    outcome=cursor.fetchall()
    for t in outcome:
        participation.insert('',0, text=t[0])

def dataflow():
    import pymysql
    dbms=pymysql.connect("localhost","root","SUJATA3322","eventsandsportsclub")
    cursor=dbms.cursor()
    code="SELECT * FROM student WHERE FullName=%s"
    cursor.execute(code, value)
    result=cursor.fetchall()
    for k in result:
        searchvalue.insert('',0,text=k[0],values=(k[1],k[2],k[3]))
    dbms.close()
    searchentry.delete(0,END)
    participation1()
def display():
    
    from tkinter import ttk
    #messagebox.showinfo("successful")
    window4=Toplevel()
    window4.geometry("850x230")
    window4.title("Searched value")
    global value
    value=searchentry.get()
    global searchvalue
    searchvalue=ttk.Treeview(window4, height=4)
    searchvalue.pack()
    
    searchvalue['column']=('firstvalue','secondvalue','thirdvalue')
    searchvalue.place(x=10, y=20)
    searchvalue.heading('#0',text="FullName", anchor='c')
    searchvalue.heading('firstvalue',text="Semester", anchor='c')
    searchvalue.heading('secondvalue',text="mobile number", anchor='c')
    searchvalue.heading('thirdvalue',text="Email", anchor='c')
    scb=ttk.Scrollbar(searchvalue,orient="vertical", command=searchvalue.yview)
    scb.place(x=785, y=1, height=103)
    searchvalue.configure(yscrollcommand=scb.set)
    global participation
    participation=ttk.Treeview(window4, height=2)
    participation.pack()
    participation['column']=('')
    participation.place(x=15,y=140)
    participation.heading('#0',text="Number of participation")

    dataflow()

    window4.mainloop()
    
def show_information():
    from tkinter import ttk
    window3=Tk()
    window3.resizable(height=0, width=0)
    import pymysql
    window3.geometry("850x500")
    window3.title("Information")
    l8=Label(window3, text="Registered Information",fg='blue', font=30)
    l8.place(x=350, y=10)
    tree=ttk.Treeview(window3)
    tree.pack()
    tree1=ttk.Treeview(window3, height=2)
    tree1.pack()
    tree1['column']=('')
    tree1.place(x=50, y=350)
    tree1.heading('#0',text="Number of participated students",anchor='c')
    global db5
    tree['column']=('first','second', 'third')
    tree.place(x=10, y=100)
    tree.heading('#0',text="Name",anchor='c')
    tree.heading('first',text="Section",anchor='c')
    tree.heading('second',text="Mobile number",anchor='c')
    tree.heading('third',text="Email",anchor='c')
    vsb = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)#treeview scrollbar
    vsb.place(x=785, y=0, height=200+25)
    tree.configure(yscrollcommand=vsb.set)#treeview scrollbar
    db5=pymysql.connect("localhost","root","SUJATA3322","eventsandsportsclub")
    cursor=db5.cursor()
    gsql="SELECT * FROM student"
    cursor.execute(gsql)
    myresult=cursor.fetchall()
    for i in myresult:
        tree.insert('',0,text=i[0],values=(i[1],i[2],i[3]))
    searchbutton=Button(window3, text="Search", width=15,command=display)
    searchbutton.place(x=700, y=50)
    global search
    search=StringVar()
    global searchentry
    searchentry=Entry(window3, textvariable=search, width=20, font=9)
    searchentry.place(x=515, y=51)


    
    #l5=Label(window3,text="Total Number of students = ", font=30)
    #l5.place(x=10, y=400)
    tsql="SELECT COUNT(mobilenumber) FROM student"
    cursor.execute(tsql)
    result=cursor.fetchall()
    for n in result:
        tree1.insert('',0,text=n[0])
    db5.close()
    window3.mainloop()
    
def end():
    print("delete")
    e1.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
def database():
    import pymysql
    global username
    global mobile
    global mail
    global section
    username=name.get()
    section=semester.get()
    mobile=mobile_number.get()
    mail=Email.get()
    db=pymysql.connect("localhost","root","SUJATA3322","eventsandsportsclub")
    cursor=db.cursor()
    sql="INSERT INTO student VALUES(%s, %s, %s, %s)"
    record=(username, section, mobile, mail)
    cursor.execute(sql, record)
    db.commit()
    cursor.close()
    e1.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def main_screen():
    global window
    window=Tk()
    window.geometry("500x500")
    window.resizable(width=0, height=0)
    window.title("Sunway Events And Sports Club")
    menu=Menu(window)
    window.config(menu=menu)
    filemenu=Menu(menu)
    menu.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Show information",command=show_information)
    global name
    global semester
    global mobile_number
    global Email
    name=StringVar()
    semester=StringVar()
    mobile_number=StringVar()
    Email=StringVar()
    l=Label(window, text="Student Registration Form", width=20, font=40)
    l.place(x=180, y=20)
    l1=Label(window, text="Full Name", width=20,font=20)
    l1.place(x=0, y=100)
    global e1
    e1=Entry(window,textvariable=name, width=30, font=30)
    e1.place(x=180, y=100)
    l2=Label(window, text="Semester", width=20, font=40)
    l2.place(x=-5, y=160)
    global e2
    #e2=Entry(window, textvariable=semester, width=20,font=20)
    semester.set("select the semester")
    e2=OptionMenu(window, semester, "first", "second", "third","fourth","fifth","sixth")
    e2.place(x=180, y=160)
    l3=Label(window, text="Mobile number", width=20, font=20)
    l3.place(x=12, y=220)
    global e3
    e3=Entry(window, textvariable=mobile_number, width=30, font=20)
    e3.place(x=180, y=220)
    l4=Label(window, text="Email", width=20, font=20)
    l4.place(x=-20, y=280)
    global e4
    e4=Entry(window, textvariable=Email, width=30, font=20)
    e4.place(x=180, y=280)
    b1=Button(window, text="Register",width=10, fg='green', font=40,  command=database)
    b1.place(x=100, y=350)
    b2=Button(window, text="Exit", width=10, fg='red', font=40, command=end)
    b2.place(x=300, y=350)
    #b3=Button(window, text="Show Information",fg='blue',font=40, command=show_information)
    #b3.place(x=180, y=420)
    window.mainloop()

main_screen()