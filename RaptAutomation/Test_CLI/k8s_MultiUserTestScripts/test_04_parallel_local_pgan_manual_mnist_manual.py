import datetime
import unittest
import os
import sys
sys.path.append("..")
import time
import threading
import multiprocessing
#from CliTestAutomation.cliEnvSetup.cmdconfig import cmdConfig
from cliEnvSetup.cmdconfig import userOne, userTwo, userThree, Paths




class Kubernetes_Multiusers_04(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self, pgan_cmd):
        result = os.system(pgan_cmd)
        #print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&" + str(pgan_cmd))
        print("***********Your data  here ******************** : " + str(result))
        #time.sleep(5)
    def run_cmd2(self, mnist_cmd):
        result2 = os.system(mnist_cmd)
        #print("&&&&&&&&&&---Yor command-2 ---&&&&&&&&&&&" + str(cmd2))
        #print("***********Your data-2 ******************** : " + str(result2))
        #time.sleep(5)
    def run_nvidia_smi(self, nvidiasmi):
        nvidia = os.system(nvidiasmi)
        print(nvidia)
    def test_parallel_pganmanual_mnistmanual01(self):
        # ******************* Command Enviromnet setup ****************
        # first user details------------------------  
       
        user1 = userThree
        name = user1.name
        path = Paths
        fw = path.tf
        application = path.app_pgan
        dirpath = path.data_path
        training = path.pgan_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        config = path.pgan_config
        memoryper = user1.memoryper
        coreper = user1.coreper

        # second user details -----------------
        user2 = userTwo
        name2 = user2.name
        path2 = Paths
        fw2 = path2.tf
        application2 = path2.app_mnist
        dirpath2 = path2.data_path
        training2 = path2.mnist_train
        type2 = path2.type1
        location2 = path2.location
        mode2 = path2.mode_manual
        memoryper2 = user2.memoryper
        coreper2 = user2.coreper


        pgan_cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -cf " + config + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        mnist_cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name2 + " -f " + fw2 + " -a " + application2 + " -d " + dirpath2 + " -t " + training2 + " -type " + type2 + " -l " + location2 + " -mode " + mode2 + " -p " + memoryper2 + " -cp " + coreper2
                

        #pgan_cmd = "raptrun -name demotwo -f tensorflow -a pggan -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/pgan/train.py -cf /tensorflow/training/pgan/config.py -type rapt -l local -mode manual -p 40 -cp 90"

        #mnist_cmd = "raptrun -name demothree -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp 90"
        nvidiasmi = "nvidia-smi"
        print("**********this is your command-1 *************" + str(pgan_cmd))
        print("**********this is your command-2 *************" + str(mnist_cmd))
        
        #m1 = multiprocessing.Process(target=self.run_cmd1, args=(cmd,))
        m1 = threading.Thread(target=self.run_cmd1, args=(pgan_cmd,))
        m2 = threading.Thread(target=self.run_cmd2, args=(mnist_cmd,))
        #m2 = multiprocessing.Process(target=self.run_cmd2, args=(cmd2,))
        
        m3 = threading.Thread(target=self.run_nvidia_smi, args=(nvidiasmi,))
        m1.start()
        m2.start()
        time.sleep(40)
        m3.start()

        m1.join()
        m2.join()
        m3.join()
        time.sleep(40)
        print("nvidia-smi : ",nvidiasmi)
        
        # self.assertEqual(expcmd, cmd, "Invalid command")
    def tearDown(self):
        print("Environment-01 Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main()
