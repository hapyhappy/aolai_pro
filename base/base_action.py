from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10.0, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*feature))

    def click(self, feature, timeout=10.0, poll_frequency=1.0):
        self.find_element(feature, timeout, poll_frequency).click()

    def clear(self, feature, timeout=10.0, poll_frequency=1.0):
        self.find_element(feature, timeout, poll_frequency).clear()

    def input(self, feature, text, timeout=10.0, poll_frequency=1.0):
        self.clear(feature, timeout, poll_frequency)
        self.find_element(feature, timeout, poll_frequency).send_keys(text)

    def get_text(self, feature, timeout=10.0, poll_frequency=1.0):
        return self.find_element(feature, timeout, poll_frequency).text

    def is_toast_exit(self, text, timeout=3.0, poll_frequency=0.1):
        try:
            self.find_element((By.XPATH, "//*[contains(@text,'%s')]" % text), timeout, poll_frequency)
            return True
        except Exception as e:
            return False

    def get_toast_text(self, text, timeout=3.0, poll_frequency=0.1):
        # 获取toast文字
        try:
            element = self.find_element((By.XPATH, "//*[contains(@text,'%s')]" % text), timeout, poll_frequency)
            return element.text
        except Exception as e:
            # 如果toast根本不存在，直接抛出异常
            raise Exception("关键词为%s的toast不存在" % text)
