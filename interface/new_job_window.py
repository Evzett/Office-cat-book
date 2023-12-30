


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog

from controlsystem import Check, HourlyJob, ManagerJob, HeadManagerJob, HiredJob


class NewJobWindow(QDialog):
    def setupUi(self, new_job_window,controlsystem):
        self.controlsystem=controlsystem
        self.new_job_window=new_job_window
        new_job_window.setObjectName("new_job_window")
        new_job_window.resize(550, 465)
        new_job_window.setStyleSheet("background-color: rgb(229, 224, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 2px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"\n"
"")
        self.btn_OK = QtWidgets.QDialogButtonBox(new_job_window)
        self.btn_OK.setGeometry(QtCore.QRect(130, 400, 361, 51))
        self.btn_OK.setStyleSheet("QPushButton {\n"
"border-radius:  10px;\n"
"background-color: rgb(240, 235, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"border-color: rgb(197, 170, 255);\n"
"selection-color: rgb(246, 247, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(211, 199, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(255, 255, 255);\n"
"}")
        self.btn_OK.setOrientation(QtCore.Qt.Horizontal)
        self.btn_OK.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_OK.setObjectName("btn_OK")
        self.text_choose_data = QtWidgets.QLabel(new_job_window)
        self.text_choose_data.setGeometry(QtCore.QRect(30, 190, 331, 41))
        self.text_choose_data.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.text_choose_data.setObjectName("text_choose_data")
        self.candy_pctr = QtWidgets.QLabel(new_job_window)
        self.candy_pctr.setGeometry(QtCore.QRect(450, 10, 91, 61))
        self.candy_pctr.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 20px; /* Закругление углов */\n"
