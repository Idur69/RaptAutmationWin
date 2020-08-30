import datetime
import unittest
import os
import time
import multiprocessing
import sys
sys.path.append("..")
from cliEnvSetup.cmdconfig import userOne,Paths

class Kubernetes_Cli_Pgan_Auto(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self, pgan_cmd):
        result = os.system(pgan_cmd)
        #gpuusage = os.system(gpuusage)
        #print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&\n" + str(pgan_cmd))
        #print("***********Your data  here ******************** : " + str(result))

        time.sleep(5)
    def run_gpucmd(self,gpuusage):
        gpuusage = os.system(gpuusage)
        #time.sleep(5)

    def test_local_pgan_auto(self):
        
        # ******************* Command Enviromnet setup ****************
        cmddata = userOne
        #raptrun = cmddata.raptrun
        name = cmddata.name
        path = Paths

        fw = path.tf
        application = path.app_pgan
        dirpath = path.data_path
        training = path.pgan_train
        type1 = path.type1
        location = path.location
        mode = path.mode_auto
        config=path.pgan_config
        #memoryper = cmddata.memoryper
        #coreper = cmddata.coreper
        pgan_cmd = "raptrun train"+" -name " + name +" -f " + fw +" -a " + application +" -d " + dirpath +" -cf " +config +" -t " + training +" -type " + type1+" -l " +location+" -mode " + mode 
        #cmd = "raptrun -name demotwo -f tensorflow -a pggan -d /home/ubuntu/tensorflow-UI/ -cf /tensorflow/training/pgan/config.py -t /tensorflow/training/pgan/train.py -type rapt -l local -mode manual -p 40 -cp 90"
       # cmd = raptrun + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode

        #cmd = "raptrun -name demotwovi -f tensorflow -a pggan -d /home/ubuntu/tensorflow-UI/ -cf /tensorflow/training/pgan/config.py -t /tensorflow/training/pgan/train.py -type rapt -l local -mode auto"
        print("**********this is your command-2 *************\n" + str(pgan_cmd))
        mode = cmddata.mode

        gpuusage = "nvidia-smi "

        m1 = multiprocessing.Process(target=self.run_cmd1, args=(pgan_cmd,))
        g1 = multiprocessing.Process(target=self.run_gpucmd, args=(gpuusage,))

        m1.start()
        time.sleep(300)
        g1.start()
        print("%%%%%%--------Gpu Memory Usage -----\n " + str(gpuusage))

        time.sleep(360)
        #g1.start()
        m1.join()
        g1.join()
       
        # self.assertEqual(expcmd, cmd, "Invalid command")

    def tearDown(self):
        print("Environment-01 Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main()
