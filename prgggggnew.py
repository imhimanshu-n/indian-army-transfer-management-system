import tkinter as tk
import sqlite3,sys
from PIL import ImageTk,Image

def connection():
    try:
        conn=sqlite3.connect("transfer.db")
    except:
        print("cannot connect to the database")
    return conn    

#---------------------------verifier table1----------------------------------------------------#
def verifier1():
    a=b=c=d=0
    if not  personel_name.get():
        t1.insert(tk.END,"<>personel name is required<>\n")
        a=1
    if not service_no.get():
        t1.insert(tk.END,"<>service number is required<>\n")
        b=1
    if not rank.get():
        t1.insert(tk.END,"<>rank is required<>\n")
        c=1
    if not serving_years.get():
        t1.insert(tk.END,"<>serving year is requrired<>\n")
        d=1

    if a==1 or b==1 or c==1 or d==1:
        return 1
    else:
        return 0

#---------------------------------------------verifier table2-----------------------------------------------#
def verifier2():
    a=b=c=0
    if not  name.get():
        tt1.insert(tk.END,"<>personel name is required<>\n")
        a=1
    if not no.get():
        tt1.insert(tk.END,"<>service number is required<>\n")
        b=1
    if not current_transfer.get():
        tt1.insert(tk.END,"<>current transfer is required<>\n")
        c=1  

    if a==1 or b==1 or c==1:
        return 1
    else:
        return 0

#------------------------------verifier table3----------------------------------------------------------#

def verifier3():
    a=b=c=d=e=0
    if not  pname.get():
        ttt1.insert(tk.END,"<>personel name is required<>\n")
        a=1
    if not pno.get():
        ttt1.insert(tk.END,"<>service number is required<>\n")
        b=1
    if not transfer.get():
        ttt1.insert(tk.END,"<>current transfer is required<>\n")
        c=1
    if not out_date.get():
        ttt1.insert(tk.END,"<>out date is required<>\n")
        d=1
    if not joining_date.get():
        ttt1.insert(tk.END,"<>joining date is required<>\n")
        e=1    

    if a==1 or b==1 or c==1 or d==1 or e==1:
        return 1
    else:
        return 0
 #---------------------------------------------------verifier table4--------------------------------------------------------#   

def verifier4():
    a=b=0
    if not  city.get():
        tttt1.insert(tk.END,"<>city is required<>\n")
        a=1
    if not vacancy.get():
        tttt1.insert(tk.END,"<>vacancy is required<>\n")
        b=1
 

    if a==1 or b==1:
        return 1
    else:
        return 0
#-------------------------------------------------verifier table5-------------------------------------------------------#
def verifier5():
    a=b=0
   
    if not mno.get():
        ttttt1.insert(tk.END,"<>service number is required<>\n")
        a=1
    if not medical.get():
        ttttt1.insert(tk.END,"<>medical status is required <>\n")
        b=1
  
    if a==1 or b==1:
        return 1
    else:
        return 0
    
#----------------------------------------------------------------------add table1-------------------------#
    
def add_student():
            Set=verifier1()
            if Set==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS EMP_DETAIL(PERSONEL_NAME TEXT ,SERVICE_NO INTEGER PRIMARY KEY,RANK TEXT,SERVING_YEARS INTEGER)")
                cur.execute("insert into EMP_DETAIL values(?,?,?,?)",(personel_name.get(),int(service_no.get()),rank.get(),int(serving_years.get())))
                conn.commit()
                conn.close()
                t1.insert(tk.END,"ADDED SUCCESSFULLY\n")


#--------------------------------------table2---------------------------------------#
def add_table2():
            ret=verifier2()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS CURRENT_TRANSFER(PERSONEL_NAME TEXT ,SERVICE_NO INTEGER,CURRENT_TRANSFER INTEGER,FOREIGN KEY (SERVICE_NO) REFERENCES EMP_DET(SERVICE_NO))")
                cur.execute("insert into CURRENT_TRANSFER values(?,?,?)",(name.get(),int(no.get()),current_transfer.get()))
                conn.commit()
                conn.close()
                tt1.insert(tk.END,"ADDED SUCCESSFULLY\n")
