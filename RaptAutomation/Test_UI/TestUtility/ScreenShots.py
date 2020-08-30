

class SS(object):

    def __init__(self,driver):
        self.driver = driver
    def ScreenShot(self,path):
        directory = r"C:\Users\Idur\PycharmProjects\RaptAutomation\ScreenShots"
        self.driver.get_screenshot_as_file(directory+path)