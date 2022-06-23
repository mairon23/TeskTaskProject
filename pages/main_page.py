from selenium.webdriver import Keys
from pages.base import BasePageObject
from selenium.webdriver.common.by import By
from data.test_data import Search


class YandexMainPage(BasePageObject):
    search_field = (By.ID, "text")

    def check_search_field(self) -> bool:
        """Проверяет наличие поля поиска."""
        return self.visibility_element(self.search_field)

    def send_in_search_field(self) -> None:
        """Вводит в поисковую строку."""
        self.wait_located(self.search_field).send_keys(Search.search_query)

    def check_prompt_table(self) -> bool:
        """Проверяет наличие таблицы с подсказками."""
        hint_table = (By.XPATH, "//ul[@role='listbox']")
        return self.visibility_element(hint_table)

    def press_enter(self) -> None:
        """Имитирует нажатие на кнопку Enter."""
        self.wait_located(self.search_field).send_keys(Keys.ENTER)

    def check_first_link(self) -> bool:
        """Проверяет первую ссылку."""
        first_link = (By.XPATH, "//li[@data-cid='0']//b[text()='tensor.ru']")
        return self.visibility_element(first_link)
