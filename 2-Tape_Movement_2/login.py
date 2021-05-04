from selenium.webdriver import Chrome
import page 

class CrownRM(): 
    def setup(self):
        self.driver = Chrome() 
        self.driver.get('https://Rmorder09.rminteract.com')
    
    def test_login(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_match()
        main_page.login("SGSIN-THUAN","09w!@E2020dnesday")
        assert main_page.is_account_match()
        
    def tear_down(self):
        self.driver.quit()


a = CrownRM()
a.setup()
a.test_login()
