from selenium.webdriver.common.by import By
from Base_App import selenium_API


class yandex_read_file_page_locators(object):
    first_string_file = (By.XPATH, './/div//p')


class yandex_actions_read_file_page(selenium_API):
    

    def __init__(self, driver) -> None:
        super().__init__(driver)


    def read_file_one_string(self):
        text = self.driver_get_text(yandex_read_file_page_locators.first_string_file)
        descriptors = self.driver_return_current_descriptors()
        self.driver_switch_descriptor(descriptors[1])
        return text
