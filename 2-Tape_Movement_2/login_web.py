from selenium.webdriver import Chrome
import page
import sys

class CrownRM(): 
    def setup(self):
        self.driver = Chrome("./chromedriver") 
        self.driver.get('https://rmorder09.rminteract.com/')
        
    def login(self,UID,PW):
        login_page = page.LoginPage(self.driver)
        assert login_page.is_title_match()
        login_page.login(UID,PW)
        assert login_page.is_account_match()
    
    def go_to_search(self):
        search_page = page.SearchPage(self.driver)
        search_page.result_view()
        search_page.max_row()
        search_page.advanced_search()
        
    def prepare_search(self):
        adv_search_page = page.AdvancedPage(self.driver)
        adv_search_page.select_query()
        adv_search_page.clear_all()
        
    def load_tape(self,file):
        adv_search_page = page.AdvancedPage(self.driver)
        with open(file,'r',newline='') as txt_f:
            tapes = txt_f.read().splitlines()
        self.result = adv_search_page.process_tapes(tapes)
    
    def print_result(self):
        print("---------------------")
        for k,v in self.result.items():
            print("{0}: {1}".format(k,len(v)))
            if len(v):
                for t in v:
                    print(t)
                print()
        print("---------------------")
        
    def tear_down(self):
        self.driver.quit()


