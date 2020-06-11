from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
from action.action import BaseAction


class GetToast(BaseAction):
    def __init__(self,driver):
        super(GetToast, self).__init__(driver)
        self.__toast = By.XPATH, '//*[@id="App"]/div/div[1]/div/span'
        self.__toast_box = By.XPATH, '//*[@id="App"]/div/div[2]/div[2]/div[2]/div/div/div[1]/p'
    def get_toast_msg(self):
        logging.info("调用get_toast_msg方法获取断言中")
        try:
            msg = self.find_element(self.__toast).text
            logging.info("根据toast路径获取登录结果成功, 登录结果为：%s"%msg)
            return msg
        except NoSuchElementException :
            msg = self.find_element(self.__toast_box).text
            logging.info("根据弹窗提示语获取登录结果成功, 登录结果为：%s"%msg)
            return msg