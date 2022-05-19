def addgraduate():
    
    path = 'images'
    images = []
    personNames = []
    myList = os.listdir(path)
    print(myList)
    for cu_img in myList:
        current_Img = cv2.imread(f'{path}/{cu_img}')
        images.append(current_Img)
        personNames.append(os.path.splitext(cu_img)[0])
    print(personNames)


    def faceEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList


    def attendance(name):
        myDataList = []
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.now()
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%y')
            print(tStr,dStr,name)
            strr = 'insert into GRADUATES values(%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(name,tStr,dStr,"wake up","sleep"))
            con.commit()
            res = messagebox.askyesnocancel('Notifications',' Added sucessfully.. and Do you want to clean the form')
            showgraduate()

    encodeListKnown = faceEncodings(images)
    print('All Encodings Complete!!!')
    cap = cv2.VideoCapture(0)
    flag=False
    cap = cv2.VideoCapture(0)
    timeout = time.time() + 5

    while time.time() < timeout:
        ret, frame = cap.read()
        faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

        facesCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

        for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                flag=True
                name = personNames[matchIndex].upper()
                print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                attendance(name)

        cv2.imshow('Webcam', frame)
        if flag:
            break

    cap.release()
    cv2.destroyAllWindows()

def searchgraduate():
    def search():
        id = idval.get()
        name = nameval.get()
        company_name = company_nameval.get()
        job_type = job_typeval.get()
        package = packageval.get()
        company_id = company_idval.get()
        phone_no = phone_noval.get()

        if(id != ''):
            strr = 'select *from GRADUATES where STUDENT_ID =%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            graduatetable.delete(*graduatetable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[1],i[2],i[0]]
                graduatetable.insert('', END, values=vv)
        elif(name != ''):
            strr = 'select *from GRADUATES  where STUDENT_NAME=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            graduatetable.delete(*graduatetable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[1],i[2],i[0]]
                graduatetable.insert('', END, values=vv)
        elif(company_name != ''):
            strr = 'select *from GRADUATES  where COMPANY_NAME=%s'
            mycursor.execute(strr,(company_name))
            datas = mycursor.fetchall()
            graduatetable.delete(*graduatetable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[1],i[2],i[0]]
                graduatetable.insert('', END, values=vv)
        elif(job_type != ''):
            strr = 'select *from GRADUATES  where COMPANY_ID=%s'
            mycursor.execute(strr,(job_type))
            datas = mycursor.fetchall()
            graduatetable.delete(*graduatetable.get_children())
            for i in datas:
                vv = [i[0],i[1],i[1],i[2],i[0]]
                graduatetable.insert('', END, values=vv)
      
        
       



    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Search Database')
    searchroot.config(bg='SeaGreen2')
    searchroot.resizable(False,False)
    #--------------------------------------------------- Add studenmt Labels
    idlabel = Label(searchroot,text='Enter Graduate ID : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=22,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text='Enter Graduate Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=22,anchor='w')
    namelabel.place(x=10,y=70)

    company_namelabel = Label(searchroot,text='Enter Company Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=22,anchor='w')
    company_namelabel.place(x=10,y=130)

    job_typelabel = Label(searchroot,text='Enter Company ID: ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=22,anchor='w')
    job_typelabel.place(x=10,y=190)

    packagelabel = Label(searchroot,text='Enter Job type : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=22,anchor='w')
    packagelabel.place(x=10,y=250)

    company_idlabel = Label(searchroot,text='Enter Package : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=22,anchor='w')
    company_idlabel.place(x=10,y=310)

    phone_nolabel = Label(searchroot,text='Enter Phone : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=22,anchor='w')
    phone_nolabel.place(x=10,y=370)


    ##----------------------------------------------------------- Add student Entry
    idval = StringVar()
    nameval = StringVar()
    company_nameval = StringVar()
    job_typeval = StringVar()
    packageval = StringVar()
    company_idval = StringVar()
    phone_noval = StringVar()


    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    company_nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=company_nameval)
    company_nameentry.place(x=250,y=130)

    job_typeentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=job_typeval)
    job_typeentry.place(x=250,y=190)

    packageentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=packageval)
    packageentry.place(x=250,y=250)

    company_identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=company_idval)
    company_identry.place(x=250,y=310)

    phone_noentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=phone_noval)
    phone_noentry.place(x=250,y=370)


    ############------------------------- add button
    submitbtn = Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',height=2,
                      bg='red',command=search)
    submitbtn.place(x=150,y=480)



    searchroot.mainloop()
def deletegraduate():
    cc = graduatetable.focus()
    content = graduatetable.item(cc)
    pp = content['values'][0]
    strr = 'delete from GRADUATES where STUDENT_ID=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','RECORD ID: {} Deleted Sucessfully'.format(pp))
    strr = 'select *from GRADUATES'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    graduatetable.delete(*graduatetable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[1],i[2],i[0]]
        graduatetable.insert('', END, values=vv)


