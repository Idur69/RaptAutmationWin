import datetime
import unittest
import os
import time
import multiprocessing
import sys
sys.path.append("..")
from cliEnvSetup.cmdconfig import userTwo,Paths

class Rvirtus_Cli_S3_Image_Manual(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self, s3image_cmd):
        result = os.system(s3image_cmd)
        #gpuusage = os.system(gpuusage)
        #print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&\n" + str(s3image_cmd))
        #print("***********Your data  here ******************** : " + str(result))
        time.sleep(5)
    def run_gpucmd(self,gpuusage):
        gpuusage = os.system(gpuusage)
        #time.sleep(5)

    def test_s3_image_manual(self):
        
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        name = cmddata.name
        path = Paths

        fw = path.tf
        application = path.app_image
        dirpath = path.s3data_path
        training = path.s3_image_train
        type1 = path.type1
        location = path.s3location
        mode = path.mode_manual
        bkeys=path.bucket_keys
        bname=path.bucket_name
       # config = path.s3_pgan_config
        modeldir = path.s3_model_dir
        imagedir = path.s3_image_dir
        bottleneck = path.s3_bottleneck
        steps = path.steps
        memoryper = cmddata.memoryper 
        coreper = cmddata.coreper
        platform = path.platform

        #cmd = 'raptrun -name demotwo -f tensorflow -a flower_classification -d /s3bucket/rapt -t /tensorflow/tensorflow-UI-less/training/flower_classification/retrain-new.py -type rapt -l s3bucket -mode manual -p 50 -cp 90 -k AKIAITOV7UZRONOPBIHA:PmlQsH2tg7+7jexDMPzN0VGat/9VPa6BIapcAPYe -bucket rapt-data-bucket -m /tensorflow/tensorflow-UI-less/inception -i /tensorflow/tensorflow-UI-less/datasets/flower_photos -b /tensorflow/tensorflow-UI-less/datasets/bottlenecks-new -s 50 -pf raptvirtus '
        s3image_cmd = "raptrun"+" -name " + name+ " -f " + fw +" -a " + application +" -d " + dirpath +" -t " + training +" -type " + type1+" -l " + location +" -mode " + mode +" -p " + memoryper +"-cp " + coreper +" -k " + bkeys +" -bucket " + bname +" -m " + modeldir+" -i " + imagedir +" -b " + bottleneck +" -s " + steps + " -pf " + platform

        print("**********this is your command *************\n" + str(s3image_cmd))

        gpuusage = "nvidia-smi "
        print("%%%%%%--------Gpu Memory Usage -----\n " + str(gpuusage))

        m1 = multiprocessing.Process(target=self.run_cmd1, args=(s3image_cmd,))
        g1 = multiprocessing.Process(target=self.run_gpucmd, args=(gpuusage,))
        m1.start()
        print("%%%%%%--------Gpu Memory Usage -----\n " + str(gpuusage))

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

