from selenium.webdriver.common.by import By
from Base_App import selenium_API


class yandex_start_page_locators(object):
    yandex_start_page_url = "https://ya.ru/"
    button_account = (By.XPATH, ".//a[text() ='Войти']")
    button_type_change_autorization = (By.XPATH, ".//button/span[text() = 'Почта']")
    button_close_message = (By.XPATH, ".//button[@class = 'simple-popup__close']")
    button_go_in_service = (By.XPATH, ".//* [contains(@d, 'M10 18c0-1.864 0-2.796.305')]/../../..")


class yandex_actions_start_page(selenium_API):
    

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def go_to_autorization(self):
        self.driver_get_url(yandex_start_page_locators.yandex_start_page_url)
        self.driver_click(yandex_start_page_locators.button_account)
        self.driver_move_click(yandex_start_page_locators.button_type_change_autorization)
        
    def go_to_yandex_service(self):
        try:
            self.driver_click(yandex_start_page_locators.button_close_message)
        except:
            pass
        self.driver_click(yandex_start_page_locators.button_go_in_service)
        descriptors = self.driver_return_current_descriptors()
        self.driver_switch_descriptor(descriptors[1])


