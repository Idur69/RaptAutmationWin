import datetime
import unittest
from time import sleep

from selenium import webdriver

class EnvironmentSetup(unittest.TestCase):

    def setUp(self):

        chrome_path = r"C:\Users\Idur\PycharmProjects\RaptAutomation\Drivers\chromedriver.exe"
        #firefox_path = r"C:\Users\Idur\PycharmProjects\RaptAutomation\Drivers\geckodriver.exe"
        # Create Chrome Browser
        self.driver = webdriver.Chrome(executable_path=chrome_path)
        #self.driver = webdriver.Firefox(executable_path=firefox_path)

        self.driver.implicitly_wait(10)
    def test_browser(self):
        driver = self.driver
        driver.get("http://crimsoninnovative.com")
        #driver.get("http://google.com")
        sleep(10)

    def tearDown(self):
        if (self.driver != None):
            print("*******************")
            print("Environment-1 Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            # self.driver.close()
            self.driver.quit()