#-----------------------------------------------------------table3----------------------------------------------------#
def add_table3():
            Det=verifier3()
            if Det==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS MANAGE_TRANSFER(PERSONEL_NAME TEXT ,SERVICE_NO INTEGER,TRANSFER INTEGER,OUT_DATE TEXT, JOINING_DATE TEXT, FOREIGN KEY (SERVICE_NO) REFERENCES EMP_DET(SERVICE_NO))")
                cur.execute("insert into MANAGE_TRANSFER values(?,?,?,?,?)",(pname.get(),int(pno.get()),transfer.get(),out_date.get(),joining_date.get()))
                conn.commit()
                conn.close()
                ttt1.insert(tk.END,"ADDED SUCCESSFULLY\n")

#--------------------------------------------------------------table4--------------------------------------------------------------------#
def add_table4():
            Fet=verifier4()
            if Fet==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS VACANCIES(CITY TEXT ,VACANCY INTEGER)")
                cur.execute("insert into VACANCIES values(?,?)",(city.get(),int(vacancy.get())))
                conn.commit()
                conn.close()
                tttt1.insert(tk.END,"ADDED SUCCESSFULLY\n")
               
#--------------------------------------------------------------table5-------------------------------------------------------------------#
def add_table5():
            Get=verifier5()
            if Get==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS MEDICAL_CERTIFICATE(SERVICE_NO INTEGER,MEDICAL  INTEGER, FOREIGN KEY (SERVICE_NO) REFERENCES EMP_DET(SERVICE_NO))")
                cur.execute("insert into MEDICAL_CERTIFICATE values(?,?)",(int(mno.get()),medical.get()))
                conn.commit()
                conn.close()
                ttttt1.insert(tk.END,"ADDED SUCCESSFULLY\n")
#------------------------------------------------trigger table--------------------------------------------------------------------------#

conn=connection()
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS lead_logs (SERVICE_NO INT PRIMARY KEY, OLD_RANK TEXT, NEW_RANK TEXT,USER_ACTION TEXT, CREATED_AT TEXT)")
cur.execute("CREATE TRIGGER IF NOT EXISTS log_after_update AFTER UPDATE ON EMP_DETAIL WHEN OLD.RANK <> NEW.RANK BEGIN INSERT INTO lead_logs(OLD_RANK,NEW_RANK,USER_ACTION,CREATED_AT) VALUES( OLD.RANK,NEW.RANK,'UPDATE',DATETIME('NOW'));END ")
#---------------------------------------------------------view log---------------------------------------------------------------#
def view_logs():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from lead_logs")
    data=cur.fetchall()
    conn.close
    for i in data:
        t1.insert(tk.END,str(i)+"\n")

    

#----------------------------------------------------------------view table--------------------------------------------------------#

def view_student():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from EMP_DETAIL")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(tk.END,str(i)+"\n")

#-----------------------------------------------------------view table2----------------------------------------------------#

def view_table2():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from CURRENT_TRANSFER")
    data=cur.fetchall()
    conn.close()
    for i in data:
        tt1.insert(tk.END,str(i)+"\n")
#---------------------------------------------------------------------view table3------------------------------------------------#
def view_table3():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from MANAGE_TRANSFER")
    data=cur.fetchall()
    conn.close()
    for i in data:
        ttt1.insert(tk.END,str(i)+"\n")
#---------------------------------------------------------------------viewtable4--------------------------------------------------------#        
def view_table4():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from VACANCIES")
    data=cur.fetchall()
    conn.close()
    for i in data:
        tttt1.insert(tk.END,str(i)+"\n")        

#------------------------------------------------------view table5------------------------------------------------#        
def view_table5():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from MEDICAL_CERTIFICATE")
    data=cur.fetchall()
    conn.close()
    for i in data:
        ttttt1.insert(tk.END,str(i)+"\n")        

#------------------------------------------------------------delete table1---------------------------------------------------------#
def delete_student():
    conn=connection()
    cur=conn.cursor()
    cur.execute("DELETE FROM EMP_DETAIL WHERE SERVICE_NO=?",(int(service_no.get()),))
    conn.commit()
    conn.close()
    t1.insert(tk.END,"SUCCESSFULLY DELETED THE USER\n")


#------------------------------------------------------delete table2----------------------------------------------------------------------#

