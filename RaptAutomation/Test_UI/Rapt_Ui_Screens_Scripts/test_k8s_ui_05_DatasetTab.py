import datetime
import pickle
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#from Src.EnvSetup.EnvironmentSetUp import EnvironmentSetup
from RaptAutomation.Src.EnvSetup.cnfgurl import EnvironmentSetup
from RaptAutomation.Src.PageObject.Pages.Admin_Login import AdminLogin
from RaptAutomation.Src.PageObject.Pages.MyUrl import Myurl
from RaptAutomation.Src.PageObject.Pages.RaptUi import RaptUi


class Rapt_Ui_DatasetTab(EnvironmentSetup):


    # ---- Test_case-1 Invalid local dircotory path---------
    def test_01_Invalid_localdirpath(self):
        driver1 = self.driver1
        memory = "60"
        core = "90"

        myurl = Myurl(self.driver1)
        myurl.access_url()
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://54.191.212.159:3020/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)

        raptui.Localfolder()
        path = "/mnt/rapt/tensorflow"
        exppath = "/mnt/rapt/tensorflow-UI"
        sleep(1)
        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        self.assertEqual(exppath, path, "Invalid local directory path")
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")

        memoryper = self.driver1.find_element(By.ID, 'gpupercent0')

        memoryper.send_keys(memory)
        sleep(2)
        print("Memory percentage :", memory)
        coreper = self.driver1.find_element(By.ID, 'gpuvalue0')
        coreper.send_keys(core)
        sleep(2)
        print("Core percentage :", core)
        raptui.Setupbtn()
        sleep(5)
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # ---- Test case-2Empty Local directory path --------------
    def test_02_empty_localdirpath(self):
        driver1 = self.driver1
        memory = "60"
        core = "90"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://35.165.255.128:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://35.165.255.128:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)

        raptui.Localfolder()
        path = ""
        sleep(1)
        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")

        raptui.Setupbtn()
        sleep(5)
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # ----Testcase-3 Valid detals --------------
    def test_03_Valid_localfolder(self):
        driver1 = self.driver1
        memory = "60"
        core = "90"
        #self.driver1.get("http://35.165.255.128:3010/users/login")
        myurl = Myurl(self.driver1)
        myurl.access_url()
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://35.165.255.128:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)

        raptui.Localfolder()
        path = "/mnt/rapt/tensorflow-UI"
        sleep(1)
        raptui.set_localpath(path)
        sleep(1)
        print("Your given path ", path)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")
        raptui.Setupbtn()
        sleep(23)
        traindir = self.driver1.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("Mnist_classification")
        sleep(2)
        trinfile = self.driver1.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("mnist_gpu.py")
        sleep(2)
        raptui.Train()
        sleep(2)
        # textpath = self.driver1.find_element_by_id("textVal")
        # textpath.clear()
        # flowerpath = "python /s3mount/tensorflow-UI-less/training/flower_classification/retrain-new.py --model_dir=/s3mount/tensorflow-UI-less/inception --image_dir /s3mount/tensorflow-UI-less/datasets/flower_photos --bottleneck_dir=/s3mount/tensorflow-UI-less/datasets/bottlenecks-new --how_many_training_steps 50"
        # textpath.send_keys(flowerpath)
        sleep(2)
        raptui.TrainButton()
        sleep(30)
        gpuTime = driver1.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert isinstance(GpuUsage.text, object)
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(30)
        # --------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(2)
        assert isinstance(myElem.text, object)
        print("Mnist Auto -", str(myElem.text))
        try:
            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test cases-4 empty bucket name
    def test_04_empty_s3_bucket_name(self):
        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://35.165.255.128:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://35.165.255.128:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.S3()
        print("S3 Selected")
        bktname = ""
        bktkeys = "AKIAITOV7UZRONOPBIHA:PmlQsH2tg7+7jexDMPzN0VGat/9VPa6BIapcAPYe"
        raptui.Becket_name(bktname)
        sleep(1)
        raptui.Becket_keys(bktkeys)
        sleep(1)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")
        raptui.Setupbtn()
        sleep(2)
        #-------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test_cases-5 Empty bucket keys
    def test_05_empty_s3_bucket_keys(self):
        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://35.165.255.128:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://35.165.255.128:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath("//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.S3()
        print("S3 Selected")
        bktname = "rapt-data-bucket"
        bktkeys = ""
        raptui.Becket_name(bktname)
        sleep(1)
        raptui.Becket_keys(bktkeys)
        sleep(1)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")
        raptui.Setupbtn()
        sleep(2)
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------

        try:
           pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test cases-6 Invalid bucket name
    def test_06_Invalid_S3_Bucket_name(self):
        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://35.165.255.128:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://35.165.255.128:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.S3()
        print("S3 Selected")
        bktname = "rapt-data-bucket=rapt-data-bucket"
        bktkeys = "AKIAITOV7UZRONOPBIHA:PmlQsH2tg7+7jexDMPzN0VGat/9VPa6BIapcAPYe"
        raptui.Becket_name(bktname)
        sleep(1)
        raptui.Becket_keys(bktkeys)
        sleep(1)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")
        raptui.Setupbtn()
        sleep(5)
        expbktname = "rapt-data-bucket"
        #expbktkeys = "AKIAITOV7UZRONOPBIHA:PmlQsH2tg7+7jexDMPzN0VGat/9VPa6BIapcAPYe"
        self.assertEqual(expbktname,bktname,"Invalid bucket name")
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test_cases-7 invalid bucket keys
    def test_07_invalid_s3_bucket_keys(self):
        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://35.165.255.128:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://35.165.255.128:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.S3()
        print("S3 Selected")
        bktname = "rapt-data-bucket"
        bktkeys = "23434ljjljfd3343434lkjjkjfdkj43"

        raptui.Becket_name(bktname)
        sleep(1)
        raptui.Becket_keys(bktkeys)
        sleep(1)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")
        raptui.Setupbtn()
        sleep(3)
        expbktkeys = "AKIAITOV7UZRONOPBIHA:PmlQsH2tg7+7jexDMPzN0VGat/9VPa6BIapcAPYe"
        self.assertEqual(expbktkeys, bktkeys, "Invalid bucket keys")
        try:

            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test cases-8 Valid S3 bucket
    def test_08_Valid_S3_Bucket(self):
        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://35.165.255.128:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://35.165.255.128:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        print("Selected Inception")
        raptui.S3()
        print("S3 Selected")
        bktname = "rapt-data-bucket"
        bktkeys = "AKIAITOV7UZRONOPBIHA:PmlQsH2tg7+7jexDMPzN0VGat/9VPa6BIapcAPYe"
        raptui.Becket_name(bktname)
        sleep(1)
        raptui.Becket_keys(bktkeys)
        sleep(1)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")
        raptui.Setupbtn()
        sleep(23)
        traindir = self.driver1.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("Mnist_classification")
        sleep(2)
        trinfile = self.driver1.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("mnist_gpu.py")
        sleep(2)
        raptui.Train()
        sleep(2)
        # textpath = self.driver1.find_element_by_id("textVal")
        # textpath.clear()
        # flowerpath = "python /s3mount/tensorflow-UI-less/training/flower_classification/retrain-new.py --model_dir=/s3mount/tensorflow-UI-less/inception --image_dir /s3mount/tensorflow-UI-less/datasets/flower_photos --bottleneck_dir=/s3mount/tensorflow-UI-less/datasets/bottlenecks-new --how_many_training_steps 50"
        # textpath.send_keys(flowerpath)
        sleep(2)
        raptui.TrainButton()
        sleep(30)
        gpuTime = driver1.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert isinstance(GpuUsage.text, object)
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(30)
        # --------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(2)
        assert isinstance(myElem.text, object)
        print("Mnist Auto -", str(myElem.text))
        try:
            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    #******** NFS STARTED **********
    # Test cases-09 Valid NFS details
    def test_09_Valid_Nfs(self):
        driver1 = self.driver1

        sysip = "52.32.163.231"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        #self.driver1.get("http://35.165.255.128:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        #self.driver1.get("http://35.165.255.128:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        raptui.Nfs()

        path = "/home/ubuntu/tensorflow-UI"
        print("Nfs selected")
        raptui.NfsSysIp(sysip)
        sleep(1)
        raptui.NfsPath(path)
        sleep(1)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")
        raptui.Setupbtn()
        sleep(23)
        traindir = self.driver1.find_element(By.ID, 'traindirectory')
        trdirectory = Select(traindir)
        trdirectory.select_by_visible_text("Mnist_classification")
        sleep(2)
        trinfile = self.driver1.find_element(By.ID, 'file_name')
        trfile = Select(trinfile)
        trfile.select_by_visible_text("mnist_gpu.py")
        sleep(2)
        raptui.Train()
        sleep(2)
        # textpath = self.driver1.find_element_by_id("textVal")
        # textpath.clear()
        # flowerpath = "python /s3mount/tensorflow-UI-less/training/flower_classification/retrain-new.py --model_dir=/s3mount/tensorflow-UI-less/inception --image_dir /s3mount/tensorflow-UI-less/datasets/flower_photos --bottleneck_dir=/s3mount/tensorflow-UI-less/datasets/bottlenecks-new --how_many_training_steps 50"
        # textpath.send_keys(flowerpath)
        sleep(2)
        raptui.TrainButton()
        sleep(30)
        gpuTime = driver1.find_elements_by_id("gputime")
        for GpuUsage in gpuTime:
            assert isinstance(GpuUsage.text, object)
            print("Gpu Usage : ", str(GpuUsage.text))
        sleep(30)
        # --------Elapsed Time -------------------
        myElem = self.driver1.find_element_by_id("elapsedTime")
        myElem.click()
        sleep(2)
        assert isinstance(myElem.text, object)
        print("Mnist Auto -", str(myElem.text))
        try:
            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test cases-9 Empty system ip

    def test_10_empty_Nfs_SysIp(self):
        driver1 = self.driver1
        memory = "40"
        core = "90"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        # self.driver1.get("http://35.165.255.128:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        # self.driver1.get("http://35.165.255.128:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()
        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        raptui.Nfs()
        sysip = ""
        path = "/home/ubuntu/tensorflow-UI"
        print("Nfs selected")
        raptui.NfsSysIp(sysip)
        sleep(1)
        raptui.NfsPath(path)
        sleep(1)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")

        raptui.Setupbtn()
        sleep(3)
        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------

        try:
            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test cases-11 Empty Path

    def test_11_empty_Nfs_Path(self):
        driver1 = self.driver1
        memory = "40"
        core = "90"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        # self.driver1.get("http://35.165.255.128:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        # self.driver1.get("http://35.165.255.128:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()
        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        raptui.Nfs()
        sysip = "52.32.163.231"
        path = ""
        print("Nfs selected")
        raptui.NfsSysIp(sysip)
        sleep(1)
        raptui.NfsPath(path)
        sleep(1)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")

        raptui.Setupbtn()
        sleep(3)

        # -------- Alert start ----------------
        # Switch the control to the Alert window
        obj = driver1.switch_to.alert
        sleep(2)
        # Retrieve the message on the Alert window
        msg = obj.text
        print("Alert shows following message: " + msg)
        sleep(2)
        # use the accept() method to accept the alert
        obj.accept()
        sleep(5)
        # ------------ Alert end -------------

        try:
            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test cases-12 Invalid System IP

    def test_12_Invalid_Nfs_SystemIp(self):
        driver1 = self.driver1
        memory = "40"
        core = "90"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        # self.driver1.get("http://35.165.255.128:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        # self.driver1.get("http://35.165.255.128:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        raptui.Nfs()
        sysip = "52.32.163.2"
        expsysip = "52.32.163.231"
        path = "/home/ubuntu/tensorflow-UI"
        print("Nfs selected")
        raptui.NfsSysIp(sysip)
        sleep(1)
        raptui.NfsPath(path)
        sleep(1)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")

        raptui.Setupbtn()
        sleep(3)
        self.assertEqual(expsysip, sysip, "Invalid System IP")

        try:
            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))

    # Test cases-13 Invalid Nfs path

    def test_13_Invalid_Nfs_Path(self):
        driver1 = self.driver1
        memory = "60"
        core = "90"
        myurl = Myurl(self.driver1)
        myurl.access_url()
        # self.driver1.get("http://35.165.255.128:3010/users/login")
        sleep(2)

        cookies = pickle.load(open("cookies.pkl", "rb"))
        # print("get cookie vlaues ", cookies)
        sleep(1)
        for cookie_dict in cookies:
            driver1.add_cookie(cookie_dict)
            # print("this is for loop")
        # self.driver1.get("http://35.165.255.128:3010/accessUI/5c7e501310ec7c705d33423c")
        myurl.acces_user()

        raptui = RaptUi(driver1)
        raptui.T_Flow()
        print("Selected Tensorflow")
        sleep(1)
        # tensorflow.inception()
        inception = self.driver1.find_element_by_xpath(
            "//*[@class='card-body text-center font-weight-normal btnNext']")
        # inception = self.driver1.find_elements_by_xpath("(//*[@class='card border border-primary'])[0]")
        inception.click()
        sleep(1)
        raptui.Nfs()
        sysip = "52.32.163.231"
        exppath = "/home/ubuntu/tensorflow-UI"
        path = "/home/ubuntu/tensorflow"
        print("Nfs selected")
        raptui.NfsSysIp(sysip)
        sleep(1)
        raptui.NfsPath(path)
        sleep(1)
        raptui.Gpu()
        sleep(1)
        raptui.Auto()
        sleep(1)
        print("Your selected Auto")

        raptui.Setupbtn()
        sleep(3)
        self.assertEqual(exppath, path, "Invalid NFS Path")

        try:
            pass
        except Exception as e:
            print("Exception Occurred :" + str(e))




