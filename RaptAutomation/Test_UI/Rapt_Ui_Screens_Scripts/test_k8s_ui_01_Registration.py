import datetime
import unittest
from time import sleep

from selenium import webdriver

#from Src.EnvSetup.EnvironmentSetUp import EnvironmentSetup
#from Src.EnvSetup.cnfgurl import EnvironmentSetup
#from Src.PageObject.Pages.Admin_Login import AdminLogin

from Src.EnvSetup.cnfgurl import EnvironmentSetup
from Src.PageObject.Pages.MyUrl import Myurl

class Rapt_Ui_Registration(EnvironmentSetup):

    def test_register_user1(self):

        name1 = "demo1"
        username1 = "demo1"
        email1 = "demo1@gmail.com"
        pwd1 = "123"
        pwd2 = "123"
        message = ""

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.registor_url()
        self.driver1.implicitly_wait(10)
        print("Title is :", driver1.title)

        name = self.driver1.find_element_by_name("name")
        name.send_keys(name1)
        sleep(2)
        username = self.driver1.find_element_by_name("username")
        username.send_keys(username1)
        sleep(2)
        email = self.driver1.find_element_by_name("email")
        email.send_keys(email1)
        sleep(2)
        password = self.driver1.find_element_by_name("password")
        password.send_keys(pwd1)
        sleep(2)
        password2 = self.driver1.find_element_by_name("password2")
        password2.send_keys(pwd2)
        sleep(2)
        submit = self.driver1.find_element_by_tag_name("button")
        submit.click()
        sleep(5)

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-success']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)
    #-------- User-2 ----------------------
    def test_register_user2(self):

        name1 = "demo2"
        username1 = "demo2"
        email1 = "demo2@gmail.com"
        pwd1 = "123"
        pwd2 = "123"
        message = ""

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.registor_url()
        self.driver1.implicitly_wait(10)
        print("Title is :", driver1.title)

        name = self.driver1.find_element_by_name("name")
        name.send_keys(name1)
        sleep(2)
        username = self.driver1.find_element_by_name("username")
        username.send_keys(username1)
        sleep(2)
        email = self.driver1.find_element_by_name("email")
        email.send_keys(email1)
        sleep(2)
        password = self.driver1.find_element_by_name("password")
        password.send_keys(pwd1)
        sleep(2)
        password2 = self.driver1.find_element_by_name("password2")
        password2.send_keys(pwd2)
        sleep(2)
        submit = self.driver1.find_element_by_tag_name("button")
        submit.click()
        sleep(5)

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-success']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)

    # -------- User-3 ----------------------
    def test_register_user3(self):

        name1 = "demo3"
        username1 = "demo3"
        email1 = "demo3@gmail.com"
        pwd1 = "123"
        pwd2 = "123"
        message = ""

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.registor_url()
        self.driver1.implicitly_wait(10)
        print("Title is :", driver1.title)

        name = self.driver1.find_element_by_name("name")
        name.send_keys(name1)
        sleep(2)
        username = self.driver1.find_element_by_name("username")
        username.send_keys(username1)
        sleep(2)
        email = self.driver1.find_element_by_name("email")
        email.send_keys(email1)
        sleep(2)
        password = self.driver1.find_element_by_name("password")
        password.send_keys(pwd1)
        sleep(2)
        password2 = self.driver1.find_element_by_name("password2")
        password2.send_keys(pwd2)
        sleep(2)
        submit = self.driver1.find_element_by_tag_name("button")
        submit.click()
        sleep(5)

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-success']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)

    # -------- User-4 ----------------------
    def test_register_user4(self):

        name1 = "demo4"
        username1 = "demo4"
        email1 = "demo4@gmail.com"
        pwd1 = "123"
        pwd2 = "123"
        message = ""

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.registor_url()
        self.driver1.implicitly_wait(10)
        print("Title is :", driver1.title)

        name = self.driver1.find_element_by_name("name")
        name.send_keys(name1)
        sleep(2)
        username = self.driver1.find_element_by_name("username")
        username.send_keys(username1)
        sleep(2)
        email = self.driver1.find_element_by_name("email")
        email.send_keys(email1)
        sleep(2)
        password = self.driver1.find_element_by_name("password")
        password.send_keys(pwd1)
        sleep(2)
        password2 = self.driver1.find_element_by_name("password2")
        password2.send_keys(pwd2)
        sleep(2)
        submit = self.driver1.find_element_by_tag_name("button")
        submit.click()
        sleep(5)

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-success']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)