def delete_table2():
    conn=connection()
    cur=conn.cursor()
    cur.execute("DELETE FROM  CURRENT_TRANSFER WHERE SERVICE_NO=?",(int(no.get()),))
    conn.commit()
    conn.close()
    tt1.insert(tk.END,"SUCCESSFULLY DELETED THE USER\n")
        
#--------------------------------------------------------------delete table3-------------------------------#
def delete_table3():
    conn=connection()
    cur=conn.cursor()
    cur.execute("DELETE FROM  MANAGE_TRANSFER WHERE SERVICE_NO=?",(int(pno.get()),))
    conn.commit()
    conn.close()
    ttt1.insert(tk.END,"SUCCESSFULLY DELETED THE USER\n")
#---------------------------------------------------------------------------delete table4-----------------------------------------------------#        
def delete_table4():
    conn=connection()
    cur=conn.cursor()
    cur.execute("DELETE FROM  VACANCIES WHERE CITY=?",(city.get(),))
    conn.commit()
    conn.close()
    tttt1.insert(tk.END,"SUCCESSFULLY DELETED THE USER\n")


#---------------------------------------------------------------------------------------------delete table5----------------------------------------------------------------------------#
def delete_table5():
    conn=connection()
    cur=conn.cursor()
    cur.execute("DELETE FROM  MEDICAL_CERTIFICATE WHERE SERVICE_NO=?",(int(mno.get()),))
    conn.commit()
    conn.close()
    ttttt1.insert(tk.END,"SUCCESSFULLY DELETED THE USER\n")


#-----------------------------------------------------------------------update table1-------------------------------------------------------------------------------#
def update_student():
    Set=verifier1()
    if Set==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE EMP_DETAIL SET PERSONEL_NAME=?,SERVICE_NO=?,RANK=?,SERVING_YEARS=?where SERVICE_NO=?",(personel_name.get(),int(service_no.get()),rank.get(),int(serving_years.get()),int(service_no.get())))
        conn.commit()
        conn.close()
        t1.insert(tk.END,"UPDATED SUCCESSFULLY\n")
#----------------------------------------------------------------------------------------update table2---------------------------------------------------------------------------------#

def update_table2():
    ret=verifier2()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE CURRENT_TRANSFER SET PERSONEL_NAME=?,CURRENT_TRANSFER=?where SERVICE_NO=?",(name.get(),current_transfer.get(),int(no.get())))
        conn.commit()
        conn.close()
        tt1.insert(tk.END,"UPDATED SUCCESSFULLY\n")
#--------------------------------------------------------------------------------------------------update table3--------------------------------------------------------------------------------------------------#
def update_table3():
    Det=verifier3()
    if Det==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE MANAGE_TRANSFER SET PERSONEL_NAME=?,TRANSFER=?,OUT_DATE=?,JOINING_DATE?where SERVICE_NO=?",(pname.get(),transfer.get(),out_date.get(),joining_date.get(),int(pno.get())))
        conn.commit()
        conn.close()
        ttt1.insert(tk.END,"UPDATED SUCCESSFULLY\n")
#--------------------------------------------------------------------------------------------------update table4--------------------------------------------------------------------------------------------------#
def update_table4():
    Fet=verifier4()
    if Det==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE VACANCIES SET VACANCY=?where CITY=?",(int(vacancy.get()),city.get()))
        conn.commit()
        conn.close()
        tttt1.insert(tk.END,"UPDATED SUCCESSFULLY\n")

#--------------------------------------------------------------------------------------------------update table5--------------------------------------------------------------------------------------------------#        
def update_table5():
    Get=verifier5()
    if Get==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE MEDICAL_CERTIFICATE SET MEDICAL=?where SERVICE_NO=?",(medical.get(),int(mno.get())))
        conn.commit()
        conn.close()
        ttttt1.insert(tk.END,"UPDATED SUCCESSFULLY\n")

#---------------------------------------------------------------------------------------trigger table1--------------------------------------------------------------------------------------------------------------------#
        


def clse():
    sys.exit() 
        

