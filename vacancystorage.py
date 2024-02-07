from abc import ABC, abstractmethod
import json


class VacancyStorage(ABC):
    """Абстрактный класс для работы с вакансиями (сохранение и удаление из файла)"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass

    @abstractmethod
    def save_to_json(self, vacancies):
        pass


class JSONVacancyStorage(VacancyStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        with open(self.file_path, 'a') as file:
            json.dump(vacancy, file)
            file.write('\n')

    def get_vacancies(self, criteria):
        with open(self.file_path, 'r') as file:
            vacancies = []
            for line in file:
                vacancy = json.loads(line)
                # Применить критерии фильтрации и добавить в список vacancies
                # вакансии, удовлетворяющие указанным критериям
            return vacancies

    def delete_vacancy(self, vacancy_id):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        with open(self.file_path, 'w') as file:
            for line in lines:
                vacancy = json.loads(line)
                if vacancy['id'] != vacancy_id:
                    file.write(line)

    def save_to_json(self, headhunter_data):
        my_list = []
        for item in headhunter_data['items']:
            if item['snippet']['requirement'] is None:
                item['snippet']['requirement'] = ""

            if item['salary'] is None:
                salary_from = 0
                salary_to = 0
                salary_currency = ""
            else:
                salary_from = item['salary']['from']
                salary_to = item['salary']['to']
                salary_currency = item['salary']['currency']
            if salary_from == None:
                salary_from = 0
            if salary_to == None:
                salary_to = 0

            data = {
                "title": item['name'],
                "url": "https://hh.ru/vacancy/" + item['id'],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "currency": salary_currency,
                "requirement": item['snippet']['requirement']
            }
            my_list.append(data)

        with open("hh.json", "w", encoding="utf-8") as f:
            json.dump(my_list, f, ensure_ascii=False)
