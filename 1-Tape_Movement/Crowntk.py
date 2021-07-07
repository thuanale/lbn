#!/usr/bin/env python3

from tkinter import *
from tkinter import Tk, ttk
from login_web import *

class App(ttk.Frame):  
  def __init__(self,master=None):
    self.master = master
    super().__init__(self.master, padding='3 3 12 12')
    
    self.grid(column=0, row=0, sticky=(N, W, E, S))
    self.create_widgets()
    self.set_labels()
    self.browser = None
    

  def create_widgets(self):
    self.uid = StringVar()
    uid_entry = Entry(self, width=20, textvariable=self.uid)
    uid_entry.grid(column=2, row=1, sticky=(W, E))
    uid_entry.focus()

    self.pw = StringVar()
    Entry(self, width=20, textvariable=self.pw, show='*').grid(column=2, row=2,
    sticky=(W, E))

    ttk.Button(self, text="Setup", command=self.setup).grid(column=1, row=3,
    sticky=(W, E))
    ttk.Button(self, text="Run", command=self.run).grid(column=2, row=3,
    sticky=(W, E))
    ttk.Button(self, text="Quit", command=self.stop).grid(column=3, row=3,
    sticky=(W, E))
  
  def set_labels(self):
    self.master.title("Crown Check Tk")
    ttk.Label(self, text="Username").grid(column=1, row=1, sticky=(E))
    ttk.Label(self, text="Password").grid(column=1, row=2, sticky=(E))
    
    for child in self.winfo_children(): 
      child.grid_configure(padx=5, pady=5)

  def setup(self):
    if not self.browser:
        self.browser = CrownRM()
        self.browser.setup()
    UID = str(self.uid.get())
    PW = str(self.pw.get())
    self.browser.login(UID, PW)
    self.browser.go_to_search()

  def run(self):
    self.browser.prepare_search()
    self.browser.load_tape(FILE)
    self.browser.check_tape()
    

  def stop(self):
    if self.browser:
      self.browser.tear_down()
    self.destroy()
    exit()