if __name__=="__main__":

    def show_frame(frame):
        frame.tkraise()
    window=tk.Tk()   
    
    window.rowconfigure(0,weight=1)
    window.columnconfigure(0,weight=1)
    window.state('zoomed')
    window.iconbitmap('images.png')
    framel=tk.Frame(window)
    framel.config(bg='red')
    frame1=tk.Frame(window)
    frame1.config(bg='red')
    frame2=tk.Frame(window)
    frame2.configure(bg='sky blue')
    frame3=tk.Frame(window)
    frame3.configure(bg='sky blue')
    frame4=tk.Frame(window)
    frame4.configure(bg='sky blue')
    frame5=tk.Frame(window)
    frame5.configure(bg='sky blue')
    frame6=tk.Frame(window)
    frame6.configure(bg='sky blue')
    for frame in(framel,frame1,frame2,frame3,frame4,frame5,frame6):
        frame.grid(row=0,column=0,sticky='nsew')
    def close ():
        window.destroy()
    #------------------------------------login frame------------------------------------------------------------#    
    user_name=tk.StringVar()
    password=tk.StringVar()
    
    def login(user_name,password):
        def error():
            mylabel=tk.Label(framel,text='ERROR!!! please check user name and password and try again!',fg='red',bg='yellow')
            mylabel.place(x=650,y=600)
        if user_name.get()=='admin' and password.get()=='admin':
            show_frame(frame1)
        else:
            error()
    mylabel=tk.Label(framel,text='PROJECT BY- HIMANSHU NAGARKOTI',fg='yellow',bg='red',font=('arial',12,'bold'))
    mylabel.place(x=1200,y=750)

    frame1_title=tk.Label(framel,text="                                      Welcome to Indian Army Transfer Management System                                  ",fg='red',bg='yellow',font=('arial',25,'bold'))
    frame1_title.grid(row=1,column=10,padx=20,pady=20)

    my_img1=ImageTk.PhotoImage(Image.open("login.jpg"))
    my_label1= tk.Label(framel,image=my_img1)
    my_label1.grid(row=2,column=10)


    frame1_title1=tk.Label(framel,text="                                      LOGIN                                 ",fg='red',font=('arial',25,'bold'))
    frame1_title1.grid(row=5,column=10,padx=20,pady=20)
    label1=tk.Label(framel,text="User Name:",fg='red',font=('arial',12,'bold'))
    label1.place(x=650,y=450)

    label2=tk.Label(framel,text="Password:",fg='red',font=('arial',12,'bold'))
    label2.place(x=650,y=500)

    e1=tk.Entry(framel,textvariable=user_name)
    e1.place(x=750,y=450)

    e2=tk.Entry(framel,textvariable=password)
    e2.place(x=750,y=500)
    frame1_button=tk.Button(framel,text='submit',command=lambda:login(user_name,password),bg='yellow',fg='red',font=('arial',15,'bold'))
    frame1_button.place(x=750,y=550)

        
    #------------------------frame1 code-------------------------------#

    my_img=ImageTk.PhotoImage(Image.open("images.png"))
    my_label= tk.Label(frame1,image=my_img)
    my_label.grid(row=1,column=10)

    my_image=ImageTk.PhotoImage(Image.open("army.jpg"))
    my_label1= tk.Label(frame1,image=my_image)
    my_label1.grid(row=3,column=10)    


    frame1_title=tk.Label(frame1,text="                                      Welcome to Indian Army Transfer Management System                                  ",fg='red',bg='yellow',font=('arial',25,'bold'))

    frame1_title.grid(row=2,column=10,padx=20,pady=20)
    frame1_bottom=tk.Label(frame1,text="                                                    INDIAN ARMY-NATION FIRST                                              ",fg='red',bg='yellow' ,font=('arial',20,'bold'))
    frame1_bottom.grid(row=5,column=10)
    frame1_button=tk.Button(frame1,text='Personal Details',command=lambda:show_frame(frame2),bg='yellow',fg='red',font=('arial',12,'bold'))
    frame1_button.place(x=200,y=250)
    frame1_button=tk.Button(frame1,text='Current Transfer',command=lambda:show_frame(frame3),bg='yellow',fg='red',font=('arial',12,'bold'))
    frame1_button.place(x=200,y=350)
    frame1_button=tk.Button(frame1,text='  Next Transfer ',command=lambda:show_frame(frame4),bg='yellow',fg='red',font=('arial',12,'bold'))
    frame1_button.place(x=200,y=450)
    frame1_button=tk.Button(frame1,text='    Vacancies    ',command=lambda:show_frame(frame5),bg='yellow',fg='red',font=('arial',12,'bold'))
    frame1_button.place(x=1200,y=350)
    frame1_button=tk.Button(frame1,text='Medical Details',command=lambda:show_frame(frame6),bg='yellow',fg='red',font=('arial',12,'bold'))
    frame1_button.place(x=1200,y=250)
    frame1_button=tk.Button(frame1,text='          Exit          ',command=close,bg='yellow',fg='red',font=('arial',12,'bold'))
    frame1_button.place(x=1200,y=450)



    
        
    #------------------------frame2 code-------------------------------#
    personel_name=tk.StringVar()
    service_no=tk.StringVar()
    rank=tk.StringVar()
    serving_years=tk.StringVar()
    

    frame2_title=tk.Label(frame2,text="PERSONEL DETAILS",fg='red',bg='sky blue',font=('arial',20,'bold'))
    frame2_title.grid(row=9,column=1,padx=20,pady=20)
    
    label1=tk.Label(frame2,text="personel name:",fg='red',font=('arial',12,'bold'))
    label1.place(x=0,y=90)

    label2=tk.Label(frame2,text="service no:",fg='red',font=('arial',12,'bold'))
    label2.place(x=0,y=120)

    label3=tk.Label(frame2,text="rank:",fg='red',font=('arial',12,'bold'))
    label3.place(x=0,y=150)

    label4=tk.Label(frame2,text="serving years:",fg='red',font=('arial',12,'bold'))
    label4.place(x=0,y=180)



    e1=tk.Entry(frame2,textvariable=personel_name)
    e1.place(x=140,y=90)

    e2=tk.Entry(frame2,textvariable=service_no)
    e2.place(x=140,y=120)

    e3=tk.Entry(frame2,textvariable=rank)
    e3.place(x=140,y=150)

    e4=tk.Entry(frame2,textvariable=serving_years)
    e4.place(x=140,y=180)
    

    
    t1=tk.Text(frame2,width=150,height=33)
    t1.grid(row=10,column=1)
    
    b1=tk.Button(frame2,text="ADD DETAILS",command=add_student,width=40,font=('arial',12,'bold'),fg='red')
    b1.grid(row=11,column=0)

    b2=tk.Button(frame2,text="VIEW ALL DETAILS",command=view_student,width=40,font=('arial',12,'bold'),fg='red')
    b2.grid(row=12,column=0)

    b3=tk.Button(frame2,text="DELETE DETAILS",command=delete_student,width=40,font=('arial',12,'bold'),fg='red')
    b3.grid(row=13,column=0)

    b4=tk.Button(frame2,text="UPDATE INFO",command=update_student,width=40,font=('arial',12,'bold'),fg='red')
    b4.grid(row=14,column=0)

    b5=tk.Button(frame2,text="CLOSE",command=close,width=40,font=('arial',12,'bold'),fg='red')
    b5.grid(row=15,column=0)

    
    b6=tk.Button(frame2,text="main menu",command=lambda:show_frame(frame1),font=('arial',12,'bold'),fg='red')
    b6.grid(row=15,column=1     )
    b7=tk.Button(frame2,text="logs",command=lambda:view_logs(),font=('arial',12,'bold'),fg='red')
    b7.grid(row=12,column=1     )
    #------------------------------------------------------------------------------------------------------frame3 code---------------------------------------------------------------------------------------------------------#
    name=tk.StringVar()
    no=tk.StringVar()
    current_transfer=tk.StringVar()
    
    

    frame2_title=tk.Label(frame3,text="CURRENT TRANSFER DETAILS",fg='red',bg='sky blue',font=('arial',20,'bold'))
    frame2_title.grid(row=9,column=1,padx=20,pady=20)
    
    label1=tk.Label(frame3,text="personel name:",fg='red',font=('arial',12,'bold'))
    label1.place(x=0,y=30)

    label2=tk.Label(frame3,text="service no:",fg='red',font=('arial',12,'bold'))
    label2.place(x=0,y=60)

    label3=tk.Label(frame3,text="currrent transfer:",fg='red',font=('arial',12,'bold'))
    label3.place(x=0,y=90)


    E1=tk.Entry(frame3,textvariable=name)
    E1.place(x=140,y=30)

    E2=tk.Entry(frame3,textvariable=no)
    E2.place(x=140,y=60)

    E3=tk.Entry(frame3,textvariable=current_transfer)
    E3.place(x=140,y=90)

    
    tt1=tk.Text(frame3,width=150,height=33)
    tt1.grid(row=10,column=1)
    
    b1=tk.Button(frame3,text="ADD DETAILS",command=add_table2,width=40,fg='red',font=('arial',12,'bold'))
    b1.grid(row=11,column=0)

    b2=tk.Button(frame3,text="VIEW ALL DETAILS",command=view_table2,width=40,fg='red',font=('arial',12,'bold'))
    b2.grid(row=12,column=0)

    b3=tk.Button(frame3,text="DELETE DETAILS",command=delete_table2,width=40,fg='red',font=('arial',12,'bold'))
    b3.grid(row=13,column=0)

    b4=tk.Button(frame3,text="UPDATE INFO",command=update_table2,width=40,fg='red',font=('arial',12,'bold'))
    b4.grid(row=14,column=0)

    b5=tk.Button(frame3,text="CLOSE",command=close,width=40,fg='red',font=('arial',12,'bold'))
    b5.grid(row=15,column=0)

    
    b6=tk.Button(frame3,text="Main menu",command=lambda:show_frame(frame1),fg='red',font=('arial',12,'bold'))
    b6.grid(row=15,column=1)
      
