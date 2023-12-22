#import tkinter
import pandas
import csv
from tkinter import *
import face_recognition
from datetime import datetime
import numpy as np
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import pandas
import tkinter
from tkinter import ttk,messagebox,Frame
import pandas as pd
import plotly.express as px
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter.font as f
'''login=Tk()
login.geometry("450x300")
q=Button(login,text="Instructor",command=instructor).place(x = 40,
                                               y = 60) 
p=Button(login,text="Student",command=student).place(x = 40,
                                            y = 100)'''
def attenf():
    root=Tk()
    root.title("Updated Attendance!!")
    root.geometry("1000x600")
    bg= ImageTk.PhotoImage(Image.open("car.jpg"))
    label1 = Label( root, image = bg)
    label1.place(x = 0,y = 0)
    x=40
    y=50
    l=Label(root,text='Date',width=9,height=1,anchor='s')
    l.place(x=x,y=y)
    x+=80
    buttons=[]
    for i in range(10):
              global ki
              def callback(index):
                text = buttons[index].cget("text")
                print(f"buttons[{index}] with text {text!r} clicked")
                root.destroy()
                display(text)
                
              ki=Button(root,text=i+1,width=9,height=1,anchor='s',command=lambda index=len(buttons): callback(index))
              ki.place(x=x,y=y)
              buttons.append(ki)
              x+=80
    '''l=Label(root,text='',width=9,height=1,anchor='s',bg='33DDFF')
    l.place(x=x,y=y)
    x+=80'''
    y+=50
    m=pd.read_csv("attendance.csv")
    for i in range(len(m)):
              x=40
              l=Label(root,text=m.iloc[i]['Date'],width=9,height=1,anchor='s')
              l.place(x=x,y=y)
              x+=80
              for j in range(1,11):
                  l=Label(root,text=m.iloc[i][str(j)],width=9,height=1,anchor='s')
                  l.place(x=x,y=y)
                  x+=80
              y+=50
          
    root.mainloop()
def imgmethod():
    global filename
    filename= askopenfilename()
def display(i):
    i=int(i)
    print('Will  be updated soon')
    print(i)
    window1=Tk()
    window1['bg']='skyblue'
    window1.geometry("1000x600")
    try:
        image = Image.open('C:/Users/Gopi Raju/AppData/Local/Programs/Python/Python310/{}/1.jpeg'.format(i))
        new_image = image.resize((200,200))
        new_image.save('fig1.jpg')
        img = ImageTk.PhotoImage(Image.open("fig1.jpg"))
    except:
        image = Image.open('C:/Users/Gopi Raju/AppData/Local/Programs/Python/Python310/{}/1.jpg'.format(i))
        image=image.rotate(-90)
        new_image = image.resize((200,200))
        new_image.save('fig1.jpg')
        img = ImageTk.PhotoImage(Image.open("fig1.jpg"))
    #Create a Label Widget to display the text or Image
    label = Label(window1, image = img,height=200,width=200)
    label.image=img
    label.place(x=100,y=100)
    label.pack()
    m=pd.read_csv("Student.csv")
    def meth():
        window1.destroy()
        attenf()
    B=Button(window1,text="Get Back to attendance",command=meth,font= ('Helvetica 15 bold'),width=20,height=1,anchor='s')
    B.place(x=370,y=250)
    bfont1 = f.Font(family='Courier', slant = 'italic', size = 15)
    label=Label(window1,text="Name:")
    label['font']=bfont1
    label.place(x=400,y=300)
    label=Label(window1,text=m.iloc[i-1]['Name'])
    label['font']=bfont1
    label.place(x=500,y=300)
    label=Label(window1,text='Phno.:')
    label['font']=bfont1
    label.place(x=400,y=350)
    label=Label(window1,text=m.iloc[i-1]['phone number'])
    label['font']=bfont1
    label.place(x=500,y=350)
    label=Label(window1,text='Cgpa:')
    label['font']=bfont1
    label.place(x=400,y=400)
    label=Label(window1,text=m.iloc[i-1]['Cgpa'])
    label['font']=bfont1
    label.place(x=500,y=400)
    label=Label(window1,text='mail-id:')
    label['font']=bfont1
    label.place(x=400,y=450)
    label=Label(window1,text=m.iloc[i-1]["gmail"])
    label['font']=bfont1
    label.place(x=500,y=450)
    window1.mainloop()
    
    
def video():
    filename1 = askopenfilename()
