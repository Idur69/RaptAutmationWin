
#from package import config
#from Src.EnvSetup import cnfgurl
from Src.EnvSetup import cnfgurl


class Myurl(object):
    def __init__(self, driver):
        self.driver = driver

    def access_url(self):
        self.driver.get(cnfgurl.URL[cnfgurl.DEFAULT_ENVIRONMENT])
    def registor_url(self):
        self.driver.get(cnfgurl.URL[cnfgurl.REGISTOR_ENVIRONMENT])
    def acces_user(self):
        self.driver.get(cnfgurl.URL[cnfgurl.USER_ENVIRONMENT])

