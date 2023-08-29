import yaml
import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class setup_driver_service():

    def __init__(self, path_to_config = str) -> None:
        try:
            with open(path_to_config, "r", encoding = "utf-8") as file:
                self.data = yaml.safe_load(file)

        except FileNotFoundError as exc:
            print(f"File not found. Ecxeption: {exc}") 
        except yaml.YAMLError as exc:
            print(f"Error while parsing YAML file: Ecxeption {exc}")


    def setup_driver(self):
        service_web_driver = Service(executable_path = self.data["settings_web_browser"]["path_to_driver"])
        options_web_driver = Options()

        options_web_driver.page_load_strategy = self.data["settings_web_browser"]["page_load_strategy"]
        options_web_driver.add_argument("--disable-blink-features=AutomationControlled")
        options_web_driver.add_argument("--start-maximized")
        options_web_driver.add_experimental_option("excludeSwitches", ['enable-automation'])
        options_web_driver.add_experimental_option('useAutomationExtension', False)     
        return webdriver.Chrome(options = options_web_driver,service = service_web_driver)

    def get_keys(self):
        return (self.data["yandex_API"]["login"], self.data["yandex_API"]["password"])
    
    def get_name(self):
        return (self.data["test_create_file"]["name_file"], self.data["test_create_file"]["name_directory"])
    
    def get_download_file(self):
        path = os.getcwd()
        path = path + self.data["test_donwload_file"]["file_name"]
        return(path, self.data["test_donwload_file"]["name_directory"])

settings_init_driver = setup_driver_service("config.yaml")

@pytest.fixture(scope = "function")
def driver():
    driver = settings_init_driver.setup_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope = "session")
def keys():
    return settings_init_driver.get_keys()

@pytest.fixture(scope = "session")
def name():
    return settings_init_driver.get_name()

@pytest.fixture(scope = "session")
def download_path_file():
    return settings_init_driver.get_download_file()