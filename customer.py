from tkinter import*
from PIL import Image, ImageTk  #pip install pillow 
from tkinter import ttk
import random
import mysql.connector
 # pip install mysql-connector-python
from tkinter import messagebox




class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Management")
        self.root.geometry("1200x500+240+250")
#variable
        self.var_ref = StringVar()
        x= random.randint(1000, 9999)
        self.var_ref.set(str(x))



        self.var_cust_name = StringVar()
        self.var_mother_name = StringVar()
        self.var_gender = StringVar() 
        self.var_Postcode = StringVar()
        self.var_Phone = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_nationality = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()   
        self.var_address = StringVar()     
        
     

# ttk style set
        style = ttk.Style()
        style.theme_use("default")

# Entry style
        style.configure(
        "Custom.TEntry",
        foreground="black",
        fieldbackground="white",
        font=("arial", 12, "bold")
    )

# Combobox style
        style.configure(
        "Custom.TCombobox",
        foreground="black",
        fieldbackground="white",
        selectforeground="black",
        selectbackground="white",
        font=("arial", 12, "bold")
)
 


        lbl_title = Label(self.root, text="Add Customer Details", font=("times new roman", 40, "bold"), bg="white", fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x= 0, y=0, width=1300, height=70)

    #logo
        img2=Image.open(r"/Users/khanjawad/Downloads/Gemini_Generated_Image_an280aan280aan28.png")
        img2=img2.resize((100,55),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=5, y=5, width=100, height=55)
    #Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("arial", 12, "bold"),bg="white",fg="black", padx=2)
        labelframeleft.place(x=1, y=60, width=400, height=4500)

 #labels and entries
        lbl_cust_ref = Label(labelframeleft, text="Customer Reference", font =("arial", 12, "bold"),bg="white",fg="black")
        lbl_cust_ref.grid(row=0, column=0)
        
        entry_ref = ttk.Entry(
        labelframeleft,
        textvariable=self.var_ref,
        font=("arial", 12, "bold"),
        background="white",
        foreground="black",
        state="readonly"
)

        entry_ref.grid(row=0, column=1)

#customer name
        lbl_cust_name = Label(labelframeleft, text="Customer Name", font=("arial", 12, "bold"),bg="white",fg="black")
        lbl_cust_name.grid(row=1, column=0, pady=8, padx=1, sticky=W)
        entry_cust_name = Entry(
        labelframeleft,
        textvariable=self.var_cust_name,
        font=("arial", 12, "bold"),
        bg="white",
        fg="black"
)
        

        entry_cust_name.grid(row=1, column=1)                                 
        entry_cust_name.bind("<Return>", lambda e: entry_mother_name.focus())
#mother name
        lbl_mother_name = Label(labelframeleft, text="Mother Name", font=("arial", 12, "bold"),bg="white",fg="black")
        lbl_mother_name.grid(row=2, column=0, pady=8, padx=2, sticky=W)
        entry_mother_name = ttk.Entry(labelframeleft,textvariable=self.var_mother_name, font=("arial", 12, "bold"))
        entry_mother_name.grid(row=2, column=1)
        entry_mother_name.bind("<Return>", lambda e: combo_gender.focus())

#gender combobox
        label_gender = Label(labelframeleft, font=("ariel", 12, "bold"),bg="white",fg="black" ,text="Gender:",padx=2, pady=6)    
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender, font=("arial", 12, "bold"),state="readonly", width=27)
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)
        combo_gender.bind("<Return>", lambda e: entry_postcode.focus())

 #postcode
        lbl_postcode = Label(labelframeleft, text="Postcode", font=("arial", 12, "bold"),bg="white",fg="black")
        lbl_postcode.grid(row=4, column=0, pady=8, padx=1, sticky=W)
        entry_postcode = ttk.Entry(labelframeleft,textvariable=self.var_Postcode, font=("arial", 12, "bold"))
        entry_postcode.grid(row=4, column=1)
        entry_postcode.bind("<Return>", lambda e: entry_phone.focus())

#phone
        lbl_phone = Label(labelframeleft, text="Phone", font=("arial", 12, "bold"),bg="white",fg="black")
        lbl_phone.grid(row=5, column=0, pady=8, padx=1, sticky=W)
        entry_phone = ttk.Entry(labelframeleft,textvariable=self.var_Phone, font=("arial", 12, "bold"))
        entry_phone.grid(row=5, column=1)
        entry_phone.bind("<Return>", lambda e: entry_email.focus())
