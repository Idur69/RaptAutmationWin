import pickle
from time import sleep

from Src.EnvSetup.EnvironmentSetUp import EnvironmentSetup
#from Src.EnvSetup.cnfgurl import EnvironmentSetup, LoginUsers
from Src.EnvSetup.cnfgurl import LoginUsers
from Src.PageObject.Pages.Admin_Login import AdminLogin
from Src.PageObject.Pages.MyUrl import Myurl


class Rapt_Ui_AdminLogin(EnvironmentSetup):

    def test_admin_Login(self):
        driver1 = self.driver1
        myurl = Myurl(self.driver1)
        myurl.access_url()
        print("myurl ", myurl.acces_user())
        driver1.implicitly_wait(10)
        print("This is Title name :", driver1.title)

        # ------- Login Details ------------
        user = LoginUsers()
        Admin = user.user1_name
        Pwd = user.user1_password
        expadmin = user.user1_expadmin
        exppass = user.user1_exppass

        admin_login = AdminLogin(driver1)
        admin_login.set_login_uname(Admin)
        admin_login.set_login_upass(Pwd)
        sleep(3)
        #sub = self.driver1.find_element_by_tag_name("button")
        #sub.click()
        #setcookie = pickle.dump(self.driver1.get_cookies(), open("cookies.pkl", "wb"))
        #print("setcookievalue :", setcookie)
        admin_login.submit_login(Admin,Pwd)
        sleep(10)

        if Admin == expadmin and Pwd == exppass:
            print("Login successful")
        else:
            assert print("Invalid credentials")
