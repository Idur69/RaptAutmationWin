



class userOne():
    name = "john"
    location = "local"
    mode = "auto"
    #memoryper = "40 "
    #coreper = "90"


class userTwo(object):

    name = "harry"
    location = "local"
    mode = "manual"
    memoryper = "40 "
    coreper = "90"
    # memory and coreper percentage for multigpus-8
    memoryper_multigpus = "30", "40", "50", "60", "70", "80", "55", "45"
    coreper_multigpus = "80", "90", "80", "90", "80", "90", "80", "90"

class userThree():
    #raptrun = " raptrun"
    name = "rabert"
    memoryper = "45"
    coreper = "90"
    # memory and coreper percentage for multigpus-8
    memoryper_multigpus = "40", "50","80", "55"
    coreper_multigpus = "80", "90", "80", "90"


class Paths:
    # commands  path -------
    raptrun = "raptrun"
    platform = "raptvirtus"
    data_path = "/mnt/rapt/tensorflow-UI/"
    #data_path = "/home/ubuntu/tensorflow-UI/"
    tf = "tensorflow"
    #------- mnist application--------
    app_mnist = "mnist"
    # ------- pgan application--------
    app_pgan = "pggan"
    # ------- image application--------
    app_image = "flower_classification"

    type1 = "rapt"
    location = "local"
    s3location = "s3bucket"
    nfslocation = "nfs"
    mode_manual = "manual"
    mode_auto = "auto"
    # local path for mnist

    mnist_gpu = "/tensorflow/training/Mnist_classification/mnist_gpu.py"
    mnist_deep = "/tensorflow/training/Mnist_classification/mnist_deep.py"
    #  path for pgan
    pgan_train = "/tensorflow/training/pgan/train.py"
    pgan_config = "/tensorflow/training/pgan/config.py"
    # local path for imageclassification
    image_train = "/tensorflow/training/flower_classification/retrain-new.py"
    model_dir = "/tensorflow/inception"
    image_dir = "/tensorflow/datasets/flower_photos4.5GB"
    bottleneck = "/tensorflow/datasets/bottlenecks4.5GB-new"
    steps = "50"
    #local_image_clf_train = "python -u /tensorflow/training/flower_classification/retrain-new.py  --model_dir=/tensorflow/inception --image_dir /tensorflow/datasets/flower_photos4.5GB --bottleneck_dir=/tensorflow/datasets/bottlenecks4.5GB-new --how_many_training_steps 50"

    # -------------NFS ----------------
    nfs_ip = '54.70.64.175'
    nfs_path = "/home/ubuntu/tensorflow-UI"
    nfsdata_path = "/home/ubuntu/tensorflow-UI/"
    nfs_mnist_gpu = "/tensorflow/training/Mnist_classification/mnist_gpu.py"
    nfs_mnist_deep = "/tensorflow/training/Mnist_classification/mnist_deep.py"
    nfs_pgan_config = "/tensorflow/training/pgan/config.py"
    nfs_pgan_train = "/tensorflow/training/pgan/train.py"
    nfs_image_train = "/tensorflow/training/flower_classification/retrain-new.py"
    nfs_model_dir = "/tensorflow/inception"
    nfs_image_dir = "/tensorflow/datasets/flower_photos4.5GB"
    nfs_bottleneck = "/tensorflow/datasets/bottlenecks4.5GB-new"

    #nfs_image_clf_train = "python -u /tensorflow/training/flower_classification/retrain-new.py --model_dir=/tensorflow/inception --image_dir /tensorflow/datasets/flower_photos4.5GB --bottleneck_dir=/tensorflow/datasets/bottlenecks4.5GB-new --how_many_training_steps 50"

    # ---------S3 bucket ---------
    s3data_path = "/s3bucket/rapt"
    bucket_name = "rapt-data-bucket"
    bucket_keys = "AKIAITOV7UZRONOPBIHA:PmlQsH2tg7+7jexDMPzN0VGat/9VPa6BIapcAPYe"
    s3_mnist_gpu = "/tensorflow/training/Mnist_classification/mnist_gpu.py"
    s3_mnist_deep = "/tensorflow/training/Mnist_classification/mnist_deep.py"
    s3_pgan_config = "/tensorflow/training/pgan/config.py"
    s3_pgan_train = "/tensorflow/training/pgan/train.py"
    s3_image_train = "/tensorflow/training/flower_classification/retrain-new.py"
    s3_model_dir = "/tensorflow/inception"
    s3_image_dir = "/tensorflow/datasets/flower_photos"
    s3_bottleneck = "/tensorflow/datasets/bottlenecks-new"

    #s3_image_clf_train = "python -u /tensorflow/training/flower_classification/retrain-new.py --model_dir=/tensorflow/inception --image_dir /tensorflow/datasets/flower_photos --bottleneck_dir=/tensorflow/datasets/bottlenecks-new --how_many_training_steps 50"