#email
        lbl_email = Label(labelframeleft, text="Email", font=("arial", 12, "bold"),bg="white",fg="black")
        lbl_email.grid(row=6, column=0, pady=8, padx=1, sticky=W)
        entry_email = ttk.Entry(labelframeleft,textvariable=self.var_email, font=("arial", 12, "bold"))
        entry_email.grid(row=6, column=1)
        entry_email.bind("<Return>", lambda e: entry_address.focus())
#address
        lbl_address = Label(labelframeleft, text="Address", font=("arial", 12, "bold"),bg="white",fg="black")
        lbl_address.grid(row=7, column=0, pady=8, padx=1, sticky=W)
        entry_address = ttk.Entry(labelframeleft,textvariable=self.var_address, font=("arial", 12, "bold"))
        entry_address.grid(row=7, column=1)  
        entry_address.bind("<Return>", lambda e: combo_Nationality.focus())

#nationality
        lblNationality = Label(labelframeleft, text="Nationality", font=("arial", 12, "bold"),bg="white",fg="black")
        lblNationality.grid(row=8, column=0, pady=8, padx=1, sticky=W)
        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=("arial", 12, "bold"),state="readonly", width=27)
        combo_Nationality["value"]=("Pakistan","India","America","England","Other")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=8, column=1)
        entry_address.bind("<Return>", lambda e: combo_id.focus())                       

#id proof
        lbl_id_proof = Label(labelframeleft, text="ID Proof", font=("arial", 12, "bold"),bg="white",fg="black")
        lbl_id_proof.grid(row=9, column=0, pady=10, padx=2, sticky=W)
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof, font=("arial", 12, "bold"),state="readonly", width=27)
        combo_id["value"]=("AdharCard","DrivingLicense","Passport","Other")
        combo_id.current(0)
        combo_id.grid(row=9, column=1)
        entry_address.bind("<Return>", lambda e: entry_id_number.focus())

#id number
        lbl_id_number = Label(labelframeleft, text="ID Number", font=("tarial", 12, "bold"),bg="white",fg="black")
        lbl_id_number.grid(row=10, column=0, pady=10, padx=2, sticky=W)
        entry_id_number = ttk.Entry(labelframeleft,textvariable=self.var_id_number, font=("arial", 12, "bold"))
        entry_id_number.grid(row=10, column=1)      
        entry_id_number.bind("<Return>", lambda e: entry_cust_name.focus())  # wapas first field pe


