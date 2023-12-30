from controlsystem.check import *
from controlsystem.mmm import *
import threading


class BaseJob:
    """класс зп для базового сотрудника"""

    salary = 30000

    def __init__(self, name, salary=30000, position="base"):
        self.position = position
        self.name = name
        self.salary = salary

    def set_salary(self, new_salary):
        """метод установления зарплаты сотрудника"""
        self.salary = new_salary

    def __str__(self):
        return f"Наименование вакансии: {self.name}, зп: {self.salary}, тип работы: {self.position}."


class HourlyJob(BaseJob):
    """класс работы для почасового работника"""

    def __init__(
        self, name: str, hourly_rate, time_work, salary=0, position="hourly"
    ):
        super().__init__(name, salary)
        self.position = position
        self.hourly_rate = hourly_rate
        self.time = time_work

    def finish_job(self):
        """метод выполнения почасовой работы с анимацией загрузки"""
        now = time.time()
        animate(self.time)
        try:
            sys.stdout.write("\rХотите досрочно завершить работу?")
            answer = input()
            if answer == "да":
                raise FinishJob
            animate(self.time)
            sys.stdout.write("\rРабота завершена!\n")
            self.salary = self.hourly_rate * self.time
            sys.stdout.write(f"Вы заработали: {self.salary}\n")
            return self.salary
        except FinishJob:
            end = time.time()
            sys.stdout.write("\rРабота завершена досрочно.\n")
            self.salary = abs(round(now - end) * self.hourly_rate)
            sys.stdout.write(f"Вы заработали: {self.salary}\n")
            return self.salary

    def stop_finish_job(self):
        """Метод для остановки выполнения почасовой работы"""
        process = threading.Thread(target=self.finish_job)
        animate(self.time)
        process.start()
        time.sleep(self.time * 1.1)
        return self.salary

    def set_salary(self, new_hourly_rate, new_time):
        self.hourly_rate = new_hourly_rate
        self.time = new_time
        self.salary = new_hourly_rate * new_time

    def __str__(self):
        return f"Наименование вакансии: {self.name}, почасовая ставка: {self.hourly_rate}, \
время отработки: {self.time}."


class HiredJob(BaseJob):
    """класс работы для наемного сотрудника"""

    salary = 25000

    def __init__(self, name, salary=25000, position="salaried"):
        super().__init__(name, salary)
        self.position = position


class ManagerJob(BaseJob):
    """класс работы для менеджера"""

    salary = 40000

    def __init__(self, name, salary=40000, position="manage"):
        super().__init__(name, salary)
        self.position = position


class HeadManagerJob(ManagerJob):
    def __init__(self, name, salary=60000, position="head_manage"):
        super().__init__(name, salary)
        self.position = position
