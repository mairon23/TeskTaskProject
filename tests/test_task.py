import allure
from pages.main_page import YandexMainPage
from pages.image_page import YandexImagePage
from data.test_data import AttributesValues


@allure.title("Search in Yandex")
@allure.severity("normal")
def test_search_in_yandex(driver):
    main_page = YandexMainPage(driver)
    assert main_page.check_search_field()

    main_page.send_in_search_field()
    assert main_page.check_prompt_table()

    main_page.press_enter()
    assert main_page.check_first_link()


@allure.title("Images in Yandex")
@allure.severity("normal")
def test_images_in_yandex(driver):
    image_page = YandexImagePage(driver)
    assert image_page.check_image_button()

    image_page.click_image_button()
    image_page.switch_to_new_tab()
    assert image_page.check_url()

    image_page.get_grid_text_first_unit_images()
    image_page.open_first_unit_images()
    image_page.get_value_search_line()
    assert image_page.comparison_attributes_image(AttributesValues.first_unit_images,
                                                  AttributesValues.search_line)

    image_page.open_first_image()
    assert image_page.check_first_image_visible()

    image_page.click_next_image()
    assert image_page.check_second_image_opened()

    assert not image_page.check_identically_image(AttributesValues.first_image_link,
                                                  AttributesValues.second_image_link)

    image_page.click_previous_image()
    assert image_page.check_identically_image(image_page.get_link_new_image(),
                                              AttributesValues.first_image_link)
