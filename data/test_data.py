from dataclasses import dataclass


@dataclass
class Routes:
    main_page: str = "https://yandex.ru/"
    image_page: str = "https://yandex.ru/images/"


@dataclass
class Search:
    search_query: str = "Тензор"


@dataclass
class Attributes:
    grid_text: str = "data-grid-text"
    value: str = "value"
    link: str = "src"


@dataclass
class AttributesValues:
    first_image_link: str
    second_image_link: str
    first_unit_images: str
    search_line: str
