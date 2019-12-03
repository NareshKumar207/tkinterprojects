from tkinter import *
import sqlite3 as sql
from tkinter import messagebox
import datetime
from tkinter import font

root = Tk()

class Ntk:
    number = None
    def __init__(self,master):
        self.f1 = Frame(master,bg="black",height=500,width=500)
        self.f1.pack(fill=BOTH, expand=1)   #to expand frame to cover root window

        self.f2 = Frame(master,height=500,width=500)
        self.f3 = Frame(master,height=500,width=500,bg="black")
        self.f4 = Frame(master,height=500,width=500,bg="black")


        self.l1 = Label(self.f1,text="MAKE NOTES",fg="#F1C40F",font=(None,35,'bold'),bg="black")
        self.l1.pack(padx=20,pady=30)
        #b1 = Button(f1,text="Add Note",bg="")
        self.l2 = Label(self.f1,text="Add Notes",fg="#2C3E50",bg="#FF5733",font=(None,30,'italic'))
        self.l2.place(x=250,y=200)

        pic = PhotoImage(file="icons8-add-100.png")
        #picimage = pic.subsample(10,10)

        self.b1 = Button(self.f1,text="+",height=3,width=5,command=self.addnote)
        self.b1.place(x=470,y=200)

        self.b2 = Button(self.f1,text="Your notes",fg='#2C3E50',bg="#FF5733",font=(None,25,'italic'),width=15,command=self.mynotes)
        self.b2.place(x=250,y=300)


    def addnote(self):
        self.f1.forget()
        self.f2.pack(fill=BOTH,expand=1)
        self.l = Label(self.f2,text=str(datetime.date.today()),fg="black",font=(None,25,'bold'))
        self.l.place(x=300)
        self.text = Text(self.f2,font=(None,20))
        self.text.config(bg="black",fg="white")
        self.text.place(x=150,y=40,height=650,width=500)
        self.text.event_generate("<<Cut>>")
        self.text.event_generate("<<Copy>>")
        self.text.event_generate("<<Paste>>")

        self.b3 = Button(self.f2,text="SAVE",font=(None,25,'bold'),bg="black",fg="white",command=self.save)
        self.b3.place(x=270,y=650)

        self.b4 = Button(self.f2,text="BACK",font=(None,25,"bold"),bg="black",fg="white",command=self.back)
        self.b4.place(x=450,y=650)


    def save(self):
        data = self.text.get(1.0,END)
        print(data)
        try:
            db = sql.connect("notes.db")
            c = db.cursor()
            date = str(datetime.date.today())
            cmd = "insert into note(data,date) values('{}','{}')".format(data,date)
            c.execute(cmd)
        except Exception as e:
            #cmd = "create table note(note varchar(200))"
            #c.execute(cmd)
            print("Error",e)
        else:
            db.commit()
            messagebox.showinfo("INFO","Successfully saved")
            self.f2.forget()
            self.f1.pack(fill=BOTH,expand=1.0)
            
            
    def back(self):
        self.f2.forget()
        self.f1.pack(fill=BOTH,expand=1.0)


    def mynotes(self):
        self.f1.forget()
        self.f3.pack(fill=BOTH,expand=1.0)
        self.listbox = Listbox(self.f3)
        small_font = font.Font(size=20)
        self.listbox.config(bg="black",fg="white",bd=5,height=250,width=250,font=small_font)
        self.listbox.place(y=70)
        db = sql.connect("notes.db")
        c = db.cursor()
        cmd = "select * from note"
        c.execute(cmd)
        data = c.fetchall()
        for var in range(len(data)):
            #b = Button(self)
            self.listbox.insert(END,(data[var][1][:30]+'::'+data[var][2]))
            #self.listbox.itemconfig(var,{'height':10,'font':(None,20,'italic'),'bd':4})
        
        self.b5 = Button(self.f3,text="SELECT",font=(None,25,'bold'),bg="white",fg="black",command=self.select)
        self.b6 = Button(self.f3,text="BACK",font=(None,25,'bold'),bg="white",fg="black",command=self.back1)
        self.b5.place(x=40)
        self.b6.place(x=250)


    def back1(self):
        self.f3.forget()
        self.f1.pack(fill=BOTH,expand=1.0)
    
    def select(self):
        self.f3.forget()
        self.f4.pack(fill=BOTH,expand=1.0)
        selected = self.listbox.curselection()
        self.number = selected[0]
        db = sql.connect("notes.db")
        c = db.cursor()
        c.execute("select * from note")
        data = c.fetchall()
        #print(data[selected[0]])
        self.text1 = Text(self.f4,font=(None,20))
        self.text1.config(bg="#F1C40F",fg="white")
        self.text1.place(x=150,y=40,height=650,width=500)
        self.text1.insert(1.0,data[selected[0]][1])
        b3 = Button(self.f4,text="SAVE",font=(None,25,'bold'),bg="white",fg="black",command=self.edit)
        b3.place(x=270,y=650)

        b4 = Button(self.f4,text="BACK",font=(None,25,"bold"),bg="white",fg="black",command=self.back2)
        b4.place(x=450,y=650)

        b4 = Button(self.f4,text="DELETE",font=(None,25,"bold"),bg="white",fg="black",command=self.delete)
        b4.place(x=350,y=700)

    def back2(self):
        self.f4.forget()
        self.f1.pack(fill=BOTH,expand=1.0)
    
    def delete(self):
        db = sql.connect("notes.db")
        c = db.cursor()
        print(self.number+1)
        c.execute("delete from note where id={}".format(int(self.number+1)))
        db.commit()
        messagebox.showinfo("INFO","Successfully deleted")
        self.f4.forget()
        self.f1.pack(fill=BOTH,expand=1.0)

    def edit(self):
        db = sql.connect("notes.db")
        c = db.cursor()
        edited = self.text1.get(1.0,END)
        print(edited)
        print(self.number+1)
        c.execute("update note set data='{}' where id={}".format(edited,self.number+1))
        db.commit()
        messagebox.showinfo("Info","Successfully Updated")


root.geometry("800x800")
root.resizable(0,0)
obj = Ntk(root)
root.mainloop()