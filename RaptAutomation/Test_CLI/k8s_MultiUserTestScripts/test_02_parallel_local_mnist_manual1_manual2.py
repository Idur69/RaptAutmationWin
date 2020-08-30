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




class Kubernetes_Multiusers_02(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("****************** Environment_01 Created ***************\n")
        print("***************************************************************")

    def run_cmd1(self, cmd1):
        result = os.system(cmd1)
        #print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&\n" + str(cmd1))
        print("***********Your data  here ******************** : " + str(result))
        #time.sleep(5)
    def run_cmd2(self, cmd2):
        result2 = os.system(cmd2)
        #print("&&&&&&&&&&---Yor command-2 ---&&&&&&&&&&&\n" + str(cmd2))
        print("***********Your data-2 ******************** : " + str(result2))
        #time.sleep(5)
    def run_nvidia_smi(self, nvidiasmi):
        nvidia = os.system(nvidiasmi)
        print(nvidia)
    def test_parallel_mnist02(self):
        # ******************* Command Enviromnet setup ****************
        # first user details------------------------  
       
        user1 = userThree
        name = user1.name
        #------- path ---------------
        path1 = Paths
        fw = path1.tf
        application = path1.app_mnist
        dirpath = path1.data_path
        training = path1.mnist_train
        type1 = path1.type1
        location = path1.location
        mode = path1.mode_manual
        memoryper = user1.memoryper
        coreper = user1.coreper
        # second user details -----------------
        user2 = userTwo 
        #raptrun = cmddata.raptrun
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

        

        cmd1 = "/home/ubuntu/test/raptcli raptrun"+" -name " + name +" -f " + fw +" -a " + application +" -d " + dirpath +" -t " + training +" -type " + type1 +" -l " + location +" -mode " + mode +" -p " + memoryper +" -cp " +coreper

        cmd2 = "/home/ubuntu/test/raptcli raptrun"+" -name " + name2 +" -f " + fw2 +" -a " + application2 +" -d " + dirpath2 +" -t " + training2 +" -type " + type2 +" -l " + location2 +" -mode " + mode2 +" -p " + memoryper2 +" -cp " +coreper2
        
        #cmd2 = raptrun2 + " -name " + name2 + " -f " + fw2 + " -a " + application2 + " -d " + dirpath2 + " -t " + training2 + " -type " + type2 + " -l " + location2 + " -mode " + mode2 + " -p " + memoryper2 + " -cp " + coreper2

        #cmd2 = "raptrun -name demotwo -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp 90"
        nvidiasmi = "nvidia-smi"
        print("**********this is your command-1 *************\n" + str(cmd1))
        print("**********this is your command-2 *************\n" + str(cmd2))
        
        #m1 = multiprocessing.Process(target=self.run_cmd1, args=(cmd,))
        m1 = threading.Thread(target=self.run_cmd1, args=(cmd1,))
        m2 = threading.Thread(target=self.run_cmd2, args=(cmd2,))
        #m2 = multiprocessing.Process(target=self.run_cmd2, args=(cmd2,))
        
        m3 = threading.Thread(target=self.run_nvidia_smi, args=(nvidiasmi,))
        m1.start()
        m2.start()
        time.sleep(50)
        m3.start()
        #print("nvidia-smi : ",nvidiasmi)
        m1.join()
        m2.join()
        #time.sleep(50)
        #m3 = threading.Thread(target=self.run_nvidia_smi, args=(nvidiasmi,))
        #m3.start()
        m3.join()
        print("nvidia-smi : ",nvidiasmi)
        
        # self.assertEqual(expcmd, cmd, "Invalid command")
        #time.sleep(20)
    def tearDown(self):
        print("Environment-01 Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))



if __name__ == "__main__":
    unittest.main()
