import datetime
import unittest
import os
import sys
sys.path.append("..")
import time
import multiprocessing
#from CliTestAutomation.cliEnvSetup.cmdconfig import cmdConfig
from cliEnvSetup.cmdconfig import userTwo,Paths


class Kubernetes_Cli_S3_Mnist_Manual(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self,s3mnist_cmd):

        result =  os.system(s3mnist_cmd)
        #gpuusage = os.system(gpuusage)
        print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&" + str(s3mnist_cmd))
        print("***********Your data  here ******************** : " +  str(result))

        time.sleep(5)
    def run_gpucmd(self,gpuusage):
        gpuusage = os.system(gpuusage)
        #time.sleep(5)
    def test_s3_mnist_manual(self):
        
        #******************* Command Enviromnet setup ****************
        cmddata = userTwo
       # raptrun = cmddata.raptrun

        name = cmddata.name
        path = Paths

        fw = path.tf
        application = path.app_mnist
        dirpath = path.s3data_path
        training = path.s3_mnist_gpu
        type1 = path.type1
        location = path.s3location
        mode = path.mode_manual
        bkeys = path.bucket_keys
        bname = path.bucket_name
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper



        #cmd = "raptrun -name demotwo -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/tensorflow-UI-less/training/Mnist_classification/mnist_gpu.py -type rapt -l s3bucket -mode manual -p 70 -cp 90 -k AKIAITOV7UZRONOPBIHA:PmlQsH2tg7+7jexDMPzN0VGat/9VPa6BIapcAPYe -bucket rapt-data-bucket"
        s3mnist_cmd = "raptrun train"+" -name "+ name +" -f " + fw +" -a " +application +" -d " + dirpath +" -t " + training +" -type " + type1 +" -l " + location +" -mode " + mode +" -p " + memoryper +"-cp " + coreper +" -k " + bkeys +" -bucket " + bname  


        print("**********this is your command *************\n" + str(s3mnist_cmd))

        gpuusage = "nvidia-smi "
        print("%%%%%%--------Gpu Memory Usage -----\n " + str(gpuusage))
        m1 = multiprocessing.Process(target=self.run_cmd1, args=(s3mnist_cmd,))
        g1 = multiprocessing.Process(target=self.run_gpucmd, args=(gpuusage,))
        m1.start()
        time.sleep(30)
        g1.start()
        print("%%%%%%--------Gpu Memory Usage -----\n " + str(gpuusage))
        time.sleep(20)
        #g1.start()
        m1.join()
        g1.join()
        #self.assertEqual(expcmd, cmd, "Invalid command")


    def tearDown(self):
        print("Environment-01 Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main()

