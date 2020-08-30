# import unittest
from unittest import TestLoader, TestSuite, TextTestRunner
import sys


sys.path.append('..')

# Importing the modules
#from Test_UI.K8s_Parallel_MultiUser_SingleGpu.test_01_singleGpu_pgan_mnist_manual import Kubernetes_Ui_Parallel_Pgan_Mnist_01

#------------ Rapt UI Screens ---------------------------------------------
'''
from Test_UI.Rapt_Ui_Screens_Scripts.test_k8s_ui_01_Registration import Rapt_Ui_Registration
from Test_UI.Rapt_Ui_Screens_Scripts.test_k8s_ui_02_Registration_Screens import Rapt_Ui_Registration_Screens
from Test_UI.Rapt_Ui_Screens_Scripts.test_k8s_ui_03_Login_Screens import Rapt_Ui_Login_Screens
from Test_UI.Rapt_Ui_Screens_Scripts.test_k8s_ui_04_Login import Rapt_Ui_AdminLogin
from Test_UI.Rapt_Ui_Screens_Scripts.test_k8s_ui_05_DatasetTab import Rapt_Ui_DatasetTab
from Test_UI.Rapt_Ui_Screens_Scripts.test_k8s_ui_06_ComputeTab import Rapt_Ui_ComputeTab
'''
# ---------------- LOCAL ------------------------------------------------------

from Test_UI.K8s_SingleUser_SingleGpu.test_01_local_mnist_auto import Kubernetes_Ui_Mnist_Auto
#from Test_UI.K8s_SingleUser_SingleGpu.test_02_local_mnist_manual import Kubernetes_Ui_Mnist_Manual
#from Test_UI.K8s_SingleUser_SingleGpu.test_03_local_pgan_auto import Kubernetes_Ui_Pgan_Auto
#from Test_UI.K8s_SingleUser_SingleGpu.test_04_local_pgan_manual import Kubernetes_Ui_Pgan_Manual
#from Test_UI.K8s_SingleUser_SingleGpu.test_05_local_image_classification_auto import Kubernetes_Ui_Image_Auto
#from Test_UI.K8s_SingleUser_SingleGpu.test_06_local_image_classification_manual import Kubernetes_Ui_Image_Manual

