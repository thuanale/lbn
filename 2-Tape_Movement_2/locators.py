from selenium.webdriver.common.by import By

class LoginLocators(object):
    DROPDOWN = (By.XPATH, '//*[@id="logon-wrapper"]/fieldset/div[1]/div[2]/span')
    LOC_SELECT = (By.XPATH, '#GUID_listbox > li:nth-child(9)')
    USER_BOX = (By.XPATH, '//*[@id="UserName"]')
    PW_BOX = (By.XPATH, '//*[@id="Password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="logon-submit"]')
     
class MainLocators(object):
    TAPE_ITEM = (By.ID, "RSNEWNavuwlb_1_Item_1")
    SEARCH_SELECT = (By.XPATH, "/html/body/div[8]/div/form/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/span/span/span[2]")
    SETTINGS = (By.XPATH, '//*[@id="results-settings"]')
    CHOOSE_FOMRAT = (By.XPATH, '//*[@id="control-menu"]/li[1]')
    TAPE_STANDARD = (By.XPATH, '//*[@id="column-format-group"]/span[2]')
    ROW_LENGTH = (By.XPATH, '//*[@id="results-grid"]/div[4]/span[1]/span/span')
    
    
class AdvSearchLocators(object):
    CLEAR_ALL = (By.NAME, "results-clear-all-group")
    UNSELECT_ALL = (By.XPATH, '//*[@id="results-unselect-all-group"]')
    PAGE_ROW = (By.XPATH, '//*[@id="results-grid"]/div[3]/table/tbody/tr')
    COLUMN = (By.TAG_NAME, 'td')
    TAPE_BOX = (By.ID, "parameter-0")
    SEARCH_BUTTON = (By.XPATH, '//*[@id="quick-query-execute"]')
    MATCHED_ITEM = (By.XPATH, '//*[@id="quick-query-results-matched"]')