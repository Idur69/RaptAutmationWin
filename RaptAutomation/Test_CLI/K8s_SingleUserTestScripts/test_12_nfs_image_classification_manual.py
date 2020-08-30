import datetime
import unittest
import os
import time
import multiprocessing
import sys
sys.path.append("..")
from cliEnvSetup.cmdconfig import userTwo,Paths

class Kubernetes_Cli_Nfs_Image_Manual(unittest.TestCase):

    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self, nfsimage_cmd):
        result = os.system(nfsimage_cmd)
        #gpuusage = os.system(gpuusage)
        #print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&\n" + str(nfsimage_cmd))
        #print("***********Your data  here ******************** : " + str(result))
        time.sleep(5)
    def run_gpucmd(self,gpuusage):
        gpuusage = os.system(gpuusage)
        #time.sleep(5)

    def test_nfs_image_manual(self):
        
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        path=Paths
        name = cmddata.name
        fw = path.tf
        application = path.app_image
        #dirpath = path.nfsdata_path
        training = path.nfs_image_train
        type1 = path.type1
        location = path.nfslocation
        mode = path.mode_manual
        nfsip = path.nfs_ip
        nfspath = path.nfs_path
        modeldir = path.nfs_model_dir
        imagedir = path.nfs_image_dir
        bottleneck = path.nfs_bottleneck
        steps = path.steps
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper


        #cmd = "raptrun -name demotwo -f tensorflow -a flower_classification -t /tensorflow/training/flower_classification/retrain-new.py -type rapt -l nfs -mode manual -p 50 -cp 90 -m /tensorflow/inception -i /tensorflow/datasets/flower_photos4.5GB -b /tensorflow/datasets/bottlenecks4.5GB-new -s 50 -nfsip 52.34.222.154 -nfspath /home/ubuntu/tensorflow-UI"
        nfsimage_cmd = "raptrun train"+" -name " + name+ " -f " + fw +" -a " + application +" -t " + training +" -type " + type1+" -l " + location +" -mode " + mode +" -p " + memoryper +"-cp " + coreper +" -m " + modeldir+" -i " + imagedir +" -b " + bottleneck +" -s " + steps +" -nfsip " +nfsip + " -nfspath " + nfspath


        print("**********this is your command-2 *************\n" + str(nfsimage_cmd))

        gpuusage = "nvidia-smi"
        print("%%%%%%--------Gpu Memory Usage ----- " + str(gpuusage))

        m1 = multiprocessing.Process(target=self.run_cmd1, args=(nfsimage_cmd,))
        g1 = multiprocessing.Process(target=self.run_gpucmd, args=(gpuusage,))

        m1.start()
        print("%%%%%%--------Gpu Memory Usage ----- " + str(gpuusage))
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

