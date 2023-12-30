from controlsystem.check import *


class BaseWorker:
    """класс базового сотрудника"""

    def __init__(self, age, name: str, surname: str, position="base"):
        self.salary = None
        self.current_work = None
        self.position = position
        self.surname = surname
        self.name = name
        self.age = age


    def __str__(self):
        if self.current_work is None:
            return f"Имя: {self.name}, фамилия: {self.surname},\
возраст: {self.age}, должность: {self.position}, пока нет работы"
        return f"Имя: {self.name}, фамилия: {self.surname},\
возраст: {self.age}, должность: {self.position}, текущая работа: [{self.current_work}]"


class HourlyWorker(BaseWorker):
    """класс почасового работника"""

    def __init__(self, age, name, surname, position="hourly"):
        super().__init__(age, name, surname)
        self.salary = None
        self.current_work = None
        self.position = position

    def set_work(self, obj_work):
        try:
            if obj_work.position == "hourly":
                self.current_work = obj_work
                self.salary = obj_work.salary

                return True
            else:
                return False
        except NoTrueJob:
            print("Работа не была назначена, тк выбран не тот тип работы")
            return False


class SalariedEmployee(BaseWorker):
    """класс наемного работника"""

    def __init__(self, age, name, surname, position="salaried"):
        super().__init__(age, name, surname)
        self.salary = None
        self.current_work = None
        self.position = position

    def set_work(self, obj_work):
        try:
            if obj_work.position == "salaried":
                self.current_work = obj_work
                self.salary = obj_work.salary

                return True
            else:
                return False
        except NoTrueJob:
            print("Работа не была назначена, тк выбран не тот тип работы")
            return False


class Manager(BaseWorker):
    """класс менеджера"""

    def __init__(self, age, name, surname, position="manage"):
        super().__init__(age, name, surname)
        self.salary = None
        self.current_work = None
        self.position = position

    def set_work(self, obj_work):
        try:
            if obj_work.position == "manage":
                self.current_work = obj_work
                self.salary = obj_work.salary

                return True
            else:
                return False
        except NoTrueJob:
            print("Работа не была назначена, тк выбран не тот тип работы")
            return False


class HeadManager(Manager):
    """класс главного менеджера"""

    def __init__(self, age, name, surname, position="head_manage"):
        super().__init__(age, name, surname)
        self.salary = None
        self.current_work = None
        self.position = position

    def set_work(self, obj_work):
        try:
            if obj_work.position == "head_manage":
                self.current_work = obj_work
                self.salary = obj_work.salary
                return True
            else:
                return False
        except NoTrueJob:
            print("Работа не была назначена, тк выбран не тот тип работы")
            return False
