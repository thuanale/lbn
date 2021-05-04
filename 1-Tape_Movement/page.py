from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
from locators import WelcomePageLocators
from locators import TapePageLocators
from locators import AdvSearchPageLocators

 
class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

class MainPage(BasePage):
    def login(self, uid, pwd):
        self.driver.find_element(*MainPageLocators.USER_BOX).send_keys(uid)
        self.driver.find_element(*MainPageLocators.PW_BOX).send_keys(pwd)
        self.driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    def is_title_match(self):
        return "RSWeb.NET Login" in self.driver.title, "Wrong link!"

    def is_account_match(self):
        return "Login failed" not in self.driver.page_source, "Account & password are not matched."
    
class WelcomePage(BasePage):
    def tape_search(self):
        #WebDriverWait(self.driver, 30).until(EC.title_is("Welcome"))
        self.driver.find_element(*WelcomePageLocators.TAPE_ITEM).click()
        WebDriverWait(self.driver, 30).until(EC.title_is("Tape"))

class TapePage(BasePage):
    page_rows_by = '//*[@id="G_gridPageuwg"]/tbody/tr'
    def adv_search(self):
        self.driver.find_element(*TapePageLocators.SEARCH_ITEM).click()
        self.driver.find_element(*TapePageLocators.ADV_SEARCH_ITEM).click();
        
    def sort_alt_code(self):
        self.driver.find_element(*TapePageLocators.ALT_CODE_ITEM).click()
        
    def unselected_all(self):
        self.driver.find_element(*TapePageLocators.RESULT_ITEM).click()
        self.driver.find_element(*TapePageLocators.UNSELECTED_ALL_ITEM).click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(TapePageLocators.RESULT_ITEM))

    def invert_selection(self):
        self.driver.find_element(*TapePageLocators.RESULT_ITEM).click()
        self.driver.find_element(*TapePageLocators.INVERT_SELECTION_ITEM).click()
        
    def clear_all(self):
        self.driver.find_element(*TapePageLocators.RESULT_ITEM).click()
        self.driver.find_element(*TapePageLocators.CLEAR_ALL_ITEM).click()
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(TapePageLocators.RESULT_ITEM))
        
    def clear_selected(self):
        self.driver.find_element(*TapePageLocators.RESULT_ITEM).click()
        self.driver.find_element(*TapePageLocators.CLEAR_SELECTED_ITEM).click()
        
    def get_added_tapes(self):
        page_tapes = []
        all_tapes = []
        page_counts = len(self.driver.find_elements(*TapePageLocators.PAGES_COUNT)) + 1
        print(page_counts)
        for i in range(page_counts):
            WebDriverWait(self.driver,60).until(EC.title_is('Tape'))
            current_page = self.driver.find_element(*TapePageLocators.PAGE_ITEM)
            page_rows = self.driver.find_elements(*TapePageLocators.PAGE_ROW)
            page_tapes = []
            for row in page_rows:
                cols = row.find_elements(*TapePageLocators.COL_ITEM)
                account = cols[0].text
                barcode = cols[1].text
                alt_code = cols[2].text
                page_tapes.append((account,barcode,alt_code))
            all_tapes.append(page_tapes)
        
            while current_page == self.driver.find_element(*TapePageLocators.PAGE_ITEM):
                try:
                    self.driver.find_element(*TapePageLocators.NEXT_PAGE_BUTTON).click()
                except:
                    break
        try:
            self.driver.find_element(*TapePageLocators.FIRST_PAGE_BUTTON).click()
        except:
            pass
        return all_tapes
    
    def select_row(self, row):
        path = "{0}[{1}]/th[1]".format(self.page_rows_by,row)
        self.driver.find_element(By.XPATH,path).click()
        WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,path)))
        
class AdvSearchPage(BasePage):
    def set_options(self):
        WebDriverWait(self.driver, 30).until(EC.title_is("Tape Advanced Search"))
        Select(self.driver.find_element(*AdvSearchPageLocators.SEARCH_FIELD_CHOICE)).select_by_visible_text("Alternate Code")
        Select(self.driver.find_element(*AdvSearchPageLocators.MATCH_TYPE_CHOICE)).select_by_visible_text("Contains")
    
    def add_tapes(self,tape):
        self.driver.find_element(*AdvSearchPageLocators.TAPE_BOX).send_keys(tape)
        self.driver.find_element(*AdvSearchPageLocators.ADD_BUTTON).click()
        
    def confirm_search(self):
        self.driver.find_element(*AdvSearchPageLocators.SEARCH_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.title_is("Tape"))
