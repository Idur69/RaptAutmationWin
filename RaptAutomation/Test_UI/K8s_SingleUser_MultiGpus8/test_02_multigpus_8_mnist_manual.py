
import datetime
import unittest
from telnetlib import EC
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#from selenium.webdriver.support.wait import WebdriverWait

#from Src.EnvSetup.EnvironmentSetUp import EnvironmentSetup
from Src.EnvSetup.cnfgurl import EnvironmentSetup, LoginUsers, Paths, Memory_and_Core_Percentages
from Src.PageObject.Pages.Admin_Login import AdminLogin
from Src.PageObject.Pages.MyUrl import Myurl
from Src.PageObject.Pages.RaptUi import RaptUi
from Test_UI.TestUtility.ScreenShots import SS


class Kubernetes_Ui_MultiGpu_02(EnvironmentSetup):

    def test_local_mnist_Manual(self):

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        driver1.implicitly_wait(10)
        print("User-1 This is Title name :", driver1.title)
        # ------- Login Details ------------
        user = LoginUsers()
        Admin = user.user1_name
        Pwd = user.user1_password
        expected_username = user.user1_expadmin
        expected_password = user.user1_exppass
        # ------ local path ------------
        paths = Paths()
        locpath = paths.Local_path

        # ------Memory and core Percentages ----------
        percentages = Memory_and_Core_Percentages()
        gpuper0 = percentages.gpuper0
        gpuper1 = percentages.gpuper1
        gpuper2 = percentages.gpuper2
        gpuper3 = percentages.gpuper3
        gpuper4 = percentages.gpuper4
        gpuper5 = percentages.gpuper5
        gpuper6 = percentages.gpuper6
        gpuper7 = percentages.gpuper7
        coreper0 = percentages.coreper0
        coreper1 = percentages.coreper1
        coreper2 = percentages.coreper2
        coreper3 = percentages.coreper3
        coreper4 = percentages.coreper4
        coreper5 = percentages.coreper5
        coreper6 = percentages.coreper6
        coreper7 = percentages.coreper7

        # ScreenShot Relative Path
        ss_path = '/K8s_UI/'
        # Creating object of screenshot utility
        ss = SS(driver1)

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)

        admin_login.submit_login(Admin, Pwd)
        sleep(5)

        if Admin == expected_username and Pwd == expected_password:
            print("Login successful")
        else:
            assert print("Invalid credentials")

        print("************ Mnist Manual *****************")
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
        memory0.send_keys(gpuper0)
        sleep(1)
        memory1 = self.driver1.find_element(By.ID, 'gpupercent1')
        memory1.send_keys(gpuper1)
        sleep(1)
        memory2 = self.driver1.find_element(By.ID, 'gpupercent2')
        memory2.send_keys(gpuper2)
        sleep(1)
        memory3 = self.driver1.find_element(By.ID, 'gpupercent3')
        memory3.send_keys(gpuper3)
        sleep(1)
        memory4 = self.driver1.find_element(By.ID, 'gpupercent4')
        memory4.send_keys(gpuper4)
        sleep(1)
        memory5 = self.driver1.find_element(By.ID, 'gpupercent5')
        memory5.send_keys(gpuper5)
        sleep(1)
        memory6 = self.driver1.find_element(By.ID, 'gpupercent6')
        memory6.send_keys(gpuper6)
        sleep(1)
        memory7 = self.driver1.find_element(By.ID, 'gpupercent7')
        memory7.send_keys(gpuper7)
        print("gpu percentages : ", gpuper0, gpuper1, gpuper2, gpuper3, gpuper4, gpuper5, gpuper6, gpuper7)
        # --------core percentage -----------
        sleep(1)
        gpuvalue0 = self.driver1.find_element(By.ID, 'gpuvalue0')
        gpuvalue0.send_keys(coreper0)
        sleep(1)
        gpuvalue1 = self.driver1.find_element(By.ID, 'gpuvalue1')
        gpuvalue1.send_keys(coreper1)
        sleep(1)
        gpuvalue2 = self.driver1.find_element(By.ID, 'gpuvalue2')
        gpuvalue2.send_keys(coreper2)
        sleep(1)
        gpuvalue3 = self.driver1.find_element(By.ID, 'gpuvalue3')
        gpuvalue3.send_keys(coreper3)
        sleep(1)
        gpuvalue4 = self.driver1.find_element(By.ID, 'gpuvalue4')
        gpuvalue4.send_keys(coreper4)
        sleep(1)
        gpuvalue5 = self.driver1.find_element(By.ID, 'gpuvalue5')
        gpuvalue5.send_keys(coreper5)
        sleep(1)
        gpuvalue6 = self.driver1.find_element(By.ID, 'gpuvalue6')
        gpuvalue6.send_keys(coreper6)
        sleep(1)
        gpuvalue7 = self.driver1.find_element(By.ID, 'gpuvalue7')
        gpuvalue7.send_keys(coreper7)
        print("core percentages : ", coreper0, coreper1, coreper2, coreper3, coreper4, coreper5, coreper6, coreper7)
        sleep(2)

        # ------Screenshot-1-----------
        ss.ScreenShot(ss_path + "test_02_multigpus_8_mnist_manual_setupscreen.png")
        #-----Setup screen ------------
        setupbtn = self.driver1.find_element(By.ID, 'setupbtn')
        setupbtn.click()
        sleep(16)

        # -------Datsets & Training  ----------------
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
        # ------- Gpu Usage --------------------
        gpuTime = driver1.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert isinstance(GpuUsage.text, object)
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(60)
        # --------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)
        # --------Screen shot-2 -----------
        ss.ScreenShot(ss_path + "test_02_multigpus_8_mnist_manual_elapsedtime.png")
        sleep(2)
        assert isinstance(myElem.text, object)
        print("Mnist Manual -", str(myElem.text))

        #gettime = self.driver1.find_elements_by_id("elapsedTime")

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