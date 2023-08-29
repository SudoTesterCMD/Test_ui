from selenium.webdriver.common.by import By
from Base_App import selenium_API


class yandex_disk_page_locators(object):
    button_choise_disk_function_create = (By.XPATH, ".//button/span[text() = 'Создать']")
    button_choise_type_file = (By.XPATH, ".//button/span[text() ='Текстовый документ']")
    button_choise_name_file = (By.XPATH, ".//span/input[@value ='Новый документ']")
    button_choise_type_directory = (By.XPATH, ".//button/span[text() ='Папку']")
    button_choise_name_directory = (By.XPATH, ".//div[@class = 'dialog__wrap']//span/input")
    button_confim_create_button_file = (By.XPATH, ".//div/button/span[text() = 'Создать']") #
    button_download_file = (By.XPATH, ".//div//span[text() = 'Загрузить']//input[@type = 'file']")
    button_confim_create_button_directory = (By.XPATH, ".//div/button/span[text() = 'Сохранить']")
    button_directory = lambda name : (By.XPATH, f".//div[@class = 'listing__items']//span[text() = '{name}']")
    confim_create_directory = lambda name : (By.XPATH, f".//div/h1/div[text() = '{name}']")
    name_file = lambda name : (By.XPATH, f".//div[@class = 'listing-item__info']//span[text() = '{name}.docx']")
    button_menu = (By.XPATH, ".//img[@class = 'user-pic__image']")
    button_log_out = (By.XPATH, ".//a/span[text() = 'Выйти']")
    button_go_in_file = lambda name : (By.XPATH, f".//*[contains(@class, 'listing listing_with-mouse-selection listing')]//span[text() = '{name}']")
    button_close_selection = (By.XPATH, ".//div/button[@aria-label = 'Отменить выделение']")
    


class yandex_actions_disk_page(selenium_API):


    def __init__(self, driver) -> None:
        super().__init__(driver)


    def create_directory(self, directory_name: None):
        self.driver_move_click(yandex_disk_page_locators.button_choise_disk_function_create)
        self.driver_click(yandex_disk_page_locators.button_choise_type_directory)
        self.driver_element_clear_optional(yandex_disk_page_locators.button_choise_name_directory)
        self.driver_send_keys(yandex_disk_page_locators.button_choise_name_directory, directory_name)
        self.driver_move_click(yandex_disk_page_locators.button_confim_create_button_directory)
        self.driver_double_click(yandex_disk_page_locators.button_directory(directory_name))
        self.driver_find(yandex_disk_page_locators.confim_create_directory(directory_name))
        
    def create_file(self, file_name: None):
        self.driver_move_click(yandex_disk_page_locators.button_choise_disk_function_create)
        self.driver_click(yandex_disk_page_locators.button_choise_type_file)
        self.driver_element_clear_optional(yandex_disk_page_locators.button_choise_name_directory)
        self.driver_send_keys(yandex_disk_page_locators.button_choise_name_directory, file_name)
        self.driver_move_click(yandex_disk_page_locators.button_confim_create_button_file)

    def download_file(self, file_path : None):
        file_name = file_path[file_path.rfind("\\")+1:]
        self.driver_send_keys(yandex_disk_page_locators.button_download_file, file_path)
        self.driver_double_click(yandex_disk_page_locators.button_go_in_file(file_name))
        descriptors = self.driver_return_current_descriptors()
        self.driver_switch_descriptor(descriptors[2])
        
    def check_file_name(self, file_name) -> str:
        return self.driver_get_text(yandex_disk_page_locators.name_file(file_name))
        
    def log_out(self):
        try:
            self.driver_click(yandex_disk_page_locators.button_close_selection)
        except:
            pass
        self.driver_move_click(yandex_disk_page_locators.button_menu)
        self.driver_click(yandex_disk_page_locators.button_log_out)

    
        
