# import unittest
from unittest import TestLoader, TestSuite, TextTestRunner
import sys

sys.path.append('..')

#from Test_CLI.K8s_SingleUserTestScripts.test_00_negative_casses09 import Kubernetes_Cli_Negative_Casses

# ---------------- LOCAL ------------------------------------------------------
#from Test_CLI.K8s_SingleUserTestScripts.test_01_local_mnist_auto import Kubernetes_Cli_Mnist_Auto

#from Test_CLI.K8s_SingleUserTestScripts.test_02_local_mnist_manual import Kubernetes_Cli_Mnist_Manual
#from Test_CLI.K8s_SingleUserTestScripts.test_03_local_pgan_auto import Kubernetes_Cli_Pgan_Auto
#from Test_CLI.K8s_SingleUserTestScripts.test_04_local_pgan_manual import Kubernetes_Cli_Pgan_Manual
#from Test_CLI.K8s_SingleUserTestScripts.test_05_local_flower_classification_auto import Kubernetes_Cli_Image_Auto
#from Test_CLI.K8s_SingleUserTestScripts.test_06_local_flower_classification_manual import Kubernetes_Cli_Image_Manual

# ----------------NFS ---------------------------------------------------------
#from Test_CLI.K8s_SingleUserTestScripts.test_07_nfs_mnist_auto import Kubernetes_Cli_Nfs_Mnist_Auto
#from Test_CLI.K8s_SingleUserTestScripts.test_08_nfs_mnist_manual import Kubernetes_Cli_Nfs_Mnist_Manual
#from Test_CLI.K8s_SingleUserTestScripts.test_09_nfs_pgan_auto import Kubernetes_Cli_Nfs_Pgan_Auto
#from Test_CLI.K8s_SingleUserTestScripts.test_10_nfs_pgan_manual import Kubernetes_Cli_Nfs_Pgan_Manual
#from Test_CLI.K8s_SingleUserTestScripts.test_11_nfs_image_classification_auto import Kubernetes_Cli_Nfs_Image_Auto
#from Test_CLI.K8s_SingleUserTestScripts.test_12_nfs_image_classification_manual import Kubernetes_Cli_Nfs_Image_Manual

# ---------------- S3 ---------------------------------------------------------
#from Test_CLI.K8s_SingleUserTestScripts.test_13_s3_mnist_auto import Kubernetes_Cli_S3_Mnist_Auto
#from Test_CLI.K8s_SingleUserTestScripts.test_14_s3_mnist_manual import Kubernetes_Cli_S3_Mnist_Manual
#from Test_CLI.K8s_SingleUserTestScripts.test_15_s3_pgan_auto import Kubernetes_Cli_S3_Pgan_Auto
#from Test_CLI.K8s_SingleUserTestScripts.test_16_s3_pgan_manual import Kubernetes_Cli_S3_Pgan_Manual
#from Test_CLI.K8s_SingleUserTestScripts.test_17_s3_flower_classification_auto import Kubernetes_Cli_S3_Image_Auto
#from Test_CLI.K8s_SingleUserTestScripts.test_18_s3_flower_classification_manual import Kubernetes_Cli_S3_Image_Manual

