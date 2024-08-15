from tkinter import *
from BOOKING3 import bookingfxn2
import pickle


# try:
#     while True:
#         f=open("pref.dat","ab+")
#         # f.seek(0)
#         list2=pickle.load(f)
# except Exception:
#     list2=[]
#     print("Reached End of file")
#     f.close()

try:
    f = open("pref.dat","rb")
    list2=pickle.load(f)
    f.close()
except FileNotFoundError:
    list2=[]

    

# f.seek(0)


# list2=list()
def preferencefxn2():
    
    win=Tk()
    def back1():
        win.destroy()
        # import MAIN3
    def bookingfxn1():
        list1=[var1.get(),(var20.get()+var21.get()+var22.get()+var23.get()),(var30.get()+var31.get()+var32.get()+var33.get()),daysvalue.get()]
        list2.append(list1)
        print(list2)
        with open("pref.dat",'wb') as fp:
            #fp.seek(0)
            pickle.dump(list2,fp)
        win.destroy()
        bookingfxn2()
    
    win.title('HOTEL PARADISE STAR')
    win.geometry('700x400+270+140')
    win.maxsize(700,400)
    win.minsize(700,400)
    Label(win,text='Please Select Your Preferences',font='Helvetica  ',borderwidth=3,relief=RAISED).place(x=0,y=20,width=700)
    Label(win,text='--ROOM PREFERENCE:',font='Helvetica 13 ').place(x=10,y=70)
    var1=StringVar(win)
    var1.set('0')
    radio1=Radiobutton(win,text="STANDARD NON-AC", variable=var1, value='900',tristatevalue='x').place(x=0,y=100)
    radio1=Radiobutton(win,text="STANDARD AC", variable=var1, value='1200',tristatevalue='x').place(x=180,y=100)
    radio1=Radiobutton(win,text="DELUXE NON-AC", variable=var1, value='1500',tristatevalue='x').place(x=360,y=100)
    radio1=Radiobutton(win,text="DELUX AC", variable=var1, value='2000',tristatevalue='x').place(x=540,y=100)
    
    days=Label(win,text='--NO. OF DAYS:',font='Helvetica 13 ').place(x=10,y=128)
    daysvalue=IntVar(win)
    daysentry = Entry(win, textvariable = daysvalue,font='Helvetica 14',borderwidth=3,relief=RAISED)
    daysentry.place(y=125, x=150,width=33)
    Label(win,text='--ADDITIONAL SERVICE:',font='Helvetica 13 ').place(x=10,y=163)
    
    var20=IntVar(win)
    var21=IntVar(win)
    var22=IntVar(win)
    var23=IntVar(win)
    a=Checkbutton(win,text="TELEVISION", variable=var20, onvalue=400,offvalue=0)
    a.place(x=0,y=193)
    b=Checkbutton(win,text="BATH TUB", variable=var21, onvalue=200,offvalue=0)
    b.place(x=180,y=193)
    c=Checkbutton(win,text="SPA", variable=var22, onvalue=300,offvalue=0)
    c.place(x=360,y=193)
    d=Checkbutton(win,text="MINI FRIDGE", variable=var23, onvalue=500,offvalue=0)
    d.place(x=540,y=193)   
    
    Label(win,text='--DO YOU WANT TO PREBOOK YOUR MEALS?IF YES:PLEASE SELECT:',font='Helvetica 13 ').place(x=10,y=223)
    var30=IntVar(win)
    var31=IntVar(win)
    var32=IntVar(win)
    var33=IntVar(win)
    c1=Checkbutton(win,text="BREAKFAST", variable=var30, onvalue=100,offvalue=0)
    c1.place(x=0,y=247)
    c2=Checkbutton(win,text="LUNCH", variable=var31, onvalue=120,offvalue=0)
    c2.place(x=180,y=247)
    c3=Checkbutton(win,text="SNACKS", variable=var32, onvalue=50,offvalue=0)
    c3.place(x=360,y=247)
    c4=Checkbutton(win,text="DINNER", variable=var33, onvalue=175,offvalue=0)
    c4.place(x=540,y=247)
    
    s=Label(win,text='EXTRA SNACKS,SPECIAL MEALS,BEAUTY AND HYGIENE PRODUCTS CAN BE \nORDERED FROM THE MAIN MENU ANY TIME.',font='Helvetica 13')
    s.place(x=20,y=290)
    Button(win,text='    SUBMIT    ',command=bookingfxn1,font='Helvetica 12').place(x=280,y=340)
    Button(win,text='Back',font='comicsansms 12',command=back1).place(x=3,y=362)
    win.mainloop()
    




    
