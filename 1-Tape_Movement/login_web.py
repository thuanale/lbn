from selenium.webdriver import Ie
import page 
import sys

UID='SGSIN-THUAN'
PWD='12s)^A2021turday2021'
FILE = "C:/Users/t.le/Desktop/RETURN.txt" #sys.argv[3]


class CrownRM(): 
    def setup(self):
        self.driver = Ie() 
        self.driver.get('https://www09.rminteract.com/')    
        self.status={"left":[], "duplicate":[], "RD1066C":[],}
        
    def login(self,uid,pwd):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_match()
        main_page.login(uid,pwd)
        assert main_page.is_account_match()
        
    def go_to_search(self):
        page.WelcomePage(self.driver).tape_search()

    def prepare_search(self):
        page.TapePage(self.driver).clear_all()
        page.TapePage(self.driver).adv_search()
        page.AdvSearchPage(self.driver).set_options()

    def load_tape(self, file):
        adv_search_page = page.AdvSearchPage(self.driver)
        with open(file,'r',newline='') as txt_f:
            tapes = txt_f.read().splitlines()
        
        self.status["left"] = tapes.copy()
        self.status["duplicate"].clear()
        self.status["RD1066C"].clear()
        
        for tape in sorted(tapes):
            adv_search_page.add_tapes(tape)
            
        adv_search_page.confirm_search()
        
    def check_tape(self):
        tape_page = page.TapePage(self.driver)
        self.status["duplicate"].clear()
        tape_page.sort_alt_code()
        tape_page.unselected_all()
        all_tapes = tape_page.get_added_tapes()
        for i,page_num in enumerate(all_tapes, start=1):
            for j,row in enumerate(page_num, start=1):
                tape = row[2][:6]
                account = row[0]
                if tape not in self.status["left"]:
                    self.status["duplicate"].append((i,j,tape))
                    tape_page.select_row(j)
                if tape in self.status["left"]:
                    self.status["left"].remove(tape)
                if account == "RD1066C":
                    self.status["RD1066C"].append((i,j,row[2])) 
        
        for k,v in self.status.items():
            print("{0}: {1}".format(k,len(v)))
            if len(v):
                print("page line tape")
                for t in v:
                    print(t)
                print()
                
    def tear_down(self):
        self.driver.quit()
