
__author___ = "idur"

class Locators(object):

    # ---------Registration----------------

    name = "//input[@name='name']"
    username = "//input[@name='username']"
    email = "//input[@name='email']"
    password1 = "//input[@name='password']"
    confpass = "//input[@name='password2']"
    #register = "//button[@class='btn btn-primary']"



    adminusername = "//input[@name='username']"
    password = "//input[@name='password']"
    submit = "//button[@class='btn btn-primary']"

    fimg = "//img[@src='/images/tenserflow.png']"
    #model = "(//div[@class='card border border-primary'])[0]"
    inception = "//div[@class='card-body text-center font-weight-normal btnNext']"

    s3 = "//input[@id='r1']"
    bktname = "//input[@id='bkt_name']"
    bktkeys = "//input[@id='bkt_keys']"

    nfs = "//input[@id='r2']"
    nfs_sysip = "//input[@id='ds_ip']"
    nfs_path = "//input[@id='ds_dirpath']"

    localfolder = "//input[@id='r100']"
    setlocalpath = "//input[@id='local_dir_path']"
    gpu = "//input[@id='r4']"
    auto = "//input[@id='r101']"
    manual = "//input[@id='r102']"
    memoryper = "//input[@id='gpupercent0']"
    #gpu1 = "//input[@id='gpupercent1']"
    coreper = "//input[@id='gpuvalue0']"
    setupbtn = "//button[@id='setupbtn']"
    #setup = "//button[@class='btn btn-success font-weight-bold text-white btnNext']"

    #datasettrain = "//button[@class='btn btn-success mb-4']"

    train = "//a[@href='#train']"
    Trainbtn = "//button[@id='train_id']"

    checkbox = "//div[@class='screen_buttons']"

    logoutlink = "//a[@id='navbarDropdownMenuLink']"
    logout = "//a[@class='dropdown-item ']"

