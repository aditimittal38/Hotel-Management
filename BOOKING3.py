from tkinter import *
from tkinter import messagebox
import random
import pickle
try:
    f = open("records.dat","rb")
    list2=pickle.load(f)
    f.close()
except FileNotFoundError:
    list2=[]

def bookingfxn2():
    root3 = Tk()
    root3.geometry('700x400+270+140')
    root3.minsize(700,400)
    root3.title('HOTEL PARADISE STAR')
    # def back2():
        # root3.destroy()
        # import MAIN3
    def getvals():
        room_num=random.randint(100,800)
        room_id=room_num
        messagebox.askokcancel('Room number',f'Congratulations\n You have successfully booked a room in our Paradise.\nYour room no. is {room_num}\n')
        list1=[namevalue.get(),room_id,phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get()]
        list2.append(list1)
        print(list2)
        with open('records.dat', 'wb') as fp:
            pickle.dump(list2, fp)
        root3.destroy()
        # import MAIN3
    #Heading
    Label(root3, text="CUSTOMER DETAILS", font="comicsansms 20 italic" ).place(x=200,y=20)

    #Making labels
    name = Label(root3, text="    Name    ",font='Helvetica 18 italic',borderwidth=3,relief=RAISED)
    phone = Label(root3, text="    Phone   ",font='Helvetica 18 italic',borderwidth=3,relief=RAISED)
    gender = Label(root3, text="   Gender   ",font='Helvetica 18 italic',borderwidth=3,relief=RAISED)
    contact = Label(root3, text="   Address  ",font='Helvetica 18 italic',borderwidth=3,relief=RAISED)
    payment = Label(root3, text="  Payment ",font='Helvetica 18 italic',borderwidth=3,relief=RAISED)

    #Pack text 
    name.place(x=100,y=60)
    phone.place(x=100,y=110)
    gender.place(x=100,y=160)
    contact.place(x=100,y=210)
    payment.place(x=100,y=260)

    # Tkinter variable for storing entries
    namevalue = StringVar(root3)
    phonevalue = StringVar(root3)
    gendervalue = StringVar(root3)
    emergencyvalue = StringVar(root3)
    paymentvalue = StringVar(root3)
    paymentvalue.set(0)
    Radiobutton(root3,text="CASH", variable=paymentvalue, value='Cash',tristatevalue='x').place(x=293,y=268)
    Radiobutton(root3,text="NET BANKING", variable=paymentvalue, value='Net Banking',tristatevalue='x').place(x=350,y=268)
    Radiobutton(root3,text="CREDIT CARD", variable=paymentvalue, value='Credit Cash',tristatevalue='x').place(x=453,y=268)
    Radiobutton(root3,text="UPI", variable=paymentvalue, value='UPI',tristatevalue='x').place(x=550,y=268)
    #Entries for our form
    nameentry = Entry(root3, textvariable = namevalue , font='Helvetica 18 italic',borderwidth=3,relief=RAISED)
    phoneentry = Entry(root3, textvariable=phonevalue,font='Helvetica 18 italic',borderwidth=3,relief=RAISED)
    genderentry = Entry(root3, textvariable=gendervalue,font='Helvetica 18 italic',borderwidth=3,relief=RAISED)
    emergencyentry = Entry(root3, textvariable=emergencyvalue,font='Helvetica 18 italic',borderwidth=3,relief=RAISED)
    
    # Packing the Entries
    nameentry.place(x=300,y=60)
    phoneentry.place(x=300,y=110)
    genderentry.place(x=300,y=160)
    emergencyentry.place(x=300,y=210)
    
    #Button & packing it and assigning it a command
    b=Button(root3,text="Submit to ParadiseStar", command=getvals,font='Helvetica 18 italic',borderwidth=3,relief=RAISED)
    b.place(x=200,y=310)
    # Button(root3,text='Back',font='comicsansms 12',command=back2).place(x=3,y=362)
    root3.mainloop()



    
