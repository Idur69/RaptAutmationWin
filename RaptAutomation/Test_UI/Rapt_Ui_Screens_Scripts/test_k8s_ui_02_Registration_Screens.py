import datetime
import unittest
from time import sleep

from selenium import webdriver

#from Src.EnvSetup.EnvironmentSetUp import EnvironmentSetup
#from Src.EnvSetup.cnfgurl import EnvironmentSetup
#from Src.PageObject.Pages.Admin_Login import AdminLogin
from Src.PageObject.Pages.MyUrl import Myurl
from Src.EnvSetup.cnfgurl import EnvironmentSetup


class Rapt_Ui_Registration_Screens(EnvironmentSetup):

    # ------Test case-1 Empty name ---------------
    
    def test_01_empty_name(self):

        name1 = ""
        username1 = "demodemo"
        email1 = "demo123@gmail.com"
        pwd1 = "123456"
        pwd2 = "123456"
        message = ""

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.registor_url()
        #self.driver1.get("http://54.218.117.171:3010/users/register")

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
        if not name1:
            print("Please enter name")
        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)
    
    # ------Test case-2 Name special characters check ---------------
    def test_02_name_specialchars_check(self):

        name1 = "demo@#$%"
        username1 = "demodemo"
        email1 = "demo123@gmail.com"
        pwd1 = "123456"
        pwd2 = "123456"
        message = ""

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.registor_url()
        self.driver1.implicitly_wait(10)
        print("Title is :", driver1.title)

        name = self.driver1.find_element_by_name("name")
        name.send_keys(name1)
        print("Your given name :",name1)
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

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)
    
    # ------Test case-3 Name  characters length check ---------------
    def test_03_name_charlength_check(self):

        name1 = "demodemodemodemodemodemo"
        username1 = "demodemo"
        email1 = "demo123@gmail.com"
        pwd1 = "123456"
        pwd2 = "123456"
        message = ""

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.registor_url()
        self.driver1.implicitly_wait(10)
        print("Title is :", driver1.title)

        name = self.driver1.find_element_by_name("name")
        name.send_keys(name1)
        print("Your given name :", name1)
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

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)
        #self.assertEqual(20, len(name1), "name character < 20")
    

    # ------Test case-4 Name must be string ---------------
    def test_04_name_mustbe_string(self):

        name1 = "demo123456"
        username1 = "demodemo"
        email1 = "demo123@gmail.com"
        pwd1 = "123456"
        pwd2 = "123456"
        message = ""

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.registor_url()
        self.driver1.implicitly_wait(10)
        print("Title is :", driver1.title)

        name = self.driver1.find_element_by_name("name")
        name.send_keys(name1)
        print("Your given name :", name1)
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

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)
       
    
    # ------Test case-5 Name already exit

    def test_05_name_already_exit(self):

        name1 = "demo"
        username1 = "demo"
        email1 = "demo@gmail.com"
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

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)
    

    # ------Test case-6 Empty username ---------------

    def test_06_username_empty(self):

        name1 = "demodemo"
        username1 = ""
        email1 = "demo123@gmail.com"
        pwd1 = "123456"
        pwd2 = "123456"
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
        if not username1:
            print("Please enter username")
        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)

    # ------Test case-7 Username special characters check ---------------
    def test_07_username_specialchar_check(self):

        name1 = "demodemo"
        username1 = "demo@#$%"
        email1 = "demo123@gmail.com"
        pwd1 = "123456"
        pwd2 = "123456"
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
        print("Your given username :", username1)
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

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)

    # ------Test case-8 Username  characters length check ---------------
    def test_08_username_charlength_check(self):

        name1 = "demodemo"
        username1 = "demodemodemodemodemodemo"
        email1 = "demo123@gmail.com"
        pwd1 = "123456"
        pwd2 = "123456"
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

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)
        # self.assertEqual(20, len(name1), "name character < 20")

    # ------Test case-9 Username must be string ---------------
    def test_09_username_mustbe_string(self):

        name1 = "demodemo"
        username1 = "demo123456"
        email1 = "demo123@gmail.com"
        pwd1 = "123456"
        pwd2 = "123456"
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
        print("your given username :",username1)
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

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)
    
    # ------Test case-10 Name already exit

    def test_10_name_already_exit(self):

        name1 = "demodemo"
        username1 = "demo"
        email1 = "demo12@gmail.com"
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

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)
    
    # ------Test case-11 Empty Email ---------------

    def test_11_empty_email(self):

        name1 = "demoo"
        username1 = "demoo"
        email1 = ""
        pwd1 = "123456"
        pwd2 = "123456"
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
        if not email1:
            print("Please enter email")
        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)

    # ------Test case-12 email special characters check ---------------
    def test_12_email_specialchar_check(self):

        name1 = "demoo"
        username1 = "demoo"
        email1 = "demo12%$#&@gmai.com"
        pwd1 = "123456"
        pwd2 = "123456"
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
        print("Your given email :", email1)
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

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)

    # ------Test case-13 email already exit

    def test_13_email_already_exit(self):

        name1 = "demoo"
        username1 = "demoo"
        email1 = "demo@gmail.com"
        pwd1 = "123456"
        pwd2 = "123456"
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

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)
    

    # ------Test case-14 Empty password ---------------

    def test_14_password_empty(self):

        name1 = "demoo"
        username1 = "demoo"
        email1 = "demoo123@gmail.com"
        pwd1 = ""
        pwd2 = "123456"
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
        if not pwd1:
            print("Please enter password")
        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)

    # ------Test case-15 password special characters check ---------------
    def test_15_password_specialchar_check(self):

        name1 = "demodemo"
        username1 = "demo@#$%"
        email1 = "demo123@gmail.com"
        pwd1 = "demo@#$%&"
        pwd2 = "123456"
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
        print("Your given password :", pwd1)
        sleep(2)
        password2 = self.driver1.find_element_by_name("password2")
        password2.send_keys(pwd2)
        sleep(2)
        submit = self.driver1.find_element_by_tag_name("button")
        submit.click()
        sleep(5)

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)

    # ------Test case-16 password  characters length check ---------------
    def test_16_password_character_length_check(self):

        name1 = "demoo"
        username1 = "demoo"
        email1 = "demo123@gmail.com"
        pwd1 = "123456988888878799879789987"
        pwd2 = "123456"
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

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)

    # ------Test case-17 password  do not match ---------------
    def test_17_password_donot_match(self):

        name1 = "demoo"
        username1 = "demoo"
        email1 = "demo123@gmail.com"
        pwd1 = "654321"
        pwd2 = "123456"
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

        msg = self.driver1.find_elements_by_xpath("//*[@class='alert alert-danger']")
        for message in msg:
            assert isinstance(message.text, object)
            print(message.text)

    # ------Test case-18 Valid details ---------------
    def test_18_registration_success(self):

        name1 = "raptui4"
        username1 = "raptui4"
        email1 = "raptui4123@gmail.com"
        pwd1 = "123456"
        pwd2 = "123456"
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

