from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from login import Login_Window

class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")  # width x height + x_axis + y_axis
        self.root.title("Face Recognition System")
        
    # ======== variables ========
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_Q = StringVar()
        self.var_security_A = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        
        
    
    # ===== Full Screen Background image =====
        img1 = Image.open(r"college_images\login_bg_img.jpeg")
        img1 = img1.resize((1550, 800))

        self.bg = ImageTk.PhotoImage(img1)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=1550, height=800)


        # ===== left Side Image =====
        self.bg1 = ImageTk.PhotoImage(file=r"college_images\login_bg_img2.png")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)
        
    # ====== Register Frame ========
        register_frame = Frame(self.root, bg="white")
        register_frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(register_frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="darkgreen")
        register_lbl.place(x=20, y=20)

    # ====== Label and Entry ======
         
         # ------------ row 1
        fname_label = Label(register_frame, text="First Name:", font=("times new roman", 15, "bold"), bg="white")
        fname_label.place(x=50, y=100)
        
        self.fname_entry = ttk.Entry(register_frame,textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=300)
        
        lname_label = Label(register_frame, text="Last Name:", font=("times new roman", 15, "bold"), bg="white")
        lname_label.place(x=400, y=100)
        
        self.lname_entry = ttk.Entry(register_frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.lname_entry.place(x=400, y=130, width=300)
        
        # ------------ row 2
        
        contact_label = Label(register_frame, text="Contact No:", font=("times new roman", 15, "bold"), bg="white")
        contact_label.place(x=50, y=200)
        self.contact_entry = ttk.Entry(register_frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.contact_entry.place(x=50, y=230, width=300)
        email_label = Label(register_frame, text="Email:", font=("times new roman", 15, "bold"), bg="white")
        email_label.place(x=400, y=200)
        self.email_entry = ttk.Entry(register_frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.email_entry.place(x=400, y=230, width=300)
        
    # --------- row 3
        security_Q = Label(register_frame, text="Select Security Question:", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=300)
        
        self.combo_security_Q = ttk.Combobox(register_frame, font=("times new roman", 15,), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Best Friend Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50, y=330, width=300)
        
        
        security_A = Label(register_frame, text="Security Answer:", font=("times new roman", 15, "bold"), bg="white",fg="black")
        security_A.place(x=400, y=300)
        
        self.security_A_entry = ttk.Entry(register_frame,textvariable=self.var_security_A, font=("times new roman", 15, "bold"))
        self.security_A_entry.place(x=400, y=330, width=300)
        
    # --------- row 4
        password_label = Label(register_frame, text="Password:", font=("times new roman", 15, "bold"), bg="white")
        password_label.place(x=50, y=400)
        
        self.password_entry = ttk.Entry(register_frame,textvariable=self.var_password, font=("times new roman", 15, "bold"), show="*")
        self.password_entry.place(x=50, y=430, width=300)
        
        confirm_password_label = Label(register_frame, text="Confirm Password:", font=("times new roman", 15, "bold"), bg="white",fg="black")
        confirm_password_label.place(x=400, y=400)
        
        self.confirm_password_entry = ttk.Entry(register_frame,textvariable=self.var_confirm_password, font=("times new roman", 15, "bold"), show="*")
        self.confirm_password_entry.place(x=400, y=430, width=300)
        

        
# =========== Register Button ============
        register_button = Button(register_frame, text="Register", font=("times new roman", 15, "bold"), fg="white", bg="green", cursor="hand2", command=self.register_data)
        register_button.place(x=90, y=480, width=200)
        
        login_button = Button(register_frame, text="Already Registered? Login", font=("times new roman", 10, "bold"), fg="white", bg="red", cursor="hand2", command=self.login)
        login_button.place(x=450, y=490, width=200)
        
        
 # =================== Function Declaration         ==================
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_security_Q.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_password.get() != self.var_confirm_password.get():
            messagebox.showerror("Error", "Password and Confirm Password must be same")
        elif self.var_security_Q.get() == "Select":
            messagebox.showerror("Error", "Please select a security question")
        else:
            
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error", "User already exists, please try another email")
            else:
                my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security_Q.get(),
                    self.var_security_A.get(),
                    self.var_password.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registered Successfully")
            
      
      
    def login(self):
        self.new_window=Toplevel(self.root)
        self.app=Login_Window(self.new_window)
      
      
      
      
      
      
        
if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()