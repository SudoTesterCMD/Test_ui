from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class selenium_API(object):


    def __init__(self, driver) -> None:
        self.driver = driver
        self.time = 15


    def driver_get_url(self, url = None):
        return self.driver.get(url)
    
    def driver_find(self, locator = None):
        return WebDriverWait(self.driver, self.time).until(
                             EC.presence_of_element_located((locator)))
    
    def driver_click(self, locator = None):
        return WebDriverWait(self.driver, self.time).until(
                             EC.element_to_be_clickable((locator))).click()
    
    def driver_move_click(self, locator = None):
        return ActionChains(self.driver).move_to_element(
                            self.driver_find(locator)).click().perform()
    
    def driver_double_click(self, locator = None):
        return ActionChains(self.driver).double_click(
                            self.driver_find(locator)).perform()
    
    def driver_send_keys(self, locator = None, data = None):
        return self.driver_find(locator).send_keys(data)
    
    def driver_return_current_descriptor(self):
        return self.driver.current_window_handle
    
    def driver_return_current_descriptors(self):
        return self.driver.window_handles
    
    def driver_switch_descriptor(self, name_window = None):
        return self.driver.switch_to.window(name_window)
    
    def driver_descriptor_close(self):
        return self.driver.close()
    
    def driver_switch_iframe(self, frame_name  = None):
        return self.driver.switch_to.frame(frame_name)
    
    def driver_element_clear(self, locator = None):
        return self.driver_find(locator).clear()

    def driver_element_clear_optional(self, locator = None):
        return  self.driver_find(locator).send_keys(
                                 Keys.CONTROL + 'a', Keys.BACKSPACE)
    
    def driver_return_url(self):
        return self.driver.current_url
    
    def driver_get_text(self, locator = None):
        return self.driver_find(locator).text
    
    def driver_quit(self):
        return self.driver.quit()