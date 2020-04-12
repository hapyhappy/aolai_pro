# 创建一个字典，包装相应的启动参数
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = dict()
# 需要连接的手机的平台(不限制大小写)
desired_caps['platformName'] = 'Android'
# 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
desired_caps['platformVersion'] = '5.1'
# 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
desired_caps['deviceName'] = '192.168.56.101:5555'
# 需要启动的程序的包名
desired_caps['appPackage'] = 'com.cyanogenmod.filemanager'
# 需要启动的程序的界面名
desired_caps['appActivity'] = '.activities.NavigationActivity'
# 告诉系统不需要重置
desired_caps['noReset'] = True
# 使用uiautomator2
desired_caps['automationName'] = 'Uiautomator2'
# 解决中文问题
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.press_keycode(4)


def find_toast(driver, message, timeout=3):
    """
    # message: 预期要获取的toast的部分消息
    """
    message = "//*[contains(@text,'" + message + "')]" # 使用包含的方式定位

    element = WebDriverWait(driver, timeout, 0.1).until(lambda x: x.find_element(By.XPATH, message))
    return element.text

print(find_toast(driver, "再次"))