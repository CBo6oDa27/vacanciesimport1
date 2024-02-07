class Vacancy():
    """Класс для работы с вакансиями (сравнение, вывод на печать)"""
    def __init__(self, title, url, salary_from, salary_to, currency, requirement):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.requirement = requirement

    def __str__(self):
        if  self.salary_from == 0 and self.salary_to == 0:
            currency = "Зарплата не указана"
        else:
            currency = self.currency
        if self.salary_from == 0:
            salary_from = ""
        else:
            salary_from = "от " + str(self.salary_from)
        if self.salary_to == 0:
            salary_to = ""
        else:
            salary_to = " до " + str(self.salary_to)

        return f'{self.title} ({self.url}) {salary_from}{salary_to} {currency}'

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from
