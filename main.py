from tkinter import * # to import the tkinter library and to use the functions of the tkinter library
from tkinter import ttk # to import the ttk library and to use the functions of the ttk library
from PIL import Image, ImageTk # to import the image and to display the image in the tkinter window
from student import Student # to import the student class from the student.py file

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  # width x height + x_axis + y_axis
        self.root.title("Face Recognition System")
       
        
        # Image 1
        
        img = Image.open(r"C:\Users\sanke\OneDrive\Desktop\Face Recognition System\college_images\stanford_university.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS) # to resize the image to fit the tkinter window
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg) # to display the image in the tkinter window
        f_lbl.place(x=0, y=0, width=500, height=130) # to place the image in the tkinter window
        
        
        # Image 2
        
        img1 = Image.open(r"C:\Users\sanke\OneDrive\Desktop\Face Recognition System\college_images\img2.png")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS) 
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130) 
        
        
        # Image 3
        
        img2 = Image.open(r"C:\Users\sanke\OneDrive\Desktop\Face Recognition System\college_images\img3.webp")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS) 
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130) 
        
        
        
        #bg image
        img3 = Image.open(r"C:\Users\sanke\OneDrive\Desktop\Face Recognition System\college_images\bg_img.jpeg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS) 
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710) 
        
        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=50)
        
        
    # student button
    
        std_img_btn = Image.open(r"C:\Users\sanke\OneDrive\Desktop\Face Recognition System\college_images\std1.png")
        std_img_btn = std_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)
        
        b1 = Button(bg_img, image=self.std_img1, command=self.student_details, cursor="hand2") # to create a button with the image
        b1.place(x=200, y=100, width=220, height=220) # to place the button in the tkinter window
        
        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)


# Detect Face button
    
        detect_img_btn = Image.open(r"C:\Users\sanke\OneDrive\Desktop\Face Recognition System\college_images\face_detect.avif")
        detect_img_btn = detect_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.detect_img1 = ImageTk.PhotoImage(detect_img_btn)
        
        b1 = Button(bg_img, image=self.detect_img1, cursor="hand2") 
        b1.place(x=500, y=100, width=220, height=220) 
        
        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)
        
        
# Attendance button
    
        attendance_img_btn = Image.open(r"C:\Users\sanke\OneDrive\Desktop\Face Recognition System\college_images\attendance_btn.webp")
        attendance_img_btn = attendance_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.attendance_img1 = ImageTk.PhotoImage(attendance_img_btn)
        
        b1 = Button(bg_img, image=self.attendance_img1, cursor="hand2") 
        b1.place(x=800, y=100, width=220, height=220) 
        
        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)
        
        
 # Help button
    
        help_img_btn = Image.open(r"C:\Users\sanke\OneDrive\Desktop\Face Recognition System\college_images\help_btn.jpeg")
        help_img_btn = help_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.help_img1 = ImageTk.PhotoImage(help_img_btn)
        
        b1 = Button(bg_img, image=self.help_img1, cursor="hand2") 
        b1.place(x=1100, y=100, width=220, height=220) 
        
        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)
        
        
    # Train button
    
        train_img_btn = Image.open(r"C:\Users\sanke\OneDrive\Desktop\Face Recognition System\college_images\train_btn.jpeg")
        train_img_btn = train_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.train_img1 = ImageTk.PhotoImage(train_img_btn)
        
        b1 = Button(bg_img, image=self.train_img1, cursor="hand2") 
        b1.place(x=200, y=380, width=220, height=220) 
        
        b1_1 = Button(bg_img, text="Train Data", cursor="hand2",font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)
        
        
 # Photos button
    
        photos_img_btn = Image.open(r"C:\Users\sanke\OneDrive\Desktop\Face Recognition System\college_images\photos_btn.webp")
        photos_img_btn = photos_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.photos_img_btn = ImageTk.PhotoImage(photos_img_btn)

        b1 = Button(bg_img, image=self.photos_img_btn, cursor="hand2")
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos  ", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)
        
        
# Developer button
    
        developer_img_btn = Image.open(r"C:\Users\sanke\OneDrive\Desktop\Face Recognition System\college_images\developer_btn.png")
        developer_img_btn = developer_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.developer_img1 = ImageTk.PhotoImage(developer_img_btn)
        
        b1 = Button(bg_img, image=self.developer_img1, cursor="hand2") 
        b1.place(x=800, y=380, width=220, height=220) 
        
        b1_1 = Button(bg_img, text="Developer", cursor="hand2",font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)
        
        
        
# Exit button
    
        exit_img_btn = Image.open(r"C:\Users\sanke\OneDrive\Desktop\Face Recognition System\college_images\exit_btn.png")
        exit_img_btn = exit_img_btn.resize((220, 220), Image.Resampling.LANCZOS)
        self.exit_img1 = ImageTk.PhotoImage(exit_img_btn)
        
        b1 = Button(bg_img, image=self.exit_img1, cursor="hand2") 
        b1.place(x=1100, y=380, width=220, height=220) 
        
        b1_1 = Button(bg_img, text="Exit", cursor="hand2",font = ("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)
        
  # =============function buttons===========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        










if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()