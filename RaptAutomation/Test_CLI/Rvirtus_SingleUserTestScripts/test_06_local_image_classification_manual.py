import datetime
import unittest
import os
import time
import multiprocessing
import sys
sys.path.append("..")
from cliEnvSetup.cmdconfig import userTwo,Paths

class Rvirtus_Cli_Image_Manual(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self, image_cmd):
        result = os.system(image_cmd)
        #gpuusage = os.system(gpuusage)
        print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&" + str(image_cmd))
        #print("***********Your data  here ******************** : " + str(result))
        time.sleep(5)
    def run_gpucmd(self,gpuusage):
        gpuusage = os.system(gpuusage)
        #time.sleep(5)

    def test_local_image_manual(self):
        
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        #raptrun = cmddata.raptrun
        name = cmddata.name
        path = Paths
        fw = path.tf
        application = path.app_image
        dirpath = path.data_path
        training = path.image_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        modeldir = path.model_dir
        imagedir = path.image_dir
        bottleneck = path.bottleneck
        steps = path.steps
        platform = path.platform
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper
 

        image_cmd = "raptrun "+" -name " + name+ " -f " + fw +" -a " + application +" -d " + dirpath +" -t " + training +" -type " + type1+" -l " + location +" -mode " + mode +" -p " + memoryper +" -cp " + coreper  +" -m " + modeldir+" -i " + imagedir +" -b " + bottleneck +" -s " + steps + " -pf " + platform
        #cmd = "raptrun -name demotwo -f tensorflow -a flower_classification -d /mnt/rapt/tensorflow-UI  -t /tensorflow/training/flower_classification/retrain-new.py -type rapt -l local  -mode manual -p 50 -cp 90 -m /tensorflow/inception -i /tensorflow/datasets/flower_photos4.5GB -b /tensorflow/datasets/bottlenecks4.5GB-new -s 50 -pf raptvirtus"

        print("**********this is your command-2 *************\n" + str(image_cmd))

        gpuusage = "nvidia-smi "
        #print("%%%%%%--------Gpu Memory Usage -----\n " + str(gpuusage))

        m1 = multiprocessing.Process(target=self.run_cmd1, args=(image_cmd,))
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

