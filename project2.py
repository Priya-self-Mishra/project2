from tkinter import *
root=Tk()
r=StringVar()
root.geometry("1536x864")
root['bg']='lightblue'
root.attributes('-topmost',True)
import mysql.connector
sql=mysql.connector.connect(host="localhost",user="root",password=r.get())
cursor=sql.cursor()
cursor.execute("create database if not exists Mission_Development")
cursor.execute("use Mission_Development")
cursor.execute("create table if not exists Project_Details(Project_id varchar(8)Primary key  Not Null unique,Name varchar(200)Not Null,Outlay double(10,2) Not Null,Location varchar(50)Not Null,Completion_expected_time varchar(15)Not Null,covered_Area varchar(15)Not Null)")
cursor.execute("create table if not exists Contractor_Details(Project_id varchar(8)Primary key  Not Null unique,Company_Name varchar(300) Not Null,Company_Contact_No int(20) Not Null,Official_email_id_of_company varchar(300)Not Null,Incharge_Name varchar(80)Not Null,incharge_contact_no int(20)Not Null,Official_email_id_of_Incharge varchar(300)Not Null,Total_Workers int(4)Not Null)")
cursor.execute("create table if not exists source_of_money(Project_id varchar(8)Primary key  Not Null unique,State_govt_Fund double(10,2) Not Null,Central_govt_Fund double(10,2) Not Null,Local_bodies_Fund double(10,2)Not Null,Private_companies_Fund double(10,2)Not Null,Total_Amount double(10,2)Not Null)")
cursor.execute("create table if not exists Feedback(Project_id varchar(8)Primary Key Not Null unique,Status varchar(300)Not Null,Reason varchar(700)Not Null)")
cursor.execute("create table if not exists user_Details(User_Name varchar(15),User_Password varchar(8))")
def Exit():
    exit()
def now_delete(id):
    cursor.execute("Delete from Project_Details where Project_id='"+str(idnum.get())+"'")
    cursor.execute("Delete from Contractor_Details where Project_id='"+str(idnum.get())+"'")
    cursor.execute("Delete from source_of_money where Project_id='"+str(idnum.get())+"'")
    cursor.execute("Delete from Feedback where Project_id='"+str(idnum.get())+"'")
    idnum.delete(0,END)
    showrecord=Label(deleterec,text="Deleted Successfully",bg="#D9D8D7",fg='blue',font=('Cambria',18))
    showrecord.place(x=300,y=600)
    

def delete(table_name):
    global deleterec
    deleterec=Tk()
    deleterec.attributes('-topmost',True)
    deleterec.geometry("1536x864")
    deleterec["bg"]="#D9D8D7"
    idlabel=Label(deleterec,bg='mintcream',fg='maroon',font=('Cambria',14),text="Project Id")
    idlabel.place(x=200,y=275)
    global idnum
    idnum=Entry(deleterec,bg='white',fg='green',font=('Cambria',12),width=50)
    idnum.place(x=370,y=275)
    deletecon=Button(deleterec,text="Delete",bg='black',fg='white',font=('Cambria',20),command=lambda:now_delete(id),padx=20,pady=10)
    deletecon.place(x=970,y=275)
    e=Button(deleterec,text=" Back",bg='black',fg='white',font=('Cambria',20),command=lambda: func(table_name),padx=50,pady=10)
    e.place(x=675,y=675)
    Button(deleterec,text="Exit",command=Exit,bg='black',fg='white',padx=50,pady=10,font=('Cambria',20)).place(x=970,y=675) 

def allshow(table_name):
    allshow=Tk()
    allshow.attributes('-topmost',True)
    allshow.geometry("1536x864")
    allshow["bg"]="#D9D8D7"
    print_record=""
    if table_name=="Project_Details":
        cursor.execute("Select * from Project_Details")
        records=cursor.fetchall()
        for record in records:
            print_record+=str(record[0])+"        "+str(record[1])+"        "+str(record[2])+"        "+str(record[3])+"        "+str(record[4])+"        "+str(record[5])+"\n\n"
    elif table_name=="Contractor_Details":
        cursor.execute("Select * from Contractor_Details")
        records=cursor.fetchall()
        for record in records:
            print_record+=str(record[0])+"   "+str(record[1])+"    "+str(record[2])+"   "+str(record[3])+"   "+str(record[4])+"    "+str(record[5])+"   "+str(record[6])+"   "+str(record[7])+"\n\n"
    elif table_name=="source_of_money":
        cursor.execute("Select * from source_of_money")
        records=cursor.fetchall()
        for record in records:
            print_record+=str(record[0])+"        "+str(record[1])+"        "+str(record[2])+"        "+str(record[3])+"        "+str(record[4])+"        "+str(record[5])+"\n\n"
    elif table_name=="Feedback": 
        cursor.execute("Select * from Feedback")
        records=cursor.fetchall()
        for record in records:
            print_record+=str(record[0])+"        "+str(record[1])+"        "+str(record[2])+"n\n"
    
    qw=Label(allshow,text="*************************Records*************************",bg='#D9D8D7',fg='black',font=('Cambria',18))
    qw.place(x=200,y=100)
    showrecord=Label(allshow,text=print_record,bg="#D9D8D7",fg='blue',font=('Cambria',18))
    showrecord.place(x=20,y=200)
    e=Button(allshow,text=" Back",bg='black',fg='white',font=('Cambria',14),command=lambda: show(table_name),padx=50,pady=10)
    e.place(x=675,y=675)
    Button(allshow,text="Exit",command=Exit,bg='black',fg='white',padx=50,pady=10,font=('Cambria',14)).place(x=900,y=675)    

