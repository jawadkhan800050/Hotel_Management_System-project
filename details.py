from tkinter import*
from PIL import Image, ImageTk  #pip install pillow 
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
 # pip install mysql-connector-python
from tkinter import messagebox


class details:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Management")
        self.root.geometry("1200x500+240+250")
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
#title
        lbl_title = Label(self.root, text="RoomBooking Details", font=("times new roman", 40, "bold"), bg="white", fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x= 0, y=0, width=1300, height=70)

    #logo
        img2=Image.open(r"/Users/khanjawad/Downloads/Gemini_Generated_Image_an280aan280aan28.png")
        img2=img2.resize((90,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=5, y=5, width=90, height=45)

         #Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=("arial", 12, "bold"),bg="white",fg="black", padx=2, )
        labelframeleft.place(x=1, y=60, width=365, height=300)


        #floor
        lbl_floor = Label(labelframeleft, text="Floor", font =("arial", 12, "bold"),bg="white",fg="black",padx=2,pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)
        
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft, textvariable=self.var_floor, font=("arial", 12, "bold"),width=20)
        entry_floor.grid(row=0, column=1, sticky=W)


        #room available
        lbl_roomno = Label(labelframeleft, text="Room No", font =("arial", 12, "bold"),bg="white",fg="black",padx=2,pady=6)
        lbl_roomno.grid(row=1, column=0, sticky=W)  
       
        self.var_roomno=StringVar()
        entry_room_available=ttk.Entry(labelframeleft,textvariable=self.var_roomno, font=("arial", 12, "bold"),width=20)
        entry_room_available.grid(row=1, column=1, sticky=W)

        #room type
        self.var_roomtype=StringVar()
        lbl_room_type = Label(labelframeleft, text="Room Type", font =("arial", 12, "bold"),bg="white",fg="black",padx=2,pady=6)  
        lbl_room_type.grid(row=3, column=0, sticky=W)
        
        self.var_roomtype=StringVar()
        entry_roomtype=ttk.Entry(labelframeleft,textvariable=self.var_roomtype, font=("arial", 12, "bold"),width=20)
        entry_roomtype.grid(row=3, column=1, sticky=W)


#button 
        btn_frame =Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=250, width=355, height=30)

        btnAdd=Button(btn_frame, text="Add",command=self.add_data, font=("arial", 8, "bold"),bg="white",fg="black", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate=Button(btn_frame, text="Update",command=self.update, font=("arial", 8, "bold"),bg="white",fg="black", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete=Button(btn_frame, text="Delete",command=self.delete, font=("arial", 8, "bold"),bg="white",fg="black", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset=Button(btn_frame, text="Reset",command=self.reset, font=("arial", 8, "bold"),bg="white",fg="black", width=9)
        btnReset.grid(row=0, column=3, padx=1)

#table frame search style
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE,bg="white",fg="black",text="Show Room Details", font=("arial", 12, "bold"), padx=2)
        table_frame.place(x=500, y=60, width=400, height=300)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.room_table=ttk.Treeview(table_frame, column=("floor","roomno","roomtype"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table["show"]="headings"
        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
    #add data
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomno.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                            self.var_floor.get(),
                                                                            self.var_roomno.get(),
                                                                            self.var_roomtype.get()
                                                                            
                                                                            
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added sucsessfuly", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}", parent=self.root)     

    #fetch details data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END, values=i)
            conn.commit()
        conn.close()
    #get cursor
    def get_cursor(self, event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])
        
    #update function
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter Floor No", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s, roomtype=%s where roomno=%s",(
                                                                                        
                                                                                        self.var_floor.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomno.get()
                                                                                        
                                                                                        
                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully", parent=self.root)

        #delete function
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer", parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
            my_cursor=conn.cursor()
            query="delete from details where roomno=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    #reset function
    def reset(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("")

        x= random.randint(1000, 9999)
        self.var_roomno.set(str(x))
     
if __name__ == "__main__":
        root=Tk()
        obj=details(root)
        root.mainloop()