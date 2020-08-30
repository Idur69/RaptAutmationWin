import datetime
import multiprocessing
import unittest

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Src.EnvSetup.cnfgurl import EnvironmentSetup, LoginUsers, Paths
from Src.PageObject.Pages.MyUrl import Myurl
from Test_UI.TestUtility.ScreenShots import SS


class Kubernetes_Ui_Parallel_Pgan_Mnist_03(EnvironmentSetup):

    def pgan_auto(self):

        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        driver1.implicitly_wait(10)
        print("User-2 This is Title name :", driver1.title)

        # ScreenShot Relative Path
        ss_path = '/K8s_UI/Parallel_MultiUser/'
        # Creating object of screenshot utility
        ss = SS(driver1)

        # ------- Login Details ------------
        user = LoginUsers()
        Admin = user.user2_name
        Pwd = user.user2_password
        expected_username = user.user2_expadmin
        expected_password = user.user2_exppass
        # ------ local path ------------
        paths = Paths()
        locpath = paths.Local_path
        # -------Pgan path -----------
        pgan_path = paths.Pgan_path

        user = self.driver1.find_element_by_name("username")
        user.send_keys(Admin)
        sleep(1)
        pwd = self.driver1.find_element_by_name("password")
        pwd.send_keys(Pwd)
        sleep(1)
        # self.driver1.find_element_by_class_name("btn btn-primary").click() ----this getting error
        # self.driver1.find_element_by_partial_link_text("Submit").click() ----this getting error--
        sub = self.driver1.find_element_by_tag_name("button")
        sub.click()
        for Logedout in self.driver1.find_elements_by_xpath("//*[@class='alert alert-success']"):
            assert isinstance(Logedout.text, object)
            assert (print(str(Logedout.text)))
        if (Admin == expected_username and Pwd == expected_password):
            print("Login successful")
        else:
            assert (print("failed to login"))
        # print("Login Successfull")
        sleep(3)
        print("************ Pgan Auto *****************")
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

        # ----------GPU Auto --------
        gpu = self.driver1.find_element(By.ID, 'r4')
        gpu.click()
        sleep(2)
        auto = self.driver1.find_element_by_id("r101")
        auto.click()
        sleep(2)
        print("Your selected Auto")
        # ------Screenshot-1-----------
        ss.ScreenShot(ss_path + "Parallel_03_singleGpu_pgan_auto-SetupScreen1.png")
        # -----Setup screen ------------
        setupbtn = self.driver1.find_element(By.ID, 'setupbtn')
        setupbtn.click()
        sleep(28)

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
            print("Gpu Usage-2 : ", str(GpuUsage.text))
        sleep(340)
        # --------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)
        # --------Screen shot-2 -----------
        ss.ScreenShot(ss_path + "test_03_singlGpu_pgan_auto_elapsedtime1.png")
        sleep(2)
        assert isinstance(myElem.text, object)
        print("Pgan Auto-2 -", str(myElem.text))

        # gettime = self.driver1.find_elements_by_id("elapsedTime")
        for logs in driver2.get_log('browser'):
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
    # Test case method 2
    def mnist_manual(self):

        gpuper = "98"
        coreper = "90"

        driver2 = self.driver2
        myurl = Myurl(self.driver2)
        myurl.access_url()
        driver2.implicitly_wait(10)
        print("User-1 This is Title name :", driver2.title)

        # ScreenShot Relative Path
        ss_path = '/K8s_UI/Parallel_MultiUser/'
        # Creating object of screenshot utility
        ss = SS(driver2)
        # ------- Login Details ------------
        user = LoginUsers()
        Admin = user.user1_name
        Pwd = user.user1_password
        expected_username = user.user1_expadmin
        expected_password = user.user1_exppass
        # ------ local path ------------
        paths = Paths()
        locpath = paths.Local_path

        sleep(2)
        user = self.driver2.find_element_by_name("username")
        user.send_keys(Admin)
        sleep(2)
        pwd = self.driver2.find_element_by_name("password")
        pwd.send_keys(Pwd)
        sleep(2)
        # self.driver2.find_element_by_class_name("btn btn-primary").click() ----this getting error
        # self.driver2.find_element_by_partial_link_text("Submit").click() ----this getting error--
        sub = self.driver2.find_element_by_tag_name("button")
        sub.click()
        for Logedout in self.driver2.find_elements_by_xpath("//*[@class='alert alert-success']"):
            assert isinstance(Logedout.text, object)
            assert (print(str(Logedout.text)))
        if (Admin == expected_username and Pwd == expected_password):
            print("Login successful")
        else:
            assert (print("failed to login"))
        # print("Login Successfull")
        sleep(3)
        print("************ Mnist Manual *****************")
        # --------Frame work--------------
        # f = self.driver2.find_element_by_class_name("f-image mxnet text-center")
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
        localpath.send_keys(locpath)

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
        print("gpu percentage-1 : ", gpuper, '%')
        # --------core percentage -----------
        sleep(1)
        gpuvalue = self.driver2.find_element(By.ID, 'gpuvalue0')
        gpuvalue.send_keys(coreper)
        print("core percentage-1 : ", coreper, '%')
        sleep(2)
        # ------Screenshot-1-----------
        ss.ScreenShot(ss_path + "test_03_singlGpu_mnist_manual_setupscreen2.png")
        # -------------------- setup btn -----------------
        setupbtn = self.driver2.find_element(By.ID, 'setupbtn')
        setupbtn.click()
        sleep(30)

        # -------Datsets & Training  ----------------
        traindir = self.driver2.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("Mnist_classification")
        sleep(2)

        trinfile = self.driver2.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("mnist_gpu.py")
        sleep(2)
        #sleep(40)
        # --------- Train --------------------
        train = self.driver2.find_element_by_xpath("//a[@href='#train']")
        train.click()
        sleep(2)
        Train = self.driver2.find_element(By.ID, 'train_id')
        Train.click()
        sleep(220)
        gpuTime = driver2.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert isinstance(GpuUsage.text, object)
            print("Gpu Usage-1 : ", str(GpuUsage.text))
        sleep(370)

        # --------Elapsed Time -------------------
        myElem = self.driver2.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)
        # ------Screenshot-2-----------
        ss.ScreenShot(ss_path + "test_03_singlGpu_mnist_manual_elapsedtime2.png")
        sleep(2)
        assert isinstance(myElem.text, object)
        print("Mnist Manual-1 -", str(myElem.text))
        for logs in driver2.get_log('browser'):
            print(logs)
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))
        # ---------Logout ----------------
        self.driver2.find_element_by_id("navbarDropdownMenuLink").click()
        logout = self.driver2.find_element_by_class_name("dropdown-item")
        logout.click()
        # print("Logout Successfull")
        sleep(5)
        for Logedout in self.driver2.find_elements_by_xpath("//*[@class='alert alert-success']"):
            assert isinstance(Logedout.text, object)
            print(str(Logedout.text))

    # Test case parallel threading
    def test_pagan_manual_mnist_manual(self):
        u1 = multiprocessing.Process(target=self.pgan_auto)
        u2 = multiprocessing.Process(target=self.mnist_manual)

        u1.start()
        sleep(5)
        u2.start()
        sleep(5)

        u1.join()
        u2.join()

