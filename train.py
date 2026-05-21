from tkinter import * # to import the tkinter library and to use the functions of the tkinter library
from tkinter import ttk # to import the ttk library and to use the functions of the ttk library
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  # width x height + x_axis + y_axis
        self.root.title("Face Recognition System")
        
# Title label    
   
        title_lbl = Label(self.root,text="TRAIN DATASET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=50)
        
# top image        
        img_top = Image.open(r"college_images\train_top_img.png")
        img_top = img_top.resize((1450, 425), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
 
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1450, height=325)
        
# button        
        
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",font = ("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)
        
        
        
# Bottom image
        img_bottom = Image.open(r"C:\Users\sanke\OneDrive\Desktop\Face Recognition System\college_images\photos_btn.webp")
        img_bottom = img_bottom.resize((1450, 425), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
 
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1450, height=325)
        
# Train function
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []
        
        for image in path:
            img = Image.open(image).convert('L') # convert the image to grayscale
            imageNp = np.array(img, 'uint8') # convert the image to numpy array
            id = int(os.path.split(image)[1].split('.')[1]) # get the id from the image name
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
            
        ids = np.array(ids)
        
 # =========== Train the classifier and save ============
        
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!")
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()