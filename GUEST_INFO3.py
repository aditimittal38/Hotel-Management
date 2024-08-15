from tkinter import *
from INFO3 import info
import pickle
import os
def guestinfofxn2():
    root3 = Tk()
    root3.geometry('700x400+270+140')
    root3.maxsize(700,400)
    root3.minsize(700,400)
    root3.title('HOTEL PARADISE STAR')
    def back3():
        root3.destroy()
        # import MAIN3
    Label(root3,text='Guest List and Info',font='Helvetica 18 italic',borderwidth=3,relief=RAISED).place(x=0,y=20,width='700')
    name = Label(root3, text="    Name    ",font='Helvetica 12 italic',borderwidth=3,relief=RAISED)
    room_id = Label(root3, text=" Room No.",font='Helvetica 12 italic',borderwidth=3,relief=RAISED)
    phone = Label(root3, text="    Phone   ",font='Helvetica 12 italic',borderwidth=3,relief=RAISED)
    gender = Label(root3, text="   Gender   ",font='Helvetica 12 italic',borderwidth=3,relief=RAISED)
    contact = Label(root3, text="  Address  ",font='Helvetica 12 italic',borderwidth=3,relief=RAISED)
    payment = Label(root3, text="  Payment ",font='Helvetica 12 italic',borderwidth=3,relief=RAISED)

    #Pack text 
    name.place(x=10,y=70)
    room_id.place(x=10,y=100)
    phone.place(x=10,y=130)
    gender.place(x=300,y=70)
    contact.place(x=300,y=100)
    payment.place(x=300,y=130)

    # Tkinter variable for storing entries
    namevalue = StringVar(root3)
    namevalue.set('Type Here')
    phonevalue = IntVar(root3)
    phonevalue.set(0)
    gendervalue = StringVar(root3)
    gendervalue.set('Type Here')
    emergencyvalue = StringVar(root3)
    emergencyvalue.set('Type Here')
    paymentvalue = StringVar(root3)
    paymentvalue.set('Type Here')
    room_idvalue=IntVar(root3)
    room_idvalue.set(0)

    #Entries for our form
    nameentry = Entry(root3, textvariable = namevalue , font='Helvetica 12 italic',borderwidth=3,relief=RAISED)
    room_identry=Entry(root3, textvariable=room_idvalue,font='Helvetica 12 italic',borderwidth=3,relief=RAISED)
    phoneentry = Entry(root3, textvariable=phonevalue,font='Helvetica 12 italic',borderwidth=3,relief=RAISED)
    genderentry = Entry(root3, textvariable=gendervalue,font='Helvetica 12 italic',borderwidth=3,relief=RAISED)
    emergencyentry = Entry(root3, textvariable=emergencyvalue,font='Helvetica 12 italic',borderwidth=3,relief=RAISED)
    paymententry = Entry(root3, textvariable=paymentvalue,font='Helvetica 12 italic',borderwidth=3,relief=RAISED)

    # Packing the Entries
    nameentry.place(x=100,y=70)
    room_identry.place(x=100,y=100)
    phoneentry.place(x=100,y=130)
    genderentry.place(x=400,y=70)
    emergencyentry.place(x=400,y=100)
    paymententry.place(x=400,y=130)

    #Opening database
    try:
        with open ('records.dat', 'rb') as fp:
            fp.seek(0)
            details = pickle.load(fp)
    except FileNotFoundError:
        details=[]
    # fp.close()
    for i in range (len(details)):
        print (details[i])
    try:
        with open('pref.dat','rb') as fp:
            fp.seek(0)
            pref=pickle.load(fp)
    except FileNotFoundError:
        pref=[]
    for j in range (len(pref)):
        print(pref[j])
    
    scrollbar = Scrollbar(root3,orient=VERTICAL)
    scrollbar.pack(side=RIGHT,fill=Y)
    
    w = Text(root3,yscrollcommand=scrollbar.set)
    w.place(x=5,y=170,width=670,height=190)
    scrollbar.config(command=w.yview)
    
    
    w.insert(INSERT,f'Sr. No.        [GuestName:Room No.:Phone,Gender: Address:Payment Mode:]\n               [Accomodation:Additional Services:Food Services:No.of Days]\n')
    for i in range(len(details)):
        w.insert(INSERT,f'Guest{i+1}:        {details[i]}\n               {pref[i]}\n')
    
    def read():
        w.delete("1.0", "end")
        for i in range (len(details)):
            if namevalue.get()==details[i][0]:
                w.insert(INSERT,f'Guest Details={details[i]}\n')
                     
            elif room_idvalue.get()==details[i][1]:
                w.insert(INSERT,f'Guest Details={details[i]}\n')
                
            elif phonevalue.get()==details[i][2]:
                w.insert(INSERT,f'Guest Details={details[i]}\n')
                
            elif gendervalue.get()==details[i][3]:
                w.insert(INSERT,f'Guest Details={details[i]}\n')
                
            elif emergencyvalue.get()==details[i][4]:
                w.insert(INSERT,f'Guest Details={details[i]}\n')
                
            elif paymentvalue.get()==details[i][5]:
                w.insert(INSERT,f'Guest Details={details[i]}\n')
                
    
    def update():
        w.delete("1.0", "end")
        for i in range (len(details)):
            if namevalue.get()==details[i][0]:
                l=[namevalue.get(),room_idvalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get()]
                details[i]=l
                w.insert(INSERT,f'Customer details successfully updated!')
                break
            elif room_idvalue.get()==details[i][1]:
                l=[namevalue.get(),room_idvalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get()]
                details[i]=l
                w.insert(INSERT,f'Customer details successfully updated!\n')
                break
            elif phonevalue.get()==details[i][2]:
                l=[namevalue.get(),room_idvalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get()]
                details[i]=l
                w.insert(INSERT,f'Customer details successfully updated!\n')
                break
            elif gendervalue.get()==details[i][3]:
                l=[namevalue.get(),room_idvalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get()]
                details[i]=l
                w.insert(INSERT,f'Customer details successfully updated!\n')
                break
            elif emergencyvalue.get()==details[i][4]:
                l=[namevalue.get(),room_idvalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get()]
                details[i]=l
                w.insert(INSERT,f'Customer details successfully updated!\n')
                break
            elif paymentvalue.get()==details[i][5]:
                l=[namevalue.get(),room_idvalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get()]
                details[i]=l
                w.insert(INSERT,f'Customer details successfully updated!\n')
                break
        with open ('records.dat', 'wb') as fp:
            #fp.seek(0)
            pickle.dump(details, fp)
        fp.close()
    
    def delete():
        w.delete("1.0", "end")
        for i in range (len(details)):
            try:
                if namevalue.get()==details[i][0]:
                    del details[i]
                    w.insert(INSERT,f'Customer Details successfully deleted!')
                elif room_idvalue.get()==details[i][1]:
                    del details[i]
                    w.insert(INSERT,f'Customer Details successfully deleted!')
                elif phonevalue.get()==details[i][2]:
                    del details[i]
                    w.insert(INSERT,f'Customer Details successfully deleted!')
                elif gendervalue.get()==details[i][3]:
                    del details[i]
                    w.insert(INSERT,f'Customer Details successfully deleted!')
                elif emergencyvalue.get()==details[i][4]:
                    del details[i]
                    w.insert(INSERT,f'Customer Details successfully deleted!')
                elif paymentvalue.get()==details[i][5]:
                    del details[i]
                    w.insert(INSERT,f'Customer Details successfully deleted!')
            except IndexError:
                pass
            with open ('records.dat', 'wb') as fp:
                #fp.seek(0)
                pickle.dump(details, fp)
            # fp.close()

    '''ANOTHER WAY OF MAKING DEL FUNCTION
    def delete():
        fp= open ('records.dat', 'rb')
        tp= open ('temp.dat','wb')
        try:
            while True:
                w.delete("1.0", "end")
                fp.seek(0)
                details = pickle.load(fp)
                for i in range (len(details)):
                    if namevalue.get()==details[i][0]:
                        del details[i]
                        w.insert(INSERT,f'Customer Details successfully deleted!')
                    elif room_idvalue.get()==details[i][1]:
                        del details[i]
                        w.insert(INSERT,f'Customer Details successfully deleted!')
                    elif phonevalue.get()==details[i][2]:
                        del details[i]
                        w.insert(INSERT,f'Customer Details successfully deleted!')
                    elif gendervalue.get()==details[i][3]:
                        del details[i]
                        w.insert(INSERT,f'Customer Details successfully deleted!')
                    elif emergencyvalue.get()==details[i][4]:
                        del details[i]
                        w.insert(INSERT,f'Customer Details successfully deleted!')
                    elif paymentvalue.get()==details[i][5]:
                        del details[i]
                        w.insert(INSERT,f'Customer Details successfully deleted!')
                    else:
                        w.insert(INSERT,f'Guest Not Found!')
            
                    pickle.dump(details,tp)
            
        except Exception:
            fp.close()
            tp.close()
        os.remove("records.dat")
        os.rename("temp.dat","records.dat")
        '''


    def openlist():
        w.delete("1.0", "end")
        w.insert(INSERT,f'Sr. No.        [GuestName:Room No.:Phone:Gender: Address:Payment Mode:]\n               [Accomodation:Additional Services:Food Services:No.of Days]\n')
        try: 
            for i in range(len(pref)):
                w.insert(INSERT,f'Guest{i+1}:        {details[i]}\n               {pref[i]}\n')
        except IndexError:
            pass

    def infofxn():
        root3.destroy()
        info()

    a=Button(root3,text="GET INFO", command=read,bg='yellow',font='Helvetica 9 italic',borderwidth=3,relief=RAISED)
    a.place(x=600,y=70)
    b=Button(root3,text=" UPDATE ", command=update,bg='yellow',font='Helvetica 9 italic',borderwidth=3,relief=RAISED)
    b.place(x=600,y=100)
    c=Button(root3,text=" DELETE  ", command=delete,bg='yellow',font='Helvetica 9 italic',borderwidth=3,relief=RAISED)
    c.place(x=600,y=130)
    d=Button(root3,text="OPEN GUEST LIST",command=openlist,bg='yellow',font='Helvetica 9 italic',borderwidth=3,relief=RAISED)
    d.place(x=560,y=368)
    Button(root3,text='Back',font='comicsansms 12',command=back3).place(x=7,y=365)
    Button(root3,text='Open Hotel Customer Records:',font='comicsansms 12',command=infofxn).place(x=80,y=365)

    
    root3.mainloop()
