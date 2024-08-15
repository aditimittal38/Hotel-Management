from tkinter import *
from RATING3 import ratefxn2
import pickle
def paymentfxn2():
    self=Tk()
    self.geometry('700x400+270+140')
    self.maxsize(700,400)
    self.minsize(700,400)
    self.title('HOTEL PARADISE STAR')
    def back5():
        self.destroy()
        # import MAIN3
    def ratefxn1():
        self.destroy()
        ratefxn2()
    Label(self, text="PAYMENT:", font="comicsansms 19 underline" ).place(x=50,y=13)
    Label(self, text="Accomodation:", font="comicsansms 20 italic" ).place(x=50,y=50)
    Label(self, text="Food Services:", font="comicsansms 20 italic" ).place(x=50,y=100)
    Label(self, text="Additional Services:", font="comicsansms 20 italic" ).place(x=50,y=150)
    Label(self, text="No. Of Days:", font="comicsansms 20 italic" ).place(x=50,y=200)
    Label(self, text="--Other utility bills have been cleared already.", font="comicsansms 12 italic" ).place(x=50,y=300)
    Label(self, text="Total Bill Amount:", font="comicsansms 20 italic" ).place(x=50,y=250)

    try:
        with open('pref.dat','rb') as fp:
            fp.seek(0)
            prefer = pickle.load(fp)
    except FileNotFoundError:
        prefer=[]
    id=Label(self,text="Customer Name:",font="comicsansms 16 underline" )
    id.place(x= 209,y=13)
    idvalue=StringVar(self)
    identry=Entry(self, textvariable=idvalue,font='Helvetica 18 italic',borderwidth=3,relief=RAISED)
    identry.place(x=380,y=13,width=250)

    def search():
        with open('records.dat','rb') as fp:
            fp.seek(0)
            details = pickle.load(fp)
        for i in range (len(prefer)):
            if idvalue.get()==details[i][0]:
                total=(int(prefer[i][0])+int(prefer[i][1])+int(prefer[i][2]))*int(prefer[i][3])
                # Button(text='Get',command=Var).place(x=150,y=50)
                Label(self, text=prefer[i][0], font="comicsansms 20 italic" ).place(x=350,y=50)
                Label(self, text=prefer[i][1], font="comicsansms 20 italic" ).place(x=350,y=100)
                Label(self, text=prefer[i][2], font="comicsansms 20 italic" ).place(x=350,y=150)
                Label(self, text=prefer[i][3], font="comicsansms 20 italic" ).place(x=350,y=200)
                Label(self, text=total, font="comicsansms 20 italic" ).place(x=350,y=250)
            

    Button(self,text="GO", command=search,font='Helvetica 12 italic',borderwidth=3,relief=RAISED).place(x=640,y=13)
    
    b=Button(self,text="Make Payment", command=ratefxn1,font='Helvetica 18 italic',borderwidth=3,relief=RAISED)
    b.place(x=450,y=286)
    Button(self,text='Back',font='comicsansms 12',command=back5).place(x=3,y=362)
    self.mainloop()