def nowshow(table_name):
    now_show=Tk()
    now_show.attributes('-topmost',True)
    now_show.geometry("1536x864")
    now_show["bg"]="#D9D8D7"
    print_record=""
    qw=Label(now_show,text="**************************Records****************************",bg='#D9D8D7',fg='black',font=('Cambria',18))
    qw.place(x=200,y=100)
    
    if table_name=="Project_Details":
        cursor.execute(" Select * from Project_Details where Project_id='"+str(idnum_show.get())+"'")
        records=cursor.fetchall()
        for record in records:
            print_record+=str(record[0])+"        "+str(record[1])+"        "+str(record[2])+"        "+str(record[3])+"        "+str(record[4])+"        "+str(record[5])+"\n\n"
            showrecord=Label(now_show,text=print_record,bg="#D9D8D7",fg='blue',font=('Cambria',18))
            showrecord.place(x=200,y=200)
            idnum_show.delete(0,END)
    elif table_name=="Contractor_Details":
        cursor.execute(" Select * from Contractor_Details where Project_id='"+str(idnum_show.get())+"'")        
        records=cursor.fetchall()
        for record in records:
            print_record+=str(record[0])+"    "+str(record[1])+"    "+str(record[2])+"    "+str(record[3])+"    "+str(record[4])+"    "+str(record[5])+"    "+str(record[6])+"    "+str(record[7])+"\n\n"
            showrecord=Label(now_show,text=print_record,bg="#D9D8D7",fg='blue',font=('Cambria',18))
            showrecord.place(x=20,y=200)
            idnum_show.delete(0,END)
    elif table_name=="source_of_money":
        cursor.execute(" Select * from source_of_money where Project_id='"+str(idnum_show.get())+"'")
        records=cursor.fetchall()
        for record in records:
            print_record+=str(record[0])+"        "+str(record[1])+"        "+str(record[2])+"        "+str(record[3])+"        "+str(record[4])+"        "+str(record[5])+"\n\n"
            showrecord=Label(now_show,text=print_record,bg="#D9D8D7",fg='blue',font=('Cambria',18))
            showrecord.place(x=200,y=200)
            idnum_show.delete(0,END)
    elif table_name=="Feedback": 
        cursor.execute(" Select * from Feedback where Project_id='"+str(idnum_show.get())+"'")
        records=cursor.fetchall()
        for record in records:
            print_record+=str(record[0])+"        "+str(record[1])+"        "+str(record[2])+"n\n"
            showrecord=Label(now_show,text=print_record,bg="#D9D8D7",fg='blue',font=('Cambria',18))
            showrecord.place(x=200,y=200)
            idnum_show.delete(0,END)
    e=Button(now_show,text=" Back",bg='black',fg='white',font=('Cambria',20),command=lambda: onesho(table_name),padx=50,pady=10)
    e.place(x=675,y=675)

    Button(now_show,text="Exit",command=Exit,bg='black',fg='white',padx=50,pady=10,font=('Cambria',20)).place(x=970,y=675)    
        
def onesho(table_name):
    oneshow=Tk()
    oneshow.attributes('-topmost',True)
    oneshow.geometry("1536x864")
    oneshow["bg"]="#D9D8D7"
    idlabel=Label(oneshow,bg='mintcream',fg='maroon',font=('Cambria',14),text="Project ID")
    idlabel.place(x=200,y=275)
    global idnum_show
    idnum_show=Entry(oneshow,bg='white',fg='green',font=('Cambria',12),width=50)
    idnum_show.place(x=370,y=275)
    deletecon=Button(oneshow,text="show",bg='black',fg='white',font=('Cambria',20),command=lambda:nowshow(table_name),padx=20,pady=10)
    deletecon.place(x=970,y=275)
    e=Button(oneshow,text=" Back",bg='black',fg='white',font=('Cambria',20),command=lambda:show(table_name),padx=50,pady=10)
    e.place(x=670,y=475)
    Button(oneshow,text="Exit",command=Exit,bg='black',fg='white',padx=50,pady=10,font=('Cambria',20)).place(x=970,y=475)    
    

