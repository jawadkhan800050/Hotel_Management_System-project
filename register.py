from tkinter import*
from PIL import Image, ImageTk  #pip install pillow 
from tkinter import ttk
import mysql.connector
 # pip install mysql-connector-python
from tkinter import messagebox



class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()
        self.var_role = StringVar(value="Customer")



        #background image
        self.bg=PhotoImage(file=r"/Users/khanjawad/Downloads/Gemini_Generated_Image_qfcj2jqfcj2jqfcj (1).png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

    #left image
      #  self.bg1=PhotoImage(file=r"/Users/khanjawad/Downloads/Gemini_Generated_Image_b82mm5b82mm5b82m.png")
      #  left_lbl=Label(self.root,image=self.bg1)
       # left_lbl.place(x=50,y=100,width=970,height=750)
        
  #      #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=100,width=700,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="black",bg="white")
        register_lbl.place(x=20,y=20)
        #labels and entries
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        fname.place(x=50,y=100)
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)
        self.fname_entry.bind("<Return>", lambda e: self.lname_entry.focus_set())

        #last name
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        lname.place(x=370,y=100)
        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.lname_entry.place(x=370,y=130,width=250)
        self.lname_entry.bind("<Return>", lambda e: self.contact_entry.focus_set())

        #contact
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)
        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contact_entry.place(x=50,y=200,width=250)  
        self.contact_entry.bind("<Return>", lambda e: self.txt_email.focus_set())
        #email
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        self.txt_email.bind("<Return>", lambda e: self.combo_security_Q.focus_set())
       
        #security question
        question=Label(frame,text="Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
        question.place(x=50,y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman",15,"bold"), state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.bind("<Return>", lambda e: self.answer_entry.focus_set())
        #security answer
        answer=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        answer.place(x=370,y=240)
        self.answer_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.answer_entry.place(x=370,y=270,width=250)
        self.answer_entry.bind("<Return>", lambda e: self.password_entry.focus_set())  
        #password
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=50,y=310)
        self.password_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.password_entry.place(x=50,y=340,width=250)
        self.password_entry.bind("<Return>", lambda e: self.cpassword_entry.focus_set())  
        #confirm password
        cpassword=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        cpassword.place(x=370,y=310)
        self.cpassword_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.cpassword_entry.place(x=370,y=340,width=250)
        self.cpassword_entry.bind("<Return>", lambda e: self.checkbtn.focus_set())
        #check button
        checkbtn=Checkbutton(frame, variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),fg="black",bg="white")
        checkbtn.place(x=50,y=380)
        
        #buttons
        img=Image.open(r"/Users/khanjawad/Desktop/images.jpeg")
        img=img.resize((300,90),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=15,y=430,width=300)

        img1=Image.open(r"/Users/khanjawad/Desktop/download (2).jpeg")
        img1=img1.resize((250,90),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=370,y=430,width=300)

#function declaration
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms & conditions", parent=self.root)
        else:
            try:
            # Connect to the database
                conn = mysql.connector.connect(host="localhost", username="root", password="Peshoo@5979", database="Hotel_Management_System")
                my_cursor = conn.cursor()

            # Check if the email already exists
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
            
                if row != None:
                    messagebox.showerror("Error", "User already exists, please try another email", parent=self.root)
                else:
                # Insert the new data
                    my_cursor.execute("INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                conn.commit()
                messagebox.showinfo("Success", "Register Successful", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)
            finally:
                conn.close()











if __name__ == "__main__":
        root=Tk()
        obj=Register(root)
        root.mainloop()