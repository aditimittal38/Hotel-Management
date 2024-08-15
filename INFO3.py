from tkinter import *
import pickle
def info():  
    root5=Tk()
    root5.geometry('700x400+270+140')
    root5.maxsize(700,400)
    root5.minsize(700,400)
    root5.title('HOTEL PARADISE STAR')
    def back6():
        root5.destroy()
        # import MAIN3  

    scrollbar = Scrollbar(root5,orient=VERTICAL)
    scrollbar.pack(side=RIGHT,fill=Y)
    
    w = Text(root5,yscrollcommand=scrollbar.set)
    w.place(x=15,y=5,width=670,height=357)
    scrollbar.config(command=w.yview)
    w.insert(INSERT,f'----------------------------------HOTEL GUEST RECORDS--------------------------------\n')

    try:
        with open ('records.dat', 'rb') as fp:
            fp.seek(0)
            details = pickle.load(fp)
            # fp.close()
    except FileNotFoundError:
        details=[]
    try:         
        with open('pref.dat','rb') as fp:
            fp.seek(0)
            pref=pickle.load(fp)
    except FileNotFoundError:
        pref=[]
    try:
        with open('check_out.dat','rb') as fp:
            fp.seek(0)
            check_out=pickle.load(fp)
    except FileNotFoundError:
        check_out=[]
    try:
        with open('rating.dat','rb') as fp:
            fp.seek(0)
            rating=pickle.load(fp)
    except FileNotFoundError:
        rating=[]

    w.insert(INSERT,f'GUEST LIST\n')
    w.insert(INSERT,f'Sr. No.        [GuestName:Room No.:Phone,Gender: Address:Payment Mode:]\n')
    try:
        for i in range(len(details)):
                w.insert(INSERT,f'Guest{i+1}:        {details[i]}\n')
    except IndexError:
        pass
    w.insert(INSERT,f'GUEST PREFERENCES\n')
    w.insert(INSERT,f'               [Accomodation:Additional Services:Food Services:No.of Days]\n')
    try:
        for i in range(len(pref)):
            w.insert(INSERT,f'Guest{i+1}:        {pref[i]}\n')
    except IndexError:
        pass
    w.insert(INSERT,f'CHECKED OUT GUEST LIST\n')
    w.insert(INSERT,f'Sr. No.        [GuestName:Room No.:Phone,Gender: Address:Payment Mode:]\n')
    try:
        for i in range(len(check_out)):
            w.insert(INSERT,f'Guest{i+1}:        {check_out[i]}\n')
    except IndexError:
        pass
    w.insert(INSERT,f'CHECKED OUT GUEST RATING\n')
    w.insert(INSERT,f'Sr. No.        [Rating:Services:Cleanliness:Price:Quality Of Food:Our Amenities]\n')
    try:
        for i in range(len(rating)):
            w.insert(INSERT,f'Guest{i+1}:        {rating[i]}\n')
    except IndexError:
        pass
    Button(root5,text='Back',font='comicsansms 12',command=back6).place(x=14,y=365)

    root5.mainloop()