#---------------------------------------------------------------------------------------------frame4-------------------------------------------------------------------------------------------------------------------#    
    pname=tk.StringVar()
    pno=tk.StringVar()
    transfer=tk.StringVar()
    out_date=tk.StringVar()
    joining_date=tk.StringVar()

    frame2_title=tk.Label(frame4,text="MANAGE TRANSFER",fg='red',bg='sky blue',font=('arial',20,'bold'))
    frame2_title.grid(row=9,column=1,padx=20,pady=20)
    
    label1=tk.Label(frame4,text="personel name:",fg='red',font=('arial',12,'bold'))
    label1.place(x=0,y=30)

    label2=tk.Label(frame4,text="service no:",fg='red',font=('arial',12,'bold'))
    label2.place(x=0,y=60)

    label3=tk.Label(frame4,text="transfer:",fg='red',font=('arial',12,'bold'))
    label3.place(x=0,y=90)
    
    label4=tk.Label(frame4,text="out date:",fg='red',font=('arial',12,'bold'))
    label4.place(x=0,y=120)

    label5=tk.Label(frame4,text="joining date:",fg='red',font=('arial',12,'bold'))
    label5.place(x=0,y=150)


    E1=tk.Entry(frame4,textvariable=pname)
    E1.place(x=140,y=30)

    E2=tk.Entry(frame4,textvariable=pno)
    E2.place(x=140,y=60)

    E3=tk.Entry(frame4,textvariable=transfer)
    E3.place(x=140,y=90)

    E4=tk.Entry(frame4,textvariable=out_date)
    E4.place(x=140,y=120)

    E5=tk.Entry(frame4,textvariable=joining_date)
    E5.place(x=140,y=150)


    
    ttt1=tk.Text(frame4,width=150,height=33)
    ttt1.grid(row=10,column=1)
    
    b1=tk.Button(frame4,text="ADD DETAILS",command=add_table3,width=40,fg='red',font=('arial',12,'bold'))
    b1.grid(row=11,column=0)

    b2=tk.Button(frame4,text="VIEW ALL DETAILS",command=view_table3,width=40,fg='red',font=('arial',12,'bold'))
    b2.grid(row=12,column=0)

    b3=tk.Button(frame4,text="DELETE DETAILS",command=delete_table3,width=40,fg='red',font=('arial',12,'bold'))
    b3.grid(row=13,column=0)

    b4=tk.Button(frame4,text="UPDATE INFO",command=update_table3,width=40,fg='red',font=('arial',12,'bold'))
    b4.grid(row=14,column=0)

    b5=tk.Button(frame4,text="CLOSE",command=close,width=40)
    b5.grid(row=15,column=0)

    
    b6=tk.Button(frame4,text="Main Menu",command=lambda:show_frame(frame1),fg='red',font=('arial',12,'bold'))
    b6.grid(row=15,column=1)
