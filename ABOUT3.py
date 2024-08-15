from tkinter import *
def aboutfxn2():
    window=Tk()
    window.title('HOTEL PARADISE STAR')
    window.geometry('700x400+270+140')
    window.maxsize(700,400)
    window.minsize(700,400)
    def back3():
        window.destroy()
        # import MAIN3
    Label(window,text='HOTEL PARADISE STAR!',font='Helvetica 25 italic').pack()
    Label(window,text='''PARADISE STAR WORLDWIDE offers a warm and friendly
    stay no matter where you travel around the world. Our guest en-
    -joys high speed wireless internet access, cozy beds for a relaxed
    and restful stay, and a variety of hotel choices to match every trip;
    from a family vacation or weekend getaway, to a full-scale conference
    or wedding. We are committed to creating caring experiences for every
    person, every time, and strive to make our guests feel truly refreshed
    and restored during their visit.''', font='Helvetica 12 italic').pack()
    
    Label(window,text='                      ',font='Helvetica 10 italic').pack()
    Label(window,text='''ADITI MITTAL (ROLL NO.03/XII) \nNISHA GAWADE (ROLL NO.11/XII)
    
    SPECIAL THANKS TO:
    SONA MAM ''',font='Helvetica 16 italic').pack()
    Button(window,text='Back',font='comicsansms 12',command=back3).place(x=3,y=362)
    window.mainloop()