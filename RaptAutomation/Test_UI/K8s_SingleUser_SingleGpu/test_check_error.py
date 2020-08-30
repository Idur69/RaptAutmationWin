import datetime
import unittest
import re
import os
import multiprocessing
import sys
from time import sleep
sys.path.append("../..")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import DesiredCapabilities


#from EnvironmentSetUp import EnvironmentSetup
from Src.EnvSetup.cnfgurl import LoginUsers, Paths, EnvironmentSetup, Memory_and_Core_Percentages
from Src.PageObject.Pages.Admin_Login import AdminLogin
from Src.PageObject.Pages.MyUrl import Myurl
from Test_UI.TestUtility.ScreenShots import SS


class Kubernetes_Ui_Mnist_Manual(unittest.TestCase):
    def setUp(self):
        #capabilites = DesiredCapabilities.FIREFOX
        #capabilites['loggingPrefs'] = {'browser': 'ALL'}
        #executable_path = '/home/cit/PycharmProjects/RaptAutomation/Drivers/geckodriver'
        #self.driver1 = webdriver.Firefox(executable_path, desired_capabilities=capabilites)

        #self.driver1 = webdriver.Firefox(executable_path=r'/home/cit/PycharmProjects/RaptAutomation/Drivers/geckodriver')
        self.driver1 = webdriver.Chrome(executable_path=r'/home/cit/PycharmProjects/RaptAutomation/Drivers/chromedriver')

        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment Created")
        print("**********************")
        #self.driver1.implicitly_wait(10)
        sleep(10)
        self.driver1.maximize_window()

    
    def test_local_mnist_manual(self):
        count = 0
        logedout_txt = None
        #gpuper = "80"
        #coreper = "90"
        driver1 = self.driver1
        
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #driver1.implicitly_wait(10)
        sleep(8)
        print("This is Title name :", driver1.title)

        # ScreenShot Relative Path
        ss_path = '/K8s_UI/'
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
        locpath = paths.Local_path

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)
        admin_login.submit_login(Admin, Pwd)
        sleep(5)
        logout_exp = "You are logged out .. please login.!"
        re_login = self.driver1.find_elements_by_xpath("//*[@class='alert alert-success']")
        print("re login : ", re_login)
        for Logedout in re_login:
            assert isinstance(Logedout.text, object)
            logedout_txt = Logedout.text
            print("please logedout text :", str(logedout_txt))
        if logout_exp == logedout_txt:
            print("logged out matched here ^^^^^^^^^^^^^^^^^^^^^^^^^^")
            
            driver1 = self.driver1

            myurl = Myurl(self.driver1)
            myurl.access_url()
            #driver1.implicitly_wait(10)
            sleep(10)
            print("This is Title name inside if 2:", driver1.title)
            #self.assertEqual("Rapt.AI", driver1.title)
            sleep(5)
            # ------- Login Details ------------
            user = LoginUsers()
            Admin = user.user2_name
            Pwd = user.user2_password
            expadmin = user.user2_expadmin
            exppass = user.user2_exppass

            admin_login = AdminLogin(driver1)
            admin_login.set_login_uname(Admin)
            sleep(2)
            admin_login.set_login_upass(Pwd)
            sleep(3)
            admin_login.submit_login(Admin, Pwd)
            sleep(5)
            

        elif Admin == expadmin and Pwd == exppass:
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
        localpath.send_keys(locpath)

        sleep(2)

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
        ss.ScreenShot(ss_path + "test_02_manual_setupscreen.png")
        # -------------------- setup btn -----------------
        setupbtn = self.driver1.find_element(By.ID, 'setupbtn')
        setupbtn.click()
        sleep(30)

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
        #****************** getting logs error ***************
        '''
        logs_file_path = "/home/ubuntu/raptLogs/"+Admin+"/retrain.log"
        regex = "(.*?)InvalidArgument(E/e)rror(.*?)"
        match_list = []
        with open(logs_file_path, "r") as file:
            for line in file:
                for match in re.finditer(regex, line, re.S):
                    match_text = match.group()
                    match_list.append(match_text)
                    print("********** Match text *********** :\n" + match_text)

        '''
        #m1 = multiprocessing.Process(target=self.get_logs)
        
        #m1.start()
        #time.sleep(10)
        #m1.join()

        #****************************************************

        gpuTime = driver1.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert isinstance(GpuUsage.text, object)
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(30)

        # --------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(1)
        # ------Screenshot-2-----------
        ss.ScreenShot(ss_path + "test_02_manual_elapsedtime.png")
        sleep(3)
        assert isinstance(myElem.text, object)
        print("Mnist Manual -", str(myElem.text))

        # ----------- logs ------------
        #console_msg = self.driver1.find_elements_by_xpath("//*[@title='/home/ubuntu/retrain.log']")
        #console_msg.click()
        #sleep(2)
        #for consolelog in console_msg :
            #assert isinstance(consolelog.text, object)
            #print("*********** console logs **************:\n")
            #print(str(consolelog.text))
        #for logs in driver1.get_log('browser'):
            #print(logs)
        frame1 = driver1.find_element_by_id("logioReload")
        driver1.switch_to.frame(frame1)
        sleep(4)
        page_source = driver1.page_source
        print("************************************************************")
        #print("console logs :\n", page_source)
        dir_path = "/home/cit/PycharmProjects/RaptAutomation/Test_UI/K8s_SingleUser_SingleGpu"
        #logs_file_path = "console_logs.txt"
        logs_file_path = Admin+".txt"
        with open(logs_file_path, 'w') as consolelogs :
            print("page creating and writing ..............")
            consolelogs.write("Console Logs :\n" + page_source)
        consolelogs.close()
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        
        driver1.switch_to.default_content()
        sleep(3)
        
        regex = "InvalidArgumentError(.*?)"
        match_list = []
        
        with open(logs_file_path, "r") as file:
            sleep(2)
            print("reading file ..............:\n" + file.readline())
            for lines in file:
                #print("getting file **********  ")
                #print(lines)
                #sleep(1)
                for match in re.finditer(regex, lines, re.S):
                    #print("error match lines :")
                    #sleep(1)
                    match_text = match.group()
                    match_list.append(match_text)
                    assert print("********** Match text *********** :\n" + match_text)

                #if re.match("(.*?)InvalidArgumentError(.*?)", lines):
                    #print("warnings ................ ")
                    #print("^^^^^^^^^^^^^^^^^^^ match ERROR : \n", lines)

                #if re.match("InvalidArgumentError", lines):
                    #print("warnings 222222................ ")
                    #print("$$$$$$$$$$$$$$$$$ match ERROR 2222222222 : \n", lines)

            #sleep(1)
            '''
            file_read = file.read()
            for line in file_read:
                print("lines : \n" + line + "\n")
                for match in re.finditer(regex, line, re.S):
                    match_text = match.group()
                    match_list.append(match_text)
                    print("********** Match text *********** :\n" + match_text)
                if re.match("(.*?)WARNING(.*?)", line):
                    print("warnings ................ ")
                    print("$$$$$$$$$$$$$$$$$ match ERROR : \n", line )
            '''
        print("************************************************************************")
        #src2 = driver1.get_p
        #text_found = re.search('No such file or directory', src)


        #print("default contents :\n", driver1.switch_to.default_content())
        #driver1.switch_to.default_content()
        #sleep(5)

        #--------------------------------- logs end ----------------
        
        try:
            pass

            #log = self.get_browser_console_log()
            #log = self.driver1.get_log(browser)
            #print("Console Log: ",log)
        except Exception as e:
            print("Exception Occurred :" + str(e))
        
        # ---------Logout ----------------
        self.driver1.find_element_by_id("navbarDropdownMenuLink").click()
        print("trying to logout")
        logout = self.driver1.find_element_by_class_name("dropdown-item")
        logout.click()
        sleep(2)
        for Logedout in self.driver1.find_elements_by_xpath("//*[@class='alert alert-success']"):
            assert isinstance(Logedout.text, object)
            print("rapt logout msg ", str(Logedout.text))

        
    def tearDown(self):
    
        if (self.driver1 != None):
           
            print("*******************")
            print("Environment-1 Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            # self.driver.close()
            self.driver1.quit()

if __name__ == '__main__':
    unittest.main()
