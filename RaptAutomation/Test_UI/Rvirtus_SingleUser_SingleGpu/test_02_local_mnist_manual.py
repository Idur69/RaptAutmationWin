import datetime
import unittest
from time import sleep


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import sys



sys.path.append('..')

#from Src.EnvSetup.EnvironmentSetUp import EnvironmentSetup
from Src.EnvSetup.cnfgurl import LoginUsers, Paths, EnvironmentSetup, Memory_and_Core_Percentages
from Src.PageObject.Pages.Admin_Login import AdminLogin
from Src.PageObject.Pages.MyUrl import Myurl
from Test_UI.TestUtility.ScreenShots import SS
#from Test.TestUtility.ScreenShots import SS

class Rvirtus_Ui_Mnist_Manual(EnvironmentSetup):

    #def errorfun(self):
        #raise ValueError("Command terminated by signal 6 ")
    def test_local_mnist_manual(self):

        #gpuper = "80"
        #coreper = "90"
        
        driver2 = self.driver2

        myurl = Myurl(self.driver2)
        myurl.access_url()
        driver2.implicitly_wait(10)
        print("This is Title name :", driver2.title)

        # ScreenShot Relative Path
        ss_path = '/Rvirtus/'
        # Creating object of screenshot utility
        ss = SS(driver2)

        # ------Memory and core Percentages ----------
        percentages = Memory_and_Core_Percentages()
        gpuper = percentages.memory_08
        coreper = percentages.core_08
        # ------- Login Details ------------
        user = LoginUsers()
        Admin = user.user1_name
        Pwd = user.user1_password
        expadmin = user.user1_expadmin
        exppass = user.user1_exppass
        # ------ local path ------------
        paths = Paths()
        locGVpath = paths.Local_GVirtus_path
        Backendip = paths.Backend_ip

        admin_login = AdminLogin(driver2)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)
        admin_login.submit_login(Admin, Pwd)
        sleep(5)
        if Admin == expadmin and Pwd == exppass:
            print("Login successful")
        else:
            assert print("Invalid credentials")

        print("************ Mnist Manual *****************")
        # --------Frame work--------------
        f = self.driver2.find_element_by_xpath("//img[@src='/images/tenserflow.png']")
        f.click()
        print("Selected Tensorflow")
        sleep(2)
        # --------if you have compound class name you should write like this-----------
        inception = self.driver2.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        inception.click()
        sleep(1)
        print("Selected Inception")

        # -----------local folder---------------
        local = self.driver2.find_element(By.ID, 'r100')
        local.click()
        sleep(1)
        localpath = self.driver2.find_element(By.ID, 'local_dir_path')
        localpath.send_keys(locGVpath)

        sleep(2)

        # ----------GPU Manual --------
        gpu = self.driver2.find_element(By.ID, 'r4')
        gpu.click()
        sleep(2)

        print("Your selected Manual")
        manual = self.driver2.find_element_by_id("r102")
        manual.click()
        sleep(1)

        # ------ gpu percentage -----------
        memory0 = self.driver2.find_element(By.ID, 'gpupercent0')
        memory0.send_keys(gpuper)
        print("gpu percentage : ", gpuper, '%')
        # --------core percentage -----------
        sleep(1)
        gpuvalue = self.driver2.find_element(By.ID, 'gpuvalue0')
        gpuvalue.send_keys(coreper)
        print("core percentage : ", coreper, '%')
        sleep(2)
        # ------Screenshot-1-----------
        sshot = ss.ScreenShot(ss_path + "test_local_mnist_manual_setupscreen.png")
        print("screen shot : ", sshot)
        # -------------------- setup btn -----------------
        setupbtn = self.driver2.find_element(By.ID, 'setupbtn')
        setupbtn.click()
        sleep(25)

        # -------Datsets & Training  ----------------
        traindir = self.driver2.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("Mnist_classification")
        sleep(2)

        trinfile = self.driver2.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("mnist_deep.py")
        sleep(2)
        # --------- Train --------------------
        train = self.driver2.find_element_by_xpath("//a[@href='#train']")
        train.click()
        sleep(2)
        Train = self.driver2.find_element(By.ID, 'train_id')
        Train.click()
        sleep(30)
        gpuTime = driver2.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert isinstance(GpuUsage.text, object)
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(60)

        #console_logs = self.driver2.find_elements_by_id("logioReload")
        #console_logs.click()
        #for logs in console_logs:
        #assert isinstance(console_logs.text, object)
        #print("Console logs :\n",console_logs.text)

        #self.assertEqual()


        # --------Elapsed Time -------------------
        myElem = self.driver2.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)
        # ------Screenshot-2-----------
        sshot = ss.ScreenShot(ss_path + "test_local_mnist_manual_elapsedtime.png")
        sleep(2)
        print("screen shot : ", sshot)
        assert isinstance(myElem.text, object)
        print("Mnist Manual -", str(myElem.text))
        #raise ValueError("Command terminated by signal")
        #with pytest.raises(ValueError, match=r".* terminated by signal .* "):
            #self.errorfun()

        try:
            for logs in driver2.get_log('browser'):
                print(logs)
            pass

            #log = self.get_browser_console_log()
            #log = self.driver2.get_log(browser)
            #print("Console Log: ",log)
        except Exception as e:
            print("Exception Occurred :" + str(e))
        # ---------Logout ----------------
        self.driver2.find_element_by_id("navbarDropdownMenuLink").click()
        logout = self.driver2.find_element_by_class_name("dropdown-item")
        logout.click()
        sleep(5)
        for Logedout in self.driver2.find_elements_by_xpath("//*[@class='alert alert-success']"):
            assert isinstance(Logedout.text, object)
            print(str(Logedout.text))
        

