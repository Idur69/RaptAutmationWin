import datetime
import unittest
import os
import time
import multiprocessing
import sys 
sys.path.append("..")
from cliEnvSetup.cmdconfig import userOne,userThree, userTwo,Paths

class Rvirtus_Cli_Negative_Casses(unittest.TestCase):

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
        expuser = " raptrun"
        raptrun = "raptrn"
        name = cmddata.name
        path = Paths
        fw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = raptrun + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        # out_file = 'cmd_result.log'
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

        #name = cmddata.name
        name = "demo12"
        expuser = cmddata.name
        path = Paths
        fw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp"

        print("********** Your given Data ******************* \n")
        #print("Raptrun : ", str(raptrun), "\n")
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
        name = cmddata.name
        path = Paths
        #fw = path.tf
        fw = "tensorf"
        expfw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp"

        print("********** Your given Data ******************* \n")
        #print("Raptrun : ", str(raptrun), "\n")
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
        name = cmddata.name

        path = Paths
        fw = path.tf
        # ---- invalid application ------
        application = "mnist1"
        expapp = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp"

        print("********** Your given Data ******************* \n")
        #print("Raptrun : ", str(raptrun), "\n")
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
        name = cmddata.name

        path = Paths
        fw = path.tf
        application = path.app_mnist
        # dirpath = path.data_path
        dirpath = "/mnt/rapt/tensorflow-UI"
        exppath = path.data_path
        training = path.mnist_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp"

        print("********** Your given Data ******************* \n")
        #print("Raptrun : ", str(raptrun), "\n")
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
        name = cmddata.name
        path = Paths
        fw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        #training = path.mnist_train
        exptrain = path.mnist_train
        training = "/tensorflow/training/Mnist_classification/mnist_gp.py"
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper

        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp"

        print("********** Your given Data ******************* \n")
        #print("Raptrun : ", str(raptrun), "\n")
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
        name = cmddata.name
        path = Paths
        fw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_train
        #type1 = path.type1
        exptype = path.type1
        type1 = "raptrapt"
        location = path.location
        mode = path.mode_manual
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper
        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp"

        print("********** Your given Data ******************* \n")
        #print("Raptrun : ", str(raptrun), "\n")
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
        name = cmddata.name
        path = Paths
        fw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_train
        type1 = path.type1
        #location = path.location
        explocation = path.location
        location = "local2"
        mode = path.mode_manual
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper
        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp 90"

        print("********** Your given Data ******************* \n")
        #print("Raptrun : ", str(raptrun), "\n")
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
        name = cmddata.name
        path = Paths
        fw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_train
        type1 = path.type1
        location = path.location
        #mode = path.mode_manual
        expmode = path.mode_manual
        mode = "manualmanual"
        memoryper = cmddata.memoryper
        coreper = cmddata.coreper

        cmd = "/home/ubuntu/test/raptcli raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper
        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp 90"

        print("********** Your given Data ******************* \n")
        #print("Raptrun : ", str(raptrun), "\n")
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
    '''
    # Test Cases-10 less memory percentage
    def test_mnist_manual_10(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        name = cmddata.name
        path = Paths
        fw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        #memoryper = cmddata.memoryper
        expmemoryper = "40"
        memoryper = "0"
        coreper = cmddata.coreper

        cmd = "raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper
        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp 90"

        print("********** Your given Data ******************* \n")
        #print("Raptrun : ", str(raptrun), "\n")
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
        #self.assertEqual(expmemoryper, memoryper, "Invalid mode ")
        self.assertLess(expmemoryper,memoryper, "Your given less memory percentage")
     
    # Test Cases-11 less core percentage
    def test_mnist_manual_11(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        name = cmddata.name
        path = Paths
        fw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        memoryper = cmddata.memoryper
        coreper = "0"
        expcoreper = "40"

        cmd = "raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper
        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp 90"

        print("********** Your given Data ******************* \n")
        # print("Raptrun : ", str(raptrun), "\n")
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
        # self.assertEqual(expmemoryper, memoryper, "Invalid mode ")
        self.assertLess(expcoreper, coreper, "Your given less core  percentage")
    
    # Test Cases-12 greater memory percentage
    def test_mnist_manual_12(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        name = cmddata.name
        path = Paths
        fw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        # memoryper = cmddata.memoryper
        expmemoryper = "40"
        memoryper = "120"
        coreper = cmddata.coreper

        cmd = "raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper
        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp 90"

        print("********** Your given Data ******************* \n")
        # print("Raptrun : ", str(raptrun), "\n")
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
        # self.assertEqual(expmemoryper, memoryper, "Invalid mode ")
        self.assertGreater(expmemoryper, memoryper, "Your given more memory percentage")

    # Test Cases-13 greater core percentage
    def test_mnist_manual_13(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        name = cmddata.name
        path = Paths
        fw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        memoryper = cmddata.memoryper
        coreper = "120"
        expcoreper = "40"

        cmd = "raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper
        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp 90"

        print("********** Your given Data ******************* \n")
        # print("Raptrun : ", str(raptrun), "\n")
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
        # self.assertEqual(expmemoryper, memoryper, "Invalid mode ")
        self.assertGreater(expcoreper, coreper, "Your given more core  percentage!")

    # Test Cases-14 Empty memory percentage
    def test_mnist_manual_14(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        name = cmddata.name
        path = Paths
        fw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        # memoryper = cmddata.memoryper
        expmemoryper = "40"
        memoryper = ""
        coreper = cmddata.coreper

        cmd = "raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper
        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp 90"

        print("********** Your given Data ******************* \n")
        # print("Raptrun : ", str(raptrun), "\n")
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
        # self.assertEqual(expmemoryper, memoryper, "Invalid mode ")
        self.assertEqual(expmemoryper, memoryper, "Your given empty memory percentage")

    # Test Cases-15 greater core percentage
    def test_mnist_manual_15(self):
        # ******************* Command Enviromnet setup ****************
        cmddata = userTwo
        name = cmddata.name
        path = Paths
        fw = path.tf
        application = path.app_mnist
        dirpath = path.data_path
        training = path.mnist_train
        type1 = path.type1
        location = path.location
        mode = path.mode_manual
        memoryper = cmddata.memoryper
        coreper = ""
        expcoreper = "40"

        cmd = "raptrun" + " -name " + name + " -f " + fw + " -a " + application + " -d " + dirpath + " -t " + training + " -type " + type1 + " -l " + location + " -mode " + mode + " -p " + memoryper + " -cp " + coreper
        # cmd = "raptrun -name demotwo  -f tensorflow -a mnist -d /home/ubuntu/tensorflow-UI/ -t /tensorflow/training/Mnist_classification/mnist_gpu.py -type rapt -l local -mode manual -p 30 -cp 90"

        print("********** Your given Data ******************* \n")
        # print("Raptrun : ", str(raptrun), "\n")
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
        # self.assertEqual(expmemoryper, memoryper, "Invalid mode ")
        self.assertEqual(expcoreper, coreper, "Your given Empty core  percentage!")
    '''    
    def tearDown(self):
        print("Environment-01 Destroyed")
        print("Run Completed at :" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main()


