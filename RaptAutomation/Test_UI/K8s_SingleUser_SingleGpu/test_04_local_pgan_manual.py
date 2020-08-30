
import datetime
import unittest
from telnetlib import EC
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#from Src.EnvSetup.EnvironmentSetUp import EnvironmentSetup
from Src.EnvSetup.cnfgurl import LoginUsers, Paths, EnvironmentSetup, Memory_and_Core_Percentages
from Src.PageObject.Pages.Admin_Login import AdminLogin
from Src.PageObject.Pages.MyUrl import Myurl
from Test_UI.TestUtility.ScreenShots import SS



class Kubernetes_Ui_Pgan_Manual(EnvironmentSetup):

    def test_local_pgan_manual(self):
        #gpuper = "50"
        #coreper = "90"

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        # ScreenShot Relative Path
        ss_path = '/K8s_UI/'
        # Creating object of screenshot utility
        ss = SS(driver1)

        # ------Memory and core Percentages ----------
        percentages = Memory_and_Core_Percentages()
        gpuper = percentages.memory_10
        coreper = percentages.core_10
        # ------- Login Details ------------
        user = LoginUsers()
        Admin = user.user1_name
        Pwd = user.user1_password
        expadmin = user.user1_expadmin
        exppass = user.user1_exppass
        # ------ local path ------------
        paths = Paths()
        locpath = paths.Local_path
        # -------Pgan path -----------
        pgan_path = paths.Pgan_path

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)
        admin_login.submit_login(Admin, Pwd)
        sleep(5)

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

        if Admin == expadmin and Pwd == exppass:
            print("Login successful")
        else:
            assert print("Invalid credentials")

        print("************ Pgan Manual *****************")
        # --------Frame work--------------
        # f = self.driver1.find_element_by_class_name("f-image mxnet text-center")
        f = self.driver1.find_element_by_xpath("//img[@src='/images/tenserflow.png']")
        f.click()
        print("Selected Tensorflow")
        sleep(2)
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        inception.click()
        sleep(1)
        print("Selected Inception")

        # -----------local folder---------------
        local = self.driver1.find_element(By.ID, 'r100')
        local.click()
        sleep(1)
        localpath = self.driver1.find_element(By.ID, 'local_dir_path')
        localpath.send_keys(locpath)
        # ----------GPU Manual --------
        gpu = self.driver1.find_element(By.ID, 'r4')
        gpu.click()
        sleep(2)
        print("Your selected Manual")
        manual = self.driver1.find_element_by_id("r102")
        manual.click()
        sleep(1)
        # ------ gpu percentage -----------
        memory0 = self.driver1.find_element(By.ID, 'gpupercent0')
        memory0.send_keys(gpuper)
        print("gpu percentage : ", gpuper, '%')
        # --------core percentage -----------
        sleep(1)
        gpuvalue = self.driver1.find_element(By.ID, 'gpuvalue0')
        gpuvalue.send_keys(coreper)
        print("core percentage : ", coreper, '%')
        sleep(2)
        # ------Screenshot-1-----------
        ss.ScreenShot(ss_path + "test_04_pgan_manual_setupscreen.png")
        setupbtn = self.driver1.find_element(By.ID, 'setupbtn')
        setupbtn.click()
        sleep(25)

        # -------Datsets & Training  ----------------
        traindir = self.driver1.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("pgan")
        sleep(2)

        trinfile = self.driver1.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("train.py")
        sleep(2)

        # --------- Train --------------------
        train = self.driver1.find_element_by_xpath("//a[@href='#train']")
        train.click()
        sleep(2)
        textpath = self.driver1.find_element_by_id("textVal")
        textpath.clear()
        textpath.send_keys(pgan_path)
        sleep(2)
        Train = self.driver1.find_element(By.ID, 'train_id')
        Train.click()

        sleep(200)
        # ------- Gpu Usage --------------------
        gpuTime = driver1.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert isinstance(GpuUsage.text, object)
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(350)
        # --------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)
        # ------Screenshot-2-----------
        ss.ScreenShot(ss_path + "test_04_pgan_manual_elapsedtime.png")
        sleep(2)
        assert isinstance(myElem.text, object)
        print("Pgan Manual -", str(myElem.text))

        #gettime = self.driver1.find_elements_by_id("elapsedTime")
        for logs in driver1.get_log('browser'):
            print(logs)
        try:
            '''
            # enable browser logging
            d = DesiredCapabilities.CHROME
            d['loggingPrefs'] = {'browser': 'ALL'}
            driver1 = webdriver1.Chrome(desired_capabilities=d)
            '''
            # print messages
            for entry in driver1.get_log('browser'):
                assert print(entry)

            '''for elapsedTime in gettime:
                assert isinstance(elapsedTime.text, object)
                print("Pggan Manual -", str(elapsedTime.text))'''
        except Exception as e:
            print("Exception Occurred :" + str(e))

        # ---------Logout ----------------
        self.driver1.find_element_by_id("navbarDropdownMenuLink").click()
        logout = self.driver1.find_element_by_class_name("dropdown-item")
        logout.click()
        sleep(5)
        for Logedout in self.driver1.find_elements_by_xpath("//*[@class='alert alert-success']"):
            assert isinstance(Logedout.text, object)
            print(str(Logedout.text))