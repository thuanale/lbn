#!/usr/bin/env python3

from tkinter import *
from tkinter import Tk, ttk
from tkcalendar import Calendar
import datetime

class App(ttk.Frame):
  def __init__(self, master=None):  
    super().__init__(master, padding='3 3 12 12')
    self.master = master
    self.grid(column=0, row=0, sticky=(N,W,E,S))
    self.columnconfigure(0, weight=1)
    self.rowconfigure(0, weight=1)

    self.create_widgets()
    self.set_labels()

  def create_widgets(self):
    self.selected_date = StringVar()
    cal = Calendar(self, selectmode='day', locale='en_US', 
          showweeknumbers=False, date_pattern="dd/mm/yyyy",
          maxdate=datetime.date.today(), disabledforeground='red',
          textvariable=self.selected_date)
    cal.grid(column=0, row=0, columnspan=2, sticky='nesw')
    
    self.shift = StringVar()
    ttk.Radiobutton(self, text='day', variable=self.shift,
    value='day').grid(column=0, row=2, sticky='e')
    ttk.Radiobutton(self, text='night', variable=self.shift, 
    value='night').grid(column=1, row=2, sticky='w')

    self.uid = StringVar()
    uid_entry = Entry(self, textvariable=self.uid)
    uid_entry.grid(column=1, row=3, sticky=(W,E))
    uid_entry.focus()

    self.pw = StringVar()
    Entry(self, textvariable=self.pw, show='*').grid(column=1, row=4, sticky=(W,E))
   
    ttk.Button(self, text='Submit', command=self.submit).grid(column=0,
    row=5, sticky='we')
    ttk.Button(self, text='Quit', command=self.stop).grid(column=1,
    row=5, sticky='we')

  def set_labels(self):
    self.master.title("Fill MTV")
    ttk.Label(self, textvariable=self.selected_date).grid(column=0, row=1,
    columnspan=2, sticky='ns')
    ttk.Label(self, text='UID').grid(column=0, row=3, sticky=(E))
    ttk.Label(self, text='Password').grid(column=0, row=4, sticky=(E))

    for child in self.winfo_children():
      child.grid_configure(padx=5, pady=5)

  def submit(self):
    #exit()
    pass

  def stop(self):
   exit()
   

root = Tk()
app = App(master=root)
app.mainloop()

