#!/usr/bin/env python3

import requests
import datetime

class Base(object):
    def __init__(self, session):
        self.session = session
        self.url = 'https://intranet.linkbynet.com/v7/api/1.1'
	
class Authen(Base):
    def login(self, uid, pw):
        credential = {
        "connetionType" : "Classique",
        "login" : uid,
        "password" : pw
        }
    
        try:
            response = self.session.post(self.url + '/Authentification.json/Login',json=credential, timeout=5)
            if response.status_code != 200:
                return "UID/Password is not correct!"
            return 200
        except requests.exceptions.Timeout:
            return "Unreachable. Please check connection!"

    def logout(self):
        response = self.session.delete(self.url + '/Authentification.json/Logout')
        return response.status_code

class Submit(Base):
    Internal = {
        "CreationDate":"",
        "Duration":"120",
        "ActivityId":"2521",
        "CompanyId":"2865",
        "ProjectId":"21057",
        "Title":"Learning, automating"
        }
        
    DFS1 = {
        "CreationDate":"",
        "Duration":"360",
        "ActivityId":"2515",
        "CompanyId":"3312",
        "ProjectId":"19713",
        "Title":"Monitoring, checking backup, take call, report, patching"
        }
        
    DFS2 = {
        "CreationDate":"",
        "Duration":"360",
        "ActivityId":"2515",
        "CompanyId":"3312",
        "ProjectId":"19713",
        "Title":"Monitoring, checking backup, take call, report, patching"
        }

    def default(self,date,shift):
        self.Internal["CreationDate"] = date
        self.DFS1["CreationDate"] = date
        
        if shift == 'day': 
            self.DFS2["CreationDate"] = date
            
        if shift == 'night':
            next_date = datetime.date.fromisoformat(date) + datetime.timedelta(days=1)
            self.DFS2["CreationDate"] = str(next_date)         
        
        for data in (self.DFS1, self.DFS2):
            self.session.post(self.url + '/MTV.json/AddTime',json=data)

