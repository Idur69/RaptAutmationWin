import pickle
from http.cookiejar import Cookie

from selenium.webdriver.common.by import By

#from Src.PageObject.Locators import Locators
# RaptAutomation.Src.PageObject import Locators
from Src.PageObject.Locators import Locators


class AdminLogin(object):
    def __init__(self, driver):
        self.driver = driver

        self.user = driver.find_element(By.XPATH, Locators.adminusername)
        self.password = driver.find_element(By.XPATH, Locators.password)
        self.submit = driver.find_element(By.XPATH, Locators.submit)

        #self.tnsfimg = driver.find_element(By.XPATH, Locators.fimg)

    def set_login_uname(self, username):
        self.user.clear()
        self.user.send_keys(username)
    def set_login_upass(self, userpass):
        self.password.clear()
        self.password.send_keys(userpass)
    def submit_login(self, username, userpass):


        #setcookie = pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))
        #print("setcookies values:", setcookie)

        self.submit.click()

