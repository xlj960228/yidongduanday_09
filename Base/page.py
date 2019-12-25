from Page.mobilePage import MobilePage
from Page.morePage import MorePage
from Page.settingPage import SettingPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_setting_page(self):
        """返回页面设置的实例化对象"""
        return SettingPage(self.driver)

    def get_more_page(self):
        """返回更多页面实例化对象"""
        return MorePage(self.driver)

    def get_mobile_page(self):
        """返回移动网络页面实例化对象"""
        return MobilePage(self.driver)
