from tkinter import*         #importing tkinter libraray function
import math,random
class Bill_App:               #creating bill class
    def __init__(self,root):  #initilizing class
        self.root=root
        self.root.geometry("1320x720+0+0")   #setting geometry of interface
        self.root.title("Billing Application")  #setting title of interface
        bg_color="#00394d"                   #Background color of interface
        #Creting first frame 
        title=Label(self.root,text="Billing Software",bd=10,relief=GROOVE,bg=bg_color,fg="white",font=("time new roman",20,"bold"),pady=2).pack(fill=X)
        #=========Variable Declaration===================
        #==============Cosmatics=========================
        self.A1=IntVar()
        self.A2=IntVar()
        self.A3=IntVar()
        self.A4=IntVar()
        self.A5=IntVar()
        self.A6=IntVar()
        #=============Grosery=============================
        self.B1=IntVar()
        self.B2=IntVar()
        self.B3=IntVar()
        self.B4=IntVar()
        self.B5=IntVar()
        self.B6=IntVar()
        #=============Breavages============================
        self.C1=IntVar()
        self.C2=IntVar()
        self.C3=IntVar()
        self.C4=IntVar()
        self.C5=IntVar()
        self.C6=IntVar()
        #==============Total Product Price & Variables=========
        self.A=StringVar()
        self.B=StringVar()
        self.C=StringVar()
        self.D=StringVar()
        #=============Customer=================================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        r=random.randint(1000,9999)
        self.bill_no.set(str(r))
        self.search_bill=StringVar()
        
        #======Customer Detail frame====================================================================================================================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Delails",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=60,relwidth=1)
        
        #=====Customer Name grid========================================================================================================================
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=18,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        #------Customer Phone number Grid---------------------------------------------------------------------------------------------------------------
        cphn_lbl=Label(F1,text="Customer Phone no:",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=12,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=10)
        
        #------Billing Number Grid----------------------------------------------------------------------------------------------------------------------
        cname_lbl=Label(F1,text="Bill no:",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cname_txt=Entry(F1,width=10,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=10)
        
        #-----Search button Grid------------------------------------------------------------------------------------------------------------------------
        bill_btn=Button(F1,text="Serach",width=10,bd=7,font="ariel 12 bold").grid(row=0,column=6,padx=20,pady=10)
        #============Cosmatic Frame===================================================================================================================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmatic",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=150,width=325,height=380)
        #---------------
        A1_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        A1_txt=Entry(F2,width=10,textvariable=self.A1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        #-----
        A2_lbl=Label(F2,text="Eye Liner",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        A2_txt=Entry(F2,width=10,textvariable=self.A2,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        #------
        A3_lbl=Label(F2,text="Face Powder",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        A3_txt=Entry(F2,width=10,textvariable=self.A3,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        #----
        A4_lbl=Label(F2,text="Lipstick",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        A4_txt=Entry(F2,width=10,textvariable=self.A4,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        #---
        A5_lbl=Label(F2,text="Rose Water",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        A5_txt=Entry(F2,width=10,textvariable=self.A5,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        #----
        A6_lbl=Label(F2,text="Cleansing Milk",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        A6_txt=Entry(F2,width=10,textvariable=self.A6,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        #========Grocery=============================================================================================================================
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=330,y=150,width=325,height=380)
        #------
        B1_lbl=Label(F3,text="Toor Dal",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        B1_txt=Entry(F3,width=10,textvariable=self.B1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        #-----
        B2_lbl=Label(F3,text="Groundnut Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        B2_txt=Entry(F3,width=10,textvariable=self.B2,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        #------
        B3_lbl=Label(F3,text="Detergent",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        B3_txt=Entry(F3,width=10,textvariable=self.B3,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        #----
        B4_lbl=Label(F3,text="Dish Wash Bar",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        B4_txt=Entry(F3,width=10,textvariable=self.B4,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        #---
        B5_lbl=Label(F3,text="Spices",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        B5_txt=Entry(F3,width=10,textvariable=self.B5,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        #----
        B6_lbl=Label(F3,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        B6_txt=Entry(F3,width=10,textvariable=self.B6,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        #=======Brevage===============================================================================================================================
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Beverage",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=655,y=150,width=325,height=380)
        #------
        C1_lbl=Label(F4,text="Cool Drinks",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        C1_txt=Entry(F4,width=10,textvariable=self.C1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        #-----
        C2_lbl=Label(F4,text="Fruit Juices",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        C2_txt=Entry(F4,width=10,textvariable=self.C2,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        #------
        C3_lbl=Label(F4,text="Mocktail",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        C3_txt=Entry(F4,width=10,textvariable=self.C3,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        #----
        C4_lbl=Label(F4,text="Soda",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        C4_txt=Entry(F4,width=10,textvariable=self.C4,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        #---
        C5_lbl=Label(F4,text="Lime Soda",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        C5_txt=Entry(F4,width=10,textvariable=self.C5,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        #----
        C6_lbl=Label(F4,text="Ice Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        C6_txt=Entry(F4,width=10,textvariable=self.C6,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #===================================Billing Area==============================================================================================
        F5=LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=980,y=150,width=300,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #============================================Billing Menu=====================================================================================

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Billing Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=530,relwidth=1,height=130)
        #------
        A_lbl=Label(F6,text="Total Cosmatic Price",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=5,sticky="w")
        A_txt=Entry(F6,width=10,textvariable=self.A,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
        #-----
        B_lbl=Label(F6,text="Total Grocery Price",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=5,sticky="w")
        B_txt=Entry(F6,width=10,textvariable=self.B,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=5)

        #-----
        
        C_lbl=Label(F6,text="Total Beverages Price",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=10,pady=5,sticky="w")
        C_txt=Entry(F6,width=10,textvariable=self.C,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)
        #-----
        D_lbl=Label(F6,text="Total Gst Tax",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=2,padx=10,pady=5,sticky="w")
        D_txt=Entry(F6,width=10,textvariable=self.D,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=5)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=720,width=525,height=85)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="Cadetblue",fg="white",pady=15,width=10,font="arial 12 bold").grid(row=0,column=0,padx=10,pady=5)
        GBill_btn=Button(btn_F,command=self.bill_area,text="G-Bill",bg="Cadetblue",fg="white",pady=15,width=10,font="arial 12 bold").grid(row=0,column=2,padx=6,pady=5)
        Clear_btn=Button(btn_F,text="Clear",bg="Cadetblue",fg="white",pady=15,width=10,font="arial 12 bold").grid(row=0,column=3,padx=6,pady=5)
        Exit_btn=Button(btn_F,text="Exit",bg="Cadetblue",fg="white",pady=15,width=10,font="arial 12 bold").grid(row=0,column=4,padx=10,pady=5)
        self.Welcome_bill()
        
    def total(self):
        self.c_A1=self.A1.get()*40
        self.c_A2=self.A2.get()*120
        self.c_A3=self.A3.get()*60
        self.c_A4=self.A4.get()*180
        self.c_A5=self.A5.get()*140
        self.c_A6=self.A6.get()*180
        self.total_cosmetic_price=float(
                                        self.c_A1+
                                        self.c_A2+
                                        self.c_A3+
                                        self.c_A4+
                                        self.c_A5+
                                        self.c_A6
                                        )
        self.x=self.total_cosmetic_price
        self.A.set("Rs "+str(self.total_cosmetic_price))
        
        self.g_B1=self.B1.get()*40
        self.g_B2=self.B2.get()*120
        self.g_B3=self.B3.get()*60
        self.g_B4=self.B4.get()*180
        self.g_B5=self.B5.get()*140
        self.g_B6=self.B6.get()*180
        self.total_grocery_price=float(
                                        self.g_B1+
                                        self.g_B2+
                                        self.g_B3+
                                        self.g_B4+
                                        self.g_B5+
                                        self.g_B6
                                        )
        self.y=self.total_grocery_price
        self.B.set("Rs "+str(self.total_grocery_price))
        
        self.b_C1=self.C1.get()*40
        self.b_C2=self.C2.get()*120
        self.b_C3=self.C3.get()*60
        self.b_C4=self.C4.get()*180
        self.b_C5=self.C5.get()*140
        self.b_C6=self.C6.get()*180
        self.total_brevage_price=float(
                                        self.b_C1+
                                        self.b_C2+
                                        self.b_C3+
                                        self.b_C4+
                                        self.b_C5+
                                        self.b_C6
                                        )
        self.z=self.total_brevage_price
        self.C.set("Rs "+str(self.total_brevage_price))
        self.D.set("Rs "+str(round((self.x*0.01+self.y*0.02+self.z*0.1),2)))

    def Welcome_bill(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END,"\tWelcome to Rj retails")
        self.txtarea.insert(END,f"\nBill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,"\n********************************")
        self.txtarea.insert(END,"\nProducts\t\tQTY\tPrice")
        self.txtarea.insert(END,"\n********************************")

    def bill_area(self):
        self.Welcome_bill()
        #=================================cosmatic==========================================
        if(self.A1.get()!=0):
            self.txtarea.insert(END,f"\nA1\t\t{self.A1.get()}\t{self.c_A1}")
        if(self.A2.get()!=0):
            self.txtarea.insert(END,f"\nA2\t\t{self.A2.get()}\t{self.c_A2}")
        if(self.A3.get()!=0):
            self.txtarea.insert(END,f"\nA3\t\t{self.A3.get()}\t{self.c_A3}")
        if(self.A4.get()!=0):
            self.txtarea.insert(END,f"\nA4\t\t{self.A4.get()}\t{self.c_A4}")
        if(self.A5.get()!=0):
            self.txtarea.insert(END,f"\nA5\t\t{self.A5.get()}\t{self.c_A5}")
        if(self.A6.get()!=0):
            self.txtarea.insert(END,f"\nA6\t\t{self.A6.get()}\t{self.c_A6}")
        #================================Grosery============================================
        if(self.B1.get()!=0):
            self.txtarea.insert(END,f"\nB1\t\t{self.B1.get()}\t{self.g_B1}")
        if(self.B2.get()!=0):
            self.txtarea.insert(END,f"\nB2\t\t{self.B2.get()}\t{self.g_B2}")
        if(self.B3.get()!=0):
            self.txtarea.insert(END,f"\nB3\t\t{self.B3.get()}\t{self.g_B3}")
        if(self.B4.get()!=0):
            self.txtarea.insert(END,f"\nB4\t\t{self.B4.get()}\t{self.g_B4}")
        if(self.B5.get()!=0):
            self.txtarea.insert(END,f"\nB5\t\t{self.B5.get()}\t{self.g_B5}")
        if(self.B6.get()!=0):
            self.txtarea.insert(END,f"\nB6\t\t{self.B6.get()}\t{self.g_B6}")
        #================================Brevages==============================================
        if(self.C1.get()!=0):
            self.txtarea.insert(END,f"\nC1\t\t{self.C1.get()}\t{self.b_C1}")
        if(self.C2.get()!=0):
            self.txtarea.insert(END,f"\nC1\t\t{self.C2.get()}\t{self.b_C2}")
        if(self.C3.get()!=0):
            self.txtarea.insert(END,f"\nC1\t\t{self.C3.get()}\t{self.b_C3}")
        if(self.C4.get()!=0):
            self.txtarea.insert(END,f"\nC1\t\t{self.C4.get()}\t{self.b_C4}")
        if(self.C5.get()!=0):
            self.txtarea.insert(END,f"\nC1\t\t{self.C5.get()}\t{self.b_C5}")
        if(self.C6.get()!=0):
            self.txtarea.insert(END,f"\nC1\t\t{self.C6.get()}\t{self.b_C6}")
        self.txtarea.insert(END,"\n********************************")
        if(self.A.get()!="Rs 0.0"):
            self.txtarea.insert(END,f"\nCosmatic Price \t\t {self.A.get()}")
        if(self.B.get()!="Rs 0.0"):
            self.txtarea.insert(END,f"\nGrocery Price \t\t {self.B.get()}")
        if(self.C.get()!="Rs 0.0"):
            self.txtarea.insert(END,f"\nBrevage Price \t\t {self.C.get()}")
        
        
        
        
        
        
        

root=Tk()
obj=Bill_App(root)#creating object
root.mainloop()  #tkinter loop closed
