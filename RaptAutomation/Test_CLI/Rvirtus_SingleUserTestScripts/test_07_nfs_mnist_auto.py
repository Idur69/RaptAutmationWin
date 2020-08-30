import datetime
import unittest
import os
import time
import multiprocessing
import sys
sys.path.append("..")
from cliEnvSetup.cmdconfig import userOne,Paths

class Rvirtus_Cli_Nfs_Mnist_Auto(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self, nfsmnist_cmd):
        result = os.system(nfsmnist_cmd)
        #gpuusage = os.system(gpuusage)
        print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&\n" + str(nfsmnist_cmd))
        print("***********Your data  here ******************** : " + str(result))
        time.sleep(5)
    def run_gpucmd(self,gpuusage):
        gpuusage = os.system(gpuusage)
        #time.sleep(5)

    def test_nfs_mnist_auto(self):
        
        # ******************* Command Enviromnet setup ****************
        cmddata = userOne
       # raptrun = cmddata.raptrun
        path=Paths
        name = cmddata.name
        fw = path.tf
        application = path.app_mnist
        dirpath = path.nfsdata_path
        training = path.nfs_mnist_deep
        type1 = path.type1
        location = path.nfslocation
        mode = path.mode_auto
        nfsip = path.nfs_ip
        nfspath = path.nfs_path
        platform = path.platform
        #memoryper = cmddata.memoryper
        #coreper = cmddata.coreper

        #cmd = "raptrun -name demotwo -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_deep.py -type rapt -l nfs -mode manual -p 50 -cp 90 -nfsip 54.149.247.58 -nfspath /home/ubuntu/tensorflow-UI -pf raptvirtus"
        nfsmnist_cmd = "raptrun"+" -name " + name +" -f " + fw +" -a " + application +" -d " + dirpath +" -t " + training +" -type " + type1 +" -l " + location +" -mode " + mode +" -nfsip " +nfsip + " -nfspath " + nfspath + " -pf " + platform
        print("**********this is your command  *************\n" + str(nfsmnist_cmd))

        gpuusage = "nvidia-smi"
        #print("%%%%%%--------Gpu Memory Usage -----\n " + str(gpuusage))

        m1 = multiprocessing.Process(target=self.run_cmd1, args=(nfsmnist_cmd,))
        g1 = multiprocessing.Process(target=self.run_gpucmd, args=(gpuusage,))
        m1.start()
        time.sleep(30)
        g1.start()
        print("%%%%%%--------Gpu Memory Usage -----\n " + str(gpuusage))

        time.sleep(30)
        #g1.start()
        m1.join()
        g1.join()
        # self.assertEqual(expcmd, cmd, "Invalid command")

    def tearDown(self):
        print("Environment-01 Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main()

