# import unittest
from unittest import TestLoader, TestSuite, TextTestRunner
import sys


sys.path.append('..')


# ---------------- LOCAL ------------------------------------------------------
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_01_local_mnist_auto import Rvirtus_Ui_Mnist_Auto
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_02_local_mnist_manual import Rvirtus_Ui_Mnist_Manual
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_03_local_pgan_auto import Rvirtus_Ui_Pgan_Auto
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_04_local_pgan_manual import Rvirtus_Ui_Pgan_Manual
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_05_local_image_classification_auto import Rvirtus_Ui_Image_Auto
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_06_local_image_classification_manual import Rvirtus_Ui_Image_Manual

# ----------------NFS ---------------------------------------------------------
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_07_nfs_mnist_auto import Rvirtus_Ui_Nfs_Mnist_Auto
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_08_nfs_mnist_manual import Rvirtus_Ui_Nfs_Mnist_Manual
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_09_nfs_pgan_auto import Rvirtus_Ui_Nfs_Pgan_Auto
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_10_nfs_pgan_manaul import Rvirtus_Ui_Nfs_Pgan_Manual
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_11_nfs_image_classification_auto import Rvirtus_Ui_Nfs_Image_Auto
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_12_nfs_image_classification_manual import Rvirtus_Ui_Nfs_Image_Manual

# ---------------- S3 ---------------------------------------------------------
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_13_s3_mnist_auto import Rvirtus_Ui_S3_Mnist_Auto
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_14_s3_mnist_manual import Rvirtus_Ui_S3_Mnist_Manual
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_15_s3_pgan_auto import Rvirtus_Ui_S3_Pgan_Auto
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_16_s3_pgan_manual import Rvirtus_Ui_S3_Pgan_Manual
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_17_s3_image_classification_auto import Rvirtus_Ui_S3_Image_Auto
from Test_UI.Rvirtus_SingleUser_SingleGpu.test_18_s3_image_classification_manual import Rvirtus_Ui_S3_Image_Manual

# --------------------------------- multiuser parallel -------------------------------------------------------------
from Test_UI.Rvirtus_Parallel_Multiuser_SingleGpu.test_parallel_01_mnist_auto_auto import Rvirtus_Parallel_01
from Test_UI.Rvirtus_Parallel_Multiuser_SingleGpu.test_parallel_02_mnist_auto_manual import Rvirtus_Parallel_02
from Test_UI.Rvirtus_Parallel_Multiuser_SingleGpu.test_parallel_03_mnist_manual_manual1 import Rvirtus_Parallel_03
from Test_UI.Rvirtus_Parallel_Multiuser_SingleGpu.test_parallel_04_mnist_manual_manual2 import Rvirtus_Parallel_04

#--------------------------- MultiGps-8 -----------------
from Test_UI.Rvirtus_SingleUser_MultiGpus8.test_01_multigpus_8_mnist_auto import Rvirtus_Ui_Multi_Gpus_01
from Test_UI.Rvirtus_SingleUser_MultiGpus8.test_02_multigpus_8_mnist_manual import Rvirtus_Ui_Multi_Gpus_02
from Test_UI.Rvirtus_SingleUser_MultiGpus8.test_03_multigpus_8_pgan_auto import Rvirtus_Ui_Multi_Gpus_03
from Test_UI.Rvirtus_SingleUser_MultiGpus8.test_04_multigpus_8_pgan_manual import Rvirtus_Ui_Multi_Gpus_04
from Test_UI.Rvirtus_SingleUser_MultiGpus8.test_05_multigpus_8_image_auto import Rvirtus_Ui_Multi_Gpus_05
from Test_UI.Rvirtus_SingleUser_MultiGpus8.test_06_multigpus_8_image_manual import Rvirtus_Ui_Multi_Gpus_06


#--------------------------------------------------


if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        # Negative casses
        #loader.loadTestsFromTestCase(),

        # Single user sequential module
        # ---------------------- local ---------------------------------
        loader.loadTestsFromTestCase(Rvirtus_Ui_Mnist_Auto),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Mnist_Manual),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Pgan_Auto),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Pgan_Manual),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Image_Auto),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Image_Manual),

        # --------------------- nfs --------------------------------------
        loader.loadTestsFromTestCase(Rvirtus_Ui_Nfs_Mnist_Auto),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Nfs_Mnist_Manual),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Nfs_Pgan_Auto),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Nfs_Pgan_Manual),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Nfs_Image_Auto),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Nfs_Image_Manual),
        # --------------------- s3 --------------------------------------
        loader.loadTestsFromTestCase(Rvirtus_Ui_S3_Mnist_Auto),
        loader.loadTestsFromTestCase(Rvirtus_Ui_S3_Mnist_Manual),
        loader.loadTestsFromTestCase(Rvirtus_Ui_S3_Pgan_Auto),
        loader.loadTestsFromTestCase(Rvirtus_Ui_S3_Pgan_Manual),
        loader.loadTestsFromTestCase(Rvirtus_Ui_S3_Image_Auto),
        loader.loadTestsFromTestCase(Rvirtus_Ui_S3_Image_Manual),
        # Multi user parallel modules
        # -------------------- parallel --------------------------------------
        loader.loadTestsFromTestCase(Rvirtus_Parallel_01),
        loader.loadTestsFromTestCase(Rvirtus_Parallel_02),
        loader.loadTestsFromTestCase(Rvirtus_Parallel_03),
        loader.loadTestsFromTestCase(Rvirtus_Parallel_04),
        # --------------------------- Multi Gpus-8 Test modules ----------------------------------
        loader.loadTestsFromTestCase(Rvirtus_Ui_Multi_Gpus_01),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Multi_Gpus_02),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Multi_Gpus_03),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Multi_Gpus_04),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Multi_Gpus_05),
        loader.loadTestsFromTestCase(Rvirtus_Ui_Multi_Gpus_06),


    ))
    # run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
    # test_local_mnist_auto_01.Kubernetes_Cli_local_Mnist_auto_01()
