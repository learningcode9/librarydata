from tkinter import *
import datetime
import backend

def timeIn():
    
    entryTime=(datetime.datetime.now())
    if(first_name.get()=="" or last_name.get()=="" or employee_id.get()==""):
        pass
    entryCount=0
    exitCount=0
    empID=employee_id.get()
    for item in backend.entry_count():
        if(item[0]==empID):
            entryCount=item[1]
        #print(item[4])
    #if(len(backend.Count_exit())>0):  
        for items in backend.exit_count():
            if(items[0]==empID):
                exitCount=items[1]
    
    if entryCount-exitCount==0:
        listbox.insert(END,entryTime)
        #listbox.insert(END,Entrytime)
        backend.insert_entrytime(first_name.get(),last_name.get(),employee_id.get(),entryTime,entryTime.strftime("%x"))
        listbox.delete(0,END)
        listbox.insert(END,"\n")
        listbox.insert(END, "Firstname                   \t\t\t\t\t\t  Lastname                          \t\t\t\t\t\t  Employeeid                          \t\t\t\t\t\t  Entrytime\n")
        listbox.insert(END,"--------------------------------------------------------------------------------------------------------------------------------------------")
        listbox.insert(END," ",(first_name.get()+"  "+last_name.get()+","+"  "+employee_id.get()+","+"  "+str(entryTime)))
    else:
        listbox.insert(END,'Invalid Entry') 
def timeOut():
    
    exitTime=datetime.datetime.now()
    if(first_name.get()=="" or last_name.get()=="" or employee_id.get()==""):
        pass
    entryCount=0
    exitCount=0
    empID=employee_id.get()
    for item in backend.entry_count():
        if(item[0]==empID):
            entryCount=item[1]
        #print(item[4])
    # if(len(backend.Count_exit())>0):  
        for items in backend.exit_count():
            if(items[0]==empID):
                exitCount=items[1]
        #print(items[4])
    if entryCount-exitCount==1:
        listbox.insert(END,exitTime)
        backend.insert_exittime(first_name.get(),last_name.get(),employee_id.get(),exitTime,exitTime.strftime("%x"))
        listbox.delete(0,END)
        listbox.insert(END,"\n")
        listbox.insert(END, "Firstname                   \t\t\t\t\t\t  Lastname                          \t\t\t\t\t\t  Employeeid                          \t\t\t\t\t\t  Entrytime\n")
        listbox.insert(END,"--------------------------------------------------------------------------------------------------------------------------------------------")
        listbox.insert(END," ",(first_name.get()+"  "+last_name.get()+","+"  "+employee_id.get()+","+"  "+str(exitTime)))
    else:
        listbox.insert(END,'Invalid Entry')    
def view_entries():
    space='                        '
    listbox.delete(0,END)
    listbox.insert(END,"\n")
    listbox.insert(END, "Firstname"+space+"Lastname"+space+"Employeeid"+space+"Entrytime\n")
    listbox.insert(END,"--------------------------------------------------------------------------------------------------------------------------------------------")
    for item in backend.all_employee_entry_details():
        listbox.insert(END,"  ",item[0]+"  "+item[1]+","+"  "+item[2]+" ,"+"  "+item[3])
        
def view_exit():
    space='                        '
    listbox.delete(0,END)
    listbox.insert(END,"\n")
    listbox.insert(END, "Firstname"+space+"Lastname"+space+"Employeeid"+space+"Exittime\n")
    listbox.insert(END,"--------------------------------------------------------------------------------------------------------------------------------------------")
    for rows in backend.all_employee_exit_details():
        listbox.insert(END," ",rows[0]+" "+rows[1]+","+" "+rows[2]+" ,"+" "+rows[3])
        
       
def search_command():
    listbox.delete(0,END)
    listbox.delete(0,END)
    listbox.insert(END,"\n")
    listbox.insert(END, "Firstname            \t\t\t\t\t\t  Lastname               \t\t\t\t\t\t  Employeeid                \t\t\t\t\t\t  Entrytime           \t\t\t\t\t\t Exittime\n")
    listbox.insert(END,"--------------------------------------------------------------------------------------------------------------------------------------------")
  
    for row in backend.search(first_name.get(),last_name.get(),employee_id.get()):
       listbox.insert(END,"  ",row[0]+"  "+row[1]+","+"  "+row[2]+" ,"+"  "+row[3]+" ,"+"  "+row[4])
    

#Creating a window and title for project
window=Tk()
window.wm_title("Library register")

#Creating 1st frame in a window
frame1=Frame(window)
frame1.pack()

#Add labels in frame1
l1=Label(frame1,text="Firstname",font="Times 12 bold",width=12)
l1.grid(row=0,column=0)
l2=Label(frame1,text="Lastname",font="Times 12 bold",width=12)
l2.grid(row=0,column=2)
l3=Label(frame1,text="EmployeeId",font="Times 12 bold",width=12)
l3.grid(row=1,column=0)

#creating entry boxes according to labels in frame1
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

#creating frame2 in window
frame2 = Frame(window)       
frame2.pack()

#Adding buttons in window
b1=Button(frame2,text="TimeIn",font="Times 11",width=9,command=timeIn)
b1.grid(row=5,column=0)
b2=Button(frame2,text="TimeOut",font="Times 11",width=9,command=timeOut)
b2.grid(row=5,column=1)
b3=Button(frame2,text="ViewEntries",font="Times 11",width=9,command=view_entries)
b3.grid(row=5,column=2)
b4=Button(frame2,text="Viewexit",font="Times 11",width=9,command=view_exit)
b4.grid(row=5,column=3)
b5=Button(frame2,text="Search",font="Times 11",width=9,command=search_command)
b5.grid(row=5,column=4)
b6=Button(frame2,text="Close",font="Times 11",width=9,command=window.destroy)
b6.grid(row=5,column=5)

#Creating frame3 in window
frame3 = Frame(window)       
frame3.pack()
#Adding scrollbar and listbox in frame3
scroll = Scrollbar(frame3, orient=VERTICAL)
listbox= Listbox(frame3, yscrollcommand=scroll.set,font="Times 11",width=80,height=16)

scroll.config(command=listbox.yview)
scroll.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH,expand=1)

#Window size is fixed
window.resizable(width=False,height=False)
#If you don’t include window.mainloop() at the end of a program in a Python file, then the Tkinter application will never run, and nothing will be displayed
window.mainloop()
