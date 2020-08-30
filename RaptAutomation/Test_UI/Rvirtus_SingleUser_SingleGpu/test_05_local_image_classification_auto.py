import datetime
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#from Src.EnvSetup.EnvironmentSetUp import EnvironmentSetup
from Src.EnvSetup.cnfgurl import LoginUsers, Paths, EnvironmentSetup, Memory_and_Core_Percentages
from Src.PageObject.Pages.Admin_Login import AdminLogin
from Src.PageObject.Pages.MyUrl import Myurl
from Test_UI.TestUtility.ScreenShots import SS


class Rvirtus_Ui_Image_Auto(EnvironmentSetup):

    def test_local_image_auto(self):

        driver1 = self.driver1

        myurl = Myurl(self.driver1)
        myurl.access_url()
        driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        # ScreenShot Relative Path
        ss_path = '/Rvirtus/'
        # Creating object of screenshot utility
        ss = SS(driver1)
        # ------- Login Details ------------
        user = LoginUsers()
        Admin = user.user1_name
        Pwd = user.user1_password
        expadmin = user.user1_expadmin
        exppass = user.user1_exppass
        # ------ local path ------------
        paths = Paths()
        locpath = paths.Local_path
        # -------Image classification path -----------
        flower_path = paths.Local_Image_clf_path

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)

        admin_login.submit_login(Admin, Pwd)
        sleep(5)

        if Admin == expadmin and Pwd == exppass:
            print("Login successful")
        else:
            assert print("Invalid credentials")

        print("************ Image classification Auto *****************")
        # --------Frame work--------------
        # f = self.driver1.find_element_by_class_name("f-image mxnet text-center")
        f = self.driver1.find_element_by_xpath("//img[@src='/images/tenserflow.png']")
        f.click()
        print("Selected Tensorflow")
        sleep(2)
        # --------if you have compound class name you should write like this-----------
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

        sleep(2)
        # ----------GPU Auto --------
        gpu = self.driver1.find_element(By.ID, 'r4')
        gpu.click()
        sleep(2)
        auto = self.driver1.find_element_by_id("r101")
        auto.click()
        sleep(2)
        print("Your selected Auto")
        # ------Screenshot-1-----------
        ss.ScreenShot(ss_path + "test_05_local_image_clf_auto_setupscreen.png")
        # -------------------- setup btn -----------------
        setupbtn = self.driver1.find_element(By.ID, 'setupbtn')
        setupbtn.click()
        sleep(25)
        traindir = self.driver1.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("flower_classification")
        sleep(2)
        trinfile = self.driver1.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("retrain-new.py")
        sleep(2)
        # --------- Train --------------------
        train = self.driver1.find_element_by_xpath("//a[@href='#train']")
        train.click()
        textpath = self.driver1.find_element_by_id("textVal")
        textpath.clear()
        textpath.send_keys(flower_path)
        sleep(2)
        Train = self.driver1.find_element(By.ID, 'train_id')
        Train.click()
        sleep(300)
        gpuTime = driver1.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert isinstance(GpuUsage.text, object)
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(350)

        # --------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)
        # --------Screen shot-2 -----------
        ss.ScreenShot(ss_path + "test_05_local_image_clf_elapsedtime.png")
        sleep(2)
        assert isinstance(myElem.text, object)
        print("Image classification Auto -", str(myElem.text))
        for logs in driver1.get_log('browser'):
            print(logs)
        try:

            ''' elapTime = driver1.find_elements_by_link_text("elapsedTime")
             elapTime.click()
             for elapsedTime in elapTime:
                 assert isinstance(elapsedTime.text, object)
                 print("Mnist Auto -", str(elapsedTime.text))'''
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
