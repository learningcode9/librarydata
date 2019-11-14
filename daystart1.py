from tkinter import *
from datetime import datetime
import backend

def select_date1():
    now=datetime.now()
    s1 = now.strftime("%Y-%m-%d , %I:%M %p")
    #print(s1)
    list1.insert(END,s1)
    backend.insert1(first_name.get(),last_name.get(),s1)
    list1.delete(0,END)
    list1.insert(END,(first_name.get(),last_name.get(),s1))
#def get_selected_row():

def select_date2():
    now=datetime.now()
    s2 = now.strftime("%m/%d/%Y, %I:%M %p")
    #l4=Label(window,text=s2,pady=16)
    #l4.grid(row=7,column=2)
    list1.insert(END,s2)
    backend.insert2(first_name.get(),last_name.get(),s2)
    list1.delete(0,END)
    list1.insert(END,(first_name.get(),last_name.get(),s2))
    

def view_command():
    list1.delete(0,END)
    for row in backend.view1():
        list1.insert(END,row)

def view_exit():
    list1.delete(0,END)
    for row in backend.view2():
        list1.insert(END,row)

window = Tk()
#print(type(window))
window.wm_title("Library register")
window.configure(background='#a9a9a9')
window.resizable(width=False,height=False)

width_of_window=400
height_of_window=200

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x_coordinates = (screen_width/2)-(width_of_window/2)
y_coordinates = (screen_height/2)-(height_of_window/2)

window.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinates,y_coordinates))

l1=Label(window,text='Firstname *',bg="#a9a9a9",font="TIMES 12 bold",pady=5,width=10)
l1.grid(row=0,column=0)

l2=Label(window,text='Lastname *',bg="#a9a9a9",font="TIMES 12 bold",pady=5,width=10)
l2.grid(row=1,column=0)

first_name=StringVar()
e1=Entry(window,exportselection=0,textvariable=first_name)
e1.grid(row=0,column=1)



last_name=StringVar()
e2=Entry(window,exportselection=0,textvariable=last_name)
e2.grid(row=1,column=1)

list1=Listbox(window,height=8,width=35)
list1.grid(row=2,column=0,pady=5,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6,padx=4)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command = list1.yview)

#list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="TImeIn", width=12,padx=8,command=select_date1)
b1.grid(row=0,column=4)

b2=Button(window,text="TimeOut", width=12,padx=8,command=select_date2)
b2.grid(row=1,column=4)

b3=Button(window,text="ViewEntries", width=12,padx=8,command=view_command)
b3.grid(row=2,column=4)

b4=Button(window,text="Viewexit", padx=8,width=12,command=view_exit)
b4.grid(row=3,column=4)

b6=Button(window,text="Close", padx=8,width=12,command=window.destroy)
b6.grid(row=4,column=4)

window.mainloop()