'''
# --------------------------------- multiuser parallel -------------------------------------------------------------
from Test_CLI.k8s_MultiUserTestScripts.test_01_parallel_local_mnist_auto_manual import Kubernetes_Multiusers_01
from Test_CLI.k8s_MultiUserTestScripts.test_02_parallel_local_mnist_manual1_manual2 import Kubernetes_Multiusers_02
from Test_CLI.k8s_MultiUserTestScripts.test_03_parallel_local_pgan_manual_mnist_auto import Kubernetes_Multiusers_03
from Test_CLI.k8s_MultiUserTestScripts.test_04_parallel_local_pgan_manual_mnist_manual import Kubernetes_Multiusers_04
from Test_CLI.k8s_MultiUserTestScripts.test_05_parallel_nfs_mnist_manual_s3mnist_manual import Kubernetes_Multiusers_05
from Test_CLI.k8s_MultiUserTestScripts.test_06_parallel_nfs_pgan_auto_s3mnist_auto import Kubernetes_Multiusers_06
from Test_CLI.k8s_MultiUserTestScripts.test_07_parallel_nfs_pgan_manual_s3mnist_manual import Kubernetes_Multiusers_07
from Test_CLI.k8s_MultiUserTestScripts.test_08_parallel_s3_mnist_manual_nfsmnist_manaul import Kubernetes_Multiusers_08
from Test_CLI.k8s_MultiUserTestScripts.test_09_parallel_s3_pgan_auto_nfsmnist_auto import Kubernetes_Multiusers_09
from Test_CLI.k8s_MultiUserTestScripts.test_10_parallel_s3_pgan_manual_nfsmnist_manual import Kubernetes_Multiusers_10
from Test_CLI.k8s_MultiUserTestScripts.test_11_parallel_s3_nfs_local_manual import Kubernetes_Multiusers_11

# -------------------- Multi Gpus-8 --------------------------
from Test_CLI.k8s_MultiGpus8TestScripts.test_01_local_mnist_auto import Kubernetes_Cli_MultiGpu_Mnist_Auto8
from Test_CLI.k8s_MultiGpus8TestScripts.test_02_local_mnist_manual import Kubernetes_Cli_MultiGpu_Mnist_Manual8
from Test_CLI.k8s_MultiGpus8TestScripts.test_03_parallel_local_mnist_auto_manual import Kubernetes_Cli_Multiusers_03
from Test_CLI.k8s_MultiGpus8TestScripts.test_04_parallel_local_mnist_manual_manual import Kubernetes_Cli_Multiusers_04
'''
#--------------------------------------------------


if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        # Negative casses
        #loader.loadTestsFromTestCase(Kubernetes_Cli_Negative_Casses),

        # Single user sequential module
        # ---------------------- local ---------------------------------
        #loader.loadTestsFromTestCase(Kubernetes_Cli_Mnist_Auto),
	        
	#loader.loadTestsFromTestCase(Kubernetes_Cli_Mnist_Manual),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_Pgan_Auto),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_Pgan_Manual),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_Image_Auto),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_Image_Manual),
        
	# --------------------- nfs --------------------------------------
        #loader.loadTestsFromTestCase(Kubernetes_Cli_Nfs_Mnist_Auto),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_Nfs_Mnist_Manual),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_Nfs_Pgan_Auto),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_Nfs_Pgan_Manual),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_Nfs_Image_Auto),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_Nfs_Image_Manual),
        
        # --------------------- s3 --------------------------------------
        #loader.loadTestsFromTestCase(Kubernetes_Cli_S3_Mnist_Auto),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_S3_Mnist_Manual),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_S3_Pgan_Auto),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_S3_Pgan_Manual),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_S3_Image_Auto),
        #loader.loadTestsFromTestCase(Kubernetes_Cli_S3_Image_Manual),
        # Multi user parallel modules
        '''
        # -------------------- parallel --------------------------------------
        loader.loadTestsFromTestCase(Kubernetes_Multiusers_01),
        loader.loadTestsFromTestCase(Kubernetes_Multiusers_02),
        loader.loadTestsFromTestCase(Kubernetes_Multiusers_03),
        loader.loadTestsFromTestCase(Kubernetes_Multiusers_04),
        loader.loadTestsFromTestCase(Kubernetes_Multiusers_05),
        loader.loadTestsFromTestCase(Kubernetes_Multiusers_06),
        loader.loadTestsFromTestCase(Kubernetes_Multiusers_07),
        loader.loadTestsFromTestCase(Kubernetes_Multiusers_08),
        loader.loadTestsFromTestCase(Kubernetes_Multiusers_09),
        loader.loadTestsFromTestCase(Kubernetes_Multiusers_10),
        loader.loadTestsFromTestCase(Kubernetes_Multiusers_11),

        # --------------------------- Multi Gpus-8 Test modules ----------------------------------
        loader.loadTestsFromTestCase(Kubernetes_Cli_MultiGpu_Mnist_Auto8),
        loader.loadTestsFromTestCase(Kubernetes_Cli_MultiGpu_Mnist_Manual8),
        loader.loadTestsFromTestCase(Kubernetes_Cli_Multiusers_03),
        loader.loadTestsFromTestCase(Kubernetes_Cli_Multiusers_04),
	'''
    ))
    # run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
    # test_local_mnist_auto_01.Kubernetes_Cli_local_Mnist_auto_01()
