from tkinter import *
import random
# import os
# import sys
# from tkinter import messagebox
def purchasefxn2():
    class Bill_App:
        def __init__(self,master):
            self.master=master
            self.master.geometry("1300x700+0+0")
            self.master.configure(bg="#f00")
            self.master.title("Billing System")
            title=Label(self.master,text="Billing System",bd=12,relief=RIDGE,font=("Arial Black",20)).pack(fill=X)
            #===================================variables=======================================================================================
            '''l=['nutella','noodles','lays','oreo','muffin','silk','namkeen','rice','paneer','roti','dal','thali','ice','soap','shampoo','lotion','cream','foam','mask','sanitizer']
            for i in range(len(l)):
                print(self.l[i])'''
            self.nutella=IntVar(self.master)
            self.noodles=IntVar(self.master)
            self.lays=IntVar(self.master)
            self.oreo=IntVar(self.master)
            self.muffin=IntVar(self.master)
            self.silk=IntVar(self.master)
            self.namkeen=IntVar(self.master)
            self.rice=IntVar(self.master)
            self.paneer=IntVar(self.master)
            self.roti=IntVar(self.master)
            self.dal=IntVar(self.master)
            self.thali=IntVar(self.master)
            self.ice=IntVar(self.master)
            self.shake=IntVar(self.master)
            self.soap=IntVar(self.master)
            self.shampoo=IntVar(self.master)
            self.lotion=IntVar(self.master)
            self.cream=IntVar(self.master)
            self.foam=IntVar(self.master)
            self.mask=IntVar(self.master)
            self.sanitizer=IntVar(self.master)
            self.total_sna=StringVar(self.master)
            self.total_mai=StringVar(self.master)
            self.total_hyg=StringVar(self.master)
            self.a=StringVar(self.master)
            self.b=StringVar(self.master)
            self.c=StringVar(self.master)
            self.c_name=StringVar(self.master)
            self.bill_no=StringVar(self.master)
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.phone=StringVar()
            #==========================================customer details label frame=================================================
            details=LabelFrame(self.master,text="Customer Details",font=("Arial Black",12),relief=GROOVE,bd=10)
            details.place(x=0,y=80,relwidth=1)
            cust_name=Label(details,text="Customer Name",font=("Arial Black",14)).grid(row=0,column=0,padx=15)
            cust_entry=Entry(details,borderwidth=4,width=30,textvariable=self.c_name).grid(row=0,column=1,padx=8)
            contact_name=Label(details,text="Contact No.",font=("Arial Black",14)).grid(row=0,column=2,padx=10)
            contact_entry=Entry(details,borderwidth=4,width=30,textvariable=self.phone).grid(row=0,column=3,padx=8)
            bill_name=Label(details,text="Bill.No.",font=("Arial Black",14)).grid(row=0,column=4,padx=10)
            bill_entry=Entry(details,borderwidth=4,width=30,textvariable=self.bill_no).grid(row=0,column=5,padx=8)
            #=======================================snacks label frame=================================================================
            snacks=LabelFrame(self.master,text="Snacks",font=("Arial Black",12),relief=GROOVE,bd=10)
            snacks.place(x=5,y=180,height=380,width=325)

            list1=["Nutella Choco Spread","Noodles(1 Pack)","Lays(10Rs)","Oreo(20Rs)","Chocolate Muffin","Dairy Milk Silk(60Rs)","Namkeen(15Rs)",]
            for i in range (len(list1)):
                Label(snacks,text=list1[i],font=("Arial Black",11)).grid(row=i,column=0,pady=11)

            item1_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.nutella).grid(row=0,column=1,padx=10)
            item2_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.noodles).grid(row=1,column=1,padx=10)
            item3_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.lays).grid(row=2,column=1,padx=10)
            item4_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.oreo).grid(row=3,column=1,padx=10)
            item5_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.muffin).grid(row=4,column=1,padx=10)
            item6_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.silk).grid(row=5,column=1,padx=10)
            item7_entry=Entry(snacks,borderwidth=2,width=15,textvariable=self.namkeen).grid(row=6,column=1,padx=10)
            
            #===================================Main_Course=====================================================================================
            Main_Course=LabelFrame(self.master,text="Main_Course",font=("Arial Black",12),relief=GROOVE,bd=10,)
            Main_Course.place(x=340,y=180,height=380,width=325)
            list2=["Veg. Biriyani(Rs.110)","Shahi Paneer(Rs.270)","Tandoori Roti(Rs.25)","Daal(Rs.170)","Veg. Thali(Rs.250)","Chocolate Ice Cream(Rs.60)","Milk Shake(Rs.75)"]
            for i in range(len(list2)):
                Label(Main_Course,text=list2[i],font=("Arial Black",11)).grid(row=i,column=0,pady=11)

            item8_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.rice).grid(row=0,column=1,padx=10)
            item9_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.paneer).grid(row=1,column=1,padx=10)
            item10_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.roti).grid(row=2,column=1,padx=10)
            item11_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.dal).grid(row=3,column=1,padx=10)
            item12_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.thali).grid(row=4,column=1,padx=10)
            item13_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.ice).grid(row=5,column=1,padx=10)
            item14_entry=Entry(Main_Course,borderwidth=2,width=15,textvariable=self.shake).grid(row=6,column=1,padx=10)
            #========================================beauty and hygine===============================================================================
            hygine=LabelFrame(self.master,text="Beauty & Hygine",font=("Arial Black",12),relief=GROOVE,bd=10)
            hygine.place(x=677,y=180,height=380,width=325)

            list3=["Bathing Soap","Shampoo(1ltr)","Body Lotion(1ltr)","Face Cream","Shaving Foam","Face Mask(1piece)","Hand Sanitizer(50ml)"]
            for i in range(len(list3)):
                Label(hygine,text=list3[i],font=("Arial Black",11)).grid(row=i,column=0,pady=11)
            
            item15_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.soap).grid(row=0,column=1,padx=10)
            item16_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.shampoo).grid(row=1,column=1,padx=10)
            item17_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.lotion).grid(row=2,column=1,padx=10)
            item18_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.cream).grid(row=3,column=1,padx=10)
            item19_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.foam).grid(row=4,column=1,padx=10)
            item20_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.mask).grid(row=5,column=1,padx=10)
            item21_entry=Entry(hygine,borderwidth=2,width=15,textvariable=self.sanitizer).grid(row=6,column=1,padx=10)
            #=====================================================billarea==============================================================================
            billarea=Frame(self.master,bd=10,relief=GROOVE)
            billarea.place(x=1010,y=188,width=330,height=372)
            
            bill_title=Label(billarea,text="Bill Preview",font=("Arial Black",17),bd=7,relief=GROOVE,).pack(fill=X)
            
            scrol_y=Scrollbar(billarea,orient=VERTICAL)
            self.txtarea=Text(billarea,yscrollcommand=scrol_y.set)
            scrol_y.pack(side=RIGHT,fill=Y)
            scrol_y.config(command=self.txtarea.yview)
            self.txtarea.pack(fill=BOTH,expand=1)
            #=================================================billing menu=========================================================================================
            billing_menu=LabelFrame(self.master,text="Billing Summary",font=("Arial Black",12),relief=GROOVE,bd=10)
            billing_menu.place(x=0,y=560,relwidth=1,height=137)
            
            list4=["Total Snacks Price","Total Main Course Price","Total Beauty & Hygine Price","Tax on Snacks","Tax on Main Course","Beauty & Hygine Tax"]
            for i in range(len(list4)):
                Label(billing_menu,text=list4[i],font=("Arial Black",11)).grid(row=i,column=0)

            total_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_sna).grid(row=0,column=1,padx=10,pady=7)
            total_Main_Course_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_mai).grid(row=1,column=1,padx=10,pady=7)
            total_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.total_hyg).grid(row=2,column=1,padx=10,pady=7)
            tax_snacks_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.a).grid(row=0,column=3,padx=10,pady=7)
            tax_Main_Course_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.b).grid(row=1,column=3,padx=10,pady=7)
            tax_hygine_entry=Entry(billing_menu,width=30,borderwidth=2,textvariable=self.c).grid(row=2,column=3,padx=10,pady=7)

            button_frame=Frame(billing_menu,bd=7,relief=GROOVE)
            button_frame.place(x=830,width=500,height=95)
            
            button_total=Button(button_frame,text="Total Bill",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:total(self)).grid(row=0,column=0,padx=12)
            button_clear=Button(button_frame,text="Clear Field",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",command=lambda:clear(self)).grid(row=0,column=1,padx=10,pady=6)
            button_exit=Button(button_frame,text="Exit",font=("Arial Black",15),pady=10,bg="#E5B4F3",fg="#6C3483",width=8,command=lambda:exit1(self)).grid(row=0,column=2,padx=10,pady=6)
            intro(self)


    def total(self):
        # if (self.c_name.get=="" or self.phone.get()==""):
            # messagebox.showerror("Error", "Fill the complete Customer Details!!")
        self.nu=self.nutella.get()*120
        self.no=self.noodles.get()*40
        self.la=self.lays.get()*10
        self.ore=self.oreo.get()*20
        self.mu=self.muffin.get()*30
        self.si=self.silk.get()*60
        self.na=self.namkeen.get()*15
        total_snacks_price=(self.nu+self.no+self.la+self.ore+self.mu+self.si+self.na)          
        self.total_sna.set(str(total_snacks_price)+" Rs")
        self.a.set(str(round(total_snacks_price*0.05,3))+" Rs")

        self.ri=self.rice.get()*110
        self.pa=self.paneer.get()*270
        self.ro=self.roti.get()*25
        self.da=self.dal.get()*170
        self.th=self.thali.get()*250
        self.ic=self.ice.get()*60
        self.sh=self.shake.get()*75
        total_Main_Course_price=(self.ri+self.pa+self.ro+self.da+self.th+self.ic+self.sh)
            
        self.total_mai.set(str(total_Main_Course_price)+" Rs")
        self.b.set(str(round(total_Main_Course_price*0.01,3))+" Rs")

        self.so=self.soap.get()*30
        self.sh=self.shampoo.get()*180
        self.cr=self.cream.get()*130
        self.lo=self.lotion.get()*500
        self.fo=self.foam.get()*85
        self.ma=self.mask.get()*100
        self.sa=self.sanitizer.get()*20
        
        total_hygine_price=(self.so+self.sh+self.cr+self.lo+self.fo+self.ma+self.sa)
            
        self.total_hyg.set(str(total_hygine_price)+" Rs")
        self.c.set(str(round(total_hygine_price*0.10,3))+" Rs")
        self.total_all_bill=(total_snacks_price+total_Main_Course_price+total_hygine_price+
                    (round(total_Main_Course_price*0.01,3))+
                    (round(total_hygine_price*0.10,3))+
                    (round(total_snacks_price*0.05,3)))
        self.total_all_bil=str(self.total_all_bill)+" Rs"
        billarea(self)
    def intro(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END,"\tWELCOME TO PARADISE STAR\n\tPhone-No.739275410")
        self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
        self.txtarea.insert(END,"\n====================================\n")
        self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
        self.txtarea.insert(END,"\n====================================\n")
    def billarea(self):
        intro(self)
        if self.nutella.get()!=0:
            self.txtarea.insert(END,f"Nutella\t\t {self.nutella.get()}\t{self.nu}\n")
        if self.noodles.get()!=0:
            self.txtarea.insert(END,f"Noodles\t\t {self.noodles.get()}\t{self.no}\n")
        if self.lays.get()!=0:
            self.txtarea.insert(END,f"Lays\t\t {self.lays.get()}\t{self.la}\n")
        if self.oreo.get()!=0:
            self.txtarea.insert(END,f"Oreo\t\t {self.oreo.get()}\t{self.ore}\n")
        if self.muffin.get()!=0:
            self.txtarea.insert(END,f"Muffins\t\t {self.muffin.get()}\t{self.mu}\n")
        if self.silk.get()!=0:
            self.txtarea.insert(END,f"Silk\t\t {self.silk.get()}\t{self.si}\n")
        if self.namkeen.get()!=0:
            self.txtarea.insert(END,f"Namkeen\t\t {self.namkeen.get()}\t{self.na}\n")
        if self.rice.get()!=0:
            self.txtarea.insert(END,f"Veg. Biriyani\t\t {self.rice.get()}\t{self.ri}\n")
        if self.paneer.get()!=0:
            self.txtarea.insert(END,f"Shahi Paneer\t\t {self.paneer.get()}\t{self.pa}\n")
        if self.roti.get()!=0:
            self.txtarea.insert(END,f"Tandoori Roti\t\t {self.roti.get()}\t{self.ro}\n")
        if self.dal.get()!=0:
            self.txtarea.insert(END,f"Daal\t\t {self.dal.get()}\t{self.da}\n")
        if self.thali.get()!=0:
            self.txtarea.insert(END,f"Veg. Thali\t\t {self.thali.get()}\t{self.th}\n")
        if self.ice.get()!=0:
            self.txtarea.insert(END,f"Chocolate Ice Cream\t\t {self.ice.get()}\t{self.ic}\n")
        if self.shake.get()!=0:
            self.txtarea.insert(END,f"Milk Shake\t\t {self.shake.get()}\t{self.sh}\n")
        if self.soap.get()!=0:
            self.txtarea.insert(END,f"Soap\t\t {self.soap.get()}\t{self.so}\n")
        if self.shampoo.get()!=0:
            self.txtarea.insert(END,f"Shampoo\t\t {self.shampoo.get()}\t{self.sh}\n")
        if self.lotion.get()!=0:
            self.txtarea.insert(END,f"Lotion\t\t {self.lotion.get()}\t{self.lo}\n")
        if self.cream.get()!=0:
            self.txtarea.insert(END,f"Cream\t\t {self.cream.get()}\t{self.cr}\n")
        if self.foam.get()!=0:
            self.txtarea.insert(END,f"Foam\t\t {self.foam.get()}\t{self.fo}\n")
        if self.mask.get()!=0:
            self.txtarea.insert(END,f"Mask\t\t {self.mask.get()}\t{self.ma}\n")
        if self.sanitizer.get()!=0:
            self.txtarea.insert(END,f"Sanitizer\t\t {self.sanitizer.get()}\t{self.sa}\n")
            
        self.txtarea.insert(END,f"------------------------------------\n")
        if self.a.get()!="0.0 Rs":
            self.txtarea.insert(END,f"Total Snacks Tax : {self.a.get()}\n")
        if self.b.get()!="0.0 Rs":
            self.txtarea.insert(END,f"Total Main Course Tax : {self.b.get()}\n")
        if self.c.get()!="0.0 Rs":
            self.txtarea.insert(END,f"Total Beauty&Hygine Tax : {self.c.get()}\n")
        self.txtarea.insert(END,f"Total Bill Amount : {self.total_all_bil}\n")
        self.txtarea.insert(END,f"------------------------------------\n")
    def clear(self):
            self.txtarea.delete(1.0,END)
            self.nutella.set(0)
            self.noodles.set(0)
            self.lays.set(0)
            self.oreo.set(0)
            self.muffin.set(0)
            self.silk.set(0)
            self.namkeen.set(0)
            self.rice.set(0)
            self.paneer.set(0)
            self.roti.set(0)
            self.dal.set(0)
            self.thali.set(0)
            self.ice.set(0)
            self.milk.set(0)
            self.soap.set(0)
            self.shampoo.set(0)
            self.lotion.set(0)
            self.cream.set(0)
            self.foam.set(0)
            self.mask.set(0)
            self.sanitizer.set(0)
            self.total_sna.set(0)
            self.total_mai.set(0)
            self.total_hyg.set(0)
            self.a.set(0)
            self.b.set(0)
            self.c.set(0)
            self.c_name.set(0)
            self.bill_no.set(0)
            self.bill_no.set(0)
            self.phone.set(0)
    def exit1(self):
        self.master.destroy()
    master=Tk()
    obj=Bill_App(master)
    def back6():
        master.destroy()
        # import MAIN3
    Button(master,text='Back',font='comicsansms 17',command=back6).place(x=10,y=10)

    master.mainloop()