"")
        self.candy_pctr.setText("")
        self.candy_pctr.setPixmap(QtGui.QPixmap("./img/candy.jpg"))
        self.candy_pctr.setObjectName("candy_pctr")
        self.inp_name_job = QtWidgets.QLineEdit(self.new_job_window)
        self.inp_name_job.setGeometry(QtCore.QRect(279, 251, 241, 22))
        self.inp_name_job.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.inp_name_job.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.inp_name_job.setObjectName("inp_name_job")
        self.inp_salary = QtWidgets.QLineEdit(self.new_job_window)
        self.inp_salary.setGeometry(QtCore.QRect(279, 282, 241, 22))
        self.inp_salary.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.inp_salary.setObjectName("inp_salary")
        self.text_name_job = QtWidgets.QLabel(new_job_window)
        self.text_name_job.setGeometry(QtCore.QRect(21, 251, 241, 24))
        self.text_name_job.setObjectName("text_name_job")
        self.text_salary = QtWidgets.QLabel(new_job_window)
        self.text_salary.setGeometry(QtCore.QRect(21, 282, 241, 24))
        self.text_salary.setObjectName("text_salary")
        self.text_hourly_rate = QtWidgets.QLabel(self.new_job_window)
        self.text_hourly_rate.setGeometry(QtCore.QRect(21, 313, 241, 24))
        self.text_hourly_rate.setObjectName("text_hourly_rate")
        self.text_time = QtWidgets.QLabel(self.new_job_window)
        self.text_time.setGeometry(QtCore.QRect(21, 344, 241, 24))
        self.text_time.setObjectName("text_time")
        self.inp_hourly_rate = QtWidgets.QLineEdit(self.new_job_window)
        self.inp_hourly_rate.setGeometry(QtCore.QRect(279, 313, 241, 22))
        self.inp_hourly_rate.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.inp_hourly_rate.setObjectName("inp_hourly_rate")
        self.inp_time = QtWidgets.QLineEdit(self.new_job_window)
        self.inp_time.setGeometry(QtCore.QRect(279, 344, 241, 22))
        self.inp_time.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.inp_time.setObjectName("inp_time")
        self.text_choose_type = QtWidgets.QLabel(new_job_window)
        self.text_choose_type.setGeometry(QtCore.QRect(10, 30, 421, 41))
        self.text_choose_type.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.text_choose_type.setObjectName("text_choose_type")
        self.choose_job_combBox = QtWidgets.QComboBox(new_job_window)
        self.choose_job_combBox.setGeometry(QtCore.QRect(230, 80, 281, 51))
        self.choose_job_combBox.setObjectName("choose_job_combBox")
        self.choose_job_combBox.addItem("Option 1")
        self.choose_job_combBox.addItem("Option 2")
        self.choose_job_combBox.addItem("Option 3")
        self.choose_job_combBox.addItem("Option 4")
        self.choose_job_combBox.currentIndexChanged.connect(self.on_combobox_choose)


        self.retranslateUi(new_job_window)


        self.btn_OK.accepted.connect(self.mod_accept_job) # type: ignore
        self.btn_OK.rejected.connect(new_job_window.reject) # type: ignore
        self.text_name_job.hide()
        self.inp_name_job.hide()
        self.text_hourly_rate.hide()
        self.inp_hourly_rate.hide()
        self.inp_salary.hide()
        self.text_salary.hide()
        self.text_time.hide()
        self.inp_time.hide()
        QtCore.QMetaObject.connectSlotsByName(new_job_window)

    def on_combobox_choose(self,index):
        self.selected_option = self.choose_job_combBox.itemText(index)
        if self.selected_option=="Почасовая вакансия":
            self.inp_name_job.show()
            self.text_name_job.show()
            self.text_salary.hide()
            self.inp_salary.hide()
            self.text_time.show()
            self.inp_time.show()
            self.inp_hourly_rate.show()
            self.text_hourly_rate.show()

        else:
            self.inp_name_job.show()
            self.text_name_job.show()
            self.text_salary.show()
            self.inp_salary.show()
            self.text_hourly_rate.hide()
            self.inp_hourly_rate.hide()
            self.text_time.hide()
            self.inp_time.hide()
    def mod_accept_job(self):
        if self.selected_option == "Почасовая вакансия":

            self.user_name_job=self.inp_name_job.text()
            self.user_hourly_rate=self.inp_hourly_rate.text()
            self.user_time=self.inp_time.text()
            if Check.check_time(self.user_time) and Check.check_hourly_rate(self.user_hourly_rate):
                hourly_job=HourlyJob(self.user_name_job,int(self.user_hourly_rate),int(self.user_time))
                self.controlsystem.add_job(hourly_job)
            else:
                # app = QApplication(sys.argv)
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Critical)
                error_dialog.setText("УУПС!")
                error_dialog.setInformativeText("Ваши данные ненастоящие,предусмотрите то,\n что рабочая смена не должна превышать 8 часов")
                error_dialog.setWindowTitle("ERROR")
                error_dialog.exec_()
                # sys.exit(app.exec_())
        if self.selected_option=="Вакансия для менеджера":
            self.user_name_job=self.inp_name_job.text()
            self.user_salary=self.inp_salary.text()
            if Check.check_salary(self.user_salary):
                manage_work=ManagerJob(self.user_name_job,int(self.user_salary))
                self.controlsystem.add_job(manage_work)
            else:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Critical)
                error_dialog.setText("УУПС ОШИБОЧКА!")
                error_dialog.setInformativeText("Возможно, вы ввели некорректные данные")
                error_dialog.setWindowTitle("ERROR")
                error_dialog.exec_()
                error_dialog.close()

        if self.selected_option=="Вакансия для руководителя":

            self.user_name_job = self.inp_name_job.text()
            self.user_salary = self.inp_salary.text()
            if Check.check_salary(self.user_salary):
                head_manage_work = HeadManagerJob(self.user_name_job, int(self.user_salary))
                self.controlsystem.add_job(head_manage_work)
            else:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Critical)
                error_dialog.setText("УУПС ОШИБОЧКА!")
                error_dialog.setInformativeText("Возможно, вы ввели некорректные данные")
                error_dialog.setWindowTitle("ERROR")
                error_dialog.exec_()
                error_dialog.close()

        if self.selected_option=="Вакансия для наемного работника":

            self.user_name_job = self.inp_name_job.text()
            self.user_salary = self.inp_salary.text()
            if Check.check_salary(self.user_salary):
                hired_work = HiredJob(self.user_name_job, int(self.user_salary))
                self.controlsystem.add_job(hired_work)
            else:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Critical)
                error_dialog.setText("УУПС ОШИБОЧКА!")
                error_dialog.setInformativeText("Возможно, вы ввели некорректные данные")
                error_dialog.setWindowTitle("ERROR")
                error_dialog.exec_()
                error_dialog.close()
        self.new_job_window.close()
        self.controlsystem.save_json()

    def retranslateUi(self, new_job_window):
        _translate = QtCore.QCoreApplication.translate
        new_job_window.setWindowTitle(_translate("new_job_window", "Dialog"))
        self.text_choose_data.setText(_translate("new_job_window", "       Введите, пожалуйста, данные"))

        self.text_name_job.setText(_translate("new_job_window", "Наименование вакансии:"))
        self.text_salary.setText(_translate("new_job_window", "Зарплата:"))
        self.text_hourly_rate.setText(_translate("new_job_window", "Почасовая ставка:"))
        self.text_time.setText(_translate("new_job_window", "Время работы:"))
        self.choose_job_combBox.setItemText(0, _translate("new_job_window", "Почасовая вакансия"))
        self.choose_job_combBox.setItemText(1, _translate("new_job_window", "Вакансия для менеджера"))
        self.choose_job_combBox.setItemText(2, _translate("new_job_window", "Вакансия для руководителя"))
        self.choose_job_combBox.setItemText(3, _translate("new_job_window", "Вакансия для наемного работника"))
        self.text_choose_type.setText(_translate("new_job_window", "Выберите какого типа хотите создать вакансию"))
