from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from attendance import Attendance
from developer import Developer
from face_recognition import Face_Recognition
from help import Help
from student import Student
from train import Train
import mysql.connector
from time import strftime
import os
import tkinter

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")  # width x height + x_axis + y_axis
        self.root.title("Face Recognition System")
    
    # ===== Full Screen Background =====
        img1 = Image.open(r"college_images\login_bg_img.jpeg")
        img1 = img1.resize((1550, 800))

        self.bg = ImageTk.PhotoImage(img1)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=1550, height=800)


        # ===== Right Side Image =====
        img2 = Image.open(r"college_images\login_bg_img2.png")
        img2 = img2.resize((400, 450))

        self.bg2 = ImageTk.PhotoImage(img2)

        lbl_bg2 = Label(self.root, image=self.bg2, bd=0)
        lbl_bg2.place(x=700, y=150, width=400, height=450)
        
    # ========= login Frame ========
        login_frame = Frame(self.root, bg="black")
        login_frame.place(x=250, y=150, width=400, height=450)
        
        logo = Image.open(r"college_images\login_img.webp")
        logo = logo.resize((100, 100))
        self.logo = ImageTk.PhotoImage(logo)

        lbl_logo = Label(login_frame, image=self.logo, bd=0,bg="black",borderwidth=0)
        lbl_logo.place(x=150, y=0,width=100, height=100)
        
        get_str = Label(login_frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=125, y=100)
        
    # ====== Label and Entry ======
        username_label = Label(login_frame, text="Username [Email]", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username_label.place(x=90, y=155)
        
        self.username_entry = ttk.Entry(login_frame, font=("times new roman", 15, "bold"))
        self.username_entry.place(x=70, y=185, width=270)
        
        password_label = Label(login_frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password_label.place(x=90, y=225)
        
        self.password_entry = ttk.Entry(login_frame, font=("times new roman", 15, "bold"), show="*")
        self.password_entry.place(x=70, y=255, width=270)
        
#  ========== icon Images ========
        img3 = Image.open(r"college_images\login_img.webp")
        img3 = img3.resize((25, 25))
        self.bg3 = ImageTk.PhotoImage(img3)

        lbl_bg3 = Label(login_frame, image=self.bg3, bd=0,bg="black",borderwidth=0)
        lbl_bg3.place(x=70, y=155, width=25, height=25)
        
        img4 = Image.open(r"college_images\password_icon_img.png")
        img4 = img4.resize((25, 25))

        self.bg4 = ImageTk.PhotoImage(img4)

        lbl_bg4 = Label(login_frame, image=self.bg4, bd=0,bg="black",borderwidth=0)
        lbl_bg4.place(x=65, y=230, width=25, height=25)
        
    # ====== Login Button ======
        login_button = Button(login_frame,command=self.login, text="Login", font=("times new roman", 15, "bold"), fg="white", bg="red", cursor="hand2")
        login_button.place(x=70, y=300, width=270)
        
    # ====== New user Register Button ======
        register_button = Button(login_frame, text="New User Register",command=self.register_window, font=("times new roman", 10, "bold"), fg="white", bg="black", cursor="hand2", borderwidth=0)
        register_button.place(x=70, y=350, width=270)
        
    # ====== Forget Password Button ======
        forget_password_button = Button(login_frame, text="Forget Password?",command=self.forgot_password, font=("times new roman", 10, "bold"), fg="white", bg="black", cursor="hand2", borderwidth=0)
        forget_password_button.place(x=70, y=380, width=270)
        
        
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)
        
        
    # ====== login Function ======
    def login(self):

        if self.username_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Error", "All fields are required")

        elif self.username_entry.get() == "kapu" and self.password_entry.get() == "ashu":

            messagebox.showinfo("Success", "Welcome to Face Recognition System")

            self.root.destroy()

            root = Tk()
            app = Face_Recognition_System(root)
            root.mainloop()

        else:

            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="root",
                database="face_recognizer"
            )

            my_cursor = conn.cursor()

            my_cursor.execute(
                "select * from register where email=%s and password=%s",
                (
                    self.username_entry.get(),
                    self.password_entry.get()
                )
            )

            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid username and password")

            else:

                messagebox.showinfo("Success", "Login Successful")

                self.root.destroy()

                root = Tk()
                app = Face_Recognition_System(root)
                root.mainloop()

            conn.close()
                            
  # =================== Reset Password window ==================
    def reset_password(self):     
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Please select a security question", parent=self.root2)
        elif self.security_A_entry.get() == "":
            messagebox.showerror("Error", "Please enter the answer to the security question", parent=self.root2)
        elif self.new_password_entry.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and securityQ=%s and LOWER(securityA)=LOWER(%s)")
            value = (self.username_entry.get().strip(), self.combo_security_Q.get().strip(), self.security_A_entry.get().strip())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter the correct answer to the security question", parent=self.root2)
            else:
                query = ("update register set password=%s where email=%s")
                value = (self.new_password_entry.get(), self.username_entry.get())
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Your password has been reset, please login with the new password", parent=self.root2)
                self.root2.destroy()
                           
                        
                        
                
 # =================== Forgot Password window ==================
    
    def forgot_password(self):
        if self.username_entry.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset your password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.username_entry.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter the valid email address")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("400x400+500+100")
                
                l = Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10,relwidth=1)
                
                security_Q = Label(self.root2, text="Select Security Question:", font=("times new roman", 15, "bold"), bg="white")
                security_Q.place(x=50, y=80)
                
                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 13,), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Best Friend Name")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50, y=110, width=300)
                
                
                security_A = Label(self.root2, text="Security Answer:", font=("times new roman", 13, "bold"), bg="white",fg="black")
                security_A.place(x=50, y=150)
                
                self.security_A_entry = ttk.Entry(self.root2, font=("times new roman", 13, "bold"))
                self.security_A_entry.place(x=50, y=180, width=300)
                
                
    #   New password label and entry
    
                new_password_label = Label(self.root2, text="New Password:", font=("times new roman", 13, "bold"), bg="white")    
                new_password_label.place(x=50, y=220)
                self.new_password_entry = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.new_password_entry.place(x=50, y=250, width=300)
    
    # Reset password button
                
                btn = Button(self.root2, text="Reset Password", command=self.reset_password, font=("times new roman", 15, "bold"), fg="white", bg="green", cursor="hand2")
                btn.place(x=100, y=300)
                
                
                
                
                
                
                
                
                
                
                
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
        
        self.combo_security_Q = ttk.Combobox(register_frame,textvariable=self.var_security_Q,font=("times new roman", 15),state="readonly")
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
        
        login_button = Button(register_frame,command=self.return_login, text="Already Registered? Login", font=("times new roman", 10, "bold"), fg="white", bg="red", cursor="hand2", borderwidth=0)
        login_button.place(x=450, y=490, width=200)
        
        
 # =================== Function Declaration         ==================
    def register_data(self):

        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_security_Q.get() == "Select":
            messagebox.showerror("Error", "All fields are required")

        elif self.var_password.get() != self.var_confirm_password.get():
            messagebox.showerror("Error", "Password and Confirm Password must be same")

        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="root",
                database="face_recognizer"
            )
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exists, please try another email")
            else:
                my_cursor.execute(
                    """
                    INSERT INTO register
                    (fname, lname, contact, email, securityQ, securityA, password)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_security_Q.get(),   # security question
                        self.var_security_A.get(),
                        self.var_password.get()
                    )
                )
                conn.commit()
                messagebox.showinfo("Success", "Registered Successfully")
                conn.close()
    

    def return_login(self):
        self.root.destroy()
      
      
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  # width x height + x_axis + y_axis
        self.root.title("Face Recognition System")
       
        
        # Image 1
        
        img = Image.open(r"college_images\stanford_university.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS) # to resize the image to fit the tkinter window
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg) # to display the image in the tkinter window
        f_lbl.place(x=0, y=0, width=500, height=130) # to place the image in the tkinter window
        
        
        # Image 2
        
        img1 = Image.open(r"college_images\img2.png")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS) 
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130) 
        
        
        # Image 3
        
        img2 = Image.open(r"college_images\img3.webp")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS) 
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130) 
        
        
        
        #bg image
        img3 = Image.open(r"college_images\bg_img.jpeg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS) 
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710) 
        
        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=50)
        
        # time
        
        def time():
            string = strftime("%H:%M:%S %p") # to get the current time in the format of hours:minutes:seconds AM/PM
            lbl.config(text=string) # to display the time in the label
            lbl.after(1000, time) # to update the time every second
        lbl = Label(title_lbl, font=("times new roman", 14, "bold"), bg="white", fg="blue")
        lbl.place(x=0, y=0, width=110, height=50)
        time()
        
        
    # student button
    
        std_img_btn = Image.open(r"college_images\std1.png")
        std_img_btn = std_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)
        
        b1 = Button(bg_img, image=self.std_img1, command=self.student_details, cursor="hand2") # to create a button with the image
        b1.place(x=200, y=100, width=220, height=220) # to place the button in the tkinter window
        
        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)


# Detect Face button
    
        detect_img_btn = Image.open(r"college_images\face_detect.avif")
        detect_img_btn = detect_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.detect_img1 = ImageTk.PhotoImage(detect_img_btn)
        
        b1 = Button(bg_img, image=self.detect_img1, cursor="hand2", command=self.face_data) 
        b1.place(x=500, y=100, width=220, height=220) 
        
        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data,font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)
        
        
# Attendance button
    
        attendance_img_btn = Image.open(r"college_images\attendance_btn.webp")
        attendance_img_btn = attendance_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.attendance_img1 = ImageTk.PhotoImage(attendance_img_btn)
        
        b1 = Button(bg_img, image=self.attendance_img1, cursor="hand2", command=self.attendance_data) 
        b1.place(x=800, y=100, width=220, height=220) 
        
        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data,font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)
        
        
 # Help button
    
        help_img_btn = Image.open(r"college_images\help_btn.jpeg") 
        help_img_btn = help_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.help_img1 = ImageTk.PhotoImage(help_img_btn)
        
        b1 = Button(bg_img, image=self.help_img1, cursor="hand2", command=self.help_data) 
        b1.place(x=1100, y=100, width=220, height=220) 
        
        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data,font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)
        
        
# Train button
    
        train_img_btn = Image.open(r"college_images\train_btn.jpeg")
        train_img_btn = train_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.train_img1 = ImageTk.PhotoImage(train_img_btn)
        
        b1 = Button(bg_img, image=self.train_img1, cursor="hand2", command=self.train_data) 
        b1.place(x=200, y=380, width=220, height=220) 
        
        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data,font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)
        
        
 # Photos button
    
        photos_img_btn = Image.open(r"college_images\photos_btn.webp")
        photos_img_btn = photos_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.photos_img_btn = ImageTk.PhotoImage(photos_img_btn)

        b1 = Button(bg_img, image=self.photos_img_btn, cursor="hand2", command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos  ", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)
        
        
# Developer button
    
        developer_img_btn = Image.open(r"college_images\developer_btn.png")
        developer_img_btn = developer_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.developer_img1 = ImageTk.PhotoImage(developer_img_btn)
        
        b1 = Button(bg_img, image=self.developer_img1, cursor="hand2", command=self.developer_data) 
        b1.place(x=800, y=380, width=220, height=220) 
        
        b1_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)
        
        
        
# Exit button
    
        exit_img_btn = Image.open(r"college_images\exit_btn.png")
        exit_img_btn = exit_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.exit_img1 = ImageTk.PhotoImage(exit_img_btn)
        
        b1 = Button(bg_img, image=self.exit_img1, cursor="hand2", command=self.iExit) 
        b1.place(x=1100, y=380, width=220, height=220) 
        
        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)



    def open_img(self):
        os.startfile("data") # to open the folder where the images are stored
        
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root) # to ask the user if they want to exit the application
        if self.iExit > 0:
            self.root.destroy() # to destroy the tkinter window
        else:
            return
    
        


  # =============function buttons===========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


     
      
                
                
                
       
        

if __name__ == "__main__":
    main()