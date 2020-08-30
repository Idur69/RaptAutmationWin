import datetime
import unittest
from telnetlib import EC
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebdriverWait

#from Src.EnvSetup.EnvironmentSetUp import EnvironmentSetup
from Src.EnvSetup.cnfgurl import LoginUsers, Paths, EnvironmentSetup, Memory_and_Core_Percentages
from Src.PageObject.Pages.Admin_Login import AdminLogin
from Src.PageObject.Pages.MyUrl import Myurl
from Test_UI.TestUtility.ScreenShots import SS



class Kubernetes_Ui_Inferencing_01(EnvironmentSetup):

    def test_inferencing_dog_classification_auto(self):

        # Second browser driver1
        driver1 = self.driver1
        # self.driver1.get("http://52.34.222.154:3050/users/login")
        myurl = Myurl(self.driver1)
        myurl.access_url()
        driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        #ScreenShot Relative Path
        ss_path = '/K8s_UI/'
        #Creating object of screenshot utility
        ss = SS(driver1)

        # ------- Login Details ------------
        user = LoginUsers()
        Admin = user.user1_name
        Pwd = user.user1_password
        expadmin = user.user1_expadmin
        exppass = user.user1_exppass
        # ------ local path ------------
        paths = Paths()
        inf_path = paths.Inference_path

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
        # ---------Inferencing -----------------
        sleep(2)
        inferencing = self.driver1.find_element(By.ID, 'INFERENCING')
        inferencing.click()
        sleep(1)
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
        localpath.send_keys(inf_path)

        sleep(2)
        # ----------GPU Auto --------
        gpu = self.driver1.find_element(By.ID, 'r4')
        gpu.click()
        sleep(2)
        auto = self.driver1.find_element_by_id("r101")
        auto.click()
        sleep(2)
        # ------Screenshot-1-----------
        ss.ScreenShot(ss_path + "test_19_inferencing_dog_images_auto_setupscreen.png")
        # -------------------- setup btn -----------------
        setupbtn = self.driver1.find_element(By.ID, 'setupbtn')
        setupbtn.click()
        sleep(24)

        # -------Datsets & Training  ----------------
        traindir = self.driver1.find_element(By.ID, 'inferencedirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("dogs_breed_classification")
        sleep(2)

        trinfile = self.driver1.find_element(By.ID, 'infer_file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("classify.py")
        sleep(2)
        # --------- Train --------------------
        train = self.driver1.find_element_by_xpath("//a[@href='#train']")
        train.click()
        sleep(2)
        Train = self.driver1.find_element(By.ID, 'train_id')
        Train.click()
        sleep(400)
        gpuTime = driver1.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert isinstance(GpuUsage.text, object)
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(440)

        # --------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)
        # ------Screenshot-2-----------
        ss.ScreenShot(ss_path + "test_19_inferencing_dog_images_auto_elapsedtime.png")
        sleep(2)
        assert isinstance(myElem.text, object)
        print("dog_classification Auto -", str(myElem.text))
        for logs in driver1.get_log('browser'):
            print(logs)
        try:
           pass
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

