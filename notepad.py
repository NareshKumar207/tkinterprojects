from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Untitled - Notepad")

menu1 = Menu(root,tearoff=False)
root.config(menu=menu1)

text = Text(root,font=(None,20))
text.grid()
text.event_generate('<Ctrl+Plus>')

filemenu = Menu(menu1,tearoff=False)
menu1.add_cascade(label='File',menu=filemenu)

def exit():
    root.destroy()

def new():
    root.title("Untitled - Notepad")
    text.delete(1.0,END)
    

def Open():
    file = filedialog.askopenfilename(filetypes=[("Text_Files","*.txt")])
    print(type(file))
    text.delete(1.0,END)
    #data = open("C:/Users/Simran Grover/Desktop/tweets.txt")
    root.title(file+" - Notepad")
    with open(file, "r") as data:
        text.insert(1.0,data.read())

def save():
    file = filedialog.asksaveasfilename(initialfile="Untitled.txt",defaultextension='.txt')
    with open(file,'w') as f:
        f.write(text.get(1.0,END))
        f.close()
    root.title(file + " - Notepad")

filemenu.add_command(label="New",command=new)
filemenu.add_command(label="Open",command=Open)
filemenu.add_command(label='Save_as',command=save)
filemenu.add_command(label='Exit',command=exit)

editmenu = Menu(menu1,tearoff=False)
menu1.add_cascade(label="Edit",menu=editmenu)

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def undo():
    text.event_generate("<<Undo>>")

editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
editmenu.add_command(label="Undo",command=undo)

viewmenu = Menu(menu1,tearoff=False)
menu1.add_cascade(label="View",menu=viewmenu)

theme = Menu(menu1,tearoff=False)
menu1.add_cascade(label="Theme",menu=theme)

def dark():
    text.config(bg="black",fg="white")

def light():
    text.config(bg="white",fg="black")

theme.add_command(label="Dark",command=dark)
theme.add_command(label="Default",command=light)



root.mainloop()
