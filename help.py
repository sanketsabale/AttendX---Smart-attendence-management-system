from tkinter import * # to import the tkinter library and to use the functions of the tkinter library
from tkinter import ttk # to import the ttk library and to use the functions of the ttk library
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  # width x height + x_axis + y_axis
        self.root.title("Face Recognition System")


# Title label    
   
        title_lbl = Label(self.root,text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
# bg image        
        img_top = Image.open(r"college_images\help.webp")
        img_top = img_top.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
 
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        dev_label = Label(f_lbl, text="For any queries, please contact:", font=("times new roman", 20, "bold"), bg="white", fg="blue")
        dev_label.place(x=550, y=260)

        dev_label = Label(f_lbl, text="sanketsabale313@gmail.com", font=("times new roman", 20, "bold"), bg="white", fg="blue")
        dev_label.place(x=565, y=300)













if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()