def showgraduate():
    strr = 'select * from GRADUATES'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    graduatetable.delete(*graduatetable.get_children())
    for i in datas:
        vv = [i[0],i[1],i[1],i[2],i[0]]
        graduatetable.insert('', END, values=vv)

def exitgraduate():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res == True):
        root.destroy()


###################################################################################Connecttion of Database
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()

        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Incorrect Login Credentials',parent=dbroot)
            return
        try:
            strr = 'create database pd100'
            mycursor.execute(strr)
            strr = 'use pd100'
            mycursor.execute(strr)
            #strr = 'CREATE TABLE COMPANY(COMPANY_ID VARCHAR(20) PRIMARY KEY ,COMPANY_NAME VARCHAR(20),CONTACT_NO VARCHAR(20),LOCATION VARCHAR(20))'
            #mycursor.execute(strr)
            strr = 'CREATE TABLE GRADUATES(STUDENT_ID VARCHAR(20) ,STUDENT_NAME varchar(20),COMPANY_NAME varchar(20),Date varchar(20),PHONE_NO varchar(20))'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Database created and Successfully Connected to  Database ',parent=dbroot)

        except:
            strr = 'use pd100'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Successfully connected to Existing database ....',parent=dbroot)
        dbroot.destroy()



    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='SeaGreen2')
    #-------------------------------Connectdb Labels
    hostlabel = Label(dbroot,text="Enter Host : ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User : ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter Password: ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

    #-------------------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    #-------------------------------- Connectdb button
    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',
                          activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()
###########################################



##########################################################################################################
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
import cv2
from tkinter import ttk
import numpy as np
import face_recognition
import os
from datetime import datetime
#import pandas
import pymysql
import time
root = Tk()
root.title("Cambridge Attendence MANAGEMENT SYSTEM")
root.config(bg='LightSkyBlue1')
root.geometry('1174x700+200+50')
root.resizable(False,False)
############################################################################################################  Frames
##---------------------------------------------------------------------------- dataentry frame

    
DataEntryFrame = Frame(root,bg='palegreen',relief=SUNKEN,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel = Label(DataEntryFrame,text='--------------------WELCOME--------------------',width=30,font=('ariel',22,'italic bold'))
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame,text='1.Add ',width=25,height=2,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='red',command=addgraduate)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2.Search',width=25,height=2,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='red',command=searchgraduate)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3.Delete',width=25,height=2,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='red',command=deletegraduate)
deletebtn.pack(side=TOP,expand=True)


showallbtn = Button(DataEntryFrame,text='4.Display',width=25,height=2,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='red',command=showgraduate)
showallbtn.pack(side=TOP,expand=True)


exitbtn = Button(DataEntryFrame,text='6.Quit',width=25,height=2,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='red',command=exitgraduate)
exitbtn.pack(side=TOP,expand=True)

##-----------------------------------------------------------Show data frame
ShowDataFrame = Frame(root,bg='azure2',relief=SUNKEN,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=600,height=600)

##-------------------------------------------------  Showdataframe
style = ttk.Style()
style.configure('Treeview.Heading',font=('times',20,'bold'),background='azure3',foreground='black')
style.configure('Treeview',font=('times',15,'bold'),background='azure3',foreground='black')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
graduatetable = Treeview(ShowDataFrame,columns=('Student ID','Student Name','Phone No','Date','Company Name'),
                      yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=graduatetable.xview)
scroll_y.config(command=graduatetable.yview)
graduatetable.heading('Student ID',text='Student ID')
graduatetable.heading('Student Name',text='Student Name')
graduatetable.heading('Phone No',text='Phone No')
graduatetable.heading('Date',text='Date')
graduatetable.heading('Company Name',text='Company Name')



graduatetable['show'] = 'headings'
graduatetable.column('Student ID',width=150)
graduatetable.column('Student Name',width=200)
graduatetable.column('Phone No',width=200)
graduatetable.column('Date',width=200)
graduatetable.column('Company Name',width=150)



graduatetable.pack(fill=BOTH,expand=1)
################################################################################################################  Slider
ss = "Cambridge Attendence Management System"
count = 0
text = ''
##################################
SliderLabel = Label(root,text=ss,font=("Helvetica",20,'bold'),relief=RAISED,border=3)
SliderLabel.place(x=200,y=0)

############################################################################################################### clock

################################################################################################################## ConnectDatabaseButton
connectbutton = Button(root,text='Login',width=13,font=('chiller',15,'italic bold'),relief=RIDGE,borderwidth=7,bg='green2',
                       activebackground='black',activeforeground='blue',height=2,command=Connectdb)
connectbutton.place(x=950,y=0)
root.mainloop()
