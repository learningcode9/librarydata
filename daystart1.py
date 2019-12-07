from tkinter import *
from tkinter import ttk
from datetime import datetime
import backend
from tabulate import tabulate



def select_date1():
    now=datetime.now()
    Entrytime = now.strftime("%Y-%m-%d , %I:%M %p")
    #print(s1)
    if(first_name.get()=="" or last_name.get()=="" or employee_id.get()==""):
        pass
    else:
        space='                                  '
        listbox.insert(END,Entrytime)
        backend.insert1(first_name.get(),last_name.get(),employee_id.get(),Entrytime)
        listbox.delete(0,END)
        listbox.insert(END, "Firstname                      \t\t\t\t\t\t  Lastname                             \t\t\t\t\t\t  Employeeid                             \t\t\t\t\t\t  Entrytime\n")
        listbox.insert(END,"--------------------------------------------------------------------------------------------------------------------------------------------")
        listbox.insert(END,"\n")
        listbox.insert(END,(first_name.get()+space+last_name.get()+space+employee_id.get()+space+Entrytime))
        
#def get_selected_row():
   
def select_date2():
  
    now=datetime.now()
    Exittime = now.strftime("%m/%d/%Y, %I:%M %p")
    if(first_name.get()=="" or last_name.get()=="" or employee_id.get()==""):
        pass
    else:
        listbox.insert(END,Exittime)
        backend.insert2(first_name.get(),last_name.get(),employee_id.get(),Exittime)
        listbox.delete(0,END)
        listbox.insert(END, "Firstname                      \t\t\t\t\t\t  Lastname                             \t\t\t\t\t\t  Employeeid                             \t\t\t\t\t\t  Exittime\n")
        listbox.insert(END,"--------------------------------------------------------------------------------------------------------------------------------------------")
        listbox.insert(END,"\n")
        listbox.insert(END,(first_name.get(),last_name.get(),employee_id.get(),Exittime))
    
def view_command():
    listbox.delete(0,END)
    listbox.insert(END, "Firstname                      \t\t\t\t\t\t  Lastname                             \t\t\t\t\t\t  Employeeid                             \t\t\t\t\t\t  Entrytime\n")
    listbox.insert(END,"--------------------------------------------------------------------------------------------------------------------------------------------")
    listbox.insert(END,"\n")
    for row in backend.view1():
        listbox.insert(END,row)

def view_exit():
    listbox.delete(0,END)
    listbox.insert(END, "Firstname                      \t\t\t\t\t\t  Lastname                             \t\t\t\t\t\t  Employeeid                             \t\t\t\t\t\t  Exittime\n")
    listbox.insert(END,"--------------------------------------------------------------------------------------------------------------------------------------------")
    listbox.insert(END,"\n")
    for row in backend.view2():
        listbox.insert(END,row)

def search_command():
    listbox.delete(0,END)
    listbox.delete(0,END)
    listbox.insert(END, "Firstname               \t\t\t\t\t\t  Lastname                  \t\t\t\t\t\t  Employeeid                   \t\t\t\t\t\t  Entrytime                \t\t\t\t\t\t Exittime\n")
    listbox.insert(END,"--------------------------------------------------------------------------------------------------------------------------------------------")
    listbox.insert(END,"\n")
    for row in backend.search(first_name.get() ,last_name.get(), employee_id.get()):
       listbox.insert(END,row)



#print(type(window))
window=Tk()
window.wm_title("Library register")
frame1=Frame(window)
frame1.pack()
treeview=ttk.Treeview(window)

    
l1=Label(frame1,text="Firstname",font="Times 12 bold",width=12)
l1.grid(row=0,column=0)
l2=Label(frame1,text="Lastname",font="Times 12 bold",width=12)
l2.grid(row=0,column=2)
l3=Label(frame1,text="EmployeeId",font="Times 12 bold",width=12)
l3.grid(row=1,column=0)

first_name=StringVar()
e1=Entry(frame1,width=25,textvariable=first_name)
e1.grid(row=0,column=1)
e1.focus()
last_name=StringVar()
e2=Entry(frame1,width=25,textvariable=last_name)
e2.grid(row=0,column=3)
employee_id=StringVar()
e3=Entry(frame1,width=25,textvariable=employee_id)
e3.grid(row=1,column=1)

frame2 = Frame(window)       
frame2.pack()

b1=Button(frame2,text="TimeIn",font="Times 11",width=9,command=select_date1)
b1.grid(row=5,column=0)
b2=Button(frame2,text="TimeOut",font="Times 11",width=9,command=select_date2)
b2.grid(row=5,column=1)
b3=Button(frame2,text="ViewEntries",font="Times 11",width=9,command=view_command)
b3.grid(row=5,column=2)
b3=Button(frame2,text="Viewexit",font="Times 11",width=9,command=view_exit)
b3.grid(row=5,column=3)
b4=Button(frame2,text="Search",font="Times 11",width=9,command=search_command)
b4.grid(row=5,column=4)
b5=Button(frame2,text="Close",font="Times 11",width=9,command=window.destroy)
b5.grid(row=5,column=5)


frame3 = Frame(window)       
frame3.pack()
scroll = Scrollbar(frame3, orient=VERTICAL)
listbox= Listbox(frame3, yscrollcommand=scroll.set,font="Times 11",width=80,height=16)

scroll.config(command=listbox.yview)
scroll.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH,expand=1)
#window.configure(background='#a9a9a9')
window.resizable(width=False,height=False)

#width_of_window=600
#height_of_window=300

#screen_width=window.winfo_screenwidth()
#screen_height=window.winfo_screenheight()

#x_coordinates = (screen_width/2)-(width_of_window/2)
#y_coordinates = (screen_height/2)-(height_of_window/2)

#window.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinates,y_coordinates))

#l1=Label(window,text='Firstname ',bg="#a9a9a9",font="TIMES 12 bold",pady=7,width=10)
#l1.grid(row=0,column=0)

#l2=Label(window,text='Lastname ',bg="#a9a9a9",font="TIMES 12 bold",pady=5,width=10)
#l2.grid(row=1,column=0)

#first_name=StringVar()
#e1=Entry(window,exportselection=0,width=25,textvariable=first_name)
#e1.grid(row=0,column=1)

#last_name=StringVar()
#e2=Entry(window,exportselection=0,width=25,textvariable=last_name)
#e2.grid(row=1,column=1)

#list1=Listbox(window,height=9,width=48)
#list1.grid(row=2,column=0,padx=2,pady=1,rowspan=5,columnspan=4)

#sb1=Scrollbar(window)
#sb1.grid(row=2,column=4,rowspan=6,padx=4)

#list1.configure(yscrollcommand=sb1.set)
#sb1.configure(command = list1.yview)

#list1.bind('<<ListboxSelect>>',get_selected_row)

#b1=Button(window,text="TimeIn", width=14,font="Times 12",command=select_date1)
#b1.grid(row=0,column=6)

#b2=Button(window,text="TimeOut", width=14,pady=5,font="Times 12",command=select_date2)
#b2.grid(row=1,column=6)

#b3=Button(window,text="ViewEntries", width=14,pady=5,font="Times 12",command=view_command)
#b3.grid(row=2,column=6)

#b4=Button(window,text="Viewexit", width=14,font="Times 12",command=view_exit)
#b4.grid(row=3,column=6)

#b5=Button(window,text="Search", width=14,pady=5,font="Times 12",command=search_command)
#b5.grid(row=4,column=6)

#b6=Button(window,text="Close",width=14,font="Times 12",command=window.destroy)
#b6.grid(row=5,column=6)

window.mainloop()
