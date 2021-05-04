from selenium.webdriver.common.by import By

class MainPageLocators(object):
    USER_BOX = (By.ID, "userName")
    PW_BOX = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "btn_login")
    
class WelcomePageLocators(object):
    TAPE_ITEM = (By.ID, "RSLeftNavuwlb_1_Item_1")
        
class TapePageLocators(object):
    SEARCH_ITEM = (By.ID, "ctl09_3")
    ADV_SEARCH_ITEM = (By.ID, "ctl09_3_2")
    RESULT_ITEM = (By.ID, "ctl09_2")
    ALT_CODE_ITEM = (By.ID, "gridPageuwg_c_0_2")
    UNSELECTED_ALL_ITEM = (By.ID, "ctl09_2_2")
    INVERT_SELECTION_ITEM = (By.ID, "ctl09_2_3")
    CLEAR_ALL_ITEM = (By.ID, "ctl09_2_4")
    CLEAR_SELECTED_ITEM = (By.ID, "ctl09_2_5")
    PAGE_ITEM = (By.CLASS_NAME, "GridPage_PageXofYCell")
    PAGE_ROW = (By.XPATH, '//*[@id="G_gridPageuwg"]/tbody/tr')
    PAGES_COUNT = (By.XPATH, "//*[@id='gridPageuwg_pager']/a")
    NEXT_PAGE_BUTTON = (By.ID, "gridPagenp")
    FIRST_PAGE_BUTTON = (By.ID, "gridPagefp")
    COL_ITEM = (By.TAG_NAME, 'td')

class AdvSearchPageLocators(object):
    SEARCH_FIELD_CHOICE = (By.ID, "ddlFields")
    MATCH_TYPE_CHOICE = (By.ID, "ddlOperators")
    TAPE_BOX = (By.ID, 'txtMultipleEdit')
    ADD_BUTTON = (By.ID, 'btnAddMultiple')
    SEARCH_BUTTON = (By.ID, 'btnSubmit')