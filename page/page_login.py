from selenium.webdriver.common.by import By

from action.action import BaseAction
import logging

class PageLogin(BaseAction):

    def __init__(self,driver):
        super().__init__(driver)
        logging.info("传入driver对象到BaseAction类")
        self.loginName = By.XPATH, '//*[@name="username"]'
        self.loginPwd = By.XPATH, '//*[@name="password"]'
        self.clicklogin = By.XPATH,'//button[@class="btn btn-primary login-btn w100per"]'


class ProxyLogin(PageLogin):

    def login(self, name, pwd):
        logging.info("登录业务进行中")
        self.input_text(self.loginName, name)
        logging.info("输入用户名成功")
        self.input_text(self.loginPwd, pwd)
        logging.info("输入密码成功")
        self.click_ele(self.clicklogin)
        logging.info("点击登录成功")