def show(table_name):
    show=Tk()
    show.attributes('-topmost',True)
    show.geometry("1536x864")
    show["bg"]="#D9D8D7"
    a=Button(show,text=" 1. All records",bg='black',fg='white',font=('Cambria',20),command=lambda: allshow(table_name),padx=90,pady=10)
    a.place(x=600,y=230)
    b=Button(show,text=" 2. Pariticular Record",bg='black',fg='white',font=('Cambria',20),command=lambda: onesho(table_name),padx=50,pady=10)
    b.place(x=600,y=330)
    e=Button(show,text=" Back",bg='black',fg='white',font=('Cambria',20),command=lambda: func(table_name),padx=140,pady=10)
    e.place(x=600,y=430)
    Button(show,text="Exit",command=Exit,bg='black',fg='white',font=('Cambria',20),padx=150,pady=10).place(x=600,y=530)

def now_add(table_name):
    if table_name=="Project_Details":
        cursor.execute("insert into Project_Details (Project_id,Name,Location,Completion_expected_time,covered_Area,Outlay) values('"+str(Project.get())+"','"+name.get()+"','"+location.get()+"','"+str(time.get())+"','"+str(area.get())+"','"+str(Outlay.get())+"')")
        sql.commit()
        Project.delete(0,END)
        name.delete(0,END)
        Outlay.delete(0,END)
        location.delete(0,END)
        time.delete(0,END)
        area.delete(0,END)

    if table_name=="Contractor_Details":
        cursor.execute("insert into Contractor_Details(Project_id,Company_Name,Company_Contact_No,Official_email_id_of_company,Incharge_Name,incharge_contact_no,Official_email_id_of_Incharge,Total_Workers) values('"+str(Pid.get())+"','"+compname.get()+"','"+str(contact.get())+"','"+str(comp_mail.get())+"','"+str(Incharge.get())+"','"+str(Incharge_contact.get())+"','"+str(Incharge_mail.get())+"','"+str(worker.get())+"')")
        sql.commit()
        Pid.delete(0,END)
        compname.delete(0,END)
        contact.delete(0,END)
        comp_mail.delete(0,END)
        Incharge.delete(0,END)
        Incharge_contact.delete(0,END)
        Incharge_mail.delete(0,END)
        worker.delete(0,END)

    if table_name=="source_of_money":
        a=int(state.get())+int(central.get())+int(local.get())+int(private.get())
        cursor.execute("insert into source_of_money(Project_id, State_govt_Fund, Central_govt_Fund,Local_bodies_Fund,Private_companies_Fund,Total_Amount) values('"+str(Proid.get())+"','"+str(state.get())+"','"+str(central.get())+"','"+str(local.get())+"','"+str(private.get())+"','"+str(a)+"')")
        sql.commit()        
        Proid.delete(0,END)
        state.delete(0,END)
        central.delete(0,END)
        local.delete(0,END)
        private.delete(0,END)

    if table_name=="Feedback":
        cursor.execute("insert into Feedback(Project_id, Status, Reason) values('"+str(Projid.get())+"','"+status.get()+"','"+reason.get()+"')")
        sql.commit()       
        Projid.delete(0,END)
        status.delete(0,END)
        reason.delete(0,END)
    Project_id=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',30),text="Recored Added Succesfuly!!! ")
    Project_id.place(x=200,y=575)

