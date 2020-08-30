import datetime
import unittest
from time import sleep

from selenium import  webdriver


#********** URL *************
from selenium.webdriver import DesiredCapabilities

REGISTOR_ENVIRONMENT = 'environment0'
DEFAULT_ENVIRONMENT = 'environment1'
USER_ENVIRONMENT = 'environment2'

# ----------Ip address ---------
URL = {
        'environment0': 'http://34.222.246.209:3010/users/register',
        'environment1': 'http://34.222.246.209:3010/users/login',
        'environment2': 'http://34.222.246.209:3010/accessUI/5c7e501310ec7c705d33423c',
}

#************* Environment Setup **************
class EnvironmentSetup(unittest.TestCase):

    def setUp(self):

        #chrome = r"C:\Users\Idur\PycharmProjects\RaptAutomation\Drivers\chromedriver"
        # Create Chrome Browser
        #self.driver = webdriver.Chrome(chrome)
        self.driver1 = webdriver.Chrome(executable_path=r"C:\Users\Idur\PycharmProjects\RaptAutomation\Drivers\chromedriver")

        '''
        # Create  Firefox Browser
        #self.driver1 = webdriver.Chrome(executable_path=r"/home/cit/PycharmProjects/Rapt/RaptAutomation/Drivers/chromedriver")
        #self.driver = webdriver.Firefox(executable_path=r'/home/cit/PycharmProjects/Rapt/RaptAutomation/Drivers/geckodriver')

        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment Created")
        print("**********************")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        '''
        #if browser.lower() == 'chrome':

        #dc = DesiredCapabilities.CHROME
        #dc['loggingPrefs'] = {'browser': 'ALL'}
        #executable_path = "C:\Users\SHAIK SHA VALI\PycharmProjects\RaptAutomation\Drivers\chromedriver.exe"
        #self.driver1 = webdriver.Chrome(executable_path, desired_capabilities=dc)
        #self.driver1 = webdriver.Chrome(executable_path=r'/home/cit/PycharmProjects/RaptAutomation/Drivers/chromedriver')

        #self.driver2 = webdriver.Firefox(executable_path=r'/home/cit/PycharmProjects/RaptAutomation/Drivers/geckodriver')

        #dc = DesiredCapabilities.CHROME
        #dc['loggingPrefs'] = {'browser': 'ALL'}
        #executable_path = "/home/cit/PycharmProjects/RaptAutomation/Drivers/chromedriver"
        #self.driver2 = webdriver.Chrome(executable_path, desired_capabilities=dc)
        # self.driver1 = webdriver.Chrome(executable_path=r'/home/cit/PycharmProjects/RaptAutomation/Drivers/chromedriver')

        #df = DesiredCapabilities.FIREFOX
        #df['loggingPrefs'] = {'browser': 'ALL'}
        #executable_path2 = 'C:\Users\SHAIK SHA VALI\PycharmProjects\RaptAutomation\Drivers\geckodriver'
        #self.driver2 = webdriver.Firefox(executable_path2, desired_capabilities=df)
        #self.driver2 = webdriver.Chrome(executable_path2, desired_capabilities=df)
        self.driver2 = webdriver.Firefox(executable_path=r'C:\Users\Idur\PycharmProjects\RaptAutomation\Drivers\geckodriver')


        # Create First Chrome Browser
        #self.driver1 = webdriver.Chrome(
            #executable_path=r"/home/cit/PycharmProjects/RaptAutomation/Drivers/chromedriver")

        # Create Second Firefox Browser
        # self.driver2 = webdriver.Chrome(executable_path=r"C:\Users\cit\PycharmProjects\RaptAutomation\Drivers\chromedriver.exe")
        #self.driver2 = webdriver.Firefox(
            #executable_path=r'/home/cit/PycharmProjects/Rapt/RaptAutomation/Drivers/geckodriver')

        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment Created")
        print("**********************")
        #self.driver1.implicitly_wait(5)
        sleep(3)
        self.driver1.maximize_window()

        #self.driver2.implicitly_wait(5)
        sleep(3)
        self.driver2.maximize_window()
    def tearDown(self):
        '''
        if(self.driver != None):
            print("*******************")
            print("Environment-1 Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            #self.driver.close()
            self.driver.quit()
        '''
        if (self.driver1 != None):
            print("*******************")
            print("Environment-1 Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            # self.driver.close()
            self.driver1.quit()

        if (self.driver2 != None):
            print("*******************")
            print("Environment-2 Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            # self.driver.close()
            self.driver2.quit()



#********** Login Users credentials ***************
class LoginUsers(object):
    #------User-1 Credentials --------
    user1_name = 'john'
    user1_password = '123'
    user1_expadmin = "john"
    user1_exppass = "123"
    # ------User-2 Credentials --------
    user2_name = 'harry'
    user2_password = '123'
    user2_expadmin = "harry"
    user2_exppass = "123"
    # ------User-3 Credentials --------
    user3_name = 'shyam'
    user3_password = '123'
    user3_expadmin = "shyam"
    user3_exppass = "123"
    # ------User-2 Credentials --------
    user4_name = 'rabert'
    user4_password = '123'
    user4_expadmin = "rabert"
    user4_exppass = "123"

#********* Paths of Local directores, NFS, S3 Bucket ************
class Paths(object):
    #--------Local directory ----------
    #Local_path = "/home/ubuntu/tensorflow-UI"
    Local_path = "/mnt/rapt/tensorflow-UI"

    Pgan_path = "python -u /tensorflow/training/pgan/config.py && python -u /tensorflow/training/pgan/train.py"
    Local_Image_clf_path = "python -u /tensorflow/training/flower_classification/retrain-new.py  --model_dir=/tensorflow/inception --image_dir /tensorflow/datasets/flower_photos4.5GB --bottleneck_dir=/tensorflow/datasets/bottlenecks4.5GB-new --how_many_training_steps 50"
    #-------- Gvitrus ----------------
    #Frontend_ip = "34.221.129.142"
    Local_GVirtus_path = "/mnt/rapt/tensorflow-UI"
    Backend_ip = "54.191.214.12"
    #-------------NFS ----------------
    NFS_ip = '52.11.135.21'
    NFS_path = "/home/ubuntu/tensorflow-UI"
    Nfs_Image_clf_path = "python -u /tensorflow/training/flower_classification/retrain-new.py --model_dir=/tensorflow/inception --image_dir /tensorflow/datasets/flower_photos4.5GB --bottleneck_dir=/tensorflow/datasets/bottlenecks4.5GB-new --how_many_training_steps 50"

    #---------S3 bucket ---------
    Bucket_name = "rapt-data-bucket"
    Bucket_keys = "AKIAITOV7UZRONOPBIHA:PmlQsH2tg7+7jexDMPzN0VGat/9VPa6BIapcAPYe"
    S3_Image_clf_path = "python -u /tensorflow/training/flower_classification/retrain-new.py --model_dir=/tensorflow/inception --image_dir /tensorflow/datasets/flower_photos --bottleneck_dir=/tensorflow/datasets/bottlenecks-new --how_many_training_steps 50"

    #-----------Inferencing --------
    Inference_path = "/home/ubuntu/tensorflow-UI"
    Inference_Image_path = "python -u /tensorflow/inferencing/flower_inferencing/label_image.py /tensorflow/flower_photos_inference/sunflowers/9558628596_722c29ec60_m.jpg"

#************ Memory and Core percentages on Gpus *****************
class Memory_and_Core_Percentages():
    # Passing memory % and core % on Gpu with Single User Single Gpu Testcases

    #********* NFS *****************
    #Rapt_02_Nfs_Mnist_Manual.py
    memory_02 = "80"
    core_02 = "90"
    #Rapt_Nfs_Pgan_Manual.py
    memory_04 = "50"
    core_04 = "90"
    #Rapt_06_Nfs_Image_classification_Manual.py
    memory_06 = "80"
    core_06 = "90"

    #*********** Local Directory ********
    #Rapt_08_Local_Mnist_Manual.py
    memory_08 = "40"
    core_08 = "90"
    #Rapt_10_Local_Pgan_Manual.py
    memory_10 = "50"
    core_10 = "90"
    #Rapt_12_Local_Image_classification_Manual.py
    memory_12 = "90"
    core_12 = "90"

    #********** S3 Bucket ***********
    #Rapt_14_S3_Mnist_Manual.py
    memory_14 = "80"
    core_14 = "90"
    #Rapt_16_S3_Pgan_Manual.py
    memory_16 = "50"
    core_16 = "90"
    #Rapt_18_S3_Image_classification_Manual.py
    memory_18 = "80"
    core_18 = "90"

    #************** Inferencinng ************
    #Rapt_20_Inferencing_dog_classification_Manual.py
    memory_20 = "80"
    core_20 = "90"
    # Rapt_22_Inferencing_image_classification_Manual.py
    memory_22 = "80"
    core_22 =  "90"

    #******** Multi Gpus ***************
    #Rapt_01_MultiGpus-8_Pgan_Manual.py
    gpuper0, gpuper1, gpuper2, gpuper3, gpuper4, gpuper5, gpuper6, gpuper7 = '40', '50', '60', '70', '80', '90', '50', '60'
    coreper0, coreper1, coreper2, coreper3, coreper4, coreper5, coreper6, coreper7 = '90', '90', '90', '90', '90', '90', '90', '90'
