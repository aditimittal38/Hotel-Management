from tkinter import *
from tkinter import messagebox
import pickle
try:
    f = open("rating.dat","rb")
    list2=pickle.load(f)
    f.close()
except FileNotFoundError:
    list2=[]

try:
    f = open("checkout.dat","rb")
    list4=pickle.load(f)
    f.close()
except FileNotFoundError:
    list4=[]

def ratefxn2():
    root2=Tk()
    root2.geometry('700x400+270+140')
    root2.maxsize(700,400)
    root2.minsize(700,400)
    root2.title('Rate Us')
    def back5():
        root2.destroy()
        # import MAIN3
    def search():
        pass
    def writefxn():
        messagebox.showinfo('Thanks','Thanks for choosing HOTEL PARADISE STAR. We hope you had a great time. We hope to see you soon again.')
        root2.destroy()
        with open("rating.dat",'wb') as f:
            list1=[var1.get(),var2.get(),var3.get(),var3.get(),var4.get(),var5.get()]
            list2.append(list1)
            #f.seek(0)
            pickle.dump(list2,f)
            # f.close()
        try:
            with open ('records.dat','rb') as f:
                f.seek(0)
                details=pickle.load(f)
                # f.close()
        except FileNotFoundError:
            details=[]
            print("No previous records are available")
        try:
            with open ('pref.dat','rb') as f:
                f.seek(0)
                pref=pickle.load(f)
                # f.close()
        except FileNotFoundError:
                pref=[]
                print("No previous preferences are available")
        for i in range(len(pref)):
            try: 
                if idvalue.get()==details[i][0]: 
                    print("Guest name matched")
                    list3=details[i]
                    list4.append(list3)
                    print(list4)
                    with open ('check_out.dat','wb') as f:
                        #f.seek(0)
                        pickle.dump(list4,f)
                    # f.close()       
                    del details[i]
                    del pref [i]
                    print("guest details and preferences deleted from files")
                    with open ('records.dat', 'wb') as fp:
                        #fp.seek(0)
                        pickle.dump(details, fp)
                    with open ('pref.dat', 'wb') as fp:
                        #fp.seek(0)
                        pickle.dump(pref, fp)
                    # fp.close()
                    print("checkout list updated")
            except IndexError:
                pass
    Label(root2,text='Please rate your experience at our Hotel.',font='Helvetica 10 italic').pack()
    Label(root2,text='                      ',font='Helvetica 10 italic').pack()
        # Label(text='                      ',font='Helvetica 10 italic').pack()
        # Label(text='                      ',font='Helvetica 10 italic').pack()
    Label(root2,text='This will help us to better ourselves with your guidence.Thank You!',font='Helvetica 10 italic').pack()
    def var():
        print(var1.get(),var2.get(),var3.get(),var4.get())
    Label(root2,text= '       Services :      ',font='Helivetica 12 italic',relief=RAISED).place(x=5,y=90)
    var1=IntVar(root2)
    var1.set(0)
    radio1=Radiobutton(root2,text="Needs Improvment",variable=var1,value=1,tristatevalue='x')
    radio1.place(x=170,y=90)
    radio1=Radiobutton(root2,text="Good",variable=var1,value=2,tristatevalue='x')
    radio1.place(x=300,y=90)
    radio1=Radiobutton(root2,text="Very Good",variable=var1,value=3,tristatevalue='x')
    radio1.place(x=400,y=90)
    radio1=Radiobutton(root2,text="Excellent",variable=var1,value=4,tristatevalue='x')
    radio1.place(x=500,y=90)
    radio1=Radiobutton(root2,text="Outstanding",variable=var1,value=5,tristatevalue='x')
    radio1.place(x=600,y=90)

    Label(root2,text='   Cleanliness :    ',font='Helvetica 12 italic',relief=RAISED).place(x=5,y=130)
    var2=IntVar(root2)
    var2.set(0)
    radio2=Radiobutton(root2,text="Needs Improvment",variable=var2,value=1,tristatevalue='x')
    radio2.place(x=170,y=130)
    radio2=Radiobutton(root2,text="Good",variable=var2,value=2,tristatevalue='x')
    radio2.place(x=300,y=130)
    radio2=Radiobutton(root2,text="Very Good",variable=var2,value=3,tristatevalue='x')
    radio2.place(x=400,y=130)
    radio2=Radiobutton(root2,text="Excellent",variable=var2,value=4,tristatevalue='x')
    radio2.place(x=500,y=130)
    radio2=Radiobutton(root2,text="Outstanding",variable=var2,value=5,tristatevalue='x')
    radio2.place(x=600,y=130)


    Label(root2,text='           Price :        ',font='Helvetica 12 italic',relief=RAISED).place(x=5,y=170)
    var3=StringVar(root2)
    var3.set('0')
    radio3=Radiobutton(root2,text="Needs Improvment",variable=var3,value='1',tristatevalue='x')
    radio3.place(x=170,y=170)
    radio3=Radiobutton(root2,text="Good",variable=var3,value='2',tristatevalue='x')
    radio3.place(x=300,y=170)
    radio3=Radiobutton(root2,text="Very Good",variable=var3,value='3',tristatevalue='x')
    radio3.place(x=400,y=170)
    radio3=Radiobutton(root2,text="Excellent",variable=var3,value='4',tristatevalue='x')
    radio3.place(x=500,y=170)
    radio3=Radiobutton(root2,text="Outstanding",variable=var3,value='5',tristatevalue='x')
    radio3.place(x=600,y=170)

    Label(root2,text=' Quality of Food :',font='Helvetica 12 italic',relief=RAISED).place(x=5,y=210)
    var4=StringVar(root2)
    var4.set('0')
    radio4=Radiobutton(root2,text="Needs Improvment",variable=var4,value='1',tristatevalue='x')
    radio4.place(x=170,y=210)
    radio4=Radiobutton(root2,text="Good",variable=var4,value='2',tristatevalue='x')
    radio4.place(x=300,y=210)
    radio4=Radiobutton(root2,text="Very Good",variable=var4,value='3',tristatevalue='x')
    radio4.place(x=400,y=210)
    radio4=Radiobutton(root2,text="Excellent",variable=var4,value='4',tristatevalue='x')
    radio4.place(x=500,y=210)
    radio4=Radiobutton(root2,text="Outstanding",variable=var4,value='5',tristatevalue='x')
    radio4.place(x=600,y=210)

    Label(root2,text= '  Our Amenities : ',font='Helvetica 12 italic',relief=RAISED).place(x=5,y=250)
    var5=StringVar(root2)
    var5.set('0')
    radio5=Radiobutton(root2,text="Needs Improvment",variable=var5,value='1',tristatevalue='x')
    radio5.place(x=170,y=250)
    radio5=Radiobutton(root2,text="Good",variable=var5,value='2',tristatevalue='x')
    radio5.place(x=300,y=250)
    radio5=Radiobutton(root2,text="Very Good",variable=var5,value='3',tristatevalue='x')
    radio5.place(x=400,y=250)
    radio5=Radiobutton(root2,text="Excellent",variable=var5,value='4',tristatevalue='x')
    radio5.place(x=500,y=250)
    radio5=Radiobutton(root2,text="Outstanding",variable=var5,value='5',tristatevalue='x')
    radio5.place(x=600,y=250)
    id=Label(root2,text="Customer Name:",font="comicsansms 16 underline" )
    id.place(x=30,y=286)
    idvalue=StringVar(root2)
    identry=Entry(root2, textvariable=idvalue,font='Helvetica 18 italic',borderwidth=3,relief=RAISED)
    identry.place(x=228,y=286,width=250)

    Button(root2,text='Submit',font='Helvetica 12 italic',relief=RAISED,command=writefxn).place(x=585,y=286)
    Button(root2,text='Back',font='comicsansms 12',command=back5).place(x=3,y=362)
    Button(root2,text="GO", command=search,font='Helvetica 12 italic',borderwidth=3,relief=RAISED).place(x=480,y=286)
    root2.mainloop()