global addnewrec
def addnewrec(table_name):
    global addnew
    addnew=Tk()
    addnew.attributes('-topmost',True)
    addnew.geometry("1536x864")
    addnew["bg"]="#D9D8D7"
    space1=Label(addnew,font=('Cambria',14),text="    ",bg="#D9D8D7",padx=250,pady=10).grid(row=0,column=0,padx=40,pady=50)
    space2=Label(addnew,font=('Cambria',14),text="    ",bg="#D9D8D7",padx=250,pady=10).grid(row=0,column=1,padx=40,pady=50)
    if table_name=="Project_Details":
        global Project
        Project=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        Project.grid(row=1,column=1)
        id=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id.grid(row=1,column=0)

        global name
        name=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        name.grid(row=2,column=1)
        name_label=Label(addnew,fg='maroon',bg='#D9D8D7',font=('Cambria',14),text="Project Name")
        name_label.grid(row=2,column=0)

        global Outlay
        Outlay=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        Outlay.grid(row=3,column=1)
        Outlay_label=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Outlay(in millions)")
        Outlay_label.grid(row=3,column=0) 

        global location
        location=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        location.grid(row=4,column=1)
        location_label=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Location")
        location_label.grid(row=4,column=0)

        global time
        time=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        time.grid(row=5,column=1)
        time_label=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="EXpected Completion Time(in months)")
        time_label.grid(row=5,column=0)  

        global area
        area=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        area.grid(row=6,column=1)
        area_label=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Covered Area(in acres)")
        area_label.grid(row=6,column=0)  


    if table_name=="Contractor_Details":
        global Pid
        Pid=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        Pid.grid(row=1,column=1)
        id=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id.grid(row=1,column=0)

        global compname
        compname=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        compname.grid(row=2,column=1)
        name_label=Label(addnew,fg='maroon',bg='#D9D8D7',font=('Cambria',14),text="Company Name")
        name_label.grid(row=2,column=0)

        global contact
        contact=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        contact.grid(row=3,column=1)
        contact_label=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Official Contact Number of Company")
        contact_label.grid(row=3,column=0) 

        global comp_mail
        comp_mail=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        comp_mail.grid(row=4,column=1)
        comp_mail_label=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Official Email id of Company")
        comp_mail_label.grid(row=4,column=0)

        global Incharge
        Incharge=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        Incharge.grid(row=5,column=1)
        Incharge_label =Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Incharge Name")
        Incharge_label.grid(row=5,column=0)  

        global Incharge_contact
        Incharge_contact=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        Incharge_contact.grid(row=6,column=1)
        Incharge_contact_label=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Incharge Contact Number")
        Incharge_contact_label.grid(row=6,column=0) 

        global Incharge_mail
        Incharge_mail=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        Incharge_mail.grid(row=7,column=1)
        Incharge_mail_label=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Official Email id of Incharge")
        Incharge_mail_label.grid(row=7,column=0)  

        global worker
        worker=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        worker.grid(row=8,column=1)
        worker_label=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Total Workers")
        worker_label.grid(row=8,column=0)  


    if table_name=="source_of_money":
        global Proid
        Proid=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        Proid.grid(row=1,column=1)
        id=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id.grid(row=1,column=0)

        global state
        state=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        state.grid(row=2,column=1)
        state_label=Label(addnew,fg='maroon',bg='#D9D8D7',font=('Cambria',14),text="State Govt Fund(in millions)")
        state_label.grid(row=2,column=0)

        global central
        central=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        central.grid(row=3,column=1)
        central_label=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Central Govt Fund(in millions)")
        central_label.grid(row=3,column=0) 

        global local
        local=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        local.grid(row=4,column=1)
        local_label=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Local Bodies Fund(in millions)")
        local_label.grid(row=4,column=0)

        global private
        private=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        private.grid(row=5,column=1)
        private_label=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Private Companies Fund(in millions)")
        private_label.grid(row=5,column=0)  


    if table_name=="Feedback": 
        global Projid
        Projid=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        Projid.grid(row=1,column=1)
        id=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id.grid(row=1,column=0)

        global status
        status=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        status.grid(row=2,column=1)
        status_label=Label(addnew,fg='maroon',bg='#D9D8D7',font=('Cambria',14),text="Status")
        status_label.grid(row=2,column=0)

        global reason
        reason=Entry(addnew,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        reason.grid(row=3,column=1)
        reason_label=Label(addnew,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Reason for delay(if delaying)")
        reason_label.grid(row=3,column=0)         

    submit=Button(addnew,text="Add Record",bg='black',fg='white',font=('Cambria',20),command=lambda:now_add(table_name),padx=20,pady=10)
    submit.place(x=850,y=675)
    e=Button(addnew,text=" Back",bg='black',fg='white',font=('Cambria',20),command=lambda: func(table_name),padx=50,pady=10)
    e.place(x=1100,y=675)
    Button(addnew,text="Exit",command=Exit,bg='black',fg='white',padx=50,pady=10,font=('Cambria',20)).place(x=1300,y=675)

def update_New_Project():
    cursor.execute("update Project_Details set Project_id='"+New_Project.get()+"' where Project_id='"+str(used_id.get())+"'")
    New_Project.delete(0,END)
    used_id.delete(0,END)

def update_New_name():
    cursor.execute("update Project_Details set Name='"+New_name.get()+"' where Project_id='"+str(used_id_name.get())+"'")
    New_name.delete(0,END)
    used_id_name.delete(0,END)
                                         

def update_New_Outlay():
    cursor.execute("update Project_Details set Outlay='"+str(New_Outlay.get())+"' where Project_id='"+str(used_id_Outlay.get())+"'")
    New_Outlay.delete(0,END)
    used_id_Outlay.delete(0,END)
                                         
def update_New_location():
    cursor.execute("update Project_Details set Location='"+New_location.get()+"' where Project_id='"+str(used_id_location.get())+"'")
    New_location.delete(0,END)
    used_id_location.delete(0,END)
                                         
def update_New_time():
    cursor.execute("update Project_Details set Completion_expected_time='"+str(New_time.get())+"' where Project_id='"+str(used_id_time.get())+"'")
    New_time.delete(0,END)
    used_id_time.delete(0,END)
                                         
def update_New_area():
    cursor.execute("update Project_Details set covered_Area='"+str(New_area.get())+"' where Project_id='"+str(used_id_area.get())+"'")
    New_area.delete(0,END)
    used_id_area.delete(0,END)
     


def update_New_Pid():
    cursor.execute("update Contractor_Details set Project_id='"+New_Pid.get()+"' where Project_id='"+str(used_id_Pid.get())+"'")
    New_Pid.delete(0,END)
    used_id_Pid.delete(0,END)
                                         
def update_New_compname():
    cursor.execute("update Contractor_Details set Company_Name='"+New_compname.get()+"' where Project_id='"+str(used_id_compname.get())+"'")               
    New_compname.delete(0,END)
    used_id_compname.delete(0,END)
     
def update_New_contact():
    cursor.execute("update Contractor_Details set Company_Contact_No='"+str(New_contact.get())+"' where Project_id='"+str(used_id_contact.get())+"'")
    New_contact.delete(0,END)
    used_id_contact.delete(0,END)
                                         
def update_New_comp_mail():
    cursor.execute("update Contractor_Details set Official_email_id_of_company='"+New_comp_mail.get()+"' where Project_id='"+str(used_id_comp_mail.get())+"'")
    New_comp_mail.delete(0,END)
    used_id_comp_mail.delete(0,END)
                                         
def update_New_Incharge():
    cursor.execute("update Contractor_Details set Incharge_Name='"+str(New_Incharge.get())+"' where Project_id='"+str(used_id_Incharge.get())+"'")
    New_Incharge.delete(0,END)
    used_id_Incharge.delete(0,END)
                                         
def update_New_Incharge_contact():
    cursor.execute("update Contractor_Details set incharge_contact_no='"+str(New_Incharge_contact.get())+"' where Project_id='"+str(used_id_Incharge_contact.get())+"'")
    New_Incharge_contact.delete(0,END)
    used_id_Incharge_contact.delete(0,END)
     
def update_New_Incharge_mail():
    cursor.execute("update Contractor_Details set Official_email_id_of_Incharge='"+str(New_Incharge_mail.get())+"' where Project_id='"+str(used_id_Incharge_mail.get())+"'")
    New_Incharge_mail.delete(0,END)
    used_id_Incharge_mail.delete(0,END)
     
def update_New_worker():
    cursor.execute("update Contractor_Details set Total_Workers='"+str(New_worker.get())+"' where Project_id='"+str(used_id_worker.get())+"'")
    New_worker.delete(0,END)
    used_id_worker.delete(0,END)
     

def update_New_Proid():
    cursor.execute("update source_of_money set Project_id='"+New_Proid.get()+"' where Project_id='"+str(used_id_Proid.get())+"'")
    New_Proid.delete(0,END)
    used_id_Proid.delete(0,END)
                                         
def update_New_state():
    cursor.execute("update source_of_money set State_govt_Fund='"+New_state.get()+"' where Project_id='"+str(used_id_state.get())+"'")
    cursor.execute("select State_govt_Fund,Central_govt_Fund,Local_bodies_Fund,Private_companies_Fund from source_of_money where Project_id='"+str(used_id_state.get())+"'")
    record=cursor.fetchall()
    sum=0
    i=0
    for a in record:
        for i in range(4):
            sum+=int(a[i])
    cursor.execute("update source_of_money set Total_Amount='"+str(sum)+"' where Project_id='"+str(used_id_state.get())+"'")
    New_state.delete(0,END)
    used_id_state.delete(0,END)
     
def update_New_central():
    cursor.execute("update source_of_money set Central_govt_Fund='"+str(New_central.get())+"' where Project_id='"+str(used_id_central.get())+"'")
    cursor.execute("select State_govt_Fund,Central_govt_Fund,Local_bodies_Fund,Private_companies_Fund from source_of_money where Project_id='"+str(used_id_central.get())+"'")
    record=cursor.fetchall()
    sum=0
    i=0
    for a in record:
        for i in range(4):
            sum+=int(a[i])
    cursor.execute("update source_of_money set Total_Amount='"+str(sum)+"' where Project_id='"+str(used_id_central.get())+"'")
    New_central.delete(0,END)
    used_id_central.delete(0,END)
     

def update_New_local():
    cursor.execute("update source_of_money set Local_bodies_Fund='"+New_local.get()+"' where Project_id='"+str(used_id_local.get())+"'")
    cursor.execute("select State_govt_Fund,Central_govt_Fund,Local_bodies_Fund,Private_companies_Fund from source_of_money where Project_id='"+str(used_id_local.get())+"'")
    record=cursor.fetchall()
    sum=0
    i=0
    for a in record:
        for i in range(4):
            sum+=int(a[i])
    cursor.execute("update source_of_money set Total_Amount='"+str(sum)+"' where Project_id='"+str(used_id_local.get())+"'")
    New_local.delete(0,END)
    used_id_local.delete(0,END)
     


def update_New_private():
    cursor.execute("update source_of_money set Private_companies_Fund='"+str(New_private.get())+"' where Project_id='"+str(used_id_private.get())+"'")
    cursor.execute("select State_govt_Fund,Central_govt_Fund,Local_bodies_Fund,Private_companies_Fund from source_of_money where Project_id='"+str(used_id_private.get())+"'")
    record=cursor.fetchall()
    sum=0
    for a in record:
        for i in range(4):
            sum+=int(a[i])
    
    cursor.execute("update source_of_money set Total_Amount='"+str(sum)+"' where Project_id='"+str(used_id_private.get())+"'")
    New_private.delete(0,END)
    used_id_private.delete(0,END)
     

def update_New_Projid():
    cursor.execute("update Feedback set Project_id='"+str(New_Projid.get())+"' where Project_id='"+str(used_id_Projid.get())+"'")
    New_Projid.delete(0,END)
    used_id_Projid.delete(0,END)
     
def update_New_status():
    cursor.execute("update Feedback set Status='"+str(New_status.get())+"' where Project_id='"+str(used_id_status.get())+"'")
    New_status.delete(0,END)
    used_id_status.delete(0,END)
     
def update_New_reason():
    cursor.execute("update Feedback set Reason='"+str(New_reason.get())+"' where Project_id='"+str(used_id_reason.get())+"'")
    New_reason.delete(0,END)
    used_id_reason.delete(0,END)
     

def update(table_name):
    global updaterec
    updaterec=Tk()
    updaterec.attributes('-topmost',True)
    updaterec.geometry("1536x864")
    updaterec["bg"]="#D9D8D7"
    space1=Label(updaterec,font=('Cambria',14),text="    ",bg="#D9D8D7",padx=50,pady=10).grid(row=0,column=0,padx=40,pady=50)
    space2=Label(updaterec,font=('Cambria',14),text="    ",bg="#D9D8D7",padx=50,pady=10).grid(row=0,column=1,padx=40,pady=50)
    if table_name=="Project_Details":
        global New_Project
        global used_id
        New_Project=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_Project.grid(row=1,column=3)
        id=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Project ID")
        id.grid(row=1,column=2)
        used_id=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id.grid(row=1,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=1,column=0)
        req_id=used_id.get()
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_Project)
        submit.grid(row=1,column=4)



        global New_name
        global used_id_name
        New_name=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_name.grid(row=2,column=3)
        name_label=Label(updaterec,fg='maroon',bg='#D9D8D7',font=('Cambria',14),text="New Name")
        name_label.grid(row=2,column=2)

        used_id_name=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_name.grid(row=2,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=2,column=0)
        req_id=used_id.get()

        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_name)
        submit.grid(row=2,column=4)

        global New_Outlay
        global used_id_Outlay
        New_Outlay=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_Outlay.grid(row=3,column=3)
        Outlay_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Outlay((in millions))")
        Outlay_label.grid(row=3,column=2) 
        used_id_Outlay=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_Outlay.grid(row=3,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=3,column=0)
        req_id=used_id.get()
        print(req_id)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_Outlay)
        submit.grid(row=3,column=4)

        global New_location
        global used_id_location
        New_location=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_location.grid(row=4,column=3)
        New_location_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Location")
        New_location_label.grid(row=4,column=2)
        used_id_location=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_location.grid(row=4,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=4,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_location)
        submit.grid(row=4,column=4)

        global New_time
        global used_id_time
        New_time=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_time.grid(row=5,column=3)
        time_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New EXpected Completion Time")
        time_label.grid(row=5,column=2) 

        used_id_time=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_time.grid(row=5,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=5,column=0)
        req_id=used_id.get()
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_time)
        submit.grid(row=5,column=4)

        global New_area
        global used_id_area
        New_area=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_area.grid(row=6,column=3)
        area_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Covered Area")
        area_label.grid(row=6,column=2)  
        used_id_area=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_area.grid(row=6,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=6,column=0)
        req_id=used_id.get()
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_area)
        submit.grid(row=6,column=4)


    if table_name=="Contractor_Details":
        global New_Pid
        global used_id_Pid
        New_Pid=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_Pid.grid(row=1,column=3)
        id=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Project ID")
        id.grid(row=1,column=2)
        
        used_id_Pid=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_Pid.grid(row=1,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=1,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_Pid)
        submit.grid(row=1,column=4)

        global New_compname
        global used_id_compname
        New_compname=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_compname.grid(row=2,column=3)
        name_label=Label(updaterec,fg='maroon',bg='#D9D8D7',font=('Cambria',14),text="New Company Name")
        name_label.grid(row=2,column=2)

        used_id_compname=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_compname.grid(row=2,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=2,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_compname)
        submit.grid(row=2,column=4)

        global New_contact
        global used_id_contact
        New_contact=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_contact.grid(row=3,column=3)
        contact_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Official Contact Number of Company")
        contact_label.grid(row=3,column=2) 

        used_id_contact=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_contact.grid(row=3,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=3,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_contact)
        submit.grid(row=3,column=4)

        global New_comp_mail
        global used_id_comp_mail
        New_comp_mail=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_comp_mail.grid(row=4,column=3)
        comp_mail_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Official Email id of Company")
        comp_mail_label.grid(row=4,column=2)

        used_id_comp_mail=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_comp_mail.grid(row=4,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=4,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_comp_mail)
        submit.grid(row=4,column=4)

        global New_Incharge
        global used_id_Incharge
        New_Incharge=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_Incharge.grid(row=5,column=3)
        Incharge_label =Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Incharge Name")
        Incharge_label.grid(row=5,column=2)

        used_id_Incharge=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_Incharge.grid(row=5,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=5,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_Incharge)
        submit.grid(row=5,column=4) 

        global New_Incharge_contact
        global used_id_Incharge_contact
        New_Incharge_contact=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_Incharge_contact.grid(row=6,column=3)
        Incharge_contact_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Incharge Contact Number")
        Incharge_contact_label.grid(row=6,column=2) 

        used_id_Incharge_contact=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_Incharge_contact.grid(row=6,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=6,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_Incharge_contact)
        submit.grid(row=6,column=4)

        global New_Incharge_mail
        global used_id_Incharge_mail
        New_Incharge_mail=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_Incharge_mail.grid(row=7,column=3)
        Incharge_mail_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Official Email id of Incharge")
        Incharge_mail_label.grid(row=7,column=2)  

        used_id_Incharge_mail=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_Incharge_mail.grid(row=7,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=7,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_Incharge_mail)
        submit.grid(row=7,column=4)

        global New_worker
        global used_id_worker
        New_worker=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_worker.grid(row=8,column=3)
        worker_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Total Workers")
        worker_label.grid(row=8,column=2) 

        used_id_worker=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_worker.grid(row=8,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=8,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_worker)
        submit.grid(row=8,column=4)


    if table_name=="source_of_money":
        global New_Proid
        global used_id_Proid
        New_Proid=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_Proid.grid(row=1,column=3)
        id=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Project ID")
        id.grid(row=1,column=2)

        used_id_Proid=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_Proid.grid(row=1,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=1,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_Proid)
        submit.grid(row=1,column=4)

        global New_state
        global used_id_state
        New_state=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_state.grid(row=2,column=3)
        state_label=Label(updaterec,fg='maroon',bg='#D9D8D7',font=('Cambria',14),text="New State Govt Fund(in millions)")
        state_label.grid(row=2,column=2)

        used_id_state=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_state.grid(row=2,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=2,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_state)
        submit.grid(row=2,column=4)

        global New_central
        global used_id_central
        New_central=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_central.grid(row=3,column=3)
        central_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Central Govt Fund(in millions)")
        central_label.grid(row=3,column=2) 
        used_id_central=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_central.grid(row=3,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=3,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_central)
        submit.grid(row=3,column=4)

        global New_local
        global used_id_local
        New_local=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_local.grid(row=4,column=3)
        local_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Local Bodies Fund(in millions)")
        local_label.grid(row=4,column=2)
        used_id_local=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_local.grid(row=4,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=4,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_local)
        submit.grid(row=4,column=4)

        global New_private
        global used_id_private
        New_private=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_private.grid(row=5,column=3)
        private_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Private Companies Fund(in millions)")
        private_label.grid(row=5,column=2)  
        used_id_private=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_private.grid(row=5,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=5,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_private)
        submit.grid(row=5,column=4)


    if table_name=="Feedback": 
        global New_Projid
        global used_id_Projid
        New_Projid=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_Projid.grid(row=1,column=3)
        New_id=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Project ID")
        New_id.grid(row=1,column=2)
        used_id_Projid=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_Projid.grid(row=1,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=1,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_Projid)
        submit.grid(row=1,column=4)

        global New_status
        global used_id_status
        New_status=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_status.grid(row=2,column=3)
        status_label=Label(updaterec,fg='maroon',bg='#D9D8D7',font=('Cambria',14),text="New Status")
        status_label.grid(row=2,column=2)
        used_id_status=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_status.grid(row=2,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=2,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_status)
        submit.grid(row=2,column=4)

        global New_reason
        global used_id_reason
        New_reason=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        New_reason.grid(row=3,column=3)
        reason_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="New Reason(if delaying)")
        reason_label.grid(row=3,column=2)  
        used_id_reason=Entry(updaterec,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
        used_id_reason.grid(row=3,column=1)
        id_label=Label(updaterec,bg='#D9D8D7',fg='maroon',font=('Cambria',14),text="Project ID")
        id_label.grid(row=3,column=0)
        submit=Button(updaterec,text="Update",bg='black',fg='white',font=('Cambria',14),command=update_New_reason)
        submit.grid(row=3,column=4) 
    e=Button(updaterec,text=" Back",bg='black',fg='white',font=('Cambria',20),command=lambda: func(table_name),padx=50,pady=10)
    Button(updaterec,text="Exit",command=Exit,bg='black',fg='white',padx=50,pady=10,font=('Cambria',20)).place(x=800,y=530)
    e.place(x=600,y=530)

global func
def func(tablename):
    fun=Tk()
    fun.attributes('-topmost',True)
    fun.geometry("1536x864")
    fun["bg"]="#D9D8D7"
    global table_name
    if tablename=="Project_Details":
        table_name="Project_Details"
    elif tablename=="Contractor_Details":
        table_name="Contractor_Details"
    elif tablename=="source_of_money":
        table_name="source_of_money"
    elif tablename=="Feedback":
        table_name="Feedback"
    a=Button(fun,text=" 1. Show Record",bg='black',fg='white',font=('Cambria',20),command=lambda: show(table_name),padx=100,pady=10)
    a.place(x=600,y=130)
    b=Button(fun,text=" 2. Add New Record",bg='black',fg='white',font=('Cambria',20),command=lambda: addnewrec(table_name),padx=80,pady=10)
    b.place(x=600,y=230)
    c=Button(fun,text=" 3. Delete Existing record",bg='black',fg='white',font=('Cambria',20),command=lambda: delete(table_name),padx=50,pady=10)
    c.place(x=600,y=330)
    d=Button(fun,text=" 4. Update",bg='black',fg='white',font=('Cambria',20),command=lambda: update(table_name),padx=140,pady=10)
    d.place(x=600,y=430)
    e=Button(fun,text=" 5. Back",bg='black',fg='white',font=('Cambria',20),command=show_tables,padx=150,pady=10)
    e.place(x=600,y=530)
    e=Button(fun,text=" 6. Exit",bg='black',fg='white',font=('Cambria',20),command=Exit,padx=150,pady=10)
    e.place(x=600,y=630)


global show_tables
def show_tables():
    tables=Tk()
    tables.attributes('-topmost',True)
    tables.geometry("1536x864")
    tables["bg"]="#D9D8D7"
    a=Button(tables,text=" 1. Details of projects",bg='black',fg='white',font=('Cambria',20),command=lambda: func("Project_Details"),padx=40,pady=10)
    a.place(x=600,y=230)
    b=Button(tables,text=" 2. Details of contractors",bg='black',fg='white',font=('Cambria',20),command=lambda: func("Contractor_Details"),padx=20,pady=10)
    b.place(x=600,y=330)
    c=Button(tables,text=" 3. Finance",bg='black',fg='white',font=('Cambria',20),command=lambda: func("source_of_money"),padx=96,pady=10)
    c.place(x=600,y=430)
    d=Button(tables,text=" 4. Feedback",bg='black',fg='white',font=('Cambria',20),command=lambda: func("Feedback"),padx=90,pady=10)
    d.place(x=600,y=530)
    e=Button(tables,text=" 5. Sign Out",bg='black',fg='white',font=('Cambria',20),command=Exit,padx=100,pady=10)
    e.place(x=600,y=630)

def add():
    cursor.execute("insert into user_details values('"+name.get()+"','"+Pass.get()+"')")
    sql.commit()
    name.delete(0,END)
    Pass.delete(0,END)
def register():
    global name
    global Pass
    name=Entry(root,bg='white',fg='green',font=('Cambria',12),width=50)
    name.grid(row=2,column=1)
    Pass=Entry(root,bg='white',fg='green',show="*",font=('Cambria',12),width=50)
    Pass.grid(row=3,column=1)
    Name=Label(root,bg='mintcream',fg='maroon',font=('Cambria',14),text="Username")
    Name.grid(row=2,column=0)
    Password=Label(root,bg='mintcream',fg='maroon',font=('Cambria',14),text="Password")
    Password.grid(row=3,column=0,padx=20,pady=10)    
    Button(root,text="Register",command=add,bg='white',fg='midnightblue',font=('Cambria',14)).grid(row=4,column=0,padx=20,pady=20,columnspan=2)
    Button(root,text="Exit",command=Exit,bg='white',fg='midnightblue',padx=20,font=('Cambria',14)).place(x=900,y=270)

def check():
    cursor.execute("select User_Password from user_details where User_name='"+signname.get()+"'")
    row=cursor.fetchall()
    for i in row:
        a=list(i)
        if a[0]==str(Password.get()):
            show_tables()
            root.destroy()
        else:
            Label(root,bg='white',fg='magenta',font=('Cambria',18),text="""\n\n\nOops!!! It's seems you haven't registered yet""").place(x=600,y=750)
    sql.commit()
def sign():
    global signname
    global Password
    signname=Entry(root,justify='center',bg='white',fg='green',font=('Cambria',12),width=50)
    signname.grid(row=2,column=1)
    Password=Entry(root,justify='center',bg='white',show='*',fg='green',font=('Cambria',12),width=50)
    Password.grid(row=3,column=1)
    Name=Label(root,bg='mintcream',fg='maroon',font=('Cambria',14),text="Username")
    Name.grid(row=2,column=0)
    phoneNumber=Label(root,bg='mintcream',fg='maroon',font=('Cambria',14),text="Password")
    phoneNumber.grid(row=3,column=0,padx=20,pady=10)    
    Button(root,text="Proceed",bg='white',fg='midnightblue',font=('Cambria',14),command=check).grid(row=4,column=0,padx=20,pady=20,columnspan=2)
    Button(root,text="Exit",bg='white',fg='midnightblue',font=('Cambria',14),command=Exit,padx=20).place(x=900,y=270) 

Button(root,text="sign in",activebackground='mintcream',bg='white',fg='indigo',font=('Cambria',20),command=sign,padx=300,pady=10).grid(row=0,column=0,padx=40,pady=50)
Button(root,text="sign up",activebackground='mintcream',bg='white',fg='indigo',font=('Cambria',20),command=register,padx=250,pady=10).grid(row=0,column=1,padx=40,pady=50)
root.mainloop()
