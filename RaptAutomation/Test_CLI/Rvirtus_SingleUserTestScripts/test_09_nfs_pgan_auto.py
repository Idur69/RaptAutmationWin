import datetime
import unittest
import os
import time
import multiprocessing
import sys
sys.path.append("..")
from cliEnvSetup.cmdconfig import userOne,Paths

class Rvirtus_Cli_Nfs_Pgan_Auto(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self,nfspgan_cmd):
        result = os.system(nfspgan_cmd)
        #gpuusage = os.system(gpuusage)
        #print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&\n" + str(nfspgan_cmd))
        #print("***********Your data  here ******************** : " + str(result))
        time.sleep(5)
    def run_gpucmd(self,gpuusage):
        gpuusage = os.system(gpuusage)
        #time.sleep(5)

    def test_nfs_pgan_auto(self):
        
        # ******************* Command Enviromnet setup ****************
        cmddata = userOne
        path=Paths
        name = cmddata.name
        fw = path.tf
        application = path.app_pgan
        dirpath = path.nfsdata_path
        training = path.nfs_pgan_train
        type1 = path.type1
        location = path.nfslocation
        mode = path.mode_auto
        nfsip = path.nfs_ip
        nfspath = path.nfs_path
        config = path.nfs_pgan_config
        platform = path.platform
        #memoryper = cmddata.memoryper
        #coreper = cmddata.coreper

        #cmd = "raptrun -name demotwo -f tensorflow -a pggan -d /home/ubuntu/tensorflow-UI/ -cf /tensorflow/training/pgan/config.py -t /tensorflow/training/pgan/train.py -type rapt -l nfs -mode manual -p 80 -cp 90 -nfsip 54.149.247.58 -nfspath /home/ubuntu/tensorflow-UI -pf raptvirtus"
        nfspgan_cmd = "raptrun"+" -name " + name +" -f " + fw +" -a " + application +" -d " + dirpath +" -cf "+ config +" -t " + training +" -type " + type1 +" -l " + location +" -mode " + mode +" -nfsip " +nfsip + " -nfspath " + nfspath + " -pf " + platform


        print("**********this is your command *************\n" + str(nfspgan_cmd))

        gpuusage = "nvidia-smi"
        #print("%%%%%%--------Gpu Memory Usage ----- \n" + str(gpuusage))

        m1 = multiprocessing.Process(target=self.run_cmd1, args=(nfspgan_cmd,))
        g1 = multiprocessing.Process(target=self.run_gpucmd, args=(gpuusage,))
        m1.start()
        print("%%%%%%--------Gpu Memory Usage ----- \n" + str(gpuusage))
        time.sleep(50)
        g1.start()
        m1.join()
        g1.join()
        
        # self.assertEqual(expcmd, cmd, "Invalid command")

    def tearDown(self):
        print("Environment-01 Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main()
