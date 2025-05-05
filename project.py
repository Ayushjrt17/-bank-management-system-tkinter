import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk




class bank:
    def __init__(self,root):
        self.root=root
        self.root.title("BANK MANAGEMENT SYSTEM")

        self.root.geometry("1540x800+0+0")

        self.Branch = StringVar()
        self.AccountNo = StringVar()
        self.FirstName = StringVar()
        self.LastName = StringVar()
        self.Age = StringVar()
        self.Address = StringVar()
        self.City = StringVar()
        self.State = StringVar()
        self.Country = StringVar()
        self.PAN = StringVar()
        self.Aadhaar = StringVar()
        self.Loan = StringVar()
        self.Contact = StringVar()
        self.Email = StringVar()
        self.AccountType = StringVar()
        self.Occupation = StringVar()

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="ATLAS NATIONAL BANK",fg="orange",bg="white",
                    font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        '''DataFRAME'''
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=100,width=1280,height=500)

        '''DataFrame Left'''

        dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                 font=("times new roman",12,"bold"),text="Account Holder Information")
        dataframeleft.place(x=0,y=5,width=900,height=320)

        '''DataFrane Right'''
        dataframeright=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                font=("times new roman",12,"bold"),text="Details")
        dataframeright.place(x=910,y=5,width=330,height=320)

        '''Buttons Frames'''
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=450,width=1280,height=80)

        '''Details Frame'''
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=530,width=1280,height=120)

        '''Label enteryfills left'''
        lblbranch=Label(dataframeleft,text="Branch :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblbranch.grid(row=0,column=0)

        combobranch=ttk.Combobox(dataframeleft,textvariable=self.Branch,font=("times new roman",12,"bold"),width=35)
        combobranch["values"]=("Bhondsi","Sohna","Tavdu","MarutiKunj","Badshahpur","Gurugram","Ghamdhoj")
        combobranch.grid(row=0,column=1)
        '''Account Number'''
        lblname=Label(dataframeleft,text="Account No.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblname.grid(row=1,column=0)

        texname=Entry(dataframeleft,textvariable=self.AccountNo,font=("arial",12,"bold"),width=35)
        texname.grid(row=1,column=1)


        lblname1=Label(dataframeleft,text="First Name :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblname1.grid(row=2,column=0)

        texname1=Entry(dataframeleft,textvariable=self.FirstName,font=("arial",12,"bold"),width=35)
        texname1.grid(row=2,column=1)

        lblname2=Label(dataframeleft,text="Last Name :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblname2.grid(row=3,column=0)

        texname2=Entry(dataframeleft,textvariable=self.LastName,font=("arial",12,"bold"),width=35)
        texname2.grid(row=3,column=1)


        ''''''
        lblage=Label(dataframeleft,text="Age :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblage.grid(row=4,column=0)

        texage=Entry(dataframeleft,textvariable=self.Age,font=("arial",12,"bold"),width=35)
        texage.grid(row=4,column=1)

        ''''''

        lbladd=Label(dataframeleft,text="Address :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbladd.grid(row=5,column=0)

        texadd=Entry(dataframeleft,textvariable=self.Address,font=("arial",12,"bold"),width=35)
        texadd.grid(row=5,column=1)
        ''''''

        lblcity=Label(dataframeleft,text="City :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblcity.grid(row=6,column=0)

        texcity=Entry(dataframeleft,textvariable=self.City,font=("arial",12,"bold"),width=35)
        texcity.grid(row=6,column=1)
        ''''''
        lblstate=Label(dataframeleft,text="State :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblstate.grid(row=7,column=0)

        texstate=Entry(dataframeleft,textvariable=self.State,font=("arial",12,"bold"),width=35)
        texstate.grid(row=7,column=1)

        ''''''
        lblcountry=Label(dataframeleft,text="Country :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblcountry.grid(row=0,column=4)

        texcountry=Entry(dataframeleft,textvariable=self.Country,font=("arial",12,"bold"),width=35)
        texcountry.grid(row=0,column=5)
        ''''''
        lblpan=Label(dataframeleft,text="PAN No.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblpan.grid(row=1,column=4)

        texpan=Entry(dataframeleft,textvariable=self.PAN,font=("arial",12,"bold"),width=35)
        texpan.grid(row=1,column=5)
        ''''''
        lbladd=Label(dataframeleft,text="Aadhaar No.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbladd.grid(row=2,column=4)

        texadd=Entry(dataframeleft,textvariable=self.Aadhaar,font=("arial",12,"bold"),width=35)
        texadd.grid(row=2,column=5)
        ''''''

        lblloan=Label(dataframeleft,text="Loan :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblloan.grid(row=3,column=4)

        texloan=Entry(dataframeleft,textvariable=self.Loan,font=("arial",12,"bold"),width=35)
        texloan.grid(row=3,column=5)


        ''''''

        lblnum=Label(dataframeleft,text="Contact No.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnum.grid(row=4,column=4)

        texnum=Entry(dataframeleft,textvariable=self.Contact,font=("arial",12,"bold"),width=35)
        texnum.grid(row=4,column=5)

        ''''''
        lblem=Label(dataframeleft,text="EMail :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblem.grid(row=5,column=4)

        texem=Entry(dataframeleft,textvariable=self.Email,font=("arial",12,"bold"),width=35)
        texem.grid(row=5,column=5)

        ''''''
        lblty=Label(dataframeleft,text="Account Type :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblty.grid(row=6,column=4)

        texty=Entry(dataframeleft,textvariable=self.AccountType,font=("arial",12,"bold"),width=35)
        texty.grid(row=6,column=5)


        ''''''
        lblocc=Label(dataframeleft,text="Occupation :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblocc.grid(row=7,column=4)

        texocc=Entry(dataframeleft,textvariable=self.Occupation,font=("arial",12,"bold"),width=35)
        texocc.grid(row=7,column=5)
        # '''''''''''''''''Dataframe Right'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        self.txtDeatils=Text(dataframeright,font=("times new roman",12,"bold"),width=36,height=14,padx=2,pady=6)
        self.txtDeatils.grid(row=0,column=0)


        # =======================Buttons==========================================================

        btndetails = Button(Buttonframe, text="DETAILS", bg="orange", fg="white",
                         font=("arial", 12, "bold"),command=self.details_button_clicked,width=20, height=1, padx=2, pady=6)
        btndetails.grid(row=0, column=0)

        btn_save = Button(Buttonframe, text="SAVE", bg="orange", fg="white",
                        font=("arial", 12, "bold"), command=self.btndetails, width=20, height=1, padx=2, pady=6)
        btn_save.grid(row=0, column=1)

        btn_update = Button(Buttonframe, text="UPDATE", bg="orange", fg="white",
                            font=("arial", 12, "bold"),command=self.update_data, width=20, height=1, padx=2, pady=6)
        btn_update.grid(row=0, column=2, )

        btn_delete = Button(Buttonframe, text="DELETE", bg="orange", fg="white",
                            font=("arial", 12, "bold"),command=self.idelete, width=20, height=1, padx=2, pady=6)
        btn_delete.grid(row=0, column=3)

        btn_reset = Button(Buttonframe, text="RESET", bg="orange", fg="white",
                        font=("arial", 12, "bold"),command=self.reset_data, width=20, height=1, padx=2, pady=6)
        btn_reset.grid(row=0, column=4)

        btn_exit = Button(Buttonframe, text="EXIT", bg="orange", fg="white",
                        font=("arial", 12, "bold"),command=self.iExit, width=17, height=1, padx=2, pady=6)
        btn_exit.grid(row=0, column=5)


        ''''''''''''''''''''''''''"SCROLLBAR"''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


        # Scrollbars for Treeview
        scroll_y_details = Scrollbar(Detailsframe, orient=VERTICAL)
        scroll_x_details = Scrollbar(Detailsframe, orient=HORIZONTAL)

        # Treeview
        self.acc_deatils = ttk.Treeview(Detailsframe,
                                        columns=("Branch", "Account No.", "First Name", "Last Name",
                                                "Age", "Address", "City", "State", "Country", "PAN No.",
                                                "Aadhaar No.", "Loan", "Contact No.", "EMail", "Account Type",
                                                "Occupation"),
                                        yscrollcommand=scroll_y_details.set,
                                        xscrollcommand=scroll_x_details.set)

        # Configure scrollbars
        scroll_y_details.config(command=self.acc_deatils.yview)
        scroll_x_details.config(command=self.acc_deatils.xview)

        # Place scrollbars
        scroll_y_details.pack(side=RIGHT, fill=Y)
        scroll_x_details.pack(side=BOTTOM, fill=X)

        # Define columns and  Setting Column Headings:
        self.acc_deatils.heading("Branch", text="Branch")
        self.acc_deatils.heading("Account No.", text="Account No.")
        self.acc_deatils.heading("First Name", text="First Name")
        self.acc_deatils.heading("Last Name", text="Last Name")
        self.acc_deatils.heading("Age", text="Age")
        self.acc_deatils.heading("Address", text="Address")
        self.acc_deatils.heading("City", text="City")
        self.acc_deatils.heading("State", text="State")
        self.acc_deatils.heading("Country", text="Country")
        self.acc_deatils.heading("PAN No.", text="PAN No.")
        self.acc_deatils.heading("Aadhaar No.", text="Aadhaar No.")
        self.acc_deatils.heading("Loan", text="Loan")
        self.acc_deatils.heading("Contact No.", text="Contact No.")
        self.acc_deatils.heading("EMail", text="EMail")
        self.acc_deatils.heading("Account Type", text="Account Type")
        self.acc_deatils.heading("Occupation", text="Occupation")

        self.acc_deatils["show"] = "headings"
        self.acc_deatils.pack(fill=BOTH, expand=1)


        # ''''''''' Set Column WIDTH''''''''''''''''''''''''''''''''''''''''''

        self.acc_deatils.column("Branch", width=100)
        self.acc_deatils.column("Account No.", width=120)
        self.acc_deatils.column("First Name", width=120)
        self.acc_deatils.column("Last Name", width=120)
        self.acc_deatils.column("Age", width=50)
        self.acc_deatils.column("Address", width=150)
        self.acc_deatils.column("City", width=100)
        self.acc_deatils.column("State", width=100)
        self.acc_deatils.column("Country", width=100)
        self.acc_deatils.column("PAN No.", width=120)
        self.acc_deatils.column("Aadhaar No.", width=130)
        self.acc_deatils.column("Loan", width=80)
        self.acc_deatils.column("Contact No.", width=130)
        self.acc_deatils.column("EMail", width=150)
        self.acc_deatils.column("Account Type", width=120)
        self.acc_deatils.column("Occupation", width=130)

        self.acc_deatils.pack(fill=BOTH,expand=1)
        self.acc_deatils.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()





    # ----------------------------------------------------------------------------------------
    # ========================FUNCTIONS================================================================
    # ==============================================================================================
    def btndetails(self):
        if self.Branch.get() == "" or self.AccountNo.get() == "":
            messagebox.showerror("Error", "All fields are required to fill")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="1234",
                    database="bank"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("""
                    INSERT INTO cus_details (Branch, Account_No, First_Name, Last_Name, Age, Address, City, State, 
                    Country, PAN_No, Aadhaar_No, Loan, Contact_No, EMail, Account_Type, Occupation)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    self.Branch.get(),
                    self.AccountNo.get(),
                    self.FirstName.get(),
                    self.LastName.get(),
                    self.Age.get(),
                    self.Address.get(),
                    self.City.get(),
                    self.State.get(),
                    self.Country.get(),
                    self.PAN.get(),
                    self.Aadhaar.get(),
                    self.Loan.get(),
                    self.Contact.get(),
                    self.Email.get(),
                    self.AccountType.get(),
                    self.Occupation.get()
                ))
                conn.commit()  # Commit after the insertion
                self.fetch_data()  # Refresh data in the Treeview
                conn.close()
                messagebox.showinfo("Success", "Record saved successfully")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

    # =======================================================================================            #    
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="1234",
            database="bank"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from  cus_details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.acc_deatils.delete(*self.acc_deatils.get_children())
        for row in rows:
            self.acc_deatils.insert("", END, values=row)

            
            conn.commit()
        conn.close()
    # =========================================================
    def show_details(self):
        self.txtDeatils.insert(END, "Branch:\t\t" + self.Branch.get() + "\n")
        self.txtDeatils.insert(END, "Account No.:\t\t" + self.AccountNo.get() + "\n")
        self.txtDeatils.insert(END, "First Name:\t\t" + self.FirstName.get() + "\n")
        self.txtDeatils.insert(END, "Last Name:\t\t" + self.LastName.get() + "\n")
        self.txtDeatils.insert(END, "Age:\t\t" + self.Age.get() + "\n")
        self.txtDeatils.insert(END, "Address:\t\t" + self.Address.get() + "\n")
        self.txtDeatils.insert(END, "City:\t\t" + self.City.get() + "\n")
        self.txtDeatils.insert(END, "State:\t\t" + self.State.get() + "\n")
        self.txtDeatils.insert(END, "Country:\t\t" + self.Country.get() + "\n")
        self.txtDeatils.insert(END, "PAN No.:\t\t" + self.PAN.get() + "\n")
        self.txtDeatils.insert(END, "Aadhaar No.:\t\t" + self.Aadhaar.get() + "\n")
        self.txtDeatils.insert(END, "Loan:\t\t" + self.Loan.get() + "\n")
        self.txtDeatils.insert(END, "Contact No.:\t\t" + self.Contact.get() + "\n")
        self.txtDeatils.insert(END, "Email:\t\t" + self.Email.get() + "\n")
        self.txtDeatils.insert(END, "Account Type:\t\t" + self.AccountType.get() + "\n")
        self.txtDeatils.insert(END, "Occupation:\t\t" + self.Occupation.get() + "\n")



# ======Call both funtion in a funtion==================================

    def details_button_clicked(self):
        self.fetch_data()  # Refresh data in the Treeview
        self.show_details()  # Show the details of the selected record


        

# =====================================================================
    def get_cursor(self, event=""):
        cursor_row = self.acc_deatils.focus()
        content = self.acc_deatils.item(cursor_row)
        row = content['values']

        if row:
            self.Branch.set(row[0])
            self.AccountNo.set(row[1])
            self.FirstName.set(row[2])
            self.LastName.set(row[3])
            self.Age.set(row[4])
            self.Address.set(row[5])
            self.City.set(row[6])
            self.State.set(row[7])
            self.Country.set(row[8])
            self.PAN.set(row[9])
            self.Aadhaar.set(row[10])
            self.Loan.set(row[11])
            self.Contact.set(row[12])
            self.Email.set(row[13])
            self.AccountType.set(row[14])
            self.Occupation.set(row[15])

# =================================================================
    def update_data(self):
        if self.AccountNo.get() == "":
            messagebox.showerror("Error", "Please select a record to update")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="1234",
                database="bank"
            )
            my_cursor = conn.cursor()

            my_cursor.execute("""
                UPDATE cus_details SET
                    Branch=%s,
                    First_Name=%s,
                    Last_Name=%s,
                    Age=%s,
                    Address=%s,
                    City=%s,
                    State=%s,
                    Country=%s,
                    PAN_No=%s,
                    Aadhaar_No=%s,
                    Loan=%s,
                    Contact_No=%s,
                    EMail=%s,
                    Account_Type=%s,
                    Occupation=%s
                WHERE Account_No=%s
            """, (
                self.Branch.get(),
                self.FirstName.get(),
                self.LastName.get(),
                self.Age.get(),
                self.Address.get(),
                self.City.get(),
                self.State.get(),
                self.Country.get(),
                self.PAN.get(),
                self.Aadhaar.get(),
                self.Loan.get(),
                self.Contact.get(),
                self.Email.get(),
                self.AccountType.get(),
                self.Occupation.get(),
                self.AccountNo.get()
            ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record updated successfully")

        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

    def iExit(self):
        iExit = messagebox.askyesno("Exit", "Do you really want to exit?")
        if iExit > 0:
            self.root.destroy()


    def reset_data(self):
        for var in [self.Branch, self.AccountNo, self.FirstName, self.LastName, self.Age, self.Address, self.City,
                    self.State, self.Country, self.PAN, self.Aadhaar, self.Loan, self.Contact, self.Email,
                    self.AccountType, self.Occupation]:
            var.set("")
        self.txtDeatils.delete("1.0", END)


    def idelete(self):
        if self.AccountNo.get() == "":
            messagebox.showerror("Error", "Account Number is required to delete!")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this account?")
        if not confirm:
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="1234",
                database="bank"
            )
            my_cursor = conn.cursor()
            query = "DELETE FROM cus_details WHERE Account_No = %s"
            value = (self.AccountNo.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            conn.close()

            self.fetch_data()
            messagebox.showinfo("Deleted", "Account Holder has been deleted successfully")

        except Exception as e:
            messagebox.showerror("Error", f"Error deleting account: {str(e)}")


# =============================================================================================

root=tk.Tk()
image = Image.open(r"C:\Users\ayush\Downloads\OIP (2).jpeg")


p1 = ImageTk.PhotoImage(image)

root.iconphoto(False, p1)
ob=bank(root)
root.mainloop()        