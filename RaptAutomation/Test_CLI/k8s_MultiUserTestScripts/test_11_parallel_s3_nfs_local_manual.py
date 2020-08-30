
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




class Kubernetes_Multiusers_11(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self, s3_cmd):
        result = os.system(s3_cmd)
        #print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&" + str(pgan_cmd))
        print("***********Your data  here ******************** : " + str(result))
        #time.sleep(5)
    def run_cmd2(self, nfs_cmd):
        result2 = os.system(nfs_cmd)
        #print("&&&&&&&&&&---Yor command-2 ---&&&&&&&&&&&" + str(cmd2))
        #print("***********Your data-2 ******************** : " + str(result2))
        #time.sleep(5)
    def run_cmd3(self, local_cmd):
        result3 = os.system(local_cmd)
    def run_nvidia_smi(self, nvidiasmi):
        nvidia = os.system(nvidiasmi)
        print(nvidia)
    def test_parallel_mnistmanual_s3_nfs_local(self):
        # ******************* Command Enviromnet setup ****************
        # ------first user  S3 details------------------------
        user1 = userThree
        name = user1.name
        path1 = Paths
        fw = path1.tf
        application = path1.app_mnist
        dirpath = path1.s3data_path
        training = path1.s3_train
        type1 = path1.type1
        location = path1.s3location
        mode = path1.mode_manual
        bkeys = path1.bucket_keys
        bname = path1.bucket_name
        memoryper = user1.memoryper
        coreper = user1.coreper

        #-----Second user NFS ---------
        user2 = userTwo
        path2 = Paths
        name2 = user2.name
        fw2 = path2.tf
        application2 = path2.app_mnist
        dirpath2 = path2.nfsdata_path
        training2 = path2.nfs_mnist_train
        type2 = path2.type1
        location2 = path2.nfslocation
        mode2 = path2.mode_manual
        nfsip2 = path2.nfs_ip
        nfspath2 = path2.nfs_path
        memoryper2 = user2.memoryper
        coreper2 = user2.coreper
        #------- Third user  local --------
        user3 = userOne
        name3 = user3.name
        path3 = Paths
        fw3 = path3.tf
        application3 = path3.app_mnist
        dirpath3 = path3.data_path
        training3 = path3.mnist_train
        type3 = path3.type1
        location3 = path3.location
        mode3 = path3.mode_manual
        memoryper3 = user1.memoryper
        coreper3 = user1.coreper

        s3_cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper + " -k " + bkeys + " -bucket " + bname

        nfs_cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name2 + " -f " + fw2 + " -a " + application2 + " -d " + dirpath2 + " -t " + training2 + " -type " + type2 + " -l " + location2 + " -mode " + mode2 + " -p " + memoryper2 + " -cp " + coreper2 + " -nfsip " + nfsip2 + " -nfspath " + nfspath2

        local_cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name3 + " -f " + fw3 + " -a " + application3 + " -d " + dirpath3 + " -t " + training3 + " -type " + type3 + " -l " + location3 + " -mode " + mode3 + " -p " + memoryper3 + " -cp " + coreper3

        # pgan_cmd = raptrun + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        # mnist_cmd = raptrun2 + " -name " + name2 + " -f " + fw2 + " -a " + application2 + " -d " + dirpath2 + " -t " + training2 + " -type " + type2 + " -l " + location2 + " -mode " + mode2 + " -p " + memoryper2 + " -cp " + coreper2

        #s3_cmd = "raptrun -name rapt -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/tensorflow-UI-less/training/Mnist_classification/mnist_gpu.py -type rapt -l s3bucket -mode manual -p 50 -cp 90 -k AKIAITOV7UZRONOPBIHA:PmlQsH2tg7+7jexDMPzN0VGat/9VPa6BIapcAPYe -bucket rapt-data-bucket"

        #nfs_cmd = " raptrun -name rapt -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l nfs -mode manual -p 50 -cp 90 -nfsip 52.34.222.154 -nfspath /home/ubuntu/tensorflow-UI"

        nvidiasmi = "nvidia-smi"
        print("**********this is your command-1 *************\n" + str(s3_cmd))
        print("**********this is your command-2 *************\n" + str(nfs_cmd))
        print("**********this is your command-3 *************\n" + str(local_cmd))

        # m1 = multiprocessing.Process(target=self.run_cmd1, args=(cmd,))
        m1 = threading.Thread(target=self.run_cmd1, args=(s3_cmd,))
        m2 = threading.Thread(target=self.run_cmd2, args=(nfs_cmd,))
        m3 = threading.Thread(target=self.run_cmd3, args=(local_cmd,))
        # m2 = multiprocessing.Process(target=self.run_cmd2, args=(cmd2,))

        m4 = threading.Thread(target=self.run_nvidia_smi, args=(nvidiasmi,))
        m1.start()
        m2.start()
        
        time.sleep(40)
        m4.start()
        #time.sleep(20)
        m3.start()

        m1.join()
        m2.join()
        m3.join()
        m4.join()
        print("nvidia-smi : ",nvidiasmi)

        # self.assertEqual(expcmd, cmd, "Invalid command")

    def tearDown(self):
        print("Environment-01 Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main()


