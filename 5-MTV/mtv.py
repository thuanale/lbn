import requests

class Base():
    def __init__(self):
        self.url = 'https://intranet.linkbynet.com/v7/api/1.1'
        self.idefix = requests.Session()
	
class Authen(Base):

    def login(self, credential):
        response = self.idefix.post(self.url + '/Authentification.json/Login',json=credential)
        return response.status_code

    def logout(self):
        response = self.idefix.delete(self.url + '/Authentification.json/Logout')
        return response.status_code

class Submit(Base):
    Engie = {
        "CreationDate":"",
        "Duration":"120",
        "ActivityId":"2515",
        "CompanyId":"3586",
        "ProjectId":"29476",
        "Title":"Monitoring HPOMI"
        }
        
    DFS1 = {
        "CreationDate":"",
        "Duration":"240",
        "ActivityId":"2515",
        "CompanyId":"3312",
        "ProjectId":"19713",
        "Title":"Robot monitoring, check backup, take call, report"
        }
        
    DFS2 = {
        "CreationDate":"",
        "Duration":"240",
        "ActivityId":"2515",
        "CompanyId":"3312",
        "ProjectId":"19713",
        "Title":"Robot monitoring, check backup, take call, report"
        }

    def default(self,date,shift):
        if shift == 'day':
            self.Engie["CreationDate"] = date
            self.DFS1["CreationDate"] = date
            self.DFS2["CreationDate"] = date
            self.idefix.post(self.url + '/MTV.json/AddTime',json=self.Engie)
            self.idefix.post(self.url + '/MTV.json/AddTime',json=self.DFS1)
            self.idefix.post(self.url + '/MTV.json/AddTime',json=self.DFS2)
            
        if shift == 'night':
            self.idefix.post(self.full_url,json=self.Engie)
            self.idefix.post(self.full_url,json=self.DFS1)
            self.idefix.post(self.full_url,json=self.DFS2)
        
credential = {
	  "connetionType" : "Classique",
	  "login" : "t.le",
	  "password" : "12s)^A2021turday2021"
	}