#-------------------------------------------------------------------------------frame5----------------------------------------------------------------------------------------#      
    city=tk.StringVar()
    vacancy=tk.StringVar()


    frame2_title=tk.Label(frame5,text="VACANCY",fg='red',bg='sky blue',font=('arial',20,'bold'))
    frame2_title.grid(row=9,column=1,padx=20,pady=20)
    


    label2=tk.Label(frame5,text="City:",fg='red',font=('arial',12,'bold'))
    label2.place(x=0,y=60)

    
    label4=tk.Label(frame5,text="Vacancy:",fg='red',font=('arial',12,'bold'))
    label4.place(x=0,y=120)





    E2=tk.Entry(frame5,textvariable=city)
    E2.place(x=140,y=60)



    E4=tk.Entry(frame5,textvariable=vacancy)
    E4.place(x=140,y=120)




    
    tttt1=tk.Text(frame5,width=150,height=33)
    tttt1.grid(row=10,column=1)
    
    b1=tk.Button(frame5,text="ADD DETAILS",command=add_table4,width=40,fg='red',font=('arial',12,'bold'))
    b1.grid(row=11,column=0)

    b2=tk.Button(frame5,text="VIEW ALL DETAILS",command=view_table4,width=40,fg='red',font=('arial',12,'bold'))
    b2.grid(row=12,column=0)

    b3=tk.Button(frame5,text="DELETE DETAILS",command=delete_table4,width=40,fg='red',font=('arial',12,'bold'))
    b3.grid(row=13,column=0)

    b4=tk.Button(frame5,text="UPDATE INFO",command=update_table4,width=40,fg='red',font=('arial',12,'bold'))
    b4.grid(row=14,column=0)

    b5=tk.Button(frame5,text="CLOSE",command=close,width=40)
    b5.grid(row=15,column=0)

    
    b6=tk.Button(frame5,text="Main Menu",command=lambda:show_frame(frame1),fg='red',font=('arial',12,'bold'))
    b6.grid(row=15,column=1)
