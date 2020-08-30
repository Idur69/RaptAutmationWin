from selenium.webdriver.common.by import By

#from Src.PageObject.Locators import Locators
from RaptAutomation.Src.PageObject.Locators import Locators

class RaptUi(object):
    def __init__(self, driver):

        self.driver = driver

        #self.tnsfimg = driver.find_element(By.XPATH, Locators.fimg)
        self.tnsfimg = driver.find_element_by_xpath(Locators.fimg)
        #self.inception = driver.find_elements(By.XPATH, Locators.model)
        self.inception = driver.find_element_by_xpath(Locators.inception)

        self.s3 = driver.find_element_by_xpath(Locators.s3)
        self.bktname = driver.find_element_by_xpath(Locators.bktname)
        self.bktkeys = driver.find_element_by_xpath(Locators.bktkeys)
        self.nfs = driver.find_element_by_xpath(Locators.nfs)
        self.nfsip = driver.find_element_by_xpath(Locators.nfs_sysip)
        self.nfspath = driver.find_element_by_xpath(Locators.nfs_path)
        self.localdir = driver.find_element_by_xpath(Locators.localfolder)
        self.selectpath = driver.find_element_by_xpath(Locators.setlocalpath)
        self.gpu = driver.find_element_by_xpath(Locators.gpu)
        self.auto = driver.find_element_by_xpath(Locators.auto)
        self.manual = driver.find_element_by_xpath(Locators.manual)
        #self.memoryper = driver.find_element(By.XPATH, Locators.memoryper)
        #self.coreper = driver.find_element_by_xpath(Locators.coreper)
        self.setup = driver.find_element_by_xpath(Locators.setupbtn)
        self.train = driver.find_element_by_xpath(Locators.train)
        self.trainbtn = driver.find_element_by_xpath(Locators.Trainbtn)


        self.logoutemail = driver.find_element(By.XPATH, Locators.logoutlink)
        self.logout = driver.find_element(By.XPATH, Locators.logout)

    def T_Flow(self):
        self.tnsfimg.click()
    def Inception(self):
        self.inception.click()

    def S3(self):
        self.s3.click()
    def Becket_name(self,bktname):
        self.bktname.clear()
        self.bktname.send_keys(bktname)
    def Becket_keys(self,bktkeys):
        self.bktkeys.clear()
        self.bktkeys.send_keys(bktkeys)
    def Nfs(self):
        self.nfs.click()
    def NfsSysIp(self,sysip):
        self.nfsip.clear()
        self.nfsip.send_keys(sysip)
    def NfsPath(self,nfspath):
        self.nfspath.clear()
        self.nfspath.send_keys(nfspath)
    def Localfolder(self):
        self.localdir.click()
    def set_localpath(self, localpath):
        self.selectpath.clear()
        self.selectpath.send_keys(localpath)
    def Gpu(self):
        self.gpu.click()
    def Auto(self):
        self.auto.click()
    def Manual(self):
        self.manual.click()

    '''def set_Memorypercentage(self,memoryper):
        self.memoryper.clear()
        self.memoryper.send_keys(memoryper)
    def set_coreperentage(self,corper):
        self.coreper.clear()
        self.coreper.send_keys()'''

    def Setupbtn(self):
        self.setup.click()

    def Train(self):
        self.train.click()
    def TrainButton(self):
        self.trainbtn.click()





    def LogoutEmail(self):
        self.logoutemail.click()
    def Logout(self):
        self.logout.click()