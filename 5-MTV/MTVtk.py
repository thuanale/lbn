#!/usr/bin/env python3

from tkinter import *
from tkinter import Tk, ttk

class App(ttk.Frame):
  def __init__(self, master=None):
    self.master = master
    
    super().__init__(self.master, padding='3 3 12 12')
    self.grid(column=0, row=0, sticky=(N,W,E,S))
    self.columnconfigure(0, weight=1)
    self.rowconfigure(0, weight=1)

    self.create_widgets()
    self.set_labels()

  def create_widgets(self):
    uid = StringVar()
    uid_entry = Entry(self, width=20, textvariable=uid)
    uid_entry.grid(column=2, row=1, sticky=(W,E))
    uid_entry.focus()

    pw = StringVar()
    Entry(self, width=20, textvariable=pw, show='*').grid(column=2, row=2, sticky=(W,E))
    
    #day
    #month
    #year
    shift = StringVar()
    ttk.Radiobutton(self, text='day', variable=shift,
    value='day').grid(column=1, row=4, sticky=(W))
    ttk.Radiobutton(self, text='night', variable=shift, 
    value='night').grid(column=3, row=4, sticky=(W))

    ttk.Button(self, text='Submit', command=self.submit()).grid(column=2,
    row=5, sticky=(W, E))

  def set_labels(self):
    self.master.title("Fill MTV")
    ttk.Label(self, text='UID').grid(column=0, row=1, sticky=(E))
    ttk.Label(self, text='Password').grid(column=0, row=2, sticky=(E))

    for child in self.winfo_children():
      child.grid_configure(padx=5, pady=5)

  def submit(self):
    pass

root = Tk()
app = App(master=root)
app.mainloop()

