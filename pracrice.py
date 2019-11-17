from tkinter import *
from tkinter.ttk import *



class HelloView(tk.Tk):
    def __init__(self,parent,*args,**kwargs):
        super().__init__(self,parent,*args,**kwargs)
        self.title("Hello tkinter")
        self.geometry("800X600")
        self.resizable(width=False,height=False)

