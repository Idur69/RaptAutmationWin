import datetime
import multiprocessing
import unittest

from time import sleep

from selenium import webdriver1
from selenium.webdriver1.common.by import By
from selenium.webdriver1.support.select import Select

from Src.EnvSetup.cnfgurl import EnvironmentSetup, LoginUsers, Paths
from Src.PageObject.Pages.MyUrl import Myurl
from Test_UI.TestUtility.ScreenShots import SS


class Kubernetes_Ui_VoltaGpu_05(EnvironmentSetup):

    def pgan_manual1(self):

        gpuper = "40"
        coreper = "90"

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
        # -------Pgan path -----------
        pgan_path = paths.Pgan_path
        # ScreenShot Relative Path
        ss_path = '/K8s_UI/Parallel_VoltaGpu/'
        # Creating object of screenshot utility
        ss = SS(driver1)
        user = self.driver1.find_element_by_name("username")
        user.send_keys(Admin)
        sleep(2)
        pwd = self.driver1.find_element_by_name("password")
        pwd.send_keys(Pwd)
        sleep(2)
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
        ss.ScreenShot(ss_path + "test_05_voltaGpu_pgan_manual1_setupscreen1.png")
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
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(350)
        # --------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)
        # ------Screenshot-2-----------
        ss.ScreenShot(ss_path + "test_05_voltaGpu_pgan_manual1_elapsedtime1.png")
        sleep(2)
        assert isinstance(myElem.text, object)
        print("Pgan Manual -", str(myElem.text))

        try:
            for logs in driver1.get_log('browser'):
                print(logs)
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
    # Test method 2
    def pgan_manual2(self):

        gpuper = "50"
        coreper = "90"
        driver2 = self.driver2
        myurl = Myurl(self.driver2)
        myurl.access_url()
        driver2.implicitly_wait(10)
        print("User-2 This is Title name :", driver2.title)

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
        # ScreenShot Relative Path
        ss_path = '/K8s_UI/Parallel_VoltaGpu/'
        # Creating object of screenshot utility
        ss = SS(driver2)
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

        print("************ Pgan Manual *****************")
        # --------Frame work--------------
        # f = self.driver2.find_element_by_class_name("f-image mxnet text-center")
        f = self.driver2.find_element_by_xpath("//img[@src='/images/tenserflow.png']")
        f.click()
        print("Selected Tensorflow")
        sleep(2)
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
        ss.ScreenShot(ss_path + "test_05_voltaGpu_pgan_manual2_setupscreen2.png")
        setupbtn = self.driver2.find_element(By.ID, 'setupbtn')
        setupbtn.click()
        sleep(28)

        # -------Datsets & Training  ----------------
        traindir = self.driver2.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("pgan")
        sleep(2)

        trinfile = self.driver2.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("train.py")
        sleep(2)

        # --------- Train --------------------
        train = self.driver2.find_element_by_xpath("//a[@href='#train']")
        train.click()
        sleep(2)
        textpath = self.driver2.find_element_by_id("textVal")
        textpath.clear()
        textpath.send_keys(pgan_path)
        sleep(2)
        Train = self.driver2.find_element(By.ID, 'train_id')
        Train.click()

        sleep(200)
        # ------- Gpu Usage --------------------
        gpuTime = driver2.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert isinstance(GpuUsage.text, object)
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(350)
        # --------Elapsed Time -------------------
        myElem = self.driver2.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)

        # ------Screenshot-2-----------
        ss.ScreenShot(ss_path + "test_05_voltaGpu_pgan_manual2_elapsedtime2.png")
        sleep(2)
        assert isinstance(myElem.text, object)
        print("Pgan Manual -", str(myElem.text))

        try:
            for logs in driver2.get_log('browser'):
                print(logs)
            pass
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
    # Test method 3
    def pgan_manual3(self):

        gpuper = "60"
        coreper = "90"
        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        driver1.implicitly_wait(10)
        print("User-3 This is Title name :", driver1.title)

        # ------- Login Details ------------
        user = LoginUsers()
        Admin = user.user3_name
        Pwd = user.user3_password
        expected_username = user.user3_expadmin
        expected_password = user.user3_exppass
        # ------ local path ------------
        paths = Paths()
        locpath = paths.Local_path
        # -------Pgan path -----------
        pgan_path = paths.Pgan_path

        # ScreenShot Relative Path
        ss_path = '/Parallel/MultiUser_MultiInstance5/'
        # Creating object of screenshot utility
        ss = SS(driver1)
        user = self.driver1.find_element_by_name("username")
        user.send_keys(Admin)
        sleep(2)
        pwd = self.driver1.find_element_by_name("password")
        pwd.send_keys(Pwd)
        sleep(2)
        # self.driver1.find_element_by_class_name("btn btn-primary").click() ----this getting error
        # self.driver1.find_element_by_partial_link_text("Submit").click() ----this getting error--
        sub = self.driver1.find_element_by_tag_name("button")
        sub.click()
        for Logedout in self.driver1.find_elements_by_xpath("//*[@class='alert alert-success']"):
            assert isinstance(Logedout.text, object)
            assert (print(str(Logedout.text)))
        if (Admin == expected_username and Pwd == expected_password):
            print("User-3 Login successful")
        else:
            assert (print("failed to login"))

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
        ss.ScreenShot(ss_path + "test_05_voltaGpu_pgan_manual3_setupscreen3.png")
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
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(350)
        # --------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)
        # ------Screenshot-2-----------
        ss.ScreenShot(ss_path + "test_05_voltaGpu_pgan_manual1_elapsedtime1.png")
        sleep(2)
        assert isinstance(myElem.text, object)
        print("Pgan Manual -", str(myElem.text))

        try:
            for logs in driver1.get_log('browser'):
                print(logs)
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


    # Test case parallel threading
    def test_pagan_auto_manual(self):
        u1 = multiprocessing.Process(target=self.pgan_manual1)
        u2 = multiprocessing.Process(target=self.pgan_manual2)
        u3 = multiprocessing.Process(target=self.pgan_manual3)

        u1.start()
        sleep(5)
        u2.start()
        sleep(5)
        u3.start()
        sleep(10)

        u1.join()
        u2.join()
        u3.join()

