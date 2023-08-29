from pages.yandex_start_page import yandex_actions_start_page
from pages.yandex_autorization_page import yandex_actions_autorization_page
from pages.yandex_service_page import yandex_actions_service_page
from pages.yandex_disk_page import yandex_actions_disk_page
from pages.yandex_work_file_page import yandex_actions_work_file_page


def test_сreate_file_yandex_disk(driver, keys, name):
   # инициализирую экземпляры классов
   yandex_main_page = yandex_actions_start_page(driver)
   yandex_autorization_page = yandex_actions_autorization_page(driver)
   yandex_service_page = yandex_actions_service_page(driver)
   yandex_disk_page = yandex_actions_disk_page(driver)
   yandex_work_file_page = yandex_actions_work_file_page(driver)

   # действия теста
   yandex_main_page.go_to_autorization()
   yandex_autorization_page.autorization(keys)
   yandex_main_page.go_to_yandex_service()
   yandex_service_page.go_to_disk_menu()
   yandex_disk_page.create_directory(name[1])
   yandex_disk_page.create_file(name[0])
   yandex_work_file_page.open_menu()
   file_name = yandex_disk_page.check_file_name(name[0])
   # Проверочное условие
   assert file_name[:-5] == name[0]
   yandex_disk_page.log_out()

    
    