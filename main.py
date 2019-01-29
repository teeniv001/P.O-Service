from Tkinter import *
from tkMessageBox import*
import sqlite3

con = sqlite3.Connection('courierdb')
cur = con.cursor()


root=Tk()

#splash screen
root.configure(bg='pink')
Label(root,text="Post Office Service",font="Aerial 20 ",bd=5,bg='pink').grid(row=1,column=1,columnspan=3)
Label(root,text="Name",font="Aerial 10 bold",bg='pink').grid(row=2,column=1,sticky=E)
Label(root,text=":",font="Aerial 10 bold",bg='pink').grid(row=2,column=2)
Label(root,text="Vineet Kumar Singh",font="Aerial 10 bold",bg='pink').grid(row=2,column=3,sticky=W)
Label(root,text="Branch",font="Aerial 10 bold",bg='pink').grid(row=5,column=1,sticky=E)
Label(root,text=":",font="Aerial 10 bold",bg='pink').grid(row=5,column=2)
Label(root,text="Computer Science",font="Aerial 10 bold",bg='pink').grid(row=5,column=3,sticky=W)
Label(root,text="& Engineering",font="Aerial 10 bold",bg='pink').grid(row=6,column=3,sticky=W)
Label(root,text="Course",font="Aerial 10 bold",bg='pink').grid(row=7,column=1,sticky=E)
Label(root,text=":",font="Aerial 10 bold",bg='pink').grid(row=7,column=2)
Label(root,text="B. Tech (2016-2020)",font="Aerial 10 bold",bg='pink').grid(row=7,column=3,sticky=W)
Label(root,text="E. Mail id",font="Aerial 10 bold",bg='pink').grid(row=8,column=1,sticky=E)
Label(root,text=":",font="Aerial 10 bold",bg='pink').grid(row=8,column=2)
Label(root,text="singhvineet486@gmail.com",font="Aerial 10 bold",bg='pink').grid(row=8,column=3,sticky=W)

#database
cur.execute("create table if not exists couriers (c_type varchar(10), id varchar(10) PRIMARY KEY, name varchar(20), password varchar(10), dob varchar(10), gender varchar(1), address varchar(20), email varchar(20), phone number(10))")
cur.execute("create table if not exists booking (id varchar(10), parcel_no number(5), booking_date varchar(10), from_name varchar(20), from_address varchar(20), from_state varchar(20), from_phone number(10), to_name varchar(20), to_address varchar(20), to_state varchar(10),to_phone number(10), details varchar(20), weight number(10,2))")

def create_acc(c_type,id, name, password,dob,gender,address,email,phone):
    #print c_type , 'in new account'
    cur.execute("insert into couriers values (?,?,?,?,?,?,?,?,?)",(c_type,id, name, password, dob, gender, address, email, phone))
    con.commit()
    cur.execute("select * from couriers")
    #print cur.fetchall()
    
