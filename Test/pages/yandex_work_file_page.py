from selenium.webdriver.common.by import By
from Base_App import selenium_API


class yandex_work_file_page_locators(object):
    iframe = ("frameEditor")
    button_open_menu = (By.XPATH, ".//ul/li/a[text() = 'Файл']/..")


class yandex_actions_work_file_page(selenium_API):
    

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open_menu(self):
        descriptors = self.driver_return_current_descriptors()
        self.driver_switch_descriptor(descriptors[2])
        self.driver_switch_iframe(yandex_work_file_page_locators.iframe)
        self.driver_descriptor_close()
        self.driver_switch_descriptor(descriptors[1])


        

