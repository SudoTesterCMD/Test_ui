from selenium.webdriver.common.by import By
from Base_App import selenium_API


class yandex_autorization_page_locators(object):
    login_button = (By.XPATH, ".//span//input[@id = 'passp-field-login'][@name = 'login']")
    password_button = (By.XPATH, ".//span//input[@id = 'passp-field-passwd']")
    confim_button = (By.XPATH, ".//button[@id = 'passp:sign-in']")


class yandex_actions_autorization_page(selenium_API):
    

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def autorization(self, keys : list):
        self.driver_send_keys(yandex_autorization_page_locators.login_button, keys[0])
        self.driver_click(yandex_autorization_page_locators.confim_button)
        self.driver_send_keys(yandex_autorization_page_locators.password_button, keys[1])
        self.driver_click(yandex_autorization_page_locators.confim_button)

