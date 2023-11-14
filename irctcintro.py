import tkinter
import tkinter as tk
#import mysql.connector
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
j = tkinter.Tk()
j.title("https://www.irctc.co.in")
j.geometry('1920x1080')
j.iconbitmap(r"railwayico.ico")
bg=tkinter.PhotoImage(file=r"vandebharat.png")
frm=tkinter.Frame(j)
frm.place(x=40,y=0,height=10000,width=10000)
lab=tkinter.Label(frm,image=bg)
lab.place(x=0,y=0)
#MARQUE
k = 50
svar = StringVar()
label = Label(j,textvariable = svar,height = 1,font=('Georgia',15),width = 106,bg = 'white',fg = 'navyblue')
def kavs():
    kavs.msg = kavs.msg[1:]+kavs.msg[0]
    svar.set(kavs.msg)
    j.after(k,kavs)
kavs.msg = '                                                                                            WELCOME TO INDIAN RAILWAYS                                                                                                                                                                                          WELCOME TO INDIAN RAILWAYS                                                                                             '
kavs()
label.place(x=44,y=120)
#frame1
frm=tkinter.Frame(j)
frm['bg']='white'
frm.place(x=42,y=5,height=100,width=1280)
#frame2
frm=tkinter.Frame(j)
frm['bg']='white'
frm.place(x=130,y=234,height=415,width=570)

lgo=tkinter.Label(frm,text='BOOK TICKET',font=('Georgia',25,'bold'),bg='white',fg='navyblue')
lgo.place(x=250,y=30)
#raillogo
a=PhotoImage(file='raillogo.png')
pics=Label(j,image=a)
pics.place(x=55,y=15,height=80,width=80)
#logoirctc
b=PhotoImage(file='logoirctc.png')
pics=Label(j,image=b)
pics.place(x=1233,y=13,height=85,width=80)
#mahatsav
c=PhotoImage(file='mahatsav.png')
pics=Label(j,image=c)
pics.place(x=200,y=250,height=95,width=145)
#Frametext1
ft1=tkinter.Label(j,text='IRCTC EXCLUSIVE FEATURES',font=('Georgia',25,'bold'),bg='white',fg='navyblue')
ft1.place(x=420,y=15)
#function
def anu():
    j.destroy()
    import signinpage
def anu1():
    j.destroy()
    import registerpage
#login/register
lg=tkinter.Button(j,text='Sign In',font=('TimesNewRoman',12,'bold'),bg='white',fg='navyblue',relief='flat',command = anu)
lg.place(x=145,y=22)
rg=tkinter.Button(j,text='Register',font=('TimesNewRoman',12,'bold'),bg='white',fg='navyblue',relief='flat',command = anu1)
rg.place(x=140,y=53)
#title
lgo=tkinter.Label(j,text='INDIAN RAILWAYS',font=('Georgia',25,'bold'),bg='navyblue',fg='white')
lgo.place(x=850,y=175)
lgo=tkinter.Label(j,text='Safety | Security | Punctuality',font=('Comic Sans MS',13,'bold'),bg='white',fg='navyblue')
lgo.place(x=895,y=225)
#frame2 workspace
lb1=tkinter.Label(frm,text='   From',font=('TimesNewRoman',10),bg='white',fg='grey')
lb1.place(x=15,y=125)
list1=['NEW DELHI - NDLS','MGR CHENNAI CENTRAL - MAS','VIRUDUNAGAR - VPT','KANYAKUMARI - CAPE','NAGARCOIL - NCJ','TIRUCHIRAPPALLI - TPJ','DELHI SARAI ROHILLA - DSR','HAZRAT NIZHAMUDIN - HZT','KARUR - KRR','SATUR - SRT','KSR BANGALORE CITY JUNCTION - SBC','TIRUNELVELI - TEN','TUTICORIN - TN','KOLLAM - QLN','SHORNUR - SNR','PALAKKAD - PGT','MANGALORE CENTRAL - MAQ','MANGALORE JUNCTION - MJ','MUMBAI CENTRAL - BOM','MAHARAJ CHATRAPATHI SIVAJI TERMINUS - CSTM','AHMEDABAD - AMD','BANARAS - BRS','VIJAYAWADA - BZA','RAJKOT - RKT','OKHA - OKHA','TIRUPATI - TPTY','RENIGUNTA - RU','GUDUR - GDR','CHENGALPATTU - CGL','SALEM - SA','HUBBALLI - UBL','SRI MATA VAISHNAV DEVI KATRA - SVDK','BARAMULLA - BRM','LUDHIYANA - LIA','JAMMU TAWI - JT','JOLLARPETTAI - JIJ','INDORE - ID','VIRANGANA LAKSHMI BAI JUNCTION - JHS','HYDERABAD DECCAN - HYB','SECUNDARABAD - SBC','SAWAI MANDOPUR - SMP','AJMER - AMR','AGRA CANTONMENT - ACT','AMBALA CANTONMENT - ABC','HOWRAH - HOW','ERNAKULAM - ERS','ERODE - ED','NAGPUR - NGP','DIBRUGARH - DBH','AGARTALA - AGT','ITARSI - IRS','GWALIOR - GLR','GUNTAKAL - GTL','KAKINADA TOWN - KNT','VISHAKAPATNAM - VIZAG','GOOTY - GTY','DHARMAVARAM - DMM','COIMBATORE - CBE','POLLACHI - POY','THANJAVUR - TJ','MADURAI - MDU']
cb1=ttk.Combobox(frm,values=list1,width=45)
cb1.place(x=25,y=155)

