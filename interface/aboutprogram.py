from PyQt5 import QtWidgets

class AboutWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('О программе')
        self.setGeometry(100,200,400,400)
        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel("""Автор: Тисецкая Анастасия\nСФУ ИКИТ КИ23-17/1б\n\
Графический интерфейс к предыдущей работе 6:\n\

Вариант 24
Реализуйте программу для распределения работ между работниками. 
Создайте иерархию классов сотрудников компании. Например, работник 
(базовый класс), почасовой работник, наемный работник, менеджер, 
руководитель. Добавьте иерархию видов работ, которые характеризуются 
длительность и оплатой. Объедините сотрудника и вид работы в классе 
текущей работы.

При нажатии на кнопку "Назначить работу сотруднику" вас перекинет 
на вторую вкладку, где вы должны выбрать сотрудника, затем перекинет
на третью вкладку, где вы должны подобрать ему вакансию.

P.S. Не хотелось делать второй эксель, поэтому в программе вы можете
встретить изображения милых котиков

P.S.S Обратите внимание, что возраст работника должен быть не менее 
14 лет, а также, время работы у почасового работника не должно превышать
10 часов
""")
        layout.addWidget(label)
        self.setLayout(layout)
        self.setStyleSheet("background-color: rgb(229, 224, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 2px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"\n"
"")


