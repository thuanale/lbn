from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from locators import *

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

class LoginPage(BasePage):
    def login(self, uid, pwd):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*LoginLocators.DROPDOWN))
        action.click().send_keys(Keys.END).send_keys(Keys.ENTER)
        action.perform()
        sleep(1)
        self.driver.find_element(*LoginLocators.USER_BOX).send_keys(uid)
        self.driver.find_element(*LoginLocators.PW_BOX).send_keys(pwd)
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def is_title_match(self):
        return "oneilOrder Login" in self.driver.title, "Wrong link"

    def is_account_match(self):
        return "unsuccessful" not in self.driver.page_source, "Account/Password is not right."
    
class SearchPage(BasePage):
    def advanced_search(self):
        driver = self.driver
        WebDriverWait(driver,300).until(lambda x: x.find_element(*MainLocators.SEARCH_SELECT))
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(*MainLocators.SEARCH_SELECT)).click()
        action.send_keys(Keys.END).send_keys(Keys.ENTER)
        action.perform()
    
    def max_row(self):
        driver = self.driver
        WebDriverWait(driver,300).until(lambda x: x.find_element(*MainLocators.ROW_LENGTH))
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(*MainLocators.ROW_LENGTH)).click()
        action.send_keys(Keys.END).send_keys(Keys.ENTER)
        action.perform()
        sleep(2)
    
    def result_view(self):
        driver = self.driver
        WebDriverWait(driver,300).until(lambda x: x.find_element(*MainLocators.ROW_LENGTH))
        driver.find_element(*MainLocators.SETTINGS).click()
        driver.find_element(*MainLocators.CHOOSE_FOMRAT).click()
        WebDriverWait(driver,300).until(lambda x: x.find_element(*MainLocators.TAPE_STANDARD))
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(*MainLocators.TAPE_STANDARD))
        action.send_keys(Keys.END).send_keys(Keys.ENTER)
        action.perform()
        sleep(2)
        
class AdvancedPage(BasePage):
    def select_query(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*AdvSearchLocators.QUERY_ITEM))
        action.click().send_keys(Keys.HOME).send_keys(Keys.ENTER)
        action.perform()
        sleep(2)
        
    def clear_all(self):
        self.driver.find_element(*AdvSearchLocators.CLEAR_ALL).click()
           
    def unselect_all(self):
        WebDriverWait(self.driver,30).until(lambda x: x.find_element(*AdvSearchLocators.UNSELECT_ALL))
        self.driver.find_element(*AdvSearchLocators.UNSELECT_ALL).click()
        
    def get_match(self):
        return self.driver.find_element(*AdvSearchLocators.MATCHED_ITEM).get_attribute("value")
    
    def process_tapes(self, tapes):
        status={"NEW":[], "DUP":[], "RD1066C":[],}
        ele = self.driver.find_element(*AdvSearchLocators.TAPE_BOX)
        sleep(2)
        for tape in tapes:
            ele.clear()
            ele.send_keys(tape)
            ele.send_keys(Keys.ENTER)
            sleep(3)
            matched = self.get_match()
            if matched == '0':
                status["NEW"].append(tape)
            elif matched != '1':
                status["DUP"].append(tape)
        self.unselect_all()
        sleep(2)
        
        page_rows = self.driver.find_elements(*AdvSearchLocators.PAGE_ROW)
        scroll = self.driver.find_element(*AdvSearchLocators.SCROLL)
        
        for row in page_rows:
            cols = row.find_elements(*AdvSearchLocators.COLUMN)
            account = cols[0].text
            alt_code = cols[2].text
            if account == "RD1066C":
                status["RD1066C"].append(alt_code)
            if alt_code[:6] in status["DUP"]:
                row.click()
            scroll.send_keys(Keys.DOWN)
            sleep(1)
        scroll.send_keys(Keys.HOME)
        return status
        