def take():
    top.destroy()
    window=Tk()
    window.title("attendance collector")
    window.geometry("1000x600")
    lbl_port=tkinter.Label(window,text="Port",fg="green")
    ent_port=tkinter.Entry(window)
    k=Button(window,text="Attendence collector",command=print())
    k.place(x=400,y=365)
    image1 = ImageTk.PhotoImage(Image.open("school.jpg"))
    limg= Label(window, image=image1)
    limg.pack()
    l=Button(window,text="choose the image file",font=("Arial Bold", 10),command=imgmethod)
    p=Button(window,text="click ok to continue",font=("Arial Bold", 10),command=window.destroy)
    l.place(x=400,y=165)
    p.place(x=405,y=265)
    window.mainloop()
    m=[]
    unknown=face_recognition.load_image_file(filename)
    def reverse(string):
        m=''
        for i in range(len(string)-1,-1,-1):
            m+=string[i]
        return m
    add="C:/Users/Gopi Raju/AppData/Local/Programs/Python/Python310"
    result=[False]
    for i in range(10):
        add1=add+"/{}/".format(i+1)
        for j in range(5):
            try:
                known=face_recognition.load_image_file(add1+"{}.jpeg".format(j+1))
                print(add1+"{}.jpeg".format(j+1))
                known_encoding=face_recognition.face_encodings(known)[0]
                unknown_encoding=face_recognition.face_encodings(unknown)[0]
                result=face_recognition.compare_faces([known_encoding],unknown_encoding)
            except Exception as e:
                try:
                    known=face_recognition.load_image_file(add1+"{}.jpeg".format(j+1))
                    known=known.rotate(-90)
                    print(add1+"{}.jpg".format(j+1))
                    known_encoding=face_recognition.face_encodings(known)[0]
                    unknown_encoding=face_recognition.face_encodings(unknown)[0]
                    result=face_recognition.compare_faces([known_encoding],unknown_encoding)
                except:
                    continue
            print(result)
            if(bool(result[0])):
                m.append(i+1)
                print(i+1)
        result.append('-')
    print(m)
    now = datetime.now()
    file=open("attendance.csv",'a+');
    now =str(now)
    now=now[0:11]
    date=reverse(str(now)[-2:-4:-1])+"-"+reverse(str(now)[-5:-7:-1])+"-"+str(now)[:4]
    file.write(date)
    file.write(',')
    for i in range(10):
        if i+1 in m:
            file.write("Present")
        else:
            file.write("absent")
        if i<9:
            file.write(',')
    file.write('')
    file.write('\n')
    file.close()
    '''file = pandas.read_csv("attendence.csv")
    file.columns =['date', '1', '2','3','4','5']
    file.to_csv('test_2.csv')'''
    print("Done!!!!")
    attenf()
    '''
    root=Tk()
    root.title("Updated Attendance!!")
    root.geometry("1000x600")
    bg= ImageTk.PhotoImage(Image.open("car.jpg"))
    label1 = Label( root, image = bg)
    label1.place(x = 0,y = 0)
    x=40
    y=50
    l=Label(root,text='Date',width=9,height=1,anchor='s')
    l.place(x=x,y=y)
    x+=80
    buttons=[]
    for i in range(5):
              global ki
              def callback(index):
                text = buttons[index].cget("text")
                print(f"buttons[{index}] with text {text!r} clicked")
                root.destroy()
                display(text)
                
              ki=Button(root,text=i+1,width=9,height=1,anchor='s',command=lambda index=len(buttons): callback(index))
              ki.place(x=x,y=y)
              buttons.append(ki)
              x+=80
    l=Label(root,text='',width=9,height=1,anchor='s')
    l.place(x=x,y=y)
    x+=80
    y+=50
    with open("attendance.csv", 'r') as file:
      csvreader = file.readlines()
      print(csvreader)
      for i in csvreader[1:]:
          x=40
          p=i.split(',')
          for i in range(len(p)):
              l=Label(root,text=p[i],width=9,height=1,anchor='s')
              l.place(x=x,y=y)
              x+=80
          y+=50
          
    root.mainloop()'''
