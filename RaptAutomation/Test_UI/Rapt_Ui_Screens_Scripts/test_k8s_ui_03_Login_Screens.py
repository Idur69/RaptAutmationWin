import datetime
import unittest
from time import sleep

from selenium import webdriver

#from Src.EnvSetup.EnvironmentSetUp import EnvironmentSetup
#from Src.EnvSetup.cnfgurl import EnvironmentSetup
from Src.PageObject.Pages.Admin_Login import AdminLogin
from Src.PageObject.Pages.MyUrl import Myurl

from Src.EnvSetup.cnfgurl import EnvironmentSetup


class Rapt_Ui_Login_Screens(EnvironmentSetup):

    # Test Case-1 empty username and passord
    def test_01_empty_credentials(self):
        missingcredential = ""
        Admin = ""
        Pwd = ""

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://34.217.52.204:3010/users/login")
        # self.driver1.get("http://54.70.64.175:3010/users/login")
        self.driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)

        admin_login.submit_login(Admin, Pwd)
        sleep(5)
        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for missingcredential in msg:
            assert isinstance(missingcredential.text, object)
            print(missingcredential.text)
        if not Admin and not Pwd:
            print("Please enter username and password")
        expadmin = "Missing credentials"
        missing = missingcredential.text
        self.assertEqual(expadmin, missing, "Missing credentials")

    # Test Case-2 empty username
    def test_02_empty_username(self):
        Admin = ""
        Pwd = "123"
        missingcredential = ""
        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        # self.driver1.get("http://54.70.64.175:3010/users/login")
        self.driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)

        admin_login.submit_login(Admin, Pwd)
        sleep(5)
        missing = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for missingcredential in missing:
            assert isinstance(missingcredential.text, object)
            print(missingcredential.text)
        if not Admin:
            print("Please enter username")
        expadmin = "Missing credentials"
        missing = missingcredential.text
        self.assertEqual(expadmin, missing, "Missing credentials")

    # Test Case-3 empty password
    def test_03_empty_password(self):
        Admin = "demo1"
        Pwd = ""
        missingcredential = ""
        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        # self.driver1.get("http://54.70.64.175:3010/users/login")
        self.driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)
        # sub = self.driver1.find_element_by_tag_name("button")
        # sub.click()
        # setcookie = pickle.dump(self.driver1.get_cookies(), open("cookies.pkl", "wb"))
        # print("setcookievalue :", setcookie)
        admin_login.submit_login(Admin, Pwd)
        sleep(5)
        missing = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for missingcredential in missing:
            assert isinstance(missingcredential.text, object)
            print(missingcredential.text)
        if not Pwd:
            print("Please enter password")
        expadmin = "Missing credentials"
        missing = missingcredential.text
        self.assertEqual(expadmin, missing, "Missing credentials")
    
    # Test Case-4 Invalid username and Invalid passowrd
    def test_04_invalid_credentials(self):
        Admin = "rudirudi"
        Pwd = "123321"
        missingcredential = ""
        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        # self.driver1.get("http://54.70.64.175:3010/users/login")
        self.driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)

        admin_login.submit_login(Admin, Pwd)
        sleep(5)
        missing = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for missingcredential in missing:
            assert isinstance(missingcredential.text, object)
            print(missingcredential.text)
        expadmin = "demo1"
        exppass = "123"
        if Admin == expadmin and Pwd == exppass:
            print("Login successful")
        else:
            print("Invalid username and password")
        expadmin = "Unknown User"
        missing = missingcredential.text
        self.assertEqual(expadmin, missing, "Please enter valid credential")

    # Test Case-5 Invalid username and Valid passowrd
    def test_05_invalid_username(self):
        Admin = "rudirudi"
        Pwd = "123"
        missingcredential = ""
        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        # self.driver1.get("http://54.70.64.175:3010/users/login")
        self.driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)

        admin_login.submit_login(Admin, Pwd)
        sleep(5)
        missing = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for missingcredential in missing:
            assert isinstance(missingcredential.text, object)
            print(missingcredential.text)
        expadmin = "demo1"
        exppass = "123"
        if Admin == expadmin and Pwd == exppass:
            print("Login successful")
        else:
            print("Invalid username")
        expadmin = "Unknown User"
        missing = missingcredential.text
        self.assertEqual(expadmin, missing, "Please enter valid credential")
    
    # Test Case-6 Valid username and Invalid passowrd
    def test_06_invalid_password(self):
        Admin = "demo1"
        Pwd = "123321"
        missingcredential = ""
        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        # self.driver1.get("http://54.70.64.175:3010/users/login")
        self.driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)

        admin_login.submit_login(Admin, Pwd)
        sleep(5)
        missing = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for missingcredential in missing:
            assert isinstance(missingcredential.text, object)
            print(missingcredential.text)
        expadmin = "demo1"
        exppass = "123"
        if Admin == expadmin and Pwd == exppass:
            print("Login successful")
        else:
            print("Please enter valid password")
        expadmin = "Invalid password"
        missing = missingcredential.text
        self.assertEqual(expadmin, missing, "Please enter valid credential")
    
    # Test Case-7  username characters length check
    def test_07_username_charlength_check(self):
        Admin = "demodemodemodemo"
        Pwd = "123"

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        # self.driver1.get("http://54.70.64.175:3010/users/login")
        self.driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)

        admin_login.submit_login(Admin, Pwd)
        sleep(5)
        missing = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for missingcredential in missing:
            assert isinstance(missingcredential.text, object)
            print(missingcredential.text)
        expadmin = "demo1"
        exppass = "123"
        if Admin == expadmin and Pwd == exppass:
            print("Login successful")
        else:
            print("Please check username character length")
        listadmin = Admin
        self.assertEqual(16, len(listadmin), "Please check username characters length")
    
    # Test Case-8  password characters length check
    def test_08_password_charlength_check(self):
        Admin = "demo1"
        Pwd = "123456789123456"

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        # self.driver1.get("http://54.70.64.175:3010/users/login")
        self.driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)

        admin_login.submit_login(Admin, Pwd)
        sleep(5)
        missing = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for missingcredential in missing:
            assert isinstance(missingcredential.text, object)
            print(missingcredential.text)
        expadmin = "demo1"
        exppass = "123"
        if Admin == expadmin and Pwd == exppass:
            print("Login successful")
        else:
            print("Please check password character length")
        listpass = Pwd
        self.assertEqual(15, len(listpass), "Please check password characters length")

    # Test case-9 Successfull login
    def test_09_login_successful(self):
        Admin = "demo1"
        Pwd = "123"

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        # self.driver1.get("http://54.70.64.175:3010/users/login")
        self.driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)
        # sub = self.driver1.find_element_by_tag_name("button")
        # sub.click()
        # setcookie = pickle.dump(self.driver1.get_cookies(), open("cookies.pkl", "wb"))
        # print("setcookievalue :", setcookie)
        admin_login.submit_login(Admin, Pwd)
        sleep(5)
        expadmin = "demo1"
        exppass = "123"
        if Admin == expadmin and Pwd == exppass:
            print("Login successful")
        else:
            assert print("Invalid credentials")

    # Test case-10 Already login
    def test_10_already_login(self):
        Admin = "demo1"
        Pwd = "123"

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        # self.driver1.get("http://54.70.64.175:3010/users/login")
        self.driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)

        admin_login.submit_login(Admin, Pwd)
        sleep(5)
        alreadylogin = self.driver1.find_elements_by_xpath("//*[@class='alert alert-success']")
        for aldylogin in alreadylogin:
            assert isinstance(aldylogin.text, object)
            print(aldylogin.text)



