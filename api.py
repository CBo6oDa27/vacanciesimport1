from abc import ABC, abstractmethod
import requests


class API(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(API):
    """Создание экземпляра класса для работы с API сайтов с вакансиями"""

    def get_vacancies(self, keyword):
        """Выгрузка данных с сайта 'HeadHunter'"""

        headhunter_data = requests.get("https://api.hh.ru/vacancies",
                            params={"text": keyword, "per_page": 100}).json()

        return headhunter_data
