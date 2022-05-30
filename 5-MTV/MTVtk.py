#!/usr/bin/env python3

from tkinter import *
from tkinter import Tk, ttk, font
from tkcalendar import Calendar
import datetime
import requests
from mtvreq import *

class App(ttk.Frame):
  def __init__(self, master=None):  
    super().__init__(master, padding='3 3 12 12')
    self.master = master
    self.grid(column=0, row=0, sticky=(N,W,E,S))
    self.columnconfigure(0, weight=1)
    self.rowconfigure(0, weight=1)
    
    self.create_widgets()
    self.set_labels()
    self.session = requests.Session()
    

  def create_widgets(self):
    self.selected_date = StringVar()
    cal = Calendar(self, selectmode='day', locale='en_US', 
          date_pattern="yyyy-mm-dd", maxdate=datetime.date.today(),
          disabledforeground='red', textvariable=self.selected_date)
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
    self.status_lable = ttk.Label(self, text='')
    self.status_lable.grid(column=0, row=1, columnspan=2, sticky='ns')
    ttk.Label(self, text='UID').grid(column=0, row=3, sticky=(E))
    ttk.Label(self, text='Password').grid(column=0, row=4, sticky=(E))

    for child in self.winfo_children():
      child.grid_configure(padx=5, pady=5)

  def submit(self):
    uid = str(self.uid.get())
    pw = str(self.pw.get())
    response = Authen(self.session).login(uid,pw)
    if response == 200:
        date = str(self.selected_date.get())
        shift = str(self.shift.get())
        Submit(self.session).default(date,shift)
        response = 'Success!!!'
    
    self.status_lable['text'] = response

  def stop(self):
    Authen(self.session).logout()
    self.master.destroy()
    exit()
