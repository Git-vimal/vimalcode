__author__ = 'vimalpat'

import unittest2
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import locators1

class gmail(unittest2.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("chromedriver.exe")
        cls.driver.get(locators1.url)

    def test_case001(self):
        self.assertEqual(Login(self.driver),"COMPOSE","compose button not found")

    def test_case002(self):
        self.assertEqual(Send_Mail(self.driver),"Your message has been sent. View message")

    @classmethod
    def tearDownClass(cls):
         cls.driver.close()

def wait_presence_id(driver,locator):
    wait = WebDriverWait(driver,20,poll_frequency=1, ignored_exceptions=[NoSuchElementException])
    wait.until(EC.presence_of_element_located((By.ID,locator)))

def wait_presence_class(driver,locator):
    wait = WebDriverWait(driver,20,poll_frequency=1, ignored_exceptions=[NoSuchElementException])
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,locator)))

def wait_visibility_id(driver,locator):
    wait = WebDriverWait(driver,20,poll_frequency=1, ignored_exceptions=[NoSuchElementException])
    wait.until(EC.visibility_of_element_located((By.ID, locator)))


def Login(driver):
        wait_presence_id(driver,locators1.Email)
        driver.find_element_by_id(locators1.Email).send_keys(locators1.username)
        driver.find_element_by_id(locators1.next).click()
        wait_visibility_id(driver,locators1.password)
        driver.find_element_by_id(locators1.password).send_keys(locators1.acc_pass)
        driver.find_element_by_id(locators1.sign_in).click()
        wait_presence_class(driver,locators1.compose)
        comp = driver.find_element_by_class_name(locators1.compose)
        return comp.find_element_by_xpath(locators1.compose_xpath).text

def Send_Mail(driver):
        driver.find_element_by_class_name(locators1.compose).click()
        wait_presence_id(driver,locators1.mail_form)
        form = driver.find_element_by_id(locators1.mail_form)
        form.find_element_by_tag_name(locators1.to).send_keys(locators1.mailto)
        sub = driver.find_element_by_id(locators1.subject)
        sub.find_element_by_tag_name(locators1.sub_input).send_keys(locators1.sub_txt)
        body = driver.find_element_by_id(locators1.body)
        body.send_keys(locators1.body_txt)
        tab = driver.find_element_by_class_name(locators1.send_btn_class)
        tab.find_element_by_xpath(locators1.send_btn_xpath).click()
        wait_presence_id(driver,locators1.send_msg_link)
        return driver.find_element_by_class_name(locators1.send_msg).text

if __name__ == '__main__':
    unittest2.main()
