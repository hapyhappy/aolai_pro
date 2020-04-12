import time
import pytest

from base.base_analyse import analyse_data
from base.base_driver import init_driver


class TestLogin:
    def setup(self):
        # 实例化driver
        self.driver = init_driver()


    def teardown(self):
        time.sleep(2)
        self.driver.quit()
    def test_login(self):
        print("123")