global c_type
def proceed():
    global c_type
    root.destroy()
    img=Tk()
    img.geometry("1280x720")
    image1=PhotoImage(file='.\images\pic7.gif')
    Label(img,image=image1).place(x=0,y=0)
    
    img.configure(bg='#3489e3')
    img.title('COURIER MANAGEMENT SYSTEM')

    Label(img,text='Login',font='jokerman 35 bold',bg='#30cc7c').place(x=670,y=280)
    Label(img,text='user type',font='Aerial 20',bg='#30cc7c').place(x=580,y=420)
    Label(img,text=':',font='Arabic 20',bg='#30cc7c').place(x=710,y=420)
    var=StringVar(img)
    var.set("option")
    OptionMenu(img,var,'Employee','Customer').place(x=760,y=420)
    c_type = var

    Label(img,text='user id',font='Aerial 20',bg='#30cc7c').place(x=580,y=480)
    Label(img,text=':',font='Arabic 20',bg='#30cc7c').place(x=710,y=480)
    id=Entry(img)
    id.place(x=760,y=480)

    Label(img,text='password',font='Aerial 20',bg='#30cc7c').place(x=580,y=520)
    Label(img,text=':',font='Arabic 20',bg='#30cc7c').place(x=710,y=520)
    password=Entry(img,show="*")
    password.place(x=760,y=530)
       
    
    def login_customer(c_type, user_id):
        lc= Toplevel()
        lc.geometry("1280x720")
        imagec=PhotoImage(file=".\images\pic15.gif")
        Label(lc,image=imagec).place(x=0,y=0)
        Label(lc, text='CUSTOMER LOGIN',font='Helvetica 22 bold').place(x=560, y=4)
        Label(lc,text='We keep Your Promises',font='Helvetica 15 bold',bg='#8d6c4c').place(x=30,y=40)
        Label(lc,text='Be Absolutely Sure',font='Helvetica 15 bold',bg='#8d6c4c').place(x=30,y=70)
        Button(lc, text='Home',width=15,height=2,bd=5).place(x=75, y=185)
        def lcd():
            pd=Toplevel()
            Label(pd,text='courier Detail',font='times 20 bold').grid(row=2,column=0)
            Label(pd,text='select the querry options').grid(row=3,column=0)
            r1=IntVar()
            Radiobutton(pd,text='parcel number',variable=r1,value=1).grid(row=3,column=1)
            r2=Entry(pd)
            r2.grid(row=3,column=2)
            
            Radiobutton(pd,text='All',variable=r1,value=2).grid(row=4,column=1)
            def view(r1):
                if r1.get()==1:
                    cur.execute("select id from booking where parcel_no=?",[r2.get()])
                    cust_id = cur.fetchall()[0][0]
                    
                    cur.execute("select * from booking where id = ?",[cust_id])
                    details = cur.fetchall()
                    
                  ######database table

                    col_val=0                
                    a = ['Id','Parcel No', ' Booking Date', 'From Name', 'From Address', 'From State', 'From phone', 'To Name', 'To Address', 'To State', 'To Phone', 'Detail', 'Weight']
                    
                    for val in details:
                        row_val=5
                        field_index=0
                        for inval in val:
                            Label(pd, text=a[field_index]).grid(row = row_val, column=col_val)
                            e = Entry(pd)
                            e.grid(row=row_val, column=col_val+1)
                            e.insert(0,inval)
                            row_val+=1
                            field_index+=1
                        
                elif(r1.get()==2):
                    cur.execute("select * from booking ")
                    r=Tk()
                    details = cur.fetchall()
                    height = 0
                    col_val=0
                    for val in details:
                        row_val = 0
                        for inval in val:
                            e = Entry(r)
                            e.grid(row=row_val, column=col_val)
                            e.insert(0,inval)
                            row_val+=1
                        col_val+=2
                    r.mainloop()
                        

            Button(pd,text='view',command=lambda:view(r1)).grid(row=4,column=5)

            def back5():
                pd.destroy()
                lc()
            Button(pd,text='back',command=back5).grid(row=6,column=5)
            
        
        Button(lc, text='Courier Details',width=15,height=2,bd=5,command=lcd).place(x=75, y=250)

        def back4():
            lc.destroy()
            proceed()
        Button(lc, text='Logout',width=15,height=2,bd=5,command=back4).place(x=75, y=315)
        
        lc.mainloop()
        
       
    def login(c_type,id):
        img.destroy()
        cm= Tk()
        cm.geometry("1280x720")
        imageb=PhotoImage(file='.\images\pic11.gif')
        Label(cm,image=imageb).place(x=0,y=0)
        
        Label(cm, text='EMPLOYEE LOGIN',font='Helvetica 22 bold',bg='#147cfc').place(x=590, y=2)
        Label(cm,text='welcome to our courier services',font='consolas 18 bold',bg='#147cfc',fg='#cd0706').place(x=390,y=65)
        Button(cm, text='Home',width=15,height=2,bd=5).place(x=200, y=300)
        
        def booking():
            cb=Toplevel()
            cb.geometry('1280x720')
            imagea=PhotoImage(file='.\images\pic10.gif')
            Label(cb,image=imagea).place(x=0,y=0)
            Label(cb,text='BOOKING FORM',font='times 20 bold',bg='white').place(x=400,y=80)
            Label(cb,text='parcel no.',font='Arabic 12',bg='white',bd=5).place(x=400,y=120)
            pn=Entry(cb)
            pn.place(x=400,y=155)
            
            Label(cb,text='user id',font='Arabic 12',bg='white',bd=5).place(x=780,y=120)
            id=Entry(cb)
            id.place(x=780,y=155)
            
            Label(cb,text='Booking Date',font='Arabic 12',bg='white',bd=5).place(x=400,y=180)
            bd=Entry(cb)
            bd.place(x=400,y=225)
            
            Label(cb,text='From Address',font='times 10 bold',bg='white').place(x=400,y=245)
            
            Label(cb,text='Name').place(x=400,y=275)
            name1=Entry(cb)
            name1.place(x=400,y=295)
            
            Label(cb,text='Address').place(x=800,y=275)
            add1=Entry(cb)
            add1.place(x=760,y=295)
            
            Label(cb,text='state').place(x=400,y=335)
            state1=Entry(cb)
            state1.place(x=400,y=365)
            
            Label(cb,text='phone no.').place(x=800,y=335)
            phone1=Entry(cb)
            phone1.place(x=760,y=365)

            Label(cb,text='To Address',font='time 10 bold').place(x=400,y=400)
            Label(cb,text='Name').place(x=400,y=435)
            name2=Entry(cb)
            name2.place(x=400,y=455)
            Label(cb,text='Address').place(x=800,y=435)
            add2=Entry(cb)
            add2.place(x=800,y=455)
            Label(cb,text='state').place(x=400,y=495)
            state2=Entry(cb)
            state2.place(x=400,y=515)
            Label(cb,text='phone no.').place(x=800,y=495)
            phone2=Entry(cb)
            phone2.place(x=800,y=515)
            Label(cb,text='Courier Details').place(x=400,y=545)
            cd=Entry(cb)
            cd.place(x=400,y=565)
            Label(cb,text='weight').place(x=800,y=545)
            weight=Entry(cb)
            weight.place(x=800,y=565)

            def submit(id, parcel,booking_date, from_name, from_address, from_state, from_phone, to_name, to_address, to_state, to_phone, detail, weight):
                cur.execute("insert into booking values (?,?,?,?,?,?,?,?,?,?,?,?,?)",(id+'C', parcel, booking_date,from_name, from_address, from_state, from_phone, to_name, to_address, to_state, to_phone, detail, weight))
                con.commit()
                showinfo('INSERTED', 'BOOKING ACCEPTED')


            def clear():
                pn.delete(0,END)
                id.delete(0,END)
                bd.delete(0,END)
                name1.delete(0,END)
                add1.delete(0,END)
                state1.delete(0,END)
                phone1.delete(0,END)
                name2.delete(0,END)
                add2.delete(0,END)
                state2.delete(0,END)
                phone2.delete(0,END)
                cd.delete(0,END)
                weight.delete(0,END)
                
            Button(cb,text='submit',command=lambda:submit(id.get(), pn.get(),bd.get(),name1.get(), add1.get(), state1.get(), phone1.get(), name2.get(), add2.get(), state2.get(), phone2.get(), cd.get(), weight.get())).place(x=700,y=605)
            Button(cb,text='reset',command=clear).place(x=500,y=605)

            def back3():
                cb.destroy()
                cm()
            Button(cb,text='back',command=back3).place(x=600,y=605)

            cb.mainloop()
        Button(cm, text='Courier Booking',width=15,height=2,bd=5,command=booking).place(x=570, y=300)

        def fun(cm):
            cm.destroy()
            proceed()
        Button(cm, text='Logout',width=15,height=2,bd=5,command=lambda:fun(cm)).place(x=1000, y=300)
        cm.mainloop()

        
    def validate(id,real_password,c_type):
        cur.execute("select password from couriers where id = ?", [id])
        
        password = cur.fetchall()[0][0]
        
        entered_pass = password
        cur.execute("select c_type from couriers where id = ?", [id])
        real_c_type = cur.fetchall()[0][0]
        
        if (real_password == entered_pass and c_type.get()==real_c_type and c_type.get()=='Employee'):
        
            login(c_type, id)
        elif(real_password == entered_pass and c_type.get()==real_c_type and c_type.get()=='Customer'):
            login_customer(c_type,id)
        else:
            showerror('ERROR', 'PASSWORD and USER_ID DONT MATCH')
                    
    Button(img,text='Login',width='13',command=lambda:validate(id.get()+c_type.get()[0],password.get(),c_type),bd='7').place(x=780,y=580)

    def new_user(c_type):
        new=Toplevel()
        new.geometry("1280x720")
        images=PhotoImage(file=".\images\pic9.gif")
        Label(new,image=images).place(x=0,y=0)
        user = c_type.get()
        new.title(user+' REGISTRATION')
        Label(new,text=user+' ID   :',font='Helvetica 15',bg='#d9374e').place(x=70,y=200)
        
        id=Entry(new)
        id.place(x=200,y=207)
        
        Label(new,text=user+' Name :',font='Helvetica 15',bg='#d9374e').place(x=70,y=240)
        name=Entry(new)
        name.place(x=200,y=247)
        
        Label(new,text='Password:',font='Helvetica 15 ',bg='#d9374e').place(x=80,y=280)
        
        password=Entry(new)
        password.place(x=200,y=282)
        
        Label(new,text='Date of Birth :',font='Helvetica 15',bg='#d9374e').place(x=70,y=320)
        
        dob=Entry(new)
        dob.place(x=200,y=322)
        
        v1=IntVar()
        Label(new,text='Gender     :',font='Helvetica 15',bg='#d9374e').place(x=85,y=360)
       
        Radiobutton(new,text='Male',variable=v1,value=1).place(x=200,y=362)
        Radiobutton(new,text='Female',variable=v1,value=2).place(x=280,y=362)
        gender = v1.get()
        
        def choice():
            Label(new,text=v1.get()).place(x=85,y=362)
        
        Label(new,text='Address     :',font='Helvetica 15',bg='#d9374e').place(x=85,y=400)   
        
        address=Entry(new)
        address.place(x=200,y=402)
        
        Label(new,text='Email_ID    :',font='Helvetica 15',bg='#d9374e').place(x=85,y=440)
        
        email=Entry(new)
        email.place(x=200,y=442)
        
        Label(new,text='Phone no.   :',font='Helvetica 15',bg='#d9374e').place(x=80,y=480)
        
        phone=Entry(new)
        phone.place(x=200,y=482)
        def clear():
            id.delete(0,END)
            name.delete(0,END)
            password.delete(0,END)
            dob.delete(0,END)
            address.delete(0,END)
            email.delete(0,END)
            phone.delete(0,END)
            
        Button(new,text='reset',command=clear).place(x=200,y=540)
        
        def cmd():
            showinfo('SUCCESSFULL', "Your account is created")
            create_acc(c_type.get(),id.get()+c_type.get()[0],name.get(),password.get(),dob.get(),gender,address.get(),email.get(),phone.get())
            
        Button(new,text='OK',command=cmd).place(x=320,y=540)
        new.mainloop()
    Button(img,text='create your account',bd='7',command=lambda:new_user(var)).place(x=600,y=580)

    img.mainloop()
Button(root,text="Press To Proceed To Project",font="ariel 15 bold",bd=5,command=proceed).grid(row=10,column=1,columnspan=3,sticky='nwes')
root.mainloop()
