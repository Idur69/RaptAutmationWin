import datetime

import unittest
from telnetlib import EC
from time import sleep
import re
import sys
sys.path.append("../..")

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#from Src.EnvSetup.EnvironmentSetUp import EnvironmentSetup
from Src.EnvSetup.cnfgurl import LoginUsers, Paths, EnvironmentSetup, Memory_and_Core_Percentages
from Src.PageObject.Pages.Admin_Login import AdminLogin
from Src.PageObject.Pages.MyUrl import Myurl
from Test_UI.TestUtility.ScreenShots import SS


class Kubernetes_Ui_Mnist_Auto(EnvironmentSetup):

    def test_local_mnist_auto(self):
        logedout_txt = None
        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        print("myurl ", myurl.acces_user())
        #driver1.implicitly_wait(10)
        sleep(5)
        #-----------Rapt Title  ----------------------
        rapt_title =  "Rapt.AI"
        if rapt_title == driver1.title:
            print("This is Title name :", driver1.title)
        else:
            assert print("Rapt title didn't match....!")

        print("This is Title name :", driver1.title)

        #ScreenShot Relative Path
        #ss_path = '/K8s_UI/'
        ss_path = '/Rhel_UI/'
        #Creating object of screenshot utility
        ss = SS(driver1)

        #------- Login Details ------------
        user = LoginUsers()
        Admin = user.user1_name
        Pwd = user.user1_password
        expadmin = user.user1_expadmin
        exppass = user.user1_exppass
        # ------ local path ------------
        paths = Paths()
        locpath = paths.Local_path

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)
        admin_login.submit_login(Admin, Pwd)
        sleep(5)
        #----------- Re login user  ------------------
        logout_exp = "You are logged out .. please login.!"
        re_login = self.driver1.find_elements_by_xpath("//*[@class='alert alert-success']")

        for Logedout in re_login:
            assert isinstance(Logedout.text, object)
            logedout_txt = Logedout.text
            print("please logedout text :", str(logedout_txt))
        if logout_exp == logedout_txt:
            print("logged out matched here ^^^^^^^^^^^^^^^^^^^^^^^^^^")

            driver1 = self.driver1

            myurl = Myurl(self.driver1)
            myurl.access_url()
            # driver1.implicitly_wait(10)
            sleep(5)
            print("This is Title name inside if 2:", driver1.title)
            # self.assertEqual("Rapt.AI", driver1.title)
            sleep(5)
            # ------- Login Details ------------
            user = LoginUsers()
            Admin = user.user1_name
            Pwd = user.user1_password
            #expadmin = user.user1_expadmin
            #exppass = user.user1_exppass

            admin_login = AdminLogin(driver1)
            admin_login.set_login_uname(Admin)
            sleep(2)
            admin_login.set_login_upass(Pwd)
            sleep(3)
            admin_login.submit_login(Admin, Pwd)
            sleep(5)

        if Admin == expadmin and Pwd == exppass:
            print("Login successful")
        else:
            assert print("Invalid credentials")

        print("************ Mnist Auto *****************")
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
        #------Screenshot-1-----------
        ss.ScreenShot(ss_path + "test_01_mnist_auto_setupscreen.png")
        # -------------------- setup btn -----------------
        setupbtn = self.driver1.find_element(By.ID, 'setupbtn')
        setupbtn.click()
        sleep(25)
        #sleep(60)

        SHORT_TIMEOUT = 10  # give enough time for the loading element to appear
        LONG_TIMEOUT = 20  # give enough time for loading to finish
        #LOADING_ELEMENT_XPATH = self.driver1.find_element(By.ID, 'loader')
        LOADING_ELEMENT_XPATH = "//*[@id='loader']"

        '''try:
            wait = Webdriver1Wait(driver1, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loader"]')))
            #element = Webdriver1Wait(driver1, 10).until(
                #EC.presence_of_element_located((By.ID, "loader")))
            myElem = Webdriver1Wait(driver1, LONG_TIMEOUT).until(EC.presence_of_element_located((By.ID, 'loader')))
            print("Page is ready!",myElem)
        except TimeoutException:
            print("Loading took too much time!")'''

        #Webdriver1Wait(self.driver1, SHORT_TIMEOUT
                      #).until(EC.presence_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))

        #Webdriver1Wait(driver1,SHORT_TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
        #Webdriver1Wait(driver1,LONG_TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))

        # then wait for the element to disappear
        #Webdriver1Wait(self.driver1, LONG_TIMEOUT
                      #).until_not(EC.presence_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))

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
         #-------- Tensor console --------------
        tensor_console = self.driver1.find_element_by_xpath("//*[@class='text-center mb-3']")
        tensor_console.click()

        sleep(20)
        gpuTime = driver1.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert  isinstance(GpuUsage.text, object)
            print("Gpu Usage : ",str(GpuUsage.text))
        sleep(60)

        #--------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)
        # --------Screen shot-2 -----------
        ss.ScreenShot(ss_path + "test_01_mnist_auto_elapsedtime.png")
        sleep(10)
        assert isinstance(myElem.text, object)
        print("Mnist Auto -", str(myElem.text))
        #------------- logs ----------------
        frame1 = driver1.find_element_by_id("logioReload")
        driver1.switch_to.frame(frame1)
        sleep(4)
        page_source = driver1.page_source
        #print("************************************************************")
        # print("console logs :\n", page_source)
        dir_path = "/home/cit/PycharmProjects/RaptAutomation/Test_UI/K8s_SingleUser_SingleGpu"
        # logs_file_path = "console_logs.txt"
        logs_file_path = Admin + ".txt"
        with open(logs_file_path, 'w') as consolelogs:
            print("file creating and writing .............." + logs_file_path)
            consolelogs.write("Console Logs :\n" + page_source)
        consolelogs.close()
        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

        driver1.switch_to.default_content()
        sleep(3)

        regex = "Error(.*?)"
        match_list = []

        with open(logs_file_path, "r") as file:
            sleep(2)
            #print("reading file ..............:\n" + file.readline())
            for lines in file:
                # print("getting file **********  ")
                # print(lines)
                #sleep(1)
                for match in re.finditer(regex, lines, re.S):
                    # print("error match lines :")
                    sleep(1)
                    match_text = match.group()
                    match_list.append(match_text)
                    assert print("********** Match text *********** :\n" + match_text)

        # --------------------------------- logs end ----------------

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
    '''
    def tearDown(self):
        if (self.driver1 != None):
            print("_--_--_--_--_--_--_--")
            print("Browser Destroyed")
            print("Browser Stop Time :" + str(datetime.datetime.now()))

    if __name__ == "__main__":
        unittest.main()
    '''