#buttons
        btn_frame = Frame(labelframeleft, bd=1, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=390, width=412, height=40)


        btnAdd=Button(btn_frame,text="Add",command=self.add_data , font=("arial", 12, "bold"), bg="white", fg="black", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate=Button(btn_frame, text="Update",command=self.update_data, font=("arial", 12, "bold"), bg="white", fg="black", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete=Button(btn_frame, text="Delete",command=self.delete_data, font=("arial", 12, "bold"), bg="white", fg="black", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset=Button(btn_frame, text="Reset",command=self.reset_data, font=("arial", 12, "bold"), bg="white", fg="black", width=9)
        btnReset.grid(row=0, column=3, padx=1)




#table frame
        table_frame=LabelFrame(self.root, bd=1, relief=RIDGE, text="View Details and Search System", font=("arial", 12, "bold"),bg="white", padx=2)
        table_frame.place(x=405, y=60, width=880, height=450)

        lblSearchBy = Label(table_frame, text="Search By:", font=("arial", 12, "bold"), bg="black", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)
        
        self.search_var = StringVar()
        combo_Search=ttk.Combobox(table_frame,textvariable=self.search_var, font=("arial", 12, "bold"),state="readonly", width=15)
        combo_Search["value"]=("Phone","reference","Name")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        entry_Search = ttk.Entry(table_frame,textvariable=self.txt_search, font=("arial", 12, "bold"), width=20)
        entry_Search.grid(row=0, column=2, padx=2)

        btnSearch=Button(table_frame, text="Search",command=self.search_data, font=("arial", 12, "bold"), bg="white", fg="black", width=9)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll=Button(table_frame, text="Show All",command=self.fetch_data, font=("arial", 12, "bold"), bg="white", fg="black", width=9)
        btnShowAll.grid(row=0, column=4, padx=1)

# show data table
        details_table=Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x=ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table, columns=("reference","name","motherName","gender","postCode","phone","email","nationality","idProof","idNumber","address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("reference", text="Refer No")
        self.cust_details_table.heading("name", text="Name")
        self.cust_details_table.heading("motherName", text="Mother Name")
        self.cust_details_table.heading("gender", text="Gender")
        self.cust_details_table.heading ("postCode", text="Post Code")    
        self.cust_details_table.heading("phone", text="Phone")
        self.cust_details_table.heading("email", text="Email")
        self.cust_details_table.heading("nationality", text="Nationality")
        self.cust_details_table.heading("idProof", text="ID Proof")
        self.cust_details_table.heading("idNumber", text="ID Number")
        self.cust_details_table.heading("address", text="Address")
        
        self.cust_details_table["show"]="headings"
        self.cust_details_table.column("reference", width=100)
        self.cust_details_table.column("name", width=100)
        self.cust_details_table.column("motherName", width=100)
        self.cust_details_table.column("gender", width=100)
        self.cust_details_table.column("postCode", width=100)
        self.cust_details_table.column("phone", width=100)
        self.cust_details_table.column("email", width=100)
        self.cust_details_table.column("nationality", width=100)
        self.cust_details_table.column("idProof", width=100)
        self.cust_details_table.column("idNumber", width=100)
        self.cust_details_table.column("address", width=150)
        


        self.cust_details_table.pack(fill=BOTH, expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>", self.get_cursor)  # Bind the click event to get_cursor method
        self.cust_details_table["selectmode"]="browse"  # Set selection mode to browse  
        self.fetch_data()  # Fetch data to populate the table initially

    def add_data(self):
        if self.var_Phone.get()=="" or self.var_mother_name.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_ref.get(),
                                                                                                        self.var_cust_name.get(),
                                                                                                        self.var_mother_name.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_Postcode.get(),
                                                                                                        self.var_Phone.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_nationality.get(),
                                                                                                        self.var_id_proof.get(),
                                                                                                        self.var_id_number.get(),
                                                                                                        self.var_address.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()               
                messagebox.showinfo("Success","Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)  


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]
        if row and len(row) > 0:  # Ensure row is not empty
            self.var_ref.set(row[0])
            self.var_cust_name.set(row[1])
            self.var_mother_name.set(row[2])
            self.var_gender.set(row[3])
            self.var_Postcode.set(row[4])
            self.var_Phone.set(row[5])
            self.var_email.set(row[6])
            self.var_nationality.set(row[7])
            self.var_id_proof.set(row[8])
            self.var_id_number.set(row[9])
            self.var_address.set(row[10])
        else:
            # Handle the case where no row is selected or row is empty
            print("No row selected or row is empty in get_cursor method.")





    def update_data(self):
        if self.var_Phone.get()=="" or self.var_mother_name.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
                my_cursor=conn.cursor()
                my_cursor.execute("update customer set Name=%s, MotherName=%s, Gender=%s, PostCode=%s, Phone=%s, Email=%s, Nationality=%s, IDProof=%s, IDNumber=%s, Address=%s where Reference=%s",(
                                                                                                        self.var_cust_name.get(),
                                                                                                        self.var_mother_name.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_Postcode.get(),
                                                                                                        self.var_Phone.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_nationality.get(),
                                                                                                        self.var_id_proof.get(),
                                                                                                        self.var_id_number.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_ref.get()
                ))                                                                                              
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been updated", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)
    

    def delete_data(self):
        delete=messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
            my_cursor=conn.cursor()
            query="delete from customer where Reference=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        # Generate a new random reference number
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name.set("")
        self.var_mother_name.set("")
        #self.var_gender.set("")
        self.var_Postcode.set("")
        self.var_Phone.set("")
        self.var_email.set("")
        #self.var_nationality.set("")
        #self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")
          
        x= random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
        my_cursor=conn.cursor()
        # build query safely
        query = "SELECT * FROM customer WHERE `" + str(self.search_var.get()) + "` LIKE %s"
        value = ("%" + str(self.txt_search.get()) + "%",)      
        my_cursor.execute(query, value)
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()





if __name__ == "__main__":
        root=Tk()
        obj=Cust_Win(root)
        root.mainloop()