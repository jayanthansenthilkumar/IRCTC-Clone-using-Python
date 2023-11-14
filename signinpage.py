import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
kalaigroups = tkinter.Tk()
kalaigroups.title("https://www.irctc.co.in")
kalaigroups.geometry('1366x786')
kalaigroups.iconbitmap(r"railwayico.ico")
bg=tkinter.PhotoImage(file=r"logologin.png")
frm=tkinter.Frame(kalaigroups)
frm.place(x=40,y=0,height=5000,width=5000)
lab=tkinter.Label(frm,image=bg)
lab.place(x=0,y=0)

def bala():
    u=entry1.get()
    sp=entry2.get()
    db=mysql.connector.connect(host='localhost',user='root',db='introir')
    cur=db.cursor()
    cur.execute("insert into login values('%s','%s')"%(u,sp))
    db.commit()
    messagebox.showinfo("IRCTC STATUS","LOGIN SUCCESSFULLY")
def kalai():
    entry1.delete(0,"end")
    entry2.delete(0,"end")
    entry1.focus()
    kalaigroups.destroy()
    import irctcintro
    
mainlabel=Label(kalaigroups,text="USER LOGIN",font=("Segoe Script",65,"bold"),fg="green")
mainlabel.place(x=375,y=0)
user=Label(kalaigroups,text="USER ID",font=("Segoe Print",20,"bold"),fg="brown",bg="#FFF8DC",relief="sunken")
pin=Label(kalaigroups,text="SECURITY PIN",font=("Segoe Print",20,"bold"),fg="brown",bg="#FFF8DC",relief="sunken")
user.place(x=300,y=250)
pin.place(x=300,y=325)
entry1=Entry(kalaigroups,font=("Segoe Print",20,"bold"),fg="brown",bg="#FFF8DC",relief="sunken")
entry2=Entry(kalaigroups,font=("Segoe Print",20,"bold"),fg="brown",bg="#FFF8DC",relief="sunken")
entry1.place(x=600,y=250)
entry2.place(x=600,y=325)

login=Button(kalaigroups,text="LOGIN",font=("Segoe Print",20,"bold"),fg="black",bg="#FFF8DC",relief="raised",command = bala)
user=Button(kalaigroups,text="BOOK TICKET",font=("Segoe Print",20,"bold"),fg="black",bg="#FFF8DC",relief="raised",command = kalai)
login.place(x=500,y=425)
user.place(x=750,y=425)

kalaigroups.mainloop()