#-----------------------------------------------------------------------------frame6------------------------------------------------------------------------------------------------------#
    mno=tk.StringVar()
    medical=tk.StringVar()

    frame2_title=tk.Label(frame6,text="MEDICAL",fg='red',bg='sky blue',font=('arial',20,'bold'))
    frame2_title.grid(row=9,column=1,padx=20,pady=20)

    label2=tk.Label(frame6,text="service no:",fg='red',font=('arial',12,'bold'))
    label2.place(x=0,y=60)


    
    label4=tk.Label(frame6,text="medical status:",fg='red',font=('arial',12,'bold'))
    label4.place(x=0,y=120)




    E2=tk.Entry(frame6,textvariable=mno)
    E2.place(x=140,y=60)


    E4=tk.Entry(frame6,textvariable=medical)
    E4.place(x=140,y=120)


    
    ttttt1=tk.Text(frame6,width=150,height=33)
    ttttt1.grid(row=10,column=1)
    
    b1=tk.Button(frame6,text="ADD DETAILS",command=add_table5,width=40,fg='red',font=('arial',12,'bold'))
    b1.grid(row=11,column=0)

    b2=tk.Button(frame6,text="VIEW ALL DETAILS",command=view_table5,width=40,fg='red',font=('arial',12,'bold'))
    b2.grid(row=12,column=0)

    b3=tk.Button(frame6,text="DELETE DETAILS",command=delete_table5,width=40,fg='red',font=('arial',12,'bold'))
    b3.grid(row=13,column=0)

    b4=tk.Button(frame6,text="UPDATE INFO",command=update_table5,width=40,fg='red',font=('arial',12,'bold'))
    b4.grid(row=14,column=0)

    b5=tk.Button(frame6,text="CLOSE",command=close,width=40,fg='red',font=('arial',12,'bold'))
    b5.grid(row=15,column=0)

    
    b6=tk.Button(frame6,text="Main Menu",command=lambda:show_frame(frame1),fg='red',font=('arial',12,'bold'))
    b6.grid(row=15,column=1)




    show_frame(framel)
    window.mainloop()
