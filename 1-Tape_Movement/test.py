#!/usr/bin/env python

from selenium.webdriver import Ie
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

b = Ie()

def load_tapes(FILE):
    with open(FILE,'r',newline='') as txt_f:
            tapes = txt_f.read().splitlines()

    for tape in tapes:
        b.find_element(By.ID, 'txtMultipleEdit').send_keys(tape)
        b.find_element(By.ID, 'btnAddMultiple').click()

    b.find_element(By.ID, 'btnSubmit').click()

    WebDriverWait(b, 30).until(EC.title_is("Tape"))
    b.find_element(By.ID, "gridPageuwg_c_0_2").click()
    
b.get('https://www09.rminteract.com/')
b.find_element(By.ID, "userName").send_keys('SGSIN-THUAN')
b.find_element(By.ID, "password").send_keys('09w!@E2020dnesday')
b.find_element(By.ID, "btn_login").click()

