from pages.yandex_start_page import yandex_actions_start_page
from pages.yandex_autorization_page import yandex_actions_autorization_page
from pages.yandex_service_page import yandex_actions_service_page
from pages.yandex_disk_page import yandex_actions_disk_page
from pages.yandex_read_file_page import yandex_actions_read_file_page


def test_download_file_yandex_disk(driver, keys, download_path_file):
    # инициализирую экземпляры классов
    yandex_main_page = yandex_actions_start_page(driver)
    yandex_autorization_page = yandex_actions_autorization_page(driver)
    yandex_service_page = yandex_actions_service_page(driver)
    yandex_disk_page = yandex_actions_disk_page(driver)
    yandex_read_file_page = yandex_actions_read_file_page(driver)

    # действия теста
    yandex_main_page.go_to_autorization()
    yandex_autorization_page.autorization(keys)
    yandex_main_page.go_to_yandex_service()
    yandex_service_page.go_to_disk_menu()
    yandex_disk_page.create_directory(download_path_file[1])
    yandex_disk_page.download_file(download_path_file[0])
    text_to_be_checked = yandex_read_file_page.read_file_one_string()

    with open(download_path_file[0], "r", encoding = "utf-8") as file:
        correct_text = file.read()

    # проверочное условие
    assert text_to_be_checked == correct_text 
    yandex_disk_page.log_out()



