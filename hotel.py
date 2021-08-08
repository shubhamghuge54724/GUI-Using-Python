from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime

class Hotel:

    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="powder blue")


        MainFrame = Frame(self.root)
        MainFrame.grid()

        TopFrame = Frame(MainFrame,bd=14,width=1350,height=550,padx=20,relief=RIDGE,bg="cadet blue")
        TopFrame.pack(side=TOP)

        LeftFrame = Frame(TopFrame,bd=10,width=450,height=550,padx=2,relief=RIDGE,bg="powder blue")
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(TopFrame,bd=10,width=820,height=550,padx=2,relief=RIDGE,bg="cadet blue")
        RightFrame.pack(side=RIGHT)

        BottomFrame = Frame(MainFrame,bd=10,width=1350,height=550,padx=2,relief=RIDGE,bg="powder blue")
        BottomFrame.pack(side=BOTTOM)
#***********************************Exit****************************
        def iExit():
            iExit = tkinter.messagebox.askyesno("Hotel Management System","Comfirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
#*******************************Receipt********************************
        def Receipt():
            self.textreceipt.insert(END,CustomerRef.get()+"\t"+FirstName.get()+"\t"+SurName.get()+"\t"+Address.get()+"\t"+PostCode.get()+
                                   "\t"+Mobile.get()+"\t"+Nationality.get()+"\t"+CheckInDate.get()+"\t"+CheckOutDate.get()+"\t"+PaidTax.get()+"\t"+SubTotal.get()+
                                   "\t"+TotalCost.get()+"\n")
#**************************Reset*************************************
        def Reset():
            CustomerRef.set("")
            FirstName.set("")
            SurName.set("")
            Address.set("")
            PostCode.set("")
            Mobile.set("")
            Email.set("")
            Nationality.set("")
            DOB.set("")
            IDType.set("")
            Gender.set("")
            CheckInDate.set("")
            CheckOutDate.set("")
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            RoomExNo.set("")
            TotalCost.set("")
            SubTotal.set("")
            PaidTax.set("")
            TotalDays.set("")
            self.textreceipt.delete("1.0",END)
#*****************************Total Cost & Date**********************
        def TotalCostAndDay():
            inDate = CheckInDate.get()
            outDate = CheckOutDate.get()
            inDate = datetime.strptime(inDate,"%d/%m/%Y")
            outDate = datetime.strptime(outDate,"%d/%m/%Y")
            TotalDays.set(abs(outDate-inDate).days)

            if (Meal.get() == 'Breakfast' and RoomType.get() == 'Single'):
                q1 = float(50)
                q2 = float(400)

                q3 = float(TotalDays.get())
                q4 = float(q3*q2)
                q5 = float(q4+q1)
                Tax = "Rs"+str('%.2f'%((q5)*0.05))
                ST = "Rs"+str('%.2f'%(q5))
                TT = "Rs"+str('%.2f'%(q5 + ((q5)*0.05)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif(Meal.get() == 'Breakfast' and RoomType.get() == 'Double'):
                q1 = float(50)
                q2 = float(600)

                q3 = float(TotalDays.get())
                q4 = float(q3*q2)
                q5 = float(q4+q1)
                Tax = "Rs"+str('%.2f'%((q5)*0.05))
                ST = "Rs"+str('%.2f'%(q5))
                TT = "Rs"+str('%.2f'%(q5 + ((q5)*0.05)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif(Meal.get() == 'Lunch' and RoomType.get() == 'Double'):
                q1 = float(400)
                q2 = float(600)

                q3 = float(TotalDays.get())
                q4 = float(q3*q2)
                q5 = float(q4+q1)
                Tax = "Rs"+str('%.2f'%((q5)*0.05))
                ST = "Rs"+str('%.2f'%(q5))
                TT = "Rs"+str('%.2f'%(q5 + ((q5)*0.05)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif(Meal.get() == 'Dinner' and RoomType.get() == 'Double'):
                q1 = float(450)
                q2 = float(600)

                q3 = float(TotalDays.get())
                q4 = float(q3*q2)
                q5 = float(q4+q1)
                Tax = "Rs"+str('%.2f'%((q5)*0.05))
                ST = "Rs"+str('%.2f'%(q5))
                TT = "Rs"+str('%.2f'%(q5 + ((q5)*0.05)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif(Meal.get() == 'Lunch' and RoomType.get() == 'Single'):
                q1 = float(200)
                q2 = float(400)

                q3 = float(TotalDays.get())
                q4 = float(q3*q2)
                q5 = float(q4+q1)
                Tax = "Rs"+str('%.2f'%((q5)*0.05))
                ST = "Rs"+str('%.2f'%(q5))
                TT = "Rs"+str('%.2f'%(q5 + ((q5)*0.05)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif(Meal.get() == 'Dinner' and RoomType.get() == 'Single'):
                q1 = float(250)
                q2 = float(400)

                q3 = float(TotalDays.get())
                q4 = float(q3*q2)
                q5 = float(q4+q1)
                Tax = "Rs"+str('%.2f'%((q5)*0.05))
                ST = "Rs"+str('%.2f'%(q5))
                TT = "Rs"+str('%.2f'%(q5 + ((q5)*0.05)))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)

#*****************************String Var*****************************
            
        CustomerRef = StringVar()#1
        FirstName = StringVar()#2
        SurName = StringVar()#3
        Address = StringVar()#4
        PostCode = StringVar()#5
        Mobile = StringVar()#6
        Email = StringVar()#7
        Nationality = StringVar()#8
        DOB = StringVar()#9
        IDType = StringVar()#10
        Gender = StringVar()#11
        CheckInDate = StringVar()#12
        CheckOutDate = StringVar()#13
        Meal = StringVar()#14
        RoomType = StringVar()#15
        RoomNo = StringVar()#16
        RoomExNo = StringVar()#17
        TotalCost = StringVar()#18
        SubTotal = StringVar()#19
        PaidTax = StringVar()#20
        TotalDays = StringVar()#21
#******************************Widget******************************
        self.lebleCust_Ref = Label(LeftFrame,font=('arial',12,'bold'),text = "Customer Ref:",padx=2,bg="powder blue")
        self.lebleCust_Ref.grid(row=0,column=0,sticky=W)
        self.textCust_Ref = Entry(LeftFrame,font=('arial',12,'bold'),textvariable = CustomerRef,width=20)
        self.textCust_Ref.grid(row=0,column=1,pady=3,padx=20)#1

        self.lebleFirstName = Label(LeftFrame,font=('arial',12,'bold'),text = "FirstName:",padx=2,bg="powder blue")
        self.lebleFirstName.grid(row=1,column=0,sticky=W)
        self.textFirstName = Entry(LeftFrame,font=('arial',12,'bold'),textvariable = FirstName,width=20)
        self.textFirstName.grid(row=1,column=1,pady=3,padx=20)#2

        self.lebleSurName = Label(LeftFrame,font=('arial',12,'bold'),text = "SurName:",padx=2,bg="powder blue")
        self.lebleSurName.grid(row=2,column=0,sticky=W)
        self.textSurName = Entry(LeftFrame,font=('arial',12,'bold'),textvariable = SurName,width=20)
        self.textSurName.grid(row=2,column=1,pady=3,padx=20)#3

        self.lebleAddress = Label(LeftFrame,font=('arial',12,'bold'),text = "Address:",padx=2,bg="powder blue")
        self.lebleAddress.grid(row=3,column=0,sticky=W)
        self.textAddress = Entry(LeftFrame,font=('arial',12,'bold'),textvariable = Address,width=20)
        self.textAddress.grid(row=3,column=1,pady=3,padx=20)#4

        self.leblePostCode = Label(LeftFrame,font=('arial',12,'bold'),text = "PostCode:",padx=2,bg="powder blue")
        self.leblePostCode.grid(row=4,column=0,sticky=W)
        self.textPostCode = Entry(LeftFrame,font=('arial',12,'bold'),textvariable = PostCode,width=20)
        self.textPostCode.grid(row=4,column=1,pady=3,padx=20)#5

        self.lebleMobile = Label(LeftFrame,font=('arial',12,'bold'),text = "Mobile:",padx=2,bg="powder blue")
        self.lebleMobile.grid(row=5,column=0,sticky=W)
        self.textMobile = Entry(LeftFrame,font=('arial',12,'bold'),textvariable = Mobile,width=20)
        self.textMobile.grid(row=5,column=1,pady=3,padx=20)#6

        self.lebleEmail = Label(LeftFrame,font=('arial',12,'bold'),text = "Email:",padx=2,bg="powder blue")
        self.lebleEmail.grid(row=6,column=0,sticky=W)
        self.textEmail = Entry(LeftFrame,font=('arial',12,'bold'),textvariable = Email,width=20)
        self.textEmail.grid(row=6,column=1,pady=3,padx=20)#7

        self.lebleNationality = Label(LeftFrame,font=('arial',12,'bold'),text= "Nationality",padx=2,pady =2 ,bg="powder blue")
        self.lebleNationality .grid(row=7,column=0,sticky=W)
        self.cboNationality = ttk.Combobox(LeftFrame,textvariable = Nationality,state = "readonly",font=('arial',12,'bold'),width=18)
        self.cboNationality['value'] = ('America','British','Canada','China','India','Japan')
        self.cboNationality.current(0)
        self.cboNationality.grid(row=7,column=1,pady=3,padx=20)#8

        self.lebleDOB = Label(LeftFrame,font=('arial',12,'bold'),text = "Date Of Birth:",padx=2,bg="powder blue")
        self.lebleDOB.grid(row=8,column=0,sticky=W)
        self.textDOB = Entry(LeftFrame,font=('arial',12,'bold'),textvariable = DOB,width=20)
        self.textDOB.grid(row=8,column=1,pady=3,padx=20)#9

        self.lebleIDType = Label(LeftFrame,font=('arial',12,'bold'),text= "IDType",padx=2,pady =2 ,bg="powder blue")
        self.lebleIDType .grid(row=9,column=0,sticky=W)
        self.cboIDType = ttk.Combobox(LeftFrame,textvariable = IDType,state = "readonly",font=('arial',12,'bold'),width=18)
        self.cboIDType['value'] = ('Driving L','Voter Id','Pan Card','Adhar')
        self.cboIDType.current(0)
        self.cboIDType.grid(row=9,column=1,pady=3,padx=20)#10

        self.lebleGender = Label(LeftFrame,font=('arial',12,'bold'),text= "Gender",padx=2,pady =2 ,bg="powder blue")
        self.lebleGender .grid(row=10,column=0,sticky=W)
        self.cboGender = ttk.Combobox(LeftFrame,textvariable = Gender,state = "readonly",font=('arial',12,'bold'),width=18)
        self.cboGender['value'] = ('Female','Male','Other')
        self.cboGender.current(0)
        self.cboGender.grid(row=10,column=1,pady=3,padx=20)#11

        self.lebleCheckInDate = Label(LeftFrame,font=('arial',12,'bold'),text = "CheckInDate:",padx=2,bg="powder blue")
        self.lebleCheckInDate.grid(row=11,column=0,sticky=W)
        self.textCheckInDate = Entry(LeftFrame,font=('arial',12,'bold'),textvariable = CheckInDate,width=20)
        self.textCheckInDate.grid(row=11,column=1,pady=3,padx=20)#12

        self.lebleCheckOutDate = Label(LeftFrame,font=('arial',12,'bold'),text = "CheckOutDate",padx=2,bg="powder blue")
        self.lebleCheckOutDate.grid(row=12,column=0,sticky=W)
        self.textCheckOutDate = Entry(LeftFrame,font=('arial',12,'bold'),textvariable = CheckOutDate,width=20)
        self.textCheckOutDate.grid(row=12,column=1,pady=3,padx=20)#13

        self.lebleMeal = Label(LeftFrame,font=('arial',12,'bold'),text= "Meal",padx=2,pady =2 ,bg="powder blue")
        self.lebleMeal .grid(row=13,column=0,sticky=W)
        self.cboMeal = ttk.Combobox(LeftFrame,textvariable = Meal,state = "readonly",font=('arial',12,'bold'),width=18)
        self.cboMeal['value'] = ('Breakfast','Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13,column=1,pady=3,padx=20)#14

        self.lebleRoomType = Label(LeftFrame,font=('arial',12,'bold'),text= "RoomType",padx=2,pady =2 ,bg="powder blue")
        self.lebleRoomType .grid(row=14,column=0,sticky=W)
        self.cboRoomType = ttk.Combobox(LeftFrame,textvariable = RoomType,state = "readonly",font=('arial',12,'bold'),width=18)
        self.cboRoomType['value'] = ('Single','Double')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14,column=1,pady=3,padx=20)#15

        self.lebleRoomNo  = Label(LeftFrame,font=('arial',12,'bold'),text= "RoomNo",padx=2,pady =2 ,bg="powder blue")
        self.lebleRoomNo .grid(row=15,column=0,sticky=W)
        self.cboRoomNo = ttk.Combobox(LeftFrame,textvariable = RoomNo,state = "readonly",font=('arial',12,'bold'),width=18)
        self.cboRoomNo['value'] = ('101','102','103','104','105')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=15,column=1,pady=3,padx=20)#16

#*********************************Receipt**********************************
        self.lbl = Label(RightFrame,font=('arial',10,'bold'),pady=10,bg="cadet blue",
                         text="CustomerRef\tFirstName\tSurname\tAddress\tPostcode\tMobile\tNationality\tCheckInDate\tCheckoutDate")
        self.lbl.grid(row=0,column=0,columnspan=17)

        self.textreceipt = Text(RightFrame,height = 15,width = 108,bd =10,font=('arial',11,'bold'))
        self.textreceipt.grid(row=1,column=0,columnspan=2,padx=2,pady=5)
#**************************************************************************
        self.lebleDays= Label(RightFrame,font=('arial',12,'bold'),text = "No Of Days",bd=7,bg="cadet blue",fg="black")
        self.lebleDays.grid(row=2,column=0,sticky=W)
        self.textDays = Entry(RightFrame,font=('arial',12,'bold'),textvariable = TotalDays,bd=7,bg='white',width=67,justify=LEFT)
        self.textDays.grid(row=2,column=1)#17

        self.leblePaidtax= Label(RightFrame,font=('arial',12,'bold'),text = "Paid Tax",bd=7,bg="cadet blue",fg="black")
        self.leblePaidtax.grid(row=3,column=0,sticky=W)
        self.textPaidtax = Entry(RightFrame,font=('arial',12,'bold'),textvariable = PaidTax,bd=7,bg='white',width=67,justify=LEFT)
        self.textPaidtax.grid(row=3,column=1)#18

        self.lebleSubTotal= Label(RightFrame,font=('arial',12,'bold'),text = "Sub Total",bd=7,bg="cadet blue",fg="black")
        self.lebleSubTotal.grid(row=4,column=0,sticky=W)
        self.textSubTotal = Entry(RightFrame,font=('arial',12,'bold'),textvariable = SubTotal,bd=7,bg='white',width=67,justify=LEFT)
        self.textSubTotal.grid(row=4,column=1)#19

        self.lebleTotalCost= Label(RightFrame,font=('arial',12,'bold'),text = "Total Cost",bd=7,bg="cadet blue",fg="black")
        self.lebleTotalCost.grid(row=5,column=0,sticky=W)
        self.textTotalCost = Entry(RightFrame,font=('arial',12,'bold'),textvariable = TotalCost,bd=7,bg='white',width=67)
        self.textTotalCost.grid(row=5,column=1)#20
        

#************************************Button*********************************
        self.btnTotal=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('aria',16,'bold'),width=21,height=2,
                             bg="powder blue",text="Total",command=TotalCostAndDay).grid(row=0,column=4,padx=4)

        self.btnReceipt=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('aria',16,'bold'),width=21,height=2,
                               bg="powder blue",text="Receipt",command=Receipt).grid(row=0,column=5,padx=4)

        self.btnReset=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('aria',16,'bold'),width=21,height=2,
                             bg="powder blue",text="Reset",command=Reset).grid(row=0,column=6,padx=4)

        self.btnExit=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('aria',16,'bold'),width=21,height=2,
                            bg="powder blue",text="Exit",command=iExit).grid(row=0,column=7,padx=4)

if __name__ =='__main__':
    root = Tk()
    application = Hotel(root)
    root.mainloop()
