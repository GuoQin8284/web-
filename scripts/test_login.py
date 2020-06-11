import logging
import os
import time
import unittest

from parameterized import parameterized

from action.analysis import analysis_data
from config import BASE_DIR
from driver.driver import webDriver
from driver.get_toast import GetToast
from page.page_login import ProxyLogin


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webDriver()
        self.login = ProxyLogin(self.driver)
        self.getToast = GetToast(self.driver)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    @parameterized.expand(analysis_data("login.json"))
    def test_login(self, item):
        name = item["name"]
        pwd = item["pwd"]
        expect = item["expect"]
        url = "https://author.osid.org.cn/"
        self.driver.get(url)
        self.login.login(name, pwd)
        filename=BASE_DIR + os.sep+"screenshot"+os.sep+"{}_{}_{}.png".format(time.strftime("%Y-%m-%d %H_%M_%S"), name, pwd)
        self.login.screen_shot(filename)
        logging.info("截图的文件名：",filename)
        logging.info("输入的username：{}，输入的pwd：{}".format(name, pwd))
        self.assertIn(expect, self.getToast.get_toast_msg(),msg="这是断言")
