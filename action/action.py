from selenium.webdriver.common.keys import Keys


class BaseAction():

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature):
        feature_by, feature_path = feature
        ele = self.driver.find_element(feature_by,feature_path)
        return ele

    def click_ele(self, feature):
        self.find_element(feature).click()

    def input_text(self, feature, text):
        self.find_element(feature).send_keys(text)

    def clear_inputBox(self, feature):
        self.select_all(feature)
        self.input_text(feature, Keys.BACKSPACE)

    def select_all(self, feature):
        command = Keys.CONTROL, "a"
        self.input_text(feature, command)

    def screen_shot(self, filename):
        self.driver.get_screenshot_as_file(filename)

