from tkinter import *
from PREFERENCES3 import preferencefxn2
from PAYMENT3 import paymentfxn2
from ABOUT3 import aboutfxn2
from GUEST_INFO3 import guestinfofxn2
from PURCHASE3 import purchasefxn2
root=Tk()
root.title('HOTEL PARADISE STAR')
root.geometry('700x400+270+140')
root.maxsize(700,400)
root.minsize(700,400)
'''def preferencefxn1():
    # root.destroy()
    preferencefxn2()
def guestinfofxn1 ():
    # root.destroy()
    guestinfofxn2()
def paymentfxn1 ():
    # root.destroy()
    paymentfxn2()
def aboutfxn1 ():
    # root.destroy()
    aboutfxn2()
def purchasefxn1():
    # root.destroy()
    purchasefxn2()'''

f0=Frame(root)
f0.place(height=300, width =900)
Label(f0, text='WELCOME TO PARADISE STAR  ',font='Helvetica 27 italic').place(y=0 , x=86 )
booking=Button(root,text='     BOOKING     ', font='comicsansms 20 italic',command=preferencefxn2)
booking.place(y=70,x=250)
guest_list=Button(root,text='   GUEST INFO  ', font='comicsansms 20 italic',command=guestinfofxn2)
guest_list.place(x=250, y=130)
rate=Button(root,text='   CHECK OUT   ', font='comicsansms 20 italic',command=paymentfxn2)
rate.place(x=250,y=190)
about=Button(root,text='    ABOUT US     ', font='comicsansms 20 italic',command=aboutfxn2)
about.place(x=250,y=310)
purchase=Button(root,text='   PURCHASE    ', font='comicsansms 20 italic',command=purchasefxn2)
purchase.place(x=250,y=250)
root.mainloop()




