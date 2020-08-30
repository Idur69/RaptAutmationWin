import datetime
import unittest
import os
import time
import multiprocessing
import sys 
sys.path.append("..")
from cliEnvSetup.cmdconfig import userTwo

class Kubernetes_Cli_Negative_Casses(unittest.TestCase):
    def setUp(self):
        print("RunStarted at :" + str(datetime.datetime.now()))
        print("Environment_01 Created")
        print("**********************")

    def run_cmd1(self,cmd):

        result =  os.system(cmd)
        #print("&&&&&&&&&&---Yor command-1 ---&&&&&&&&&&&" + str(cmd))
        #print("***********Your data  here ******************** : " +  str(result))

        time.sleep(5)
    #-------Tetcase-1 Invalid raptrun -----------
    def test_mnist_manual_01(self):

        #******************* Command Enviromnet setup ****************
        cmddata = userTwo
        # raptrun = cmddata.raptrun
        raptrun = "raptrn"
        name = cmddata.name
        fw = cmddata.tf
        application = cmddata.application
        dirpath = cmddata.dirpath
        training = cmddata.training
        type1 = cmddata.type1
        location = cmddata.location
        mode = cmddata.mode
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper
        cmd = raptrun + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        # out_file = 'cmd_result.log'
        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp 90"

        expuser = " raptrun"

        print("********** Your given Data ******************* \n")
        print("Raptrun : ", str(raptrun), "\n")
        print("User Name : ", str(name), "\n")
        print("Framework : ", str(fw), '\n')
        print("Application : ", str(application), "\n")
        print("Path : ", str(dirpath), "\n")
        print("Training  : ", str(training), "\n")
        print("Type : ", str(type1), "\n")
        print("Mode : ", str(mode), "\n")
        print("Memory% : ", str(memoryper),"%,", " Core% : ", str(coreper),"%", "\n")
        print("*************************************************")
        m1 = multiprocessing.Process(target=self.run_cmd1, args=(cmd,))
        m1.start()
        m1.join()
        self.assertEqual(expuser, cmd, "Invalid Raptrun")

    # -------Tetcase-2 Invalid Username -----------
    def test_mnist_manual_02(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        raptrun = cmddata.raptrun
        #name = cmddata.name
        name = "demo12"
        expuser = "demoone"
        fw = cmddata.tf
        application = cmddata.application
        dirpath = cmddata.dirpath
        training = cmddata.training
        type1 = cmddata.type1
        location = cmddata.location
        mode = cmddata.mode
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = raptrun + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp"

        print("********** Your given Data ******************* \n")
        print("Raptrun : ", str(raptrun), "\n")
        print("User Name : ", str(name), "\n")
        print("Framework : ", str(fw), '\n')
        print("Application : ", str(application), "\n")
        print("Path : ", str(dirpath), "\n")
        print("Training  : ", str(training), "\n")
        print("Type : ", str(type1), "\n")
        print("Mode : ", str(mode), "\n")
        print("Memory% : ", str(memoryper), "%", " Core% : ", str(coreper), "%", "\n")
        print("*************************************************")
        m1 = multiprocessing.Process(target=self.run_cmd1, args=(cmd,))
        m1.start()
        m1.join()
        self.assertEqual(expuser, cmd, "Invalid Username")
          
    # -------Tetcase-3 Invalid Framework -----------
    def test_mnist_manual_03(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        raptrun = cmddata.raptrun
        name = cmddata.name
        #fw = cmddata.tf
        fw = "tensorf"
        expfw = "tensorflow"
        application = cmddata.application
        dirpath = cmddata.dirpath
        training = cmddata.training
        type1 = cmddata.type1
        location = cmddata.location
        mode = cmddata.mode
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = raptrun + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp"

        print("********** Your given Data ******************* \n")
        print("Raptrun : ", str(raptrun), "\n")
        print("User Name : ", str(name), "\n")
        print("Framework : ", str(fw), '\n')
        print("Application : ", str(application), "\n")
        print("Path : ", str(dirpath), "\n")
        print("Training  : ", str(training), "\n")
        print("Type : ", str(type1), "\n")
        print("Mode : ", str(mode), "\n")
        print("Memory% : ", str(memoryper), "%", " Core% : ", str(coreper), "%", "\n")
        print("*************************************************")
        m1 = multiprocessing.Process(target=self.run_cmd1, args=(cmd,))
        m1.start()
        m1.join()
        self.assertEqual(expfw, cmd, "Invalid Framework ")
    # -------Tetcase-5 Invalid Application -----------
    def test_mnist_manual_04(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        raptrun = cmddata.raptrun
        name = cmddata.name
        fw = cmddata.tf
        #application = cmddata.application
        application = "mnist1"
        expapp = cmddata.application
        dirpath = cmddata.dirpath
        training = cmddata.training
        type1 = cmddata.type1
        location = cmddata.location
        mode = cmddata.mode
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = raptrun + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp"

        print("********** Your given Data ******************* \n")
        print("Raptrun : ", str(raptrun), "\n")
        print("User Name : ", str(name), "\n")
        print("Framework : ", str(fw), '\n')
        print("Application : ", str(application), "\n")
        print("Path : ", str(dirpath), "\n")
        print("Training  : ", str(training), "\n")
        print("Type : ", str(type1), "\n")
        print("Mode : ", str(mode), "\n")
        print("Memory% : ", str(memoryper), "%", " Core% : ", str(coreper), "%", "\n")
        print("*************************************************")
        m1 = multiprocessing.Process(target=self.run_cmd1, args=(cmd,))
        m1.start()
        m1.join()
        self.assertEqual(expapp, cmd, "Invalid Application ")

    # -------Tetcase-5 Invalid dirpath -----------
    def test_mnist_manual_05(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        raptrun = cmddata.raptrun
        name = cmddata.name
        fw = cmddata.tf
        application = cmddata.application
        #dirpath = cmddata.dirpath
        dirpath = "/mnt/rapt/tensorflow-UI"
        exppath = cmddata.dirpath
        training = cmddata.training
        type1 = cmddata.type1
        location = cmddata.location
        mode = cmddata.mode
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = raptrun + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp"

        print("********** Your given Data ******************* \n")
        print("Raptrun : ", str(raptrun), "\n")
        print("User Name : ", str(name), "\n")
        print("Framework : ", str(fw), '\n')
        print("Application : ", str(application), "\n")
        print("Path : ", str(dirpath), "\n")
        print("Training  : ", str(training), "\n")
        print("Type : ", str(type1), "\n")
        print("Mode : ", str(mode), "\n")
        print("Memory% : ", str(memoryper), "%", " Core% : ", str(coreper), "%", "\n")
        print("*************************************************")
        m1 = multiprocessing.Process(target=self.run_cmd1, args=(cmd,))
        m1.start()
        m1.join()
        self.assertEqual(exppath, cmd, "Invalid Dir Path ")
    # -------Tetcase-6 Invalid training -----------
    def test_mnist_manual_06(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        raptrun = cmddata.raptrun
        name = cmddata.name
        fw = cmddata.tf
        application = cmddata.application
        dirpath = cmddata.dirpath
        #training = cmddata.training
        exptrain = cmddata.training

        training = "/tensorflow/training/Mnist_classification/mnist_gp.py"
        type1 = cmddata.type1
        location = cmddata.location
        mode = cmddata.mode
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = raptrun + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp"

        print("********** Your given Data ******************* \n")
        print("Raptrun : ", str(raptrun), "\n")
        print("User Name : ", str(name), "\n")
        print("Framework : ", str(fw), '\n')
        print("Application : ", str(application), "\n")
        print("Path : ", str(dirpath), "\n")
        print("Training  : ", str(training), "\n")
        print("Type : ", str(type1), "\n")
        print("Mode : ", str(mode), "\n")
        print("Memory% : ", str(memoryper), "%", " Core% : ", str(coreper), "%", "\n")
        print("*************************************************")
        m1 = multiprocessing.Process(target=self.run_cmd1, args=(cmd,))
        m1.start()
        m1.join()
        self.assertEqual(exptrain, cmd, "Invalid Training file ")
    # -------Tetcase-7 Invalid type (rapt or original) -----------
    def test_mnist_manual_07(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        raptrun = cmddata.raptrun
        name = cmddata.name
        fw = cmddata.tf
        application = cmddata.application
        dirpath = cmddata.dirpath
        training = cmddata.training
        #type1 = cmddata.type1
        exptype = cmddata.type1
        type1 = "raptrapt"
        location = cmddata.location
        mode = cmddata.mode
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = raptrun + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper
        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp"

        print("********** Your given Data ******************* \n")
        print("Raptrun : ", str(raptrun), "\n")
        print("User Name : ", str(name), "\n")
        print("Framework : ", str(fw), '\n')
        print("Application : ", str(application), "\n")
        print("Path : ", str(dirpath), "\n")
        print("Training  : ", str(training), "\n")
        print("Type : ", str(type1), "\n")
        print("Mode : ", str(mode), "\n")
        print("Memory% : ", str(memoryper), "%", " Core% : ", str(coreper), "%", "\n")
        print("*************************************************")
        m1 = multiprocessing.Process(target=self.run_cmd1, args=(cmd,))
        m1.start()
        m1.join()
        self.assertEqual(exptype, type1, "Invalid Type rapt ")

    # -------Tetcase-8 Invalid location -----------
    def test_mnist_manual_08(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        raptrun = cmddata.raptrun
        name = cmddata.name
        fw = cmddata.tf
        application = cmddata.application
        dirpath = cmddata.dirpath
        training = cmddata.training
        type1 = cmddata.type1
        #location = cmddata.location
        explocation = cmddata.location
        location = "local2"
        mode = cmddata.mode
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = raptrun + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper
        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp 90"

        print("********** Your given Data ******************* \n")
        print("Raptrun : ", str(raptrun), "\n")
        print("User Name : ", str(name), "\n")
        print("Framework : ", str(fw), '\n')
        print("Application : ", str(application), "\n")
        print("Path : ", str(dirpath), "\n")
        print("Training  : ", str(training), "\n")
        print("Type : ", str(type1), "\n")
        print("Mode : ", str(mode), "\n")
        print("Memory% : ", str(memoryper), "%", " Core% : ", str(coreper), "%", "\n")
        print("*************************************************")
        m1 = multiprocessing.Process(target=self.run_cmd1, args=(cmd,))
        m1.start()
        m1.join()
        self.assertEqual(explocation, location, "Invalid location ")
    # -------Tetcase-9 Invalid mode (auto or manual) -----------
    def test_mnist_manual_09(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        raptrun = cmddata.raptrun
        name = cmddata.name
        fw = cmddata.tf
        application = cmddata.application
        dirpath = cmddata.dirpath
        training = cmddata.training
        type1 = cmddata.type1
        location = cmddata.location
        #mode = cmddata.mode
        expmode = cmddata.mode
        mode = "manualmanual"
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = raptrun + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper
        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp 90"

        print("********** Your given Data ******************* \n")
        print("Raptrun : ", str(raptrun), "\n")
        print("User Name : ", str(name), "\n")
        print("Framework : ", str(fw), '\n')
        print("Application : ", str(application), "\n")
        print("Path : ", str(dirpath), "\n")
        print("Training  : ", str(training), "\n")
        print("Type : ", str(type1), "\n")
        print("Mode : ", str(mode), "\n")
        print("Memory% : ", str(memoryper), "%", " Core% : ", str(coreper), "%", "\n")
        print("*************************************************")
        m1 = multiprocessing.Process(target=self.run_cmd1, args=(cmd,))
        m1.start()
        m1.join()
        self.assertEqual(expmode, mode, "Invalid mode ")

    def tearDown(self):
        print("Environment-01 Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main()

