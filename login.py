from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk  #pip install pillow
from tkinter import messagebox
from customer import Cust_Win
from room import Roombooking
from details import details
import mysql.connector

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        #background image
        self.bg=PhotoImage(file=r"/Users/khanjawad/Downloads/Gemini_Generated_Image_iaggm2iaggm2iagg.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)    

        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"/Users/khanjawad/Downloads/ChatGPT Image Aug 24, 2025, 04_07_46 PM.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100) 

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="#070707",bg="white")
        get_str.place(x=120,y=100)

        #label
        lbl_username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="white")
        lbl_username.place(x=70,y=155)
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        #password
        lbl_password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        lbl_password.place(x=70,y=225)
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)

        #login button
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="#070707",activeforeground="white",activebackground="#070707")
        loginbtn.place(x=110,y=300,width=120,height=35) 
    
         
       
        #icons
        img2=Image.open(r"/Users/khanjawad/Desktop/usernameicon.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"/Users/khanjawad/Desktop/passwordicon.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="white",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)
        
        #login button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="#070707",activeforeground="white",activebackground="#070707")
        loginbtn.place(x=110,y=300,width=120,height=35) 

        #register button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="#070707")
        registerbtn.place(x=15,y=350,width=100) 

        #forgot password button
        forgotbtn=Button(frame,text="Forgot Password",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activeforeground="white",activebackground="#070707")
        forgotbtn.place(x=200,y=350,width=100)

    def register_window(self):
            self.new_window=Toplevel(self.root)
            self.app=Register(self.new_window)



        #login function
    def login(self):
            if self.txtuser.get()=="" or self.txtpass.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            elif self.txtuser.get()=="kapil" and self.txtpass.get()=="12345":
                messagebox.showinfo("Success","Welcome to Hotel Management System",parent=self.root)
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Peshoo@5979",database="Hotel_Management_System")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                                        self.txtuser.get(),
                                                                                                        self.txtpass.get()
                                                                                                    ))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username & Password",parent=self.root)
                else:
                    open_main=messagebox.askyesno("YesNo","Access only Admin",parent=self.root)
                    if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=HotelManagementSystem(self.new_window)
                    else:
                        if not open_main:
                            return
                conn.commit()
                conn.close()        

    def forget_password(self):
            if self.txtuser.get()=="":
                messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Peshoo@5979",database="Hotel_Management_System")
                my_cursor=conn.cursor()
                query=("select * from register where email=%s")
                value=(self.txtuser.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid username",parent=self.root)
                else:
                    conn.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("340x450+610+170")

                    l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="#070707",bg="white")
                    l.place(x=0,y=10,relwidth=1)

                    security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
                    security_Q.place(x=50,y=80)

                    self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                    self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
                    self.combo_security_Q.current(0)
                    self.combo_security_Q.place(x=50,y=110,width=250)

                    security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
                    security_A.place(x=50,y=150)

                    self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                    self.txt_security.place(x=50,y=180,width=250)

                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black",bg="white")
                    new_password.place(x=50,y=220)

                    self.txt_new_password=ttk.Entry(self.root2,font=("times new roman",15))
                    self.txt_new_password.place(x=50,y=250,width=250)

                    btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="#070707",activeforeground="white",activebackground="#070707")




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
        
        #last name
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        lname.place(x=370,y=100)
        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.lname_entry.place(x=370,y=130,width=250)

        #contact
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)
        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contact_entry.place(x=50,y=200,width=250)  

        #email
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
       
       
        #security question
        question=Label(frame,text="Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
        question.place(x=50,y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman",15,"bold"), state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)
        #security answer
        answer=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        answer.place(x=370,y=240)
        self.answer_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.answer_entry.place(x=370,y=270,width=250)  
        #password
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=50,y=310)
        self.password_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.password_entry.place(x=50,y=340,width=250)  
        #confirm password
        cpassword=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        cpassword.place(x=370,y=310)
        self.cpassword_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.cpassword_entry.place(x=370,y=340,width=250)
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



class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel  Management System")
        self.root.geometry("1550x800+0+0")
       
       
   
#first image
        img1=Image.open(r"/Users/khanjawad/Desktop/pic1.jpeg")
        img1=img1.resize((1550,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1,bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=200)

#logo
        img2=Image.open(r"/Users/khanjawad/Desktop/logo.webp")
        img2=img2.resize((230,140),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=230, height=140)

#title
        lbl_title = Label(self.root, text="Hotel Management System", font=("times new roman", 50, "bold"), bg="Black", fg="Gold", bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=60)

#frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height= 620)   

#menu
        lbl_menu = Label(main_frame, text="MENU",font=("Times new roman",20,"bold"),bg="Black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=225,)  
#Button frame 
        btn_frame =Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=225, height= 150)
       
        cust_btn = Button(btn_frame, text="CUSTOMER",command =self.cust_details,width=22, font=("times new roman", 14, "bold"),bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)
        
        room_btn=Button(btn_frame, text="ROOM",command=self.Roombooking, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)
        
        details_btn=Button(btn_frame, text="DETAILS",command=self.details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)
        
        report_btn=Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn=Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

#right side image
        img3 = Image.open(r"/Users/khanjawad/Desktop/pic3.jpeg")
        img3 = img3.resize((1320, 590), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=230, y=0, width=1320, height=590)

#down image
        img4 = Image.open(r"/Users/khanjawad/Desktop/pic4.jpeg")
        img4 = img4.resize((230, 210), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(self.root, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=380, width=230, height=210)


        img5 = Image.open(r"/Users/khanjawad/Desktop/pic5.jpeg")
        img5 = img5.resize((230, 190), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg5 = Label(self.root, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=590, width=229, height=190)
        

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)    

    def Roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)    
    def details(self):
        self.new_window = Toplevel(self.root)
        self.app = details(self.new_window)

if __name__ == "__main__":
    main()