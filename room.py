from tkinter import*
from PIL import Image, ImageTk  #pip install pillow 
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
 # pip install mysql-connector-python
from tkinter import messagebox
from tkcalendar import DateEntry


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Management")
        self.root.geometry("1200x500+240+250")
    #variable
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_subtotal=StringVar()
        self.var_totalcost=StringVar()

    #title    
        lbl_title = Label(self.root, text="RoomBooking Details", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x= 0, y=0, width=1300, height=70)

    #logo
        img2=Image.open(r"/Users/khanjawad/Downloads/Gemini_Generated_Image_an280aan280aan28.png")
        img2=img2.resize((100,50),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=5, y=5, width=100, height=50)

         #Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="RoomBooking Details", font=("arial", 12, "bold"), padx=2, )
        labelframeleft.place(x=1, y=60, width=400, height=400)
    
     #labels and entries
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact", font =("arial", 12, "bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact, font=("arial", 12, "bold"),width=20)
        entry_contact.grid(row=0, column=1, sticky=W)
        entry_contact.bind("<Return>", lambda e: txtcheck_in_data.focus_set())


     #fetch data button
        btnFetchData=Button(labelframeleft,command=self.fetch_customer_details, text="Fetch Data", font=("arial", 8, "bold"), bg="black", fg="gold", width=8)
        btnFetchData.place(x=280, y=2)  
      #check in data
        check_in_data= Label(labelframeleft, text="Check In Data", font =("arial", 12, "bold"),padx=2,pady=6)
        check_in_data.grid(row=1, column=0, sticky=W)
        # Check-in calendar
        txtcheck_in_data = DateEntry(
        labelframeleft,
        textvariable=self.var_checkin,
        font=("arial", 12, "bold"),
        width=27,
        background="darkblue",
        foreground="white",
        date_pattern="dd/mm/yyyy"  # match your bill function format
            )
        txtcheck_in_data.grid(row=1, column=1)
        txtcheck_in_data.bind("<Return>", lambda e: txtcheck_out_data.focus_set())

        #check out data
        lbl_check_out_data = Label(labelframeleft, text="Check Out Data", font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_check_out_data.grid(row=2, column=0, sticky=W)
        # Check-out calendar
        txtcheck_out_data = DateEntry(
        labelframeleft,
        textvariable=self.var_checkout,
        font=("arial", 12, "bold"),
        width=27,
        background="darkblue",
        foreground="white",
        date_pattern="dd/mm/yyyy"
        )
        txtcheck_out_data.grid(row=2, column=1)
        txtcheck_out_data.bind("<Return>", lambda e: combo_room_type.focus_set())
        #room type
        lbl_room_type = Label(labelframeleft, text="Room Type", font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_room_type.grid(row=3, column=0, sticky=W)
        
        conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()
        combo_room_type = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=("arial", 12, "bold"), state="readonly", width=17)
        combo_room_type["value"] = ide
        combo_room_type.current(0)
        combo_room_type.grid(row=3, column=1)
        combo_room_type.bind("<Return>", lambda e: combo_RoomNo.focus_set())
        #room available
        lbl_room_available = Label(labelframeleft, text="Room Available", font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_room_available.grid(row=4, column=0, sticky=W)
        #txtroom_available = ttk.Entry(labelframeleft,textvariable=self.var_roomavailable, font=("arial", 12, "bold"),width=29)
        #txtroom_available.grid(row=4, column=1)
        #create database
        
        conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()
        

        combo_RoomNo= ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable, font=("arial", 12, "bold"), state="readonly", width=17)
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)
        combo_RoomNo.bind("<Return>", lambda e: txtMeal_plan.focus_set())
       
        #Meal Plan
        lbl_meal_plan = Label(labelframeleft, text="Meal Plan", font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_meal_plan.grid(row=5, column=0, sticky=W)
        txtMeal_plan = ttk.Entry(labelframeleft,textvariable=self.var_meal, font=("arial", 12, "bold"), width=29)
        txtMeal_plan.grid(row=5, column=1)
        txtMeal_plan.bind("<Return>", lambda e: txtno_of_days.focus_set())

        #no of days
        lbl_no_of_days = Label(labelframeleft, text="No of Days", font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_no_of_days.grid(row=6, column=0, sticky=W)
        txtno_of_days = ttk.Entry(labelframeleft,textvariable=self.var_noofdays, font=("arial", 12, "bold"),width=29)
        txtno_of_days.grid(row=6, column=1)
        txtno_of_days.bind("<Return>", lambda e: txtpaid_tax.focus_set())
        #paid tax
        lbl_paid_tax = Label(labelframeleft, text="Paid Tax", font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_paid_tax.grid(row=7, column=0, sticky=W)
        txtpaid_tax = ttk.Entry(labelframeleft,textvariable=self.var_paidtax, font=("arial", 12, "bold"), width=29)
        txtpaid_tax.grid(row=7, column=1)
        txtpaid_tax.bind("<Return>", lambda e: txtsub_total.focus_set())
        #sub total
        lbl_sub_total = Label(labelframeleft, text="Sub Total", font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_sub_total.grid(row=8, column=0, sticky=W)
        txtsub_total = ttk.Entry(labelframeleft,textvariable=self.var_subtotal, font=("arial", 12, "bold"), width=29)
        txtsub_total.grid(row=8, column=1)
        txtsub_total.bind("<Return>", lambda e: txttotal_cost.focus_set())
        #total cost
        lbl_total_cost = Label(labelframeleft, text="Total Cost", font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_total_cost.grid(row=9, column=0, sticky=W)
        txttotal_cost = ttk.Entry(labelframeleft,textvariable=self.var_totalcost, font=("arial", 12, "bold"), width=29)
        txttotal_cost.grid(row=9, column=1)
        txttotal_cost.bind("<Return>", lambda e: btnBill.focus_set())
   #bill botton
        btnBill=Button(labelframeleft, text="Bill",command=self.total, font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

   # buttons
        btn_frame = Frame(labelframeleft, bd=1, relief=RIDGE)
        btn_frame.grid(row=11, column=0, columnspan=5, pady=20)

        btnAdd = Button(btn_frame, text="Add",comman=self.add_data, font=("arial", 12, "bold"),
                        bg="black", fg="gold", width=8)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.update, font=("arial", 12, "bold"),
                           bg="black", fg="gold", width=8)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.delete, font=("arial", 12, "bold"),
                           bg="black", fg="gold", width=8)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("arial", 12, "bold"),
                          bg="black", fg="gold", width=8)
        btnReset.grid(row=0, column=3, padx=1)
        

        #right side image
        img3=Image.open(r"/Users/khanjawad/Downloads/Gemini_Generated_Image_e7aj3e7aj3e7aj3e.png")
        img3=img3.resize((520,300),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg= Label(self.root, image=self.photoimg3,bd=4, relief=RIDGE)
        lblimg.place(x=740, y=70, width=520, height=250)
     #table frame search 
        table_frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("arial", 12, "bold"), padx=2)
        table_frame.place(x=400, y=250, width=860, height=500)

        lblSearchBy = Label(table_frame, text="Search By:", font=("arial", 12, "bold"), bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W)
        
        self.search_var = StringVar()
        combo_Search=ttk.Combobox(table_frame,textvariable=self.search_var, font=("arial", 12, "bold"),state="readonly", width=15)
        combo_Search["value"]=("contact","roomavailable")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        entry_Search = ttk.Entry(table_frame,textvariable=self.txt_search, font=("arial", 12, "bold"), width=20)
        entry_Search.grid(row=0, column=2, padx=2)

        btnSearch=Button(table_frame, text="Search",command=self.search, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll=Button(table_frame, text="Show All",command=self.fetch_all_rooms, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnShowAll.grid(row=0, column=4, padx=1)

        # show data table
        details_table=Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=150)

        scroll_x=ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table, columns=("Contact","checkin","checkout","roomtype","roomavailable","meal","days"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact", text="Contact no")
        self.room_table.heading("checkin", text="checkin")
        self.room_table.heading("checkout", text="checkout")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading ("roomavailable", text="roomavailable")    
        self.room_table.heading("meal", text="meal")
        self.room_table.heading("days", text="days")
        
        
        
        self.room_table["show"]="headings"
        
        self.room_table.column("Contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("days", width=100)
       
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_all_rooms()
    
    #add function
    
    def add_data(self):
        if self.var_roomavailable.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.var_contact.get(),
                                                                                                        self.var_checkin.get(),
                                                                                                        self.var_checkout.get(),
                                                                                                        self.var_roomtype.get(),
                                                                                                        self.var_roomavailable.get(),
                                                                                                        self.var_meal.get(),
                                                                                                        self.var_noofdays.get()
                                                                                                        
                                                                                                        
                                                                                                    ))
                conn.commit()
                self.fetch_all_rooms()
                conn.close()               
            except mysql.connector.IntegrityError:
                messagebox.showerror("Error", f"Room {self.var_roomavailable.get()} already exists!", parent=self.root)
                messagebox.showinfo("Success","Room Booked.", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)  


    def fetch_all_rooms(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

#get cursor
    def get_cursor(self, event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
    
   #update function
    def update(self):
        if self.var_roomavailable.get()=="":
            messagebox.showerror("Error","Please enter room number",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
                my_cursor=conn.cursor()
                my_cursor.execute("update room SET checkin=%s, checkout=%s, roomtype=%s, contact=%s, meal=%s, noofdays=%s WHERE roomavailable=%s",(
                                                                                                        self.var_checkin.get(),
                                                                                                        self.var_checkout.get(),
                                                                                                        self.var_roomtype.get(),
                                                                                                        self.var_contact.get(),
                                                                                                        self.var_meal.get(),
                                                                                                        self.var_noofdays.get(),
                                                                                                        self.var_roomavailable.get(),
                                                                                                    ))
            
                print("Rows affected:", my_cursor.rowcount)

                conn.commit()
                self.fetch_all_rooms()
                conn.close()               
                messagebox.showinfo("Update","Room details has been updated.", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)


    def delete(self):
        if self.var_roomavailable.get()=="":
            messagebox.showerror("Error","Please enter room number",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer?", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
                    my_cursor=conn.cursor()
                    sql="delete from room where roomavailable=%s"
                    val=(self.var_roomavailable.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_all_rooms()
                conn.close()               
                messagebox.showinfo("Delete","Customer has been deleted.", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)  
 #reset function
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_subtotal.set(""),
        self.var_totalcost.set("")

        x= random.randint(1000, 9999)
        self.var_roomavailable.set(str(x))

#all customer fetch data
    
    
    def fetch_customer_details(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
            my_cursor=conn.cursor()
            query=("select Name from customer where Phone =%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showDataframe=Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=410, y=70, width=300, height=180)
                lblname=Label(showDataframe, text="Name:", font=("arial", 12, "bold"))
                lblname.place(x=0, y=0)
                lbl=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                
            #Gender
                conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Phone =%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


                lblGender=Label(showDataframe, text="Gender:", font=("arial", 12, "bold"))
                lblGender.place(x=0, y=20)
                lbl2=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=20)

            #email
                conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
                my_cursor=conn.cursor()
                query=("select Email from customer where Phone =%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()    
                lblEmail=Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
                lblEmail.place(x=0, y=40)
                lbl3=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl3.place(x=90, y=40)
            #nationality
                conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Phone =%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblNationality=Label(showDataframe, text="nationality", font=("arial", 12, "bold"))
                lblNationality.place(x=0, y=60)
                lbl4=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl4.place(x=90, y=60)    
            #address
                conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
                my_cursor=conn.cursor()
                query=("select Address from customer where Phone =%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                lblAddress=Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
                lblAddress.place(x=0, y=90)
                lbl5=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl5.place(x=90, y=90)
   
   #search system
    def search(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()



   
   
   
   #bill button function 
 

    def total(self):
    # Get dates
        inDate = datetime.strptime(self.var_checkin.get(), "%d/%m/%Y")
        outDate = datetime.strptime(self.var_checkout.get(), "%d/%m/%Y")
        no_of_days = abs((outDate - inDate).days)
        self.var_noofdays.set(no_of_days)

    # Define prices
        room_prices = {"Single": 700, "Double": 1200, "Deluxe": 2000}
        meal_prices = {"Breakfast": 300, "Lunch": 500, "Dinner": 700}

        room_type = self.var_roomtype.get()
        meal_type = self.var_meal.get()

    # Ensure the selected options exist
        room_price = room_prices.get(room_type, 0)
        meal_price = meal_prices.get(meal_type, 0)

    # Calculate bill
        subtotal = no_of_days * (room_price + meal_price)
        tax = subtotal * 0.09
        total_cost = subtotal + tax

        # Update GUI variables
        self.var_subtotal.set(f"Rs.{subtotal:.2f}")
        self.var_paidtax.set(f"Rs.{tax:.2f}")
        self.var_totalcost.set(f"Rs.{total_cost:.2f}")

 

if __name__ == "__main__":
        root=Tk()
        obj=Roombooking(root)
        root.mainloop()