'''
# ----------------NFS ---------------------------------------------------------

from Test_UI.K8s_SingleUser_SingleGpu.test_07_nfs_mnist_auto import Kubernetes_Ui_Nfs_Mnist_Auto
from Test_UI.K8s_SingleUser_SingleGpu.test_08_nfs_mnist_manual import Kubernetes_Ui_Nfs_Mnist_Manual
from Test_UI.K8s_SingleUser_SingleGpu.test_09_nfs_pgan_auto import Kubernetes_Ui_Nfs_Pgan_Auto
from Test_UI.K8s_SingleUser_SingleGpu.test_10_nfs_pgan_manual import Kubernetes_Ui_Nfs_Pgan_Manual
from Test_UI.K8s_SingleUser_SingleGpu.test_11_nfs_image_classification_auto import Kubernetes_Ui_Nfs_Image_Auto
from Test_UI.K8s_SingleUser_SingleGpu.test_12_nfs_image_classification_manual import Kubernetes_Ui_Nfs_Image_Manual

# ---------------- S3 ---------------------------------------------------------
from Test_UI.K8s_SingleUser_SingleGpu.test_13_s3_mnist_auto import Kubernetes_Ui_S3_Mnist_Auto
from Test_UI.K8s_SingleUser_SingleGpu.test_14_s3_mnist_manual import Kubernetes_Ui_S3_Mnist_Manual
from Test_UI.K8s_SingleUser_SingleGpu.test_15_s3_pgan_auto import Kubernetes_Ui_S3_Pgan_Auto
from Test_UI.K8s_SingleUser_SingleGpu.test_16_s3_pgan_manual import Kubernetes_Ui_S3_Pgan_Manual
from Test_UI.K8s_SingleUser_SingleGpu.test_17_s3_image_classification_auto import Kubernetes_Ui_S3_Image_Auto
from Test_UI.K8s_SingleUser_SingleGpu.test_18_s3_image_classification_manual import Kubernetes_Ui_S3_Image_Manual
# ---------------- inferencing -------------------------------------------------
from Test_UI.K8s_SingleUser_SingleGpu.test_19_inferencing_dog_classification_auto import Kubernetes_Ui_Inferencing_01
from Test_UI.K8s_SingleUser_SingleGpu.test_20_Inferencing_dog_classification_manual import Kubernetes_Ui_Inferencing_02
from Test_UI.K8s_SingleUser_SingleGpu.test_21_Inferencing_image_classification_auto import Kubernetes_Ui_Inferencing_03
from Test_UI.K8s_SingleUser_SingleGpu.test_22_inferencing_image_classification_manual import Kubernetes_Ui_Inferencing_04

# --------------------------------- multiuser parallel -------------------------------------------------------------
from Test_UI.K8s_Parallel_MultiUser_SingleGpu.test_01_singleGpu_pgan_mnist_manual import Kubernetes_Ui_Parallel_Pgan_Mnist_01
from Test_UI.K8s_Parallel_MultiUser_SingleGpu.test_02_singleGpu_pgan_mnist_manual import Kubernetes_Ui_Parallel_Pgan_Mnist_02
from Test_UI.K8s_Parallel_MultiUser_SingleGpu.test_03_singleGpu_pgan_auto_mnist_mnaul import Kubernetes_Ui_Parallel_Pgan_Mnist_03
from Test_UI.K8s_Parallel_MultiUser_SingleGpu.test_04_singleGpu_pgan_mnist_auto import Kubernetes_Ui_Parallel_Pgan_Mnist_04
from Test_UI.K8s_Parallel_MultiUser_SingleGpu.test_05_singleGpu_mnist2_manual import Kubernetes_Ui_Parallel_Pgan_Mnist_05
from Test_UI.K8s_Parallel_MultiUser_SingleGpu.test_06_singleGpu_mnist3_manual3 import Kubernetes_Ui_Parallel_Mnist_06
from Test_UI.K8s_Parallel_MultiUser_SingleGpu.test_07_singleGpu_mnist4_manual4 import Kubernetes_Ui_Parallel_Mnist4_07

# -------------------- Multi Gpus-8 --------------------------
from Test_UI.K8s_SingleUser_MultiGpus8.test_01_multigpus_8_mnist_auto import Kubernetes_Ui_MultiGpu_01
from Test_UI.K8s_SingleUser_MultiGpus8.test_02_multigpus_8_mnist_manual import Kubernetes_Ui_MultiGpu_02
from Test_UI.K8s_SingleUser_MultiGpus8.test_03_multigpus_8_pgan_auto import Kubernetes_Ui_MultiGpu_03
from Test_UI.K8s_SingleUser_MultiGpus8.test_04_multigpus_8_pgan_manual import Kubernetes_Ui_MultiGpu_04
from Test_UI.K8s_SingleUser_MultiGpus8.test_05_multigpus_8_image_auto import Kubernetes_Ui_MultiGpu_05
from Test_UI.K8s_SingleUser_MultiGpus8.test_06_multigpus_8_image_manual import Kubernetes_Ui_MultiGpu_06

# ----------------------- Volta Gpu ------------------------------------
from Test_UI.K8s_Parallel_MultiInstance_VoltaGpuTest.test_01_singleGpu_parallel_pgan_manual1 import Kubernetes_Ui_VoltaGpu_01
from Test_UI.K8s_Parallel_MultiInstance_VoltaGpuTest.test_02_singleGpu_parallel_pgan_auto_manual import Kubernetes_Ui_VoltaGpu_02
from Test_UI.K8s_Parallel_MultiInstance_VoltaGpuTest.test_03_singleGpu_parallel_pgan_manual_auto import Kubernetes_Ui_VoltaGpu_03
from Test_UI.K8s_Parallel_MultiInstance_VoltaGpuTest.test_04_singleGpu_parallel_pgan_auto import Kubernetes_Ui_VoltaGpu_04
from Test_UI.K8s_Parallel_MultiInstance_VoltaGpuTest.test_05_singleGpu_parallel_pgan3_manual import Kubernetes_Ui_VoltaGpu_05
from Test_UI.K8s_Parallel_MultiInstance_VoltaGpuTest.test_06_singleGpu_parallel_pgan3_auto_manual2 import Kubernetes_Ui_VoltaGpu_06
from Test_UI.K8s_Parallel_MultiInstance_VoltaGpuTest.test_07_singleGpu_parallel_pgan3_manual2_auto import Kubernetes_Ui_VoltaGpu_07
'''
#--------------------------------------------------------------------


