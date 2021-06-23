#!/usr/bin/env python3

from tkinter import *
from tkinter import Tk, ttk

class App(ttk.Frame):
  def __init__(self,master=None):
    self.master = master
    super().__init__(self.master, padding='3 3 12 12')
    
    self.grid(column=0, row=0, sticky=(N, W, E, S))
    self.create_widgets()
    self.set_labels()


  def create_widgets(self):
    user = StringVar()
    user_entry = Entry(self, width=20, textvariable=user)
    user_entry.grid(column=2, row=1, sticky=(W, E))
    user_entry.focus()

    password = StringVar()
    Entry(self, width=20, textvariable=password, show='*').grid(column=2, row=2,
    sticky=(W, E))

    ttk.Button(self, text="Start", command=self.login).grid(column=1, row=3,
    sticky=(W, E))
    ttk.Button(self, text="Again", command=self.rerun).grid(column=3, row=3,
    sticky=(W, E))
    ttk.Button(self, text="Stop", command=self.logout).grid(column=2, row=4,
    sticky=(W, E))
  
  def set_labels(self):
    self.master.title("Crown Check Tk")
    ttk.Label(self, text="ID").grid(column=1, row=1, sticky=(E))
    ttk.Label(self, text="Password").grid(column=1, row=2, sticky=(E))
    
    for child in self.winfo_children(): 
      child.grid_configure(padx=5, pady=5)

  def login(self):
    pass

  def rerun(self):
    pass

  def logout(self):
    pass

root = Tk()
app = App(master=root)
app.mainloop()
