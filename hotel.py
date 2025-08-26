from tkinter import*
from PIL import Image, ImageTk  #pip install pillow
from customer import Cust_Win
from room import Roombooking
from details import details

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel  Management System")
        self.root.geometry("1550x800+0+0")
       
       
   
#first image
        img1=Image.open(r"/Users/khanjawad/Downloads/Gemini_Generated_Image_yi5706yi5706yi57.png")
        img1=img1.resize((1550,200),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1,bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=200)

#logo
        img2=Image.open(r"/Users/khanjawad/Downloads/Gemini_Generated_Image_an280aan280aan28.png")
        img2=img2.resize((230,140),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=230, height=140)

#title
        lbl_title = Label(self.root, text="Hotel Management System", font=("times new roman", 50, "bold"), bg="white", fg="black", bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=80, width=1550, height=60)

#frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height= 620)   

#menu
        lbl_menu = Label(main_frame, text="MENU",font=("Times new roman",20,"bold"),bg="white",fg="black",bd=4,relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=225,)  
#Button frame 
        btn_frame =Frame(main_frame, bd=4,bg="white", relief=RIDGE)
        btn_frame.place(x=0, y=35, width=225, height= 150)
       
        cust_btn = Button(btn_frame, text="CUSTOMER",command =self.cust_details,width=22, font=("times new roman", 14, "bold"),bg="white", fg="black", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)
        
        room_btn=Button(btn_frame, text="ROOM",command=self.Roombooking, width=22, font=("times new roman", 14, "bold"), bg="white", fg="black", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)
        
        details_btn=Button(btn_frame, text="DETAILS",command=self.details, width=22, font=("times new roman", 14, "bold"), bg="white", fg="black", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)
        
        report_btn=Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="white", fg="black", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn=Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="white", fg="black", bd=0, cursor="hand1")
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
    root= Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()



