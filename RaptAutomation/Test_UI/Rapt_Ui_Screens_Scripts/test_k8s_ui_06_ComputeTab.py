import datetime
import pickle
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#from Src.EnvSetup.EnvironmentSetUp import EnvironmentSetup
from Src.EnvSetup.cnfgurl import EnvironmentSetup
#from RaptAutomation.Src.PageObject.Pages.Admin_Login import AdminLogin
from Src.PageObject.Pages.MyUrl import Myurl
from Src.PageObject.Pages.RaptUi import RaptUi


class Rapt_Ui_ComputeTab(EnvironmentSetup):

    # Test case-1 Empty Memory %
    def test_01_empty_memroy_percentage(self):
        driver1 = self.driver1
        memory = ""
        core = "90"
        path = "/mnt/rapt/tensorflow-UI"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(3)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.Localfolder()
        sleep(1)

        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Manual()
        sleep(1)
        print("Your selected Manual")
        # raptui.set_Memorypercentage("80")
        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')
        memoryper.send_keys(memory)
        sleep(1)
        print("Memory percetage :", memory, "%")
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(1)
        print("Core percetage :", core, "%")
        raptui.Setupbtn()
        sleep(2)
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test case-2 Empty Core %
    def test_02_empty_core_percentage(self):
        driver1 = self.driver1
        memory = "60"
        core = ""
        path = "/mnt/rapt/tensorflow-UI"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(3)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.Localfolder()
        sleep(1)

        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Manual()
        sleep(1)
        print("Your selected Manual")
        # raptui.set_Memorypercentage("80")
        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')
        memoryper.send_keys(memory)
        sleep(1)
        print("Memory percetage :", memory, "%")
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(1)
        print("Core percetage :", core, "%")
        raptui.Setupbtn()
        sleep(2)
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))
    # Test case-3 Empty Memory % and core %
    def test_03_empty_memory_and_core_percentage(self):
        driver1 = self.driver1
        memory = ""
        core = ""
        path = "/mnt/rapt/tensorflow-UI"
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        myurl = Myurl(self.driver1)
        myurl.access_url()
        sleep(3)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.Localfolder()
        sleep(1)

        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Manual()
        sleep(1)
        print("Your selected Manual")
        # raptui.set_Memorypercentage("80")
        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')
        memoryper.send_keys(memory)
        sleep(1)
        print("Memory percetage :", memory, "%")
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(1)
        print("Core percetage :", core, "%")
        raptui.Setupbtn()
        sleep(2)
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test case-4 Negative memory %
    def test_04_negative_memory_percentage(self):
        driver1 = self.driver1
        memory = "-50"
        core = "90"
        path = "/mnt/rapt/tensorflow-UI"
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        myurl = Myurl(self.driver1)
        myurl.access_url()
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.Localfolder()
        sleep(1)

        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Manual()
        sleep(1)
        print("Your selected Manual")
        # raptui.set_Memorypercentage("80")
        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')
        memoryper.send_keys(memory)
        sleep(1)
        print("Memory percetage :", memory, "%")


        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(1)
        print("Core percetage :", core, "%")
        raptui.Setupbtn()
        sleep(2)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test case-5 Negative core %
    def test_05_negative_core_percentage(self):
        driver1 = self.driver1
        memory = "80"
        core = "-90"
        path = "/mnt/rapt/tensorflow-UI"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(3)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.Localfolder()
        sleep(1)

        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Manual()
        sleep(1)
        print("Your selected Manual")
        # raptui.set_Memorypercentage("80")
        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')
        memoryper.send_keys(memory)
        sleep(1)
        print("Memory percetage :", memory, "%")
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(1)
        print("Core percetage :", core, "%")

        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)

        raptui.Setupbtn()
        sleep(2)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test case-6 Dont enter string at memory percentage %
    def test_06_memory_percentage_string(self):
        driver1 = self.driver1
        memory = "80p"
        core = "90"
        path = "/mnt/rapt/tensorflow-UI"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.Localfolder()
        sleep(1)

        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Manual()
        sleep(1)
        print("Your selected Manual")
        # raptui.set_Memorypercentage("80")
        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')
        memoryper.send_keys(memory)
        sleep(1)
        print("Memory percetage :", memory, "%")


        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(1)
        print("Core percetage :", core, "%")
        raptui.Setupbtn()
        sleep(2)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test case-7 Dont enter string at core percentage %
    def test_07_core_percentage_string(self):
        driver1 = self.driver1
        memory = "40"
        core = "90p"
        path = "/mnt/rapt/tensorflow-UI"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(3)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.Localfolder()
        sleep(1)

        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Manual()
        sleep(1)
        print("Your selected Manual")
        # raptui.set_Memorypercentage("80")
        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')
        memoryper.send_keys(memory)
        sleep(1)
        print("Memory percetage :", memory)
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(2)
        print("Core percetage :", core )

        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)

        #raptui.Setupbtn()
        #sleep(2)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test case-8 Empty Memory %
    def test_08_memroy_percentage_zero(self):
        driver1 = self.driver1
        memory = "0"
        core = "90"
        path = "/mnt/rapt/tensorflow-UI"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(3)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.Localfolder()
        sleep(1)

        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Manual()
        sleep(1)
        print("Your selected Manual")
        # raptui.set_Memorypercentage("80")
        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')
        memoryper.send_keys(memory)
        sleep(1)
        print("Memory percetage :", memory, "%")
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(1)
        print("Core percetage :", core, "%")
        raptui.Setupbtn()
        sleep(2)
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test case-9 Empty Core %
    def test_09_core_percentage_zero(self):
        driver1 = self.driver1
        memory = "60"
        core = "0"
        path = "/mnt/rapt/tensorflow-UI"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(3)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.Localfolder()
        sleep(1)

        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Manual()
        sleep(1)
        print("Your selected Manual")
        # raptui.set_Memorypercentage("80")
        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')
        memoryper.send_keys(memory)
        sleep(1)
        print("Memory percetage :", memory, "%")
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(1)
        print("Core percetage :", core, "%")
        raptui.Setupbtn()
        sleep(2)
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test case-10 memory % = 120
    def test_10_memroy_percentage_greater(self):
        driver1 = self.driver1
        memory = "120"
        core = "90"
        path = "/mnt/rapt/tensorflow-UI"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(3)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.Localfolder()
        sleep(1)

        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Manual()
        sleep(1)
        print("Your selected Manual")
        # raptui.set_Memorypercentage("80")
        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')
        memoryper.send_keys(memory)
        sleep(1)
        print("Memory percetage :", memory, "%")
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(1)
        print("Core percetage :", core, "%")
        raptui.Setupbtn()
        sleep(2)
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test case-11 Core % = 120
    def test_11_core_percentage_greater(self):
        driver1 = self.driver1
        memory = "60"
        core = "120"
        path = "/mnt/rapt/tensorflow-UI"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(3)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.Localfolder()
        sleep(1)

        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Manual()
        sleep(1)
        print("Your selected Manual")
        # raptui.set_Memorypercentage("80")
        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')
        memoryper.send_keys(memory)
        sleep(1)
        print("Memory percetage :", memory, "%")
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(1)
        print("Core percetage :", core, "%")
        raptui.Setupbtn()
        sleep(2)
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test case-12 without auto and manual
    def test_12_without_auto_manual(self):
        driver1 = self.driver1

        path = "/mnt/rapt/tensorflow-UI"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(3)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.Localfolder()
        sleep(1)

        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        #raptui.Manual()
        raptui.Setupbtn()
        sleep(2)
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    #Test case-13 empty train directory
    def test_13_empty_train_directory(self):
        driver1 = self.driver1
        memory = "40"
        core = "90"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)

        raptui.Localfolder()
        path = "/mnt/rapt/tensorflow-UI"
        sleep(1)
        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Manual()
        sleep(1)
        print("Selected Manual")

        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')

        memoryper.send_keys(memory)
        sleep(1)
        print("Memory percentage :", memory)
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(1)
        print("Core percentage :", core)
        raptui.Setupbtn()
        sleep(23)
        traindir = self.driver1.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("Mnist_classification")
        sleep(2)
        trinfile = self.driver1.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("mnist_gpu.py")
        sleep(2)
        traindir = self.driver1.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("Select File")
        sleep(2)
        nextbtn = self.driver1.find_element_by_xpath("//*[@class='btnTrain btn btn-secondary float-lg-right ml-2']")
        nextbtn.click()
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(3)
        # ------------ Alert end -------------
        #raptui.Train()
        sleep(1)
        #raptui.TrainButton()
        sleep(5)

        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))
    #Test case-14 empty train file
    def test_14_empty_train_file(self):
        driver1 = self.driver1
        memory = "40"
        core = "90"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)

        raptui.Localfolder()
        path = "/mnt/rapt/tensorflow-UI"
        sleep(1)
        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")
       # memoryper = self.driver1.find_element(By.ID, 'gpupercent0')

        #memoryper.send_keys(memory)
        #sleep(1)
        #print("Memory percentage :", memory)
        #coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        #coreper.send_keys(core)
        #sleep(1)
        #print("Core percentage :", core)
        raptui.Setupbtn()
        sleep(23)
        traindir = self.driver1.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("Mnist_classification")
        sleep(2)
        trinfile = self.driver1.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("Select File")
        sleep(2)

        nextbtn = self.driver1.find_element_by_xpath("//*[@class='btnTrain btn btn-secondary float-lg-right ml-2']")
        nextbtn.click()
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(3)
        # ------------ Alert end -------------
        #raptui.Train()
        sleep(1)
        #raptui.TrainButton()
        sleep(5)

        try:
            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    #Test case-15 empty train path
    def test_15_empty_train_path(self):
        driver1 = self.driver1
        memory = "40"
        core = "90"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)

        raptui.Localfolder()
        path = "/mnt/rapt/tensorflow-UI"
        sleep(1)
        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")
        # memoryper = self.driver1.find_element(By.ID, 'gpupercent0')

        # memoryper.send_keys(memory)
        # sleep(1)
        # print("Memory percentage :", memory)
        # coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        # coreper.send_keys(core)
        # sleep(1)
        # print("Core percentage :", core)
        raptui.Setupbtn()
        sleep(24)
        traindir = self.driver1.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("Mnist_classification")
        sleep(2)
        trinfile = self.driver1.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("mnist_gpu.py")
        sleep(2)

        nextbtn = self.driver1.find_element_by_xpath("//*[@class='btnTrain btn btn-secondary float-lg-right ml-2']")
        nextbtn.click()
        sleep(3)
        txttrain = self.driver1.find_element(By.ID, 'textVal')
        txttrain.clear()
        sleep(3)

        Train = self.driver1.find_element(By.ID, 'train_id')
        Train.click()
        sleep(3)
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(3)
        # ------------ Alert end -------------
        #raptui.Train()
        sleep(1)
        #raptui.TrainButton()

        sleep(5)
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    #Test case-16  Invalid train path
    def test_16_Invalid_train_path(self):
        driver1 = self.driver1
        memory = "40"
        core = "90"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)

        raptui.Localfolder()
        path = "/mnt/rapt/tensorflow-UI"
        sleep(1)
        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")
        # memoryper = self.driver1.find_element(By.ID, 'gpupercent0')

        # memoryper.send_keys(memory)
        # sleep(1)
        # print("Memory percentage :", memory)
        # coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        # coreper.send_keys(core)
        # sleep(1)
        # print("Core percentage :", core)
        raptui.Setupbtn()
        sleep(24)
        traindir = self.driver1.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("Mnist_classification")
        sleep(2)
        trinfile = self.driver1.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("mnist_gpu.py")
        sleep(2)

        nextbtn = self.driver1.find_element_by_xpath("//*[@class='btnTrain btn btn-secondary float-lg-right ml-2']")
        nextbtn.click()
        sleep(2)
        txttrain = self.driver1.find_element(By.ID, 'textVal')
        txttrain.clear()
        sleep(1)
        exppath = "python -u /tensorflow/training/Mnist_classification/mnist_gpu.py"
        path = "python -u /tensorflow/training/Mnist_classification/mnistgpu.py"
        path = txttrain.send_keys(path)
        sleep(2)
        self.assertEqual(exppath,path,"Please enter valid path")
        #Train = self.driver1.find_element(By.ID, 'train_id')
        #Train.click()
        sleep(2)
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    #Test case-17  Logout
    def test_17_Logout(self):
        driver1 = self.driver1
        memory = "40"
        core = "90"
        #memory1 = "50"
        #core1 = "90"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://54.201.43.175:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.201.43.175:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        sleep(2)
        '''
        print("Selected Tensorflow")
        sleep(1)
        
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)

        raptui.Localfolder()
        path = "/mnt/rapt/tensorflow-UI"
        sleep(1)
        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Manual()
        sleep(1)
        print("Selected Manual")

        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')
        memoryper.send_keys(memory)
        sleep(1)
        print("Memory percentage :", memory)
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(1)
        print("Core percentage :", core)
        raptui.Setupbtn()
        sleep(24)

        #--------- setup back ----------
        setupback = self.driver1.find_element_by_xpath("//a[@href='#setup1']")
        setupback.click()
        sleep(2)
        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')
        memoryper.clear()
        memoryper.send_keys(memory1)
        sleep(1)
        print("Memory percentage :", memory1)
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.clear()
        coreper.send_keys(core1)
        sleep(1)
        print("Core percentage :", core1)
        raptui.Setupbtn()
        sleep(24)
        traindir = self.driver1.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("Mnist_classification")
        sleep(2)
        trinfile = self.driver1.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("mnist_gpu.py")
        sleep(2)
        # --------- Train --------------------
        train = self.driver1.find_element_by_xpath("//a[@href='#train']")
        train.click()
        sleep(2)
        Train = self.driver1.find_element(By.ID, 'train_id')
        Train.click()
        sleep(20)
        gpuTime = driver1.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert isinstance(GpuUsage.text, object)
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(30)
        # --------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(2)
        assert isinstance(myElem.text, object)
        print("Mnist Manual -", str(myElem.text))
        '''


        # ---------Logout ----------------
        self.driver1.find_element_by_id("navbarDropdownMenuLink").click()
        logout = self.driver1.find_element_by_class_name("dropdown-item")
        logout.click()
        sleep(5)
        for Logedout in self.driver1.find_elements_by_xpath("//*[@class='alert alert-success']"):
            assert isinstance(Logedout.text, object)
            print(str(Logedout.text))
            #print("Your logout successful")