lb2=tkinter.Label(frm,text='   To',font=('TimesNewRoman',10),bg='white',fg='grey')
lb2.place(x=15,y=185)
list2=['NEW DELHI - NDLS','MGR CHENNAI CENTRAL - MAS','VIRUDUNAGAR - VPT','KANYAKUMARI - CAPE','NAGARCOIL - NCJ','TIRUCHIRAPPALLI - TPJ','DELHI SARAI ROHILLA - DSR','HAZRAT NIZHAMUDIN - HZT','KARUR - KRR','SATUR - SRT','KSR BANGALORE CITY JUNCTION - SBC','TIRUNELVELI - TEN','TUTICORIN - TN','KOLLAM - QLN','SHORNUR - SNR','PALAKKAD - PGT','MANGALORE CENTRAL - MAQ','MANGALORE JUNCTION - MJ','MUMBAI CENTRAL - BOM','MAHARAJ CHATRAPATHI SIVAJI TERMINUS - CSTM','AHMEDABAD - AMD','BANARAS - BRS','VIJAYAWADA - BZA','RAJKOT - RKT','OKHA - OKHA','TIRUPATI - TPTY','RENIGUNTA - RU','GUDUR - GDR','CHENGALPATTU - CGL','SALEM - SA','HUBBALLI - UBL','SRI MATA VAISHNAV DEVI KATRA - SVDK','BARAMULLA - BRM','LUDHIYANA - LIA','JAMMU TAWI - JT','JOLLARPETTAI - JIJ','INDORE - ID','VIRANGANA LAKSHMI BAI JUNCTION - JHS','HYDERABAD DECCAN - HYB','SECUNDARABAD - SBC','SAWAI MANDOPUR - SMP','AJMER - AMR','AGRA CANTONMENT - ACT','AMBALA CANTONMENT - ABC','HOWRAH - HOW','ERNAKULAM - ERS','ERODE - ED','NAGPUR - NGP','DIBRUGARH - DBH','AGARTALA - AGT','ITARSI - IRS','GWALIOR - GLR','GUNTAKAL - GTL','KAKINADA TOWN - KNT','VISHAKAPATNAM - VIZAG','GOOTY - GTY','DHARMAVARAM - DMM','COIMBATORE - CBE','POLLACHI - POY','THANJAVUR - TJ','MADURAI - MDU']
cb2=ttk.Combobox(frm,values=list2,width=45)
cb2.place(x=25,y=210)

lb3=tkinter.Label(frm,text='   Date',font=('TimesNewRoman',10),bg='white',fg='grey')
lb3.place(x=335,y=125)
list3=['11/09/2022','12/09/2022','13/09/2022','14/09/2022','15/09/2022','16/09/2022','17/09/2022','18/09/2022','19/09/2022',]
cb3=ttk.Combobox(frm,values=list3,width=25)
cb3.set('07/09/2022')
cb3.place(x=350,y=155)

