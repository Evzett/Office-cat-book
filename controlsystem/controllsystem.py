from PyQt5.QtCore import pyqtSignal

from controlsystem.employees import *
from controlsystem.jobs import *
import json
from copy import deepcopy
import os


class ControlSystem:
    """класс системы со всеми сотрудниками"""
    def __init__(self):
        self.employeess = []
        self.jobs = []
        self.button_click = False

    def add_job(self,job_obj):
        self.jobs.append(job_obj)



    def add_employee(self, age, name, surname, position):
        """Добавление сотрудника в бд
        вход: объект класса сотрудник и объект класса работы"""
        position_dict = {
            "почасовой": HourlyWorker,
            "наемный": SalariedEmployee,
            "менеджер": Manager,
            "главный менеджер": HeadManager,
            "руководитель": HeadManager,
        }
        if Check.check_position_answer(position):
            worker = position_dict[position](age, name, surname)
            self.employeess.append(worker)
            return worker

    def dismissal(self, ind):
        """Увольнение сотрудника
        входные данные: индекс"""
        try:
            emp = self.employeess.pop(ind)
            if not emp.current_work is None:
                self.jobs.append(emp.current_work)
            return emp
        except IndexError:
            print("Сотрудника с таким номером не существует")
            return None

    def del_job(self, ind):
        try:
            curr = self.jobs.pop(ind)
            return curr
        except IndexError:
            print("Такой вакансии не существует")
            return None

    def change_position(self, ind, ans):
        """
        входные данные: индекс объекта, находящегося
        в списке self. employeess, ans-до какой должности
        нужно повысить сотрудника"""
        new_age, new_name, new_surname = (
            self.employeess[ind].age,
            self.employeess[ind].name,
            self.employeess[ind].surname,
        )
        self.dismissal(ind)
        worker = self.add_employee(new_age, new_name, new_surname, ans)
        return worker

    def __str__(self):
        """красивый вывод массива с объектами"""
        text = ""
        if Check.chek_base(self.employeess) or Check.chek_base(self.jobs):
            text += "Все текущие сотрудники:\n"
            for number, item in enumerate(self.employeess):
                text += f"{number + 1}.{str(item)}\n"
            if Check.chek_base(self.jobs):
                text += "Все доступные вакансии:\n"
                for position, elem in enumerate(self.jobs):
                    text += f"{position + 1}. {str(elem)}\n"
            else:
                text += "Здесь нет доступных вакансий"
        else:
            text += "Здесь нет сотрудников"
        return text


    def save_json(self):
        """Сохранение в джэйсон файл сотрудников, хранятся только зарегистрированные сотрудники"""
        arr_empl = []
        for elem in self.employeess:
            obj_dict = deepcopy(elem.__dict__)
            if not elem.current_work is None:
                obj_dict["current_work"] = None
                attr_dict = {
                    "name_job": elem.current_work.name,
                    "salary": elem.current_work.salary,
                }
                if elem.current_work.position == "hourly":
                    attr_dict.update(
                        {
                            "hourly_rate": elem.current_work.hourly_rate,
                            "time": elem.current_work.time,
                        }
                    )
                obj_dict.update(attr_dict)
            obj_dict = dict(sorted(obj_dict.items()))
            arr_empl.append(obj_dict)
        arr_jobs=[]
        for elem in self.jobs:
            job_dict=deepcopy(elem.__dict__)
            sort_job_dict=dict(sorted(job_dict.items()))
            arr_jobs.append(sort_job_dict)
        with open("controlsystem_empl.json", "w+", encoding="utf-8") as file:
            json.dump(arr_empl, file, ensure_ascii=False)
        with open("controlsystem_jobs.json", "w+", encoding="utf-8") as file_j:
            json.dump(arr_jobs, file_j, ensure_ascii=False)

    def load_json(self):
        """Чтение с джэйсон файла, хранятся только зарегистрированные сотрудники"""
        if os.stat("controlsystem_empl.json").st_size != 0:
            with open("controlsystem_empl.json", "r+", encoding="utf-8") as file:
                data = json.load(file)
                position_dict = {
                    "hourly": HourlyWorker,
                    "salaried": SalariedEmployee,
                    "manage": Manager,
                    "head_manage": HeadManager,
                }
                for elem in data:
                    worker = position_dict[elem["position"]](
                        int(elem["age"]), elem["name"], elem["surname"]
                    )
                    if not elem["salary"] is None:
                        work_dict = {
                            "salaried": HiredJob,
                            "manage": ManagerJob,
                            "head_manage": HeadManagerJob,
                        }
                        if "time" in elem.keys():
                            worker.current_work = HourlyJob(
                                elem["name_job"],
                                elem["hourly_rate"],
                                elem["time"],
                            )
                        else:
                            worker.current_work = work_dict[elem["position"]](
                                elem["name"], elem["salary"]
                            )

                    if not worker is None:
                        self.employeess.append(worker)
        if os.stat("controlsystem_jobs.json").st_size != 0:
            with open("controlsystem_jobs.json", "r+", encoding="utf-8") as job_file:
                data = json.load(job_file)
                dict_job={'hourly':HourlyJob,
                          'salaried': HiredJob,
                          'manage': ManagerJob,
                          'head_manage': HeadManagerJob,
                          }
                for elem in data:
                    if "time" in elem.keys():
                        job = HourlyJob(
                            elem["name"],
                            elem["hourly_rate"],
                            elem["time"],
                        )
                    else:
                        job = dict_job[elem["position"]](
                            elem["name"], elem["salary"]
                        )
                    if not job is None:
                        self.jobs.append(job)
    def del_all(self):
        self.employeess.clear()

        with open("controlsystem_empl.json", "w+", encoding="utf-8") as _:
            ...
