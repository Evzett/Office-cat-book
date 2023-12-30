import sys


class FinishJob(Exception):
    """собственное исключение для завершения
    работы анимации"""


class NoTrueType(Exception):
    """собственное исключение для проверки на корректность
    введенных данных"""


class NoTrueTime(Exception):
    """собственное исключение для проверки
    на корректность введенных данных"""


class NoTrueHourlyRate(Exception):
    """собственное исключение для проверки
    на корректность введенных данных"""


class NoTruePosition(Exception):
    """собственное исключение для проверки
    на корректность введенных данных"""


class NoTrueJob(Exception):
    """собственное исключение для проверки
    на корректность введенных данных"""


class Check:
    @staticmethod
    def check(age, name, surname):
        """Функция проверки на корректность данных:
        имени, возраста и фамилии"""
        try:
            if name.isalpha() and surname.isalpha() and age.isdigit() and  14 <= int(age) <= 90:
                return True

            raise NoTrueType
        except NoTrueType:
            print(
                "Данные должны быть настоящими, предусмотрите то, \
что официально можно работать только с 14 лет"
            )
            return None
    @staticmethod
    def check_salary(salary):
        if salary.isdigit():
            return True
        else:
            return False
    @staticmethod
    def check_position_answer(ans):
        try:
            status = {
                "базовый": "base",
                "почасовой": "hourly",
                "наемный": "salaried",
                "менеджер": "manage",
                "главный менеджер": "head_manage",
                "руководитель": "head_manage",
            }
            if ans in status.keys():
                return True
            raise NoTruePosition
        except NoTruePosition:
            print("Такой позиции не существует в данной компании")
        return False

    @staticmethod
    def check_time(tim):
        """Функция проверки на корректность данных:
        времени и почасовой ставки"""
        try:
            if tim.isdigit():
                if 0 < int(tim) <= 10:
                    return True
            raise NoTrueTime
        except NoTrueTime:
            print("В нашей компании рабочая смена не может превышать 10 часов")
            return None

    @staticmethod
    def check_hourly_rate(hourly_rate):
        try:
            if hourly_rate.isdigit():
                if 10 < int(hourly_rate) < 500:
                    return True
            raise NoTrueHourlyRate
        except NoTrueHourlyRate:
            print("Почасовая ставка должна быть в пределах от 10 до 500")
            return None

    @staticmethod
    def chek_base(bas: list):
        """Функция проверки на существование списка(было проще сделать от
        дельную функцию"""
        if not bas:
            return False

        return True

    @staticmethod
    def check_index(ind):
        try:
            if ind < 0:
                raise ValueError
            else:
                return True
        except ValueError:
            print("Неккоректный индекс элемента")

    @staticmethod
    def mod_input():
        """Модифицированный инпут"""
        answer = input()
        if answer == "exit":
            print("Работа завершена")
            sys.exit()
        return answer
