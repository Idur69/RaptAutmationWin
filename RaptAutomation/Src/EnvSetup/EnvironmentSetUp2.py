import datetime
import unittest


from selenium import  webdriver
from selenium.webdriver import DesiredCapabilities


class EnvironmentSetup2(unittest.TestCase):
    def setUp(self):

        # ---------- Chrome Browser 1 ----------------
        dc = DesiredCapabilities.CHROME
        dc['loggingPrefs'] = {'browser': 'ALL'}
        executable_path = "/home/cit/PycharmProjects/Rapt/RaptAutomation/Drivers/chromedriver"
        self.driver1 = webdriver.Chrome(executable_path, desired_capabilities=dc)

        # ------------ Firefox Browser ------------------
        capabilites = DesiredCapabilities.FIREFOX
        capabilites['loggingPrefs'] = {'browser': 'ALL'}
        executable_path2 = '/home/cit/PycharmProjects/Rapt/RaptAutomation/Drivers/geckodriver'
        # self.driver2 = webdriver.Firefox(executable_path2, desired_capabilities=df)
        self.driver2 = webdriver.Chrome(executable_path2, desired_capabilities=capabilites)

        # ---------- Chrome Browser 1 ----------------
        dc = DesiredCapabilities.CHROME
        dc['loggingPrefs'] = {'browser': 'ALL'}
        executable_path = "/home/cit/PycharmProjects/Rapt/RaptAutomation/Drivers/chromedriver"
        self.driver3 = webdriver.Chrome(executable_path, desired_capabilities=dc)


        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment Created")
        print("**********************")
        self.driver1.implicitly_wait(5)
        self.driver1.maximize_window()

        self.driver2.implicitly_wait(5)
        self.driver2.maximize_window()
        self.driver3.implicitly_wait(5)
        self.driver3.maximize_window()

    def tearDown(self):


        if (self.driver1 != None):
            print("*******************")
            print("Environment-1 Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            # self.driver.close()
            self.driver1.quit()

        if (self.driver2 != None):
            print("*******************")
            print("Environment-2 Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            # self.driver.close()
            self.driver2.quit()
        if (self.driver3 != None):
            print("*******************")
            print("Environment-1 Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            # self.driver.close()
            self.driver3.quit()


