from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import PIL

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

         #First image 
        img = Image.open(r"C:\Mini_Peroject\Photos\office.jpg")
        img = img.resize((500, 130),PIL.Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        #Second image
        img1 = Image.open(r"C:\Mini_Peroject\Photos\Employee.jpg")
        img1 = img1.resize((500, 130),PIL.Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        #Third image
        img2 = Image.open(r"C:\Mini_Peroject\Photos\Security.jpg")
        img2 = img2.resize((500, 130),PIL.Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        #bg image
        img3 = Image.open(r"C:\Mini_Peroject\Photos\bg.jpg")
        img3 = img3.resize((1530,790),PIL.Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=790)

        title_lbl=Label(bg_img,text="EMPLOYEE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #Left Label frame
        Left_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)

        img_Left = Image.open(r"C:\Mini_Peroject\Photos\stud1.jpg")
        img_Left = img_Left.resize((720, 130),PIL.Image.LANCZOS)
        self.photoimg_Left = ImageTk.PhotoImage(img_Left)

        f_lbl = Label(Left_frame,image=self.photoimg_Left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        

        #Current Course
        current_course_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Sem-1","Sem-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class employee information
        class_employee_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Class employee Information",font=("times new roman",12,"bold"))
        class_employee_frame.place(x=5,y=250,width=720,height=300)

        #employee id
        employeeID_label=Label(class_employee_frame,text="employeeID:",font=("times new roman",13,"bold"),bg="white")
        employeeID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        employeeID_entry=ttk.Entry(class_employee_frame,width=20,font=("times new roman",13,"bold"))
        employeeID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


         #employee name
        employeeName_label=Label(class_employee_frame,text="employee Name:",font=("times new roman",13,"bold"),bg="white")
        employeeName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        employeeName_entry=ttk.Entry(class_employee_frame,width=20,font=("times new roman",13,"bold"))
        employeeName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         #Gender
        gender_label=Label(class_employee_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_employee_frame,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

         #Email
        email_label=Label(class_employee_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_employee_frame,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Phone no
        phone_no_label=Label(class_employee_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_no_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_employee_frame,width=20,font=("times new roman",13,"bold"))
        phone_no_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

          #Address
        address_label=Label(class_employee_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_employee_frame,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #radio Buttons
        radiobtn1=ttk.Radiobutton(class_employee_frame,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_employee_frame,text="No Photo Sample",value="Yes")
        radiobtn2.grid(row=6,column=1)

        #buttons frame
        btn_frame=Frame(class_employee_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_employee_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

         #Right Label frame
        Right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_Right = Image.open(r"C:\Mini_Peroject\Photos\stud1.jpg")
        img_Right = img_Right.resize((720, 130),PIL.Image.LANCZOS)
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)

        f_lbl = Label(Right_frame,image=self.photoimg_Right)
        f_lbl.place(x=5, y=0, width=720, height=130)


        #========= Search System ==========

        Search_frame=LabelFrame(Right_frame,bg="white",bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","employee ID","employee Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)

        showAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=3)


        #========= Table Frame ==========

        table_frame=Frame(Right_frame,bg="white",bd=2,relief=RIDGE,)
        table_frame.place(x=5,y=210,width=710,height=250)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("sid","sname","gen","mail","phone","add","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("sid",text="employee ID")
        self.employee_table.heading("sname",text="employee Name")
        self.employee_table.heading("gen",text="Gender")
        self.employee_table.heading("mail",text="Email")
        self.employee_table.heading("phone",text="Phone No.")
        self.employee_table.heading("add",text="Address")
        self.employee_table.heading("photo",text="PhotoSampleStatus")
        self.employee_table["show"]="headings"

        self.employee_table.column("sid",width=100)
        self.employee_table.column("sname",width=100)
        self.employee_table.column("gen",width=100)
        self.employee_table.column("mail",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("add",width=100)
        self.employee_table.column("photo",width=100)

        self.employee_table.pack(fill=BOTH,expand=1)

    




       





    






        
if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()