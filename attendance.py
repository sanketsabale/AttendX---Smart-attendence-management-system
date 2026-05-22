from tkinter import * # to import the tkinter library and to use the functions of the tkinter library
from tkinter import ttk # to import the ttk library and to use the functions of the ttk library
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  # width x height + x_axis + y_axis
        self.root.title("Face Recognition System")

# Image 1
        
        img = Image.open(r"college_images\studentimg1.jpeg")
        img = img.resize((800, 200), Image.Resampling.LANCZOS) # to resize the image to fit the tkinter window
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl = Label(self.root, image=self.photoimg) # to display the image in the tkinter window
        f_lbl.place(x=0, y=0, width=800, height=200) # to place the image in the tkinter window
        
        
# Image 2
        
        img1 = Image.open(r"college_images\studentimg3.jpeg")
        img1 = img1.resize((800, 200), Image.Resampling.LANCZOS) 
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

 #bg image
           
        img3 = Image.open(r"college_images\bg_img.jpeg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS) 
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710) 

        title_lbl = Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=50)
  
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

# Left label frame
        
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman", 12, "bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)
        
        img_left = Image.open(r"college_images\frameimg1.jpeg")
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
 
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        left_inside_frame.place(x=0,y=135,width=720,height=370)

# labels entry
    # attendanceId 
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

    # Name 
        nameLabel = Label(left_inside_frame, text="Name:", font=("times new roman", 13, "bold"), bg="white")
        nameLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        nameEntry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        nameEntry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

    # Roll No 
        rollLabel = Label(left_inside_frame, text="Roll No:", font=("times new roman", 13, "bold"), bg="white")
        rollLabel.grid(row=0, column=2, padx=4, pady=8, sticky=W)

        rollEntry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        rollEntry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

    # Department
        depLabel = Label(left_inside_frame, text="Department:", font=("times new roman", 13, "bold"), bg="white")
        depLabel.grid(row=1, column=2, padx=4, pady=8, sticky=W)

        depEntry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        depEntry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

    # Time  
        timeLabel = Label(left_inside_frame, text="Time:", font=("times new roman", 13, "bold"), bg="white")
        timeLabel.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        timeEntry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        timeEntry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

    # Date
        dateLabel = Label(left_inside_frame, text="Date:", font=("times new roman", 13, "bold"), bg="white")
        dateLabel.grid(row=2, column=2, padx=4, pady=8, sticky=W)

        dateEntry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        dateEntry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

    # Attendance Status
        attendanceLabel = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 13, "bold"), bg="white")
        attendanceLabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, font=("times new roman", 13, "bold"), state="readonly", width=20)
        self.atten_status['values'] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        self.atten_status.current(0)


# Buttons Frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)
        
        import_btn = Button(btn_frame, text="Import Csv",font=("times new roman", 13, "bold"), bg="blue", fg="white", width=17)
        import_btn.grid(row=0, column=0)
        
        export_btn = Button(btn_frame, text="Export Csv",font=("times new roman", 13, "bold"), bg="blue", fg="white", width=17)
        export_btn.grid(row=0, column=1)
        
        update_btn = Button(btn_frame, text="Update",font=("times new roman", 13, "bold"), bg="blue", fg="white", width=17)
        update_btn.grid(row=0, column=2)
        
        reset_btn = Button(btn_frame, text="Reset",font=("times new roman", 13, "bold"), bg="blue", fg="white", width=17)
        reset_btn.grid(row=0, column=3)




  
# Right label frame
        
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman", 13, "bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)
       
        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=710,height=455)
 
    # scroll bar table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "name", "roll", "dep", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
       
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("roll", text="Roll No")
        self.AttendanceReportTable.heading("dep", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance Status")
        
        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("dep", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)







if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()