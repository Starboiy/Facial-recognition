from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #========Variables=================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_emp_id=StringVar()
        self.var_emp_name=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()

         #First image 
        img = Image.open(r"C:\Users\iamai\OneDrive\Desktop\Mini Project\Photos\office.jpg")
        img = img.resize((500, 130),PIL.Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        #Second image
        img1 = Image.open(r"C:\Users\iamai\OneDrive\Desktop\Mini Project\Photos\Employee.jpg")
        img1 = img1.resize((500, 130),PIL.Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        #Third image
        img2 = Image.open(r"C:\Users\iamai\OneDrive\Desktop\Mini Project\Photos\Security.jpg")
        img2 = img2.resize((500, 130),PIL.Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        #bg image
        img3 = Image.open(r"C:\Users\iamai\OneDrive\Desktop\Mini Project\Photos\bg.jpg")
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

        img_Left = Image.open(r"C:\Users\iamai\OneDrive\Desktop\Mini Project\Photos\stud1.jpg")
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

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Sem-1","Sem-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class employee information
        class_employee_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Class employee Information",font=("times new roman",12,"bold"))
        class_employee_frame.place(x=5,y=250,width=720,height=300)

        #employee id
        employeeID_label=Label(class_employee_frame,text="employeeID:",font=("times new roman",13,"bold"),bg="white")
        employeeID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        employeeID_entry=ttk.Entry(class_employee_frame,textvariable=self.var_emp_id,width=20,font=("times new roman",13,"bold"))
        employeeID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


         #employee name
        employeeName_label=Label(class_employee_frame,text="employee Name:",font=("times new roman",13,"bold"),bg="white")
        employeeName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        employeeName_entry=ttk.Entry(class_employee_frame,textvariable=self.var_emp_name,width=20,font=("times new roman",13,"bold"))
        employeeName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         #Gender
        gender_label=Label(class_employee_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_employee_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=20)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        

         #Email
        email_label=Label(class_employee_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_employee_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Phone no
        phone_no_label=Label(class_employee_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_no_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_employee_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_no_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

          #Address
        address_label=Label(class_employee_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_employee_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_employee_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_employee_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #buttons frame
        btn_frame=Frame(class_employee_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_employee_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

         #Right Label frame
        Right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Employee Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_Right = Image.open(r"C:\Users\iamai\OneDrive\Desktop\Mini Project\Photos\stud1.jpg")
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
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #===============Function Declaration=======================
    
    def add_data(self):
      if self.var_dep.get()=="Select Department" or self.var_emp_name.get()=="" or self.var_emp_id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
          try:
            conn=mysql.connector.connect(host="localhost", username="root",password="", database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                          self.var_dep.get(),
                                                                                          self.var_course.get(),
                                                                                          self.var_year.get(),
                                                                                          self.var_semester.get(),
                                                                                          self.var_emp_id.get(),
                                                                                          self.var_emp_name.get(),
                                                                                          self.var_gender.get(),
                                                                                          self.var_email.get(),
                                                                                          self.var_phone.get(),
                                                                                          self.var_address.get(),
                                                                                          self.var_radio1.get()
                                            
                                                                                         ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Employee details have been added.",parent=self.root)  
          except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    #============Fetching data from database===================
    def  fetch_data(self):
      conn=mysql.connector.connect(host="localhost", username="root",password="", database="face_recognizer")
      my_cursor=conn.cursor()
      my_cursor.execute("select * from employee")
      data=my_cursor.fetchall()
      
      if len(data)!=0:
        self.employee_table.delete(*self.employee_table.get_children())
        for i in data:
          self.employee_table.insert("",END,values=i)
        conn.commit()
      conn.close()
      
    #==================Getting the cursor================
    def get_cursor(self,event=""):
      cursor_focus=self.employee_table.focus()
      content=self.employee_table.item(cursor_focus)
      data=content["values"]
      
      self.var_dep.set(data[0])
      self.var_course.set(data[1]),
      self.var_year.set(data[2]),
      self.var_semester.set(data[3]),
      self.var_emp_id.set(data[4]),
      self.var_emp_name.set(data[5]),
      self.var_gender.set(data[6]),
      self.var_email.set(data[7]),
      self.var_phone.set(data[8]),
      self.var_address.set(data[9]),
      self.var_radio1.set(data[10])
          
    #===================Update Function==============
    def update_data(self):
      if self.var_dep.get()=="Select Department" or self.var_emp_name.get()=="" or self.var_emp_id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
        try:
          update=messagebox.askyesno("Update","Do you want to update the details",parent=self.root)
          if update>0:
            conn=mysql.connector.connect(host="localhost", username="root",password="", database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("Update Employee Set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Gender=%s, Email=%s, Phone=%s, Address=%s, PhotoSample=%s where Employee_id=%s",(
              self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.var_emp_name.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_radio1.get(),
                                                                                                    self.var_emp_id.get()
                                                                                                    ))
          else:
            if not update:
              return
          messagebox.showinfo("Success", "Employee Details successfully added",parent=self.root)
          conn.commit()
          self.fetch_data()
          conn.close()
        except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)  
    
    #================Delete Function==============
    def delete_data(self):
      if self.var_emp_id.get()=="":
        messagebox.showerror("Error","Employee-Id Required",parent=self.root)
      else:
        try:
          delete=messagebox.askyesno("Delete","Are you sure you want to delete?",parent=self.root)
          if delete>0:
            conn=mysql.connector.connect(host="localhost", username="root",password="", database="face_recognizer")
            my_cursor=conn.cursor()
            sql="Delete from employee where Employee_id=%s"
            val=(self.var_emp_id.get(),)
            my_cursor.execute(sql,val)
          else:
            if not delete:
              return
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Delete","Details have been deleted successfully",parent=self.root)  
        except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)     

    #===========Reset function============
    def reset_data(self):
      self.var_dep.set("Select Department")
      self.var_course.set("Select Course"),
      self.var_year.set("Select Year"),
      self.var_semester.set("Select Semester"),
      self.var_emp_id.set(""),
      self.var_emp_name.set(""),
      self.var_gender.set("Male"),
      self.var_email.set(""),
      self.var_phone.set(""),
      self.var_address.set(""),
      self.var_radio1.set("")
    
    #=================Generating a data set or taking photo samples============
    def generate_dataset(self):
      if self.var_dep.get()=="Select Department" or self.var_emp_name.get()=="" or self.var_emp_id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root)
      else:
        try:
          conn=mysql.connector.connect(host="localhost", username="root",password="", database="face_recognizer")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from employee")
          myresult=my_cursor.fetchall()
          id=0
          for x in myresult:
            id+=1
          my_cursor.execute("Update Employee Set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Gender=%s, Email=%s, Phone=%s, Address=%s, PhotoSample=%s where Employee_id=%s",(
              self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.var_emp_name.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_radio1.get(),
                                                                                                    self.var_emp_id.get()==id+1
                                                                                                    ))
          conn.commit()
          self.fetch_data()
          self.reset_data()
          conn.close()
          
          #==========Loading predefined data on a face frontal using opencv=============
          
          face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
          
          def face_cropped(img):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_classifier.detectMultiScale(gray,1.3,5)
            #Scaling factor=1.3
            #Minimum Neighbor=5
            
            for (x,y,w,h) in faces:
              face_cropped=img[y:y+h,x:x+w]
              return face_cropped
            
          cap=cv2.VideoCapture(0)
          img_id=0
          while True:
            ret,my_frame=cap.read()
            if face_cropped(my_frame) is not None:
              img_id+=1
              face=cv2.resize(face_cropped(my_frame),(450,450))
              face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
              file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
              cv2.imwrite(file_name_path,face)
              cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
              cv2.imshow("Copped Face",face)
            
            if cv2.waitKey(1)==13 or int(img_id)==100:
              break
          cap.release()
          cv2.destroyAllWindows()
          messagebox.showinfo("Result","Generating Data Set has been completed")
        except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)   
          



        
if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
