import datetime
import multiprocessing
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#from Src.EnvSetup.EnvironmentSetUp import EnvironmentSetup
from RaptAutomation.Src.EnvSetup.cnfgurl import LoginUsers, Paths, EnvironmentSetup, Memory_and_Core_Percentages
from RaptAutomation.Src.PageObject.Pages.Admin_Login import AdminLogin
from RaptAutomation.Src.PageObject.Pages.MyUrl import Myurl
from RaptAutomation.Test.TestUtility.ScreenShots import SS


class Rvirtus_Parallel_01(EnvironmentSetup):

    def mnist_auto_01(self):
        # gpuper = "80"
        # coreper = "90"
        driver1 = self.driver1

        myurl = Myurl(self.driver1)
        myurl.access_url()
        driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        # ScreenShot Relative Path
        ss_path = '/Rvirtus/'
        # Creating object of screenshot utility
        ss = SS(driver1)

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

        print("************ Mnist Manual *****************")
        # --------Frame work--------------
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
        localpath.send_keys(locGVpath)

        sleep(2)
        # ----------GPU Auto --------
        gpu = self.driver1.find_element(By.ID, 'r4')
        gpu.click()
        sleep(2)
        auto = self.driver1.find_element_by_id("r101")
        auto.click()
        sleep(5)
        print("Your selected Auto")
        # ---------Backend IP --------------
        '''
        backendip = self.driver1.find_element(By.ID, 'gpuip0')
        backendip.clear()
        sleep(1)
        backendip.send_keys(Backendip)
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
        '''

        # ------Screenshot-1-----------
        ss.ScreenShot(ss_path + "test_parallel_01_mnist_auto1_setupsscreen.png")
        # -------------------- setup btn -----------------
        setupbtn = self.driver1.find_element(By.ID, 'setupbtn')
        setupbtn.click()
        sleep(25)

        # -------Datsets & Training  ----------------
        traindir = self.driver1.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("Mnist_classification")
        sleep(2)

        trinfile = self.driver1.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("mnist_deep.py")
        sleep(2)
        # --------- Train --------------------
        train = self.driver1.find_element_by_xpath("//a[@href='#train']")
        train.click()
        sleep(2)
        Train = self.driver1.find_element(By.ID, 'train_id')
        Train.click()
        sleep(30)
        gpuTime = driver1.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert isinstance(GpuUsage.text, object)
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(80)
        # --------- console logs ---------
        #console_logs = self.driver2.find_elements_by_id("logioReload")
        #console_logs.click()
        # for logs in console_logs:
        #assert isinstance(console_logs.text, object)
        #print("Console logs :\n", console_logs.text)

        # --------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)
        # ------Screenshot-2-----------
        ss.ScreenShot(ss_path + "test_parallel_01_mnist_auto1_elapsedtime.png")
        sleep(2)
        assert isinstance(myElem.text, object)
        print("Mnist Auto -", str(myElem.text))

        try:
            pass

            # log = self.get_browser_console_log()
            # log = self.driver1.get_log(browser)
            # print("Console Log: ",log)
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

    # Test case 2

    def mnist_auto_02(self):

        # gpuper = "80"
        # coreper = "90"

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
        Admin = user.user2_name
        Pwd = user.user2_password
        expadmin = user.user2_expadmin
        exppass = user.user2_exppass
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
        # ----------GPU Auto --------
        gpu = self.driver2.find_element(By.ID, 'r4')
        gpu.click()
        sleep(2)
        auto = self.driver2.find_element_by_id("r101")
        auto.click()
        sleep(10)
        print("Your selected Auto")
        # ---------Backend IP --------------
        '''
        backendip = self.driver1.find_element(By.ID, 'gpuip0')
        backendip.clear()
        sleep(1)
        backendip.send_keys(Backendip)
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
        '''

        # ------Screenshot-1-----------
        ss.ScreenShot(ss_path + "test_parallel_01_mnist_auto2_setupscreen.png")
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
        sleep(80)
        # --------- console logs ---------
        #console_logs = self.driver2.find_elements_by_id("logioReload")
        #console_logs.click()
        # for logs in console_logs:
        #assert isinstance(console_logs.text, object)
        #print("Console logs :\n", console_logs.text)

        # logs = self.driver2.find_element_by_class_name("log")
        # assert isinstance(logs.text, object)
        # print("logs :\n",logs.text)

        # --------Elapsed Time -------------------
        myElem = self.driver2.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)
        # ------Screenshot-2-----------
        ss.ScreenShot(ss_path + "test_parallel_01_mnist_auto2_elapsedtime.png")
        sleep(5)
        assert isinstance(myElem.text, object)
        print("Mnist Auto -", str(myElem.text))

        try:
            pass

            # log = self.get_browser_console_log()
            # log = self.driver2.get_log(browser)
            # print("Console Log: ",log)
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

    # Multithreading for Parallel test cases
    def test_mnist_auto_mnist_manual(self):

        u1 = multiprocessing.Process(target=self.mnist_auto_01)
        u2 = multiprocessing.Process(target=self.mnist_auto_02)

        u1.start()
        sleep(5)
        u2.start()
        sleep(5)

        u1.join()
        u2.join()
