from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

  
class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

class MainPage(BasePage):
    dropdownBy = "k-select"
    locationBy = "#GUID_listbox > li:nth-child(9)"
    usernameBy = '//*[@id="UserName"]'
    passwordBy = '//*[@id="Password"]'
    loginBy = "logon-submit"

    def login(self, uid, pwd):
        self.driver.find_element(By.CLASS_NAME, self.dropdownBy).click()
        self.driver.find_element(By.CSS_SELECTOR, self.locationBy).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.usernameBy).send_keys(uid)
        self.driver.find_element(By.XPATH, self.passwordBy).send_keys(pwd)
        self.driver.find_element(By.ID, self.loginBy).click()

    def is_title_match(self):
        return "oneilOrder Login" in self.driver.title, "Wrong link"

    def is_account_match(self):
        return "unsuccessful" not in self.driver.page_source, "Account/Password is not right."
    
class WelcomePage(BasePage):
    tapeBy = "RSLeftNavuwlb_1_Item_1"
    advSearchBy = "ctl09_3_2"
    
    def tape_search(self):
        self.driver = driver
        self.driver.find_element(By.ID, self.tapeBy).click()

class TapePage(BasePage):
    searchBy = "ctl09_3"
    advSearchBy = "ctl09_2"
    altCodeBy = ""
    
    def advancedSearch(self):
        ActionChains(self.driver).move_to_element(By.ID, self.searchBy).click(By.ID, self.advSearchBy).perform()
        
    def sort(self):
        self.driver.find_element(By.ID, self.altCodeBy).click()
        
