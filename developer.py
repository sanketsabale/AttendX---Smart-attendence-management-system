from tkinter import * # to import the tkinter library and to use the functions of the tkinter library
from tkinter import ttk # to import the ttk library and to use the functions of the ttk library
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  # width x height + x_axis + y_axis
        self.root.title("Face Recognition System")


# Title label    
   
        title_lbl = Label(self.root,text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
# bg image        
        img_top = Image.open(r"college_images\dev.jpg")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
 
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=65, width=1530, height=720)

# frame
        main_frame = Frame(f_lbl,bd=2, bg="white")
        main_frame.place(x=1000,y=20,width=500,height=600)

        my_img = Image.open(r"C:\Users\sanke\OneDrive\Desktop\pic.jpg")
        my_img = my_img.resize((200, 200), Image.Resampling.LANCZOS)
        self.my_img = ImageTk.PhotoImage(my_img)
 
        f_lbl = Label(main_frame, image=self.my_img)
        f_lbl.place(x=300, y=0, width=200, height=200)

# dev info
        dev_label = Label(main_frame, text="Hello i am Sanket", font=("times new roman", 20, "bold"), bg="white", fg="blue")
        dev_label.place(x=0, y=5)

        dev_label = Label(main_frame, text="I am a Data Scientist   ", font=("times new roman", 20, "bold"), bg="white", fg="blue")
        dev_label.place(x=0, y=40)


        img2 = Image.open(r"college_images\studentimg3.jpeg")
        img2 = img2.resize((500, 390), Image.Resampling.LANCZOS) 
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=200, width=500, height=390) 
        
        
        





                    
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()