lb4=tkinter.Label(frm,text='QUOTA',font=('TimesNewRoman',12,'bold'),bg='white',fg='grey')
lb4.place(x=345,y=187)
list4=['GENERAL','TATKAL','LADIES','PREMIUM TATKAL','PERSON WITH DISABILITY (LOWER BIRTH)']
cb4=ttk.Combobox(frm,values=list4,width=25)
cb4.set('GENERAL')
cb4.place(x=350,y=210)
lb5=tkinter.Label(frm,text='CLASS',font=('TimesNewRoman',12,'bold'),bg='white',fg='grey')
lb5.place(x=20,y=240)
list5=['ANUBHUTI CLASS (EA)','AC FIRST CLASS (1A)','VISTADOME AC (EV)','EXEC. CHAIR CAR (EC)','JAN CHAIR CAR (JC)','AC 2 TIER (2A)','AC 3 TIER (3A)','FIRST CLASS (FC)','AC 3 ECONOMY (3E)','VISTADOME CHAIR CAR (VC)','AC CHAIR CAR (CC)','SLEEPER (SL)','VISTADOME NON AC (VS)','SECOND SITTING']
cb5=ttk.Combobox(frm,values=list5,width=40)
cb5.set('---> ALL CLASSES')
cb5.place(x=25,y=270)

lb6=tkinter.Label(frm,text='ADULTS',font=('TimesNewRoman',10,'bold'),bg='white',fg='grey')
lb6.place(x=310,y=250)
list6=['1','2','3','4','5','6']
cb6=ttk.Combobox(frm,values=list6,width=12)
cb6.set('1')
cb6.place(x=310,y=270)

lb7=tkinter.Label(frm,text='CHILD',font=('TimesNewRoman',10,'bold'),bg='white',fg='grey')
lb7.place(x=427,y=250)
list7=['0','1','2','3','4']
cb7=ttk.Combobox(frm,values=list7,width=12)
cb7.set('0')
cb7.place(x=427,y=270)

def kalai():
    a=cb1.get()
    b=cb2.get()
    c=cb3.get()
    d=cb4.get()
    e=cb5.get()
    f=cb6.get()
    g=cb7.get()
    db=mysql.connector.connect(host='localhost',user='root',db='proirctc')
    cur=db.cursor()
    cur.execute("insert into ticket values('%s','%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f,g))
    db.commit()
    messagebox.showinfo("IRCTC STATUS","YOUR TICKET HAS BOOKED SUCCESSFULLY")

src=tkinter.Button(frm,text='BOOK TICKET',font=('Georgia',17,),bg='orange',fg='white',relief='groove',width =30,command = kalai)
src.place(x=60,y=325)

pnr=tkinter.Button(j,text='PNR STATUS',font=('Lucida Sans Unicode',17,'bold'),width =16,height =1,bg='navyblue',fg='white',relief='flat')
pnr.place(x=130,y=180)
chrt=tkinter.Button(j,text='CHARTS / VACCANCY',font=('Lucida Sans Unicode',17,'bold'),width =18,height =1,bg='navyblue',fg='white',relief='flat')
chrt.place(x=420,y=180)

#frame 1 workspace
trn=tkinter.Button(j,text='TRAINS',font=('TimesNewRoman',10,'bold'),command = a,bg='white',fg='navy blue',relief='flat')
trn.place(x=260,y=65)
flt=tkinter.Button(j,text='FLIGHTS',font=('TimesNewRoman',10,'bold'),bg='white',fg='navy blue',relief='flat')
flt.place(x=330,y=65)
hot=tkinter.Button(j,text='HOTELS',font=('TimesNewRoman',10,'bold'),bg='white',fg='navy blue',relief='flat')
hot.place(x=410,y=65)
bus=tkinter.Button(j,text='BUSES',font=('TimesNewRoman',10,'bold'),bg='white',fg='navy blue',relief='flat')
bus.place(x=490,y=65)
mel=tkinter.Button(j,text='MEALS',font=('TimesNewRoman',10,'bold'),bg='white',fg='navy blue',relief='flat')
mel.place(x=565,y=65)
hol=tkinter.Button(j,text='HOLIDAYS',font=('TimesNewRoman',10,'bold'),bg='white',fg='navy blue',relief='flat')
hol.place(x=635,y=65)
loc=tkinter.Button(j,text='LOCALITY',font=('TimesNewRoman',10,'bold'),bg='white',fg='navy blue',relief='flat')
loc.place(x=735,y=65)
prp=tkinter.Button(j,text='PREMIUM PARTNER',font=('TimesNewRoman',10,'bold'),bg='white',fg='navy blue',relief='flat')
prp.place(x=825,y=65)
mr=tkinter.Button(j,text='MORE',font=('TimesNewRoman',10,'bold'),bg='white',fg='navy blue',relief='flat')
mr.place(x=975,y=65)
cus=tkinter.Button(j,text='CONTACT US',font=('TimesNewRoman',10,'bold'),bg='white',fg='navy blue',relief='flat')
cus.place(x=1035,y=65)
