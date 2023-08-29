from selenium.webdriver.common.by import By
from Base_App import selenium_API


class yandex_service_page_locators(object):
    button_disk_menu = (By.XPATH, ".//div//*[text() = 'Диск']")


class yandex_actions_service_page(selenium_API):


    def __init__(self, driver) -> None:
        super().__init__(driver)

    def go_to_disk_menu(self):
        self.driver_click(yandex_service_page_locators.button_disk_menu)
