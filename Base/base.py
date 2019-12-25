from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def search_ele(self, loc, timeout=5, poll_frequency=1):
        """
        定位单个元素
        :param loc: 元组(By.ID,属性) (By.CLASS_NAME,属性值)(By.XPATH,属性值)
        :param timeout: 等待的时间
        :param poll_frequency:  搜索间隔时间
        :return:定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll_frequency=1):
        """
        定位一组元素
        :param loc: 元组(By.ID,属性) (By.CLASS_NAME,属性值)(By.XPATH,属性值)
        :param timeout: 等待的时间
        :param poll_frequency:  搜索间隔时间
        :return:定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll_frequency=1):
        self.search_ele(loc, timeout, poll_frequency).click()

    def send_ele(self, loc, text, timeout=5, poll_frequency=1):
        # 定位元素
        input_text = self.search_ele(loc, timeout, poll_frequency)
        # 清空元素
        input_text.clear()
        # 输入文本
        input_text.send_keys(text)


if __name__ == '__main__':
    # 实例化Base
    base = Base()
    # 搜索按钮
    search_btn = (By.ID, "com.android.settings:id/search")
    # 输入框
    search_input = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result = (By.ID, "com.android.settings:id/title")
    # 点击搜索按钮
    base.click_ele(search_btn)
    # 输入搜索内容  1
    base.send_ele(search_input, "1")

    # 打印搜索结果
    result = base.search_ele(search_result)
