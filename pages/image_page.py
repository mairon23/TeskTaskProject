from selenium.webdriver.remote.webelement import WebElement
from pages.base import BasePageObject
from selenium.webdriver.common.by import By
from data.test_data import Routes, Attributes, AttributesValues


class YandexImagePage(BasePageObject):
    image_button = (By.XPATH, "//div[text()='Картинки']")
    first_unit_in_general_page = (By.XPATH, "//div[@class='PopularRequestList']//div[1]")
    image = (By.XPATH, "//img[@class='MMImage-Origin']")
    switch_image_button = (By.XPATH, "//i[@class='CircleButton-Icon']")

    def check_image_button(self) -> bool:
        """Проверяет наличие кнопки 'Картинки'."""
        return self.visibility_element(self.image_button)

    def click_image_button(self) -> None:
        """Кликает на кнопку 'Картинки'."""
        self.click(self.image_button)

    def switch_to_new_tab(self) -> None:
        """Переключает вебдрайвер на новую вкладку."""
        self.switch_to_new_window()

    def check_url(self) -> bool:
        """Проверяет содержит ли заданныый указатель в фактическом URL."""
        return self.url_comparison(Routes.image_page)

    def get_grid_text_first_unit_images(self) -> None:
        """Получает аттрибут от первого блока картинок."""
        AttributesValues.first_unit_images = self.wait_located(self.first_unit_in_general_page).\
            get_attribute(Attributes.grid_text)

    def open_first_unit_images(self) -> None:
        """Открывает первый блок картинок."""
        self.click(self.first_unit_in_general_page)

    def get_value_search_line(self) -> None:
        """Получает значение value с поисковой строки."""
        search_input = (By.XPATH, "//input[@name='text']")
        AttributesValues.search_line = self.wait_located(search_input).get_attribute(
            Attributes.value)

    @staticmethod
    def comparison_attributes_image(first_attribute: str, second_attribute: str) -> bool:
        """
        Сравнивает два аттрибута.

        :param first_attribute: строка, с записанным первым аттрибутом
        :param second_attribute: строка, с записанным вторым аттрибутом.
        """
        return BasePageObject.compares_attributes(first_attribute, second_attribute)

    def open_first_image(self) -> None:
        """Открывает первую картинку."""
        first_image_second_page = (By.XPATH, "//a[@class='serp-item__link']/img")
        self.click(first_image_second_page)

    def check_first_image_visible(self) -> WebElement:
        """Проверяет присутствие картинки на странице."""
        AttributesValues.first_image_link = self.wait_located(self.image).get_attribute(Attributes.link)
        return self.wait_located(self.image)

    def click_next_image(self) -> None:
        """Нажимает на кнопку вперед."""
        self.find_elements(self.switch_image_button)[3].click()

    def check_second_image_opened(self) -> WebElement:
        """Проверяет наличие картинки, а также записывает ссылку на картинку в dataclass"""
        AttributesValues.second_image_link = self.wait_located(self.image).get_attribute(Attributes.link)
        return self.wait_located(self.image)

    @staticmethod
    def check_difference_image(first_attribute: str, second_attribute: str) -> bool:
        """
        Сравнивает два аттрибута.

        :param first_attribute: строка, с записанным первым аттрибутом
        :param second_attribute: строка, с записанным вторым аттрибутом.
        """
        return BasePageObject.compares_attributes(first_attribute, second_attribute)

    def click_previous_image(self) -> None:
        """Нажимает на кнопку назад."""
        self.find_elements(self.switch_image_button)[0].click()

    def get_link_new_image(self) -> str:
        """Получает link с новой картинки"""
        return self.wait_located(self.image).get_attribute(Attributes.link)

    @staticmethod
    def check_identically_image(first_attribute: str, second_attribute: str) -> bool:
        """
        Сравнивает два аттрибута.

        :param first_attribute: строка, с записанным первым аттрибутом
        :param second_attribute: строка, с записанным вторым аттрибутом.
        """
        return BasePageObject.compares_attributes(first_attribute, second_attribute)
