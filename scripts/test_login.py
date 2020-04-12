import time
import pytest

from base.base_analyse import analyse_data
from base.base_driver import init_driver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.reg_page import RegPage


class TestLogin:
    def setup(self):
        # 实例化driver
        self.driver = init_driver()
        self.home_page = HomePage(self.driver)
        self.reg_page = RegPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyse_data("login_data", "test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        self.home_page.click_close()
        self.home_page.click_me()

        self.reg_page.click_login()

        self.login_page.input_username(username)
        time.sleep(1)
        self.login_page.input_password(password)
        self.login_page.click_login()

        if toast is None:
            # toast为空，登录成功，验证用户名
            pass
        else:
            self.login_page.is_toast_exit(toast)
