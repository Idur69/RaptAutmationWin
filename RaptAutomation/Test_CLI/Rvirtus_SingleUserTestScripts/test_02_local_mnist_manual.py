import datetime
import unittest
import os
import time
import multiprocessing
import sys
sys.path.append("..")
from cliEnvSetup.cmdconfig import userOne, userTwo, Paths

class Rvirtus_Cli_Mnist_Manual(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self, mnist_cmd):
        result = os.system(mnist_cmd)
        #gpuusage = os.system(gpuusage)
        #print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&\n" + str(mnist_cmd))
        print("***********Your data  here ********************\n : " + str(result))

        time.sleep(5)
    def run_gpucmd(self,gpuusage):
        gpuusage = os.system(gpuusage)
        #time.sleep(5)

    def test_local_mnist_manual(self):
        
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
       # raptrun = cmddata.raptrun

        name = cmddata.name
        path = Paths
         
        fw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_deep
        type1 = path.type1
        location = path.location
        #mode = path.mode_auto
        mode = path.mode_manual
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper
        platform = path.platform

        mnist_cmd = "raptrun"+" -name " + name +" -f " + fw +" -a " + application +" -d " + dirpath +" -t " + training +" -type " + type1 +" -l " + location +" -mode " + mode +" -p " + memoryper +" -cp " + coreper + " -pf " + platform

        #mnist_cmd = "raptcli raptrun -name demotwo -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_deep.py -type rapt -l local -mode manual -p 40 -cp 90"
        #mnist_cmd = "raptcli raptrun -name demotwo -f tensorflow -a mnist -d /mnt/rapt/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_deep.py -type rapt -l local -mode auto -pf raptvirtus"
        print("**********this is your command-2 *************\n" + str(mnist_cmd))

        gpuusage = "nvidia-smi"
        print("%%%%%%--------Gpu Memory Usage -----:\n " + str(gpuusage))

        m1 = multiprocessing.Process(target=self.run_cmd1, args=(mnist_cmd,))
        g1 = multiprocessing.Process(target=self.run_gpucmd, args=(gpuusage,))
      
        m1.start()
        time.sleep(30)
        g1.start()
        print("%%%%%%--------Gpu Memory Usage -----:\n " + str(gpuusage))

        time.sleep(20)
        #g1.start()
        m1.join()
        g1.join()
        #regexp = "AttributeError:"
        #if self.assertTrue(regexp):
            #print("Error True")
        #else:
            #assert print("Error Occured.... !")
        #self.assertEqual(mode1, mode, "Invalid mode")

    def tearDown(self):
        print("Environment-01 Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main()

