import datetime
import unittest
import os
import sys
sys.path.append("..")
import time
import multiprocessing
#from CliTestAutomation.cliEnvSetup.cmdconfig import cmdConfig
from cliEnvSetup.cmdconfig import userTwo,Paths


class Rvirtus_Cli_Nfs_Pgan_Manual(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self,nfspgan_cmd):

        result =  os.system(nfspgan_cmd)
        #gpuusage = os.system(gpuusage)
        #print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&\n" + str(nfspgan_cmd))
        #print("***********Your data  here ******************** : " +  str(result))
        time.sleep(5)
    def run_gpucmd(self,gpuusage):
        gpuusage = os.system(gpuusage)
        #time.sleep(5)
    def test_nfs_pgan_manual(self):

        #******************* Command Enviromnet setup ****************
        cmddata = userTwo
        path=Paths
        name = cmddata.name
        fw = path.tf
        application = path.app_pgan
        dirpath = path.nfsdata_path
        training = path.nfs_pgan_train
        type1 = path.type1
        location = path.nfslocation
        mode = path.mode_manual
        nfsip = path.nfs_ip
        nfspath = path.nfs_path
        config = path.nfs_pgan_config
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper
        platform = path.platform

        nfspgan_cmd = "raptrun"+" -name " + name +" -f " + fw +" -a " + application +" -d " + dirpath +" -cf "+ config +" -t " + training +" -type " + type1 +" -l " + location +" -mode " + mode +" -p " + memoryper +"-cp " + coreper +" -nfsip " +nfsip + " -nfspath " + nfspath + " -pf " + platform
         
        #cmd = "raptrun -name demotwo -f tensorflow -a pggan -d /mnt/rapt/tensorflow-UI/ -t /tensorflow/training/pgan/train.py -cf /tensorflow/training/pgan/config.py -type rapt -l local -mode manual -p 40 -cp 90 -pf raptvirtus"

        print("**********this is your command *************\n" + str(nfspgan_cmd))

        gpuusage = "nvidia-smi"
        #print("%%%%%%--------Gpu Memory Usage -----\n " + str(gpuusage))
        m1 = multiprocessing.Process(target=self.run_cmd1, args=(nfspgan_cmd,))
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