def call(id,percentage):
    top.destroy()
    window=Tk()
    h=pd.read_csv('Student.csv')
    name=h.iloc[int(id)-1]['Name']
    window.geometry("1000x600")
    window.title("Welcome Student")
    k=Label(window,text='hi').place(x=900,y=900,anchor ='ne')
    window['background']='skyblue'
    bfont1 = f.Font(family='Courier', slant = 'italic', size = 25)
    l=Label(window,text="welcome {}".format(name),font=bfont1,bg='skyblue')
    l.place(x=400,y=20)
    l.pack()
    bfont1 = f.Font(family='Courier', slant = 'italic', size = 10)
    m=Label(window,text="Your attendance percentage is {}".format(round(percentage,2)),font=bfont1,bg='skyblue')
    m.place(x=400,y=100)
    m.pack()
    df=pd.read_csv("attendance.csv")
    fig = px.pie(df, title='attendance percentage', names=id)
    fig.write_image("fig1.jpg")
    print('end')
    image = Image.open('fig1.jpg')
    new_image = image.resize((600,600))
    new_image.save('fig1.jpg')

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("fig1.jpg"))

    #Create a Label Widget to display the text or Image
    label = Label(window, image = img,height=600,width=600)
    label.image=img
    label.place(x=400,y=500)
    label.pack()
    
def instructor():
    global window
    window.destroy()
    global top
    top = Tk()
    top.geometry("450x300") 
    top.title("Login")
    bfont1 = f.Font(family='Courier', slant = 'italic', size = 15)
    def login():
        print(user.get())
        m=pd.read_csv("Instructor.csv")
        print(len(m))
        if(len(m)>=int(user.get())):
           print(m.iloc[(int(user.get()))-1]['Password'],password.get())
           if m.iloc[int(user.get())-1]['Password']==password.get() :
               messagebox.showinfo(title="Login Success", message="You successfully logged in.")
               take()
           else:
            messagebox.showerror(title="Error", message="Invalid login.")
        else:
            messagebox.showerror(title="Error", message="Invalid login.")
    # the label for user_name
    user_name = Label(top,
                      text = "instructor",font=bfont1).place(x = 40,
                                               y = 60) 
       
    # the label for user_password 
    user_password= Label(top,text = "Password",font=bfont1)
    user_password.place(x = 40,y = 100)      
    user= ttk.Entry(top, width =20,font=('Century 12'))
    user.place(x = 170,y = 60) 
       
    password = ttk.Entry(top,width = 20,font=('Century 12'))
    password.place(x = 170,y = 100,)
    submit_button= Button(top,
                           text = "Login",command=login).place(x = 160,
                                                  y = 130)
           
    window.mainloop() 
def student():
    window.destroy()
    global top
    top = Tk()  
    top.geometry("450x300") 
    top.title("Login")
    # the label for user_name
    def login():
        print(user.get())
        m=pd.read_csv("Student.csv")
        print(len(m))
        count=0
        if(len(m)>=int(user.get())):
           print(m.iloc[(int(user.get()))-1]['Password'],password.get())
           if m.iloc[int(user.get())-1]['Password']==password.get() :
               messagebox.showinfo(title="Login Success", message="You successfully logged in.")
               m=pd.read_csv('attendance.csv')
               for i in range(len(m)):
                   if m.iloc[i][user.get()]=='Present':
                       count+=1
               call(user.get(),count*100/len(m))
                   
                   
           else:
            messagebox.showerror(title="Error", message="Invalid login.")
        else:
            messagebox.showerror(title="Error", message="Invalid login.")
    bfont1 = f.Font(family='Courier', slant = 'italic', size = 15)
    user_name = Label(top,
                      text = "Student_id",font=bfont1).place(x = 40,
                                               y = 60) 
       
    # the label for user_password 
    user_password= Label(top,text = "Password",font=bfont1)
    user_password.place(x = 40,y = 100)      
    user= ttk.Entry(top, width = 20,font=('Century 12'))
    user.place(x = 170,y = 60) 
       
    password = ttk.Entry(top,width = 20,font=('Century 12'))
    password.place(x = 170,y = 100,)
    submit_button= Button(top,
                           text = "Login",command=login).place(x = 160,
                                                  y = 130)
    
    
window=Tk()
window.title("select your role")
window.geometry("1000x600")
img=ImageTk.PhotoImage(Image.open("instructor.png"))
img1=ImageTk.PhotoImage(Image.open("studnet.png"))
lbl_port=tkinter.Label(window,text="Port",fg="green")
ent_port=tkinter.Entry(window)
k=Button(window,text="Attendence collector",command=print())
k.place(x=400,y=365)
image = ImageTk.PhotoImage(Image.open("school.jpg"))
limg= Label(window, i=image)
limg.pack()
l=Button(window,image=img,command=instructor,borderwidth = 0,height= 200, width=200,bg='skyblue')
l.borderwidth=0
l["border"] = "0"
p=Button(window,image=img1,command=student,borderwidth = 0,bg='skyblue',height= 200, width=200)
l.place(x=400,y=65)
p["border"] = "0"
p.place(x=405,y=365)
window.mainloop()
