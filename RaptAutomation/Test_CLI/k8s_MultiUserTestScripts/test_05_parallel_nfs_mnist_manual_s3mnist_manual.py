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




class Kubernetes_Multiusers_05(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self, s3_cmd):
        result = os.system(s3_cmd)
        #print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&" + str(pgan_cmd))
        print("***********Your data  here ******************** : " + str(result))
        time.sleep(5)
    def run_cmd2(self, nfs_cmd):
        result2 = os.system(nfs_cmd)
        #print("&&&&&&&&&&---Yor command-2 ---&&&&&&&&&&&" + str(cmd2))
        #print("***********Your data-2 ******************** : " + str(result2))
        time.sleep(5)
    def run_nvidia_smi(self, nvidiasmi):
        nvidia = os.system(nvidiasmi)
        print(nvidia)
    def test_parallel_nfsmnistmanual_s3mnistmanual(self):
        # ******************* Command Enviromnet setup ****************
        # first user details------------------------  
        user1 = userThree
        path = Paths
        name = user1.name
        fw = path.tf
        application = path.app_mnist
        dirpath = path.nfsdata_path
        training = path.nfs_mnist_train
        type1 = path.type1
        location = path.nfslocation
        mode = path.mode_manual
        nfsip = path.nfs_ip
        nfspath = path.nfs_path
        memoryper = user1.memoryper
        coreper = user1.coreper
        # second user details -----------------
        user2 = userTwo
        name2 = user2.name
        path2 = Paths
        fw2 = path2.tf
        application2 = path2.app_mnist
        dirpath2 = path2.s3data_path
        training2 = path2.s3_train
        type2 = path2.type1
        location2 = path2.s3location
        mode2 = path2.mode_manual
        bkeys2 = path2.bucket_keys
        bname2 = path2.bucket_name
        memoryper2 = user2.memoryper
        coreper2 = user2.coreper

        nfs_cmd = "/home/ubuntu/test/raptcli raptrun"+" -name " + name +" -f " + fw +" -a " + application +" -d " + dirpath + training +" -type " + type1 +" -l " + location +" -mode " + mode +" -p " + memoryper +" -cp " + coreper +" -nfsip " +nfsip + " -nfspath " + nfspath

        s3_cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name2 + " -f " + fw2 + " -a " + application2 + " -d " + dirpath2 + " -t " + training2 + " -type " + type2 + " -l " + location2 + " -mode " + mode2 + " -p " + memoryper2 + " -cp " + coreper2 + " -k " + bkeys2 + " -bucket " + bname2


        #s3_cmd = "raptrun -name rapt -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/tensorflow-UI-less/training/Mnist_classification/mnist_gpu.py -type rapt -l s3bucket -mode manual -p 50 -cp 90 -k AKIAITOV7UZRONOPBIHA:PmlQsH2tg7+7jexDMPzN0VGat/9VPa6BIapcAPYe -bucket rapt-data-bucket"

        #nfs_cmd = "raptrun -name rapt -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/tensorflow-UI-less/training/Mnist_classification/mnist_gpu.py -type rapt -l s3bucket -mode manual -p 50 -cp 90 -k AKIAITOV7UZRONOPBIHA:PmlQsH2tg7+7jexDMPzN0VGat/9VPa6BIapcAPYe -bucket rapt-data-bucket"
        nvidiasmi = "nvidia-smi"
        print("**********this is your command-1 *************\n" + str(nfs_cmd))
        print("**********this is your command-2 *************\n" + str(s3_cmd))
        
        #m1 = multiprocessing.Process(target=self.run_cmd1, args=(cmd,))
        m1 = threading.Thread(target=self.run_cmd1, args=(nfs_cmd,))
        m2 = threading.Thread(target=self.run_cmd2, args=(s3_cmd,))
        #m2 = multiprocessing.Process(target=self.run_cmd2, args=(cmd2,))
        
        m3 = threading.Thread(target=self.run_nvidia_smi, args=(nvidiasmi,))
	
        m1.start()
        m2.start()
        time.sleep(40)
        m3.start()

        m1.join()
        m2.join()
        m3.join()
        print("nvidia-smi : ",nvidiasmi)
        
        # self.assertEqual(expcmd, cmd, "Invalid command")
    def tearDown(self):
        print("Environment-01 Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main()
