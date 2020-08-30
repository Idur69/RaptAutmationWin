import datetime
import unittest
import os
import sys
sys.path.append("..")
import time
import multiprocessing
#from CliTestAutomation.cliEnvSetup.cmdconfig import cmdConfig
from cliEnvSetup.cmdconfig import userTwo,Paths


class Rvirtus_Cli_Pgan_Manual(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self,pgan_cmd):

        result =  os.system(pgan_cmd)
        #gpuusage = os.system(gpuusage)
        #print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&\n" + str(pgan_cmd))
        print("***********Your data  here ******************** : " +  str(result))

        time.sleep(5)
    def run_gpucmd(self,gpuusage):
        gpuusage = os.system(gpuusage)
        #time.sleep(5)
    def test_local_pgan_manual(self):
        
        '''
        raptrun = " raptrun"
        name = " -name demotwo"
        tf = " -f tensorflow"
        application = " -a mnist"
        dirpath = " -d /home/ubuntu/tensorflow-UI"
        training = " -t /tensorflow/training/Mnist_classification/mnist_gpu.py"
        type1 = " -type rapt -l local"
        mode = " -mode manual"
        percetage = " -p 40 -cp 90"
        '''
        #******************* Command Enviromnet setup ****************
 
        cmddata = userTwo
       # raptrun = cmddata.raptrun

        name = cmddata.name
        path = Paths

        fw = path.tf
        application = path.app_pgan
        dirpath = path.data_path
        training = path.pgan_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        config=path.pgan_config
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper
        platform = path.platform
        pgan_cmd = "raptrun"+" -name " + name +" -f " + fw +" -a " + application +" -d " + dirpath +" -cf " +config +" -t " + training +" -type " + type1+" -l " +location+" -mode " + mode+" -p " + memoryper+" -cp " + coreper + " -pf " + platform
        #cmd = "raptrun -name demotwo -f tensorflow -a pggan -d /mnt/rapt/tensorflow-UI/ -cf /tensorflow/training/pgan/config.py -t /tensorflow/training/pgan/train.py -type rapt -l local -mode manual -p 40 -cp 90 -pf raptvirtus"
        #cmd = raptrun + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper
       
        print("**********this is your command *************" + str(pgan_cmd))

        gpuusage = "nvidia-smi"
        #print("%%%%%%--------Gpu Memory Usage -----\n " + str(gpuusage))
        m1 = multiprocessing.Process(target=self.run_cmd1, args=(pgan_cmd,))
        g1 = multiprocessing.Process(target=self.run_gpucmd, args=(gpuusage,))
        m1.start()
        print("%%%%%%--------Gpu Memory Usage -----\n " + str(gpuusage))

        time.sleep(50)
        g1.start()
        m1.join()
        g1.join()
        #self.assertEqual(expcmd, cmd, "Invalid command")


    def tearDown(self):
        print("Environment-01 Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main()

