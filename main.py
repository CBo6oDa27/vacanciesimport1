from api import HeadHunterAPI
from vacancystorage import JSONVacancyStorage
from vacancy import Vacancy
import json


def show_sorted_vacancies(top=None):
    # Прочитаем данные из JSON файла
    with open('hh.json') as file:
        data = json.load(file)

    # Отсортируем список по полю "salary_from"
    sorted_data = sorted(data, key=lambda x: x['salary_from'], reverse=True)

    # Выведите отсортированный список
    if top is None:
        for item in sorted_data:
            vacancy_to_show = Vacancy(item["title"], item["url"], item["salary_from"], item["salary_to"], item["currency"], item["requirement"])
            print(vacancy_to_show)
    else:
        for item in sorted_data[:top]:
            vacancy_to_show = Vacancy(item["title"], item["url"], item["salary_from"], item["salary_to"],
                                      item["currency"], item["requirement"])
            print(vacancy_to_show)

def user_interaction():

    while True:
        keyword = input('Введите вакансию для поиска (ключевое слово, на пример python):')

        # Создание экземпляра класса для работы с API сайтов с вакансиями
        hh_api = HeadHunterAPI()

        # Получение вакансий с hh.ru в формате JSON
        hh_vacancies = hh_api.get_vacancies(keyword)

        VacancyStorage = JSONVacancyStorage('hh.json')
        VacancyStorage.save_to_json(hh_vacancies)

        what_to_print = input('''Что вывести (укажите только цифру)?
                                1. Все найденные вакансии.
                                2. Топ вакансий.
                                ''')

        if int(what_to_print) == 2:
            top = input('Сколько вакансий вывести?')
            show_sorted_vacancies(int(top))
        else:
            show_sorted_vacancies()

        user_choice = input("Продолжить работу (введите только цифру)?\n 1. Да\n 2. Нет")

        if int(user_choice) == 2:
            break


if __name__ == "__main__":
    user_interaction()