if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((

        # --------------- Rapt UI Screens and Negative casses------------
        #loader.loadTestsFromTestCase(Rapt_Ui_Registration),
        #loader.loadTestsFromTestCase(Rapt_Ui_Registration_Screens),
        #loader.loadTestsFromTestCase(Rapt_Ui_Login_Screens),
        #loader.loadTestsFromTestCase(Rapt_Ui_AdminLogin),
        #loader.loadTestsFromTestCase(Rapt_Ui_DatasetTab),
        #loader.loadTestsFromTestCase(Rapt_Ui_ComputeTab),

        # Single user single gpu

        # ---------------------- local ---------------------------------
        loader.loadTestsFromTestCase(Kubernetes_Ui_Mnist_Auto),
        #loader.loadTestsFromTestCase(Kubernetes_Ui_Mnist_Manual),
        '''
        #loader.loadTestsFromTestCase(Kubernetes_Ui_Pgan_Auto),
        #loader.loadTestsFromTestCase(Kubernetes_Ui_Pgan_Manual),

        loader.loadTestsFromTestCase(Kubernetes_Ui_Image_Auto),
        
        loader.loadTestsFromTestCase(Kubernetes_Ui_Image_Manual),

        
        # --------------------- nfs --------------------------------------
        loader.loadTestsFromTestCase(Kubernetes_Ui_Nfs_Mnist_Auto),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Nfs_Mnist_Manual),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Nfs_Pgan_Auto),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Nfs_Pgan_Manual),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Nfs_Image_Auto),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Nfs_Image_Manual),

        # --------------------- s3 --------------------------------------
        loader.loadTestsFromTestCase(Kubernetes_Ui_S3_Mnist_Auto),
        loader.loadTestsFromTestCase(Kubernetes_Ui_S3_Mnist_Manual),
        loader.loadTestsFromTestCase(Kubernetes_Ui_S3_Pgan_Auto),
        loader.loadTestsFromTestCase(Kubernetes_Ui_S3_Pgan_Manual),
        loader.loadTestsFromTestCase(Kubernetes_Ui_S3_Image_Auto),
        loader.loadTestsFromTestCase(Kubernetes_Ui_S3_Image_Manual),
        # ----------------- Inferencing  ---------------------------
        loader.loadTestsFromTestCase(Kubernetes_Ui_Inferencing_01),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Inferencing_02),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Inferencing_03),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Inferencing_04),

        # -------------------Parallel Multi user single gpu
        loader.loadTestsFromTestCase(Kubernetes_Ui_Parallel_Pgan_Mnist_01),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Parallel_Pgan_Mnist_02),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Parallel_Pgan_Mnist_03),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Parallel_Pgan_Mnist_04),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Parallel_Pgan_Mnist_05),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Parallel_Mnist_06),
        loader.loadTestsFromTestCase(Kubernetes_Ui_Parallel_Mnist4_07),

        # -------------************ Multi Gpus-8 Test modules ******** ----------------------------------
        loader.loadTestsFromTestCase(Kubernetes_Ui_MultiGpu_01),
        loader.loadTestsFromTestCase(Kubernetes_Ui_MultiGpu_02),
        loader.loadTestsFromTestCase(Kubernetes_Ui_MultiGpu_03),
        loader.loadTestsFromTestCase(Kubernetes_Ui_MultiGpu_04),
        loader.loadTestsFromTestCase(Kubernetes_Ui_MultiGpu_05),
        loader.loadTestsFromTestCase(Kubernetes_Ui_MultiGpu_06),

        #-------------************ MultiInstance volta Gpu *********------------------------
        loader.loadTestsFromTestCase(Kubernetes_Ui_VoltaGpu_01),
        loader.loadTestsFromTestCase(Kubernetes_Ui_VoltaGpu_02),
        loader.loadTestsFromTestCase(Kubernetes_Ui_VoltaGpu_03),
        loader.loadTestsFromTestCase(Kubernetes_Ui_VoltaGpu_04),
        loader.loadTestsFromTestCase(Kubernetes_Ui_VoltaGpu_05),
        loader.loadTestsFromTestCase(Kubernetes_Ui_VoltaGpu_06),
        loader.loadTestsFromTestCase(Kubernetes_Ui_VoltaGpu_07),
        '''
        #-------------------------------------------------------
    ))
    # run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
    # test_local_mnist_auto_01.Kubernetes_Cli_local_Mnist_auto_01()
