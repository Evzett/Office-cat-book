# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_salary_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog

from controlsystem import Check


class NewSalaryWindow(QDialog):
    def setupUi(self, new_salary_window,controlsystem,employees_list):
        self.controlsystem=controlsystem
        self.new_salary_window=new_salary_window
        self.employees_list=employees_list
        new_salary_window.setObjectName("new_empl_window")
        new_salary_window.resize(400, 320)
        new_salary_window.setStyleSheet("background-color: rgb(229, 224, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 2px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"\n"
"")
        self.btn_OK = QtWidgets.QDialogButtonBox(new_salary_window)
        self.btn_OK.setGeometry(QtCore.QRect(20, 270, 361, 51))
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
        self.text_label_salary = QtWidgets.QLabel(new_salary_window)
        self.text_label_salary.setGeometry(QtCore.QRect(20, 30, 361, 41))
        self.text_label_salary.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.text_label_salary.setObjectName("text_label_salary")
        self.inp_new_salary = QtWidgets.QLineEdit(new_salary_window)
        self.inp_new_salary.setGeometry(QtCore.QRect(20, 140, 231, 51))
        self.inp_new_salary.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.inp_new_salary.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.inp_new_salary.setObjectName("inp_new_salary")
        self.text_new_salary = QtWidgets.QLabel(new_salary_window)
        self.text_new_salary.setGeometry(QtCore.QRect(20, 80, 231, 51))
        self.text_new_salary.setObjectName("text_new_salary")
        self.text_new_hourly_rate = QtWidgets.QLabel(new_salary_window)
        self.text_new_hourly_rate.setGeometry(QtCore.QRect(20, 200, 231, 51))
        self.text_new_hourly_rate.setObjectName("text_new_hourly_rate")
        self.inp_new_hourly_rate = QtWidgets.QLineEdit(new_salary_window)
        self.inp_new_hourly_rate.setGeometry(QtCore.QRect(20, 260, 231, 51))
        self.inp_new_hourly_rate.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.inp_new_hourly_rate.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.inp_new_hourly_rate.setObjectName("inp_new_hourly_rate")
        self.text_new_time = QtWidgets.QLabel(new_salary_window)
        self.text_new_time.setGeometry(QtCore.QRect(20, 80, 231, 51))
        self.text_new_time.setObjectName("text_new_time")
        self.inp_new_time = QtWidgets.QLineEdit(new_salary_window)
        self.inp_new_time.setGeometry(QtCore.QRect(20, 140, 231, 51))
        self.inp_new_time.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.inp_new_time.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.inp_new_time.setObjectName("inp_new_time")
        self.inp_new_time.hide()
        self.inp_new_hourly_rate.hide()
        self.text_new_time.hide()
        self.text_new_hourly_rate.hide()
        self.text_new_salary.hide()
        self.inp_new_salary.hide()
        self.ind_selected_empl=self.employees_list.currentIndex()
        self.current_empl=self.controlsystem.employeess[self.ind_selected_empl.row()]
        if self.current_empl.current_work.position == 'hourly':
            self.text_new_hourly_rate.show()
            self.inp_new_hourly_rate.show()
            self.text_new_time.show()
            self.inp_new_time.show()
        else:
            self.inp_new_salary.show()
            self.text_new_salary.show()
        self.retranslateUi(new_salary_window)
        self.btn_OK.accepted.connect(self.add_new_salary) # type: ignore
        self.btn_OK.rejected.connect(new_salary_window.reject) # type: ignore

        QtCore.QMetaObject.connectSlotsByName(new_salary_window)

    def add_new_salary(self):

            #new_salary = self.inp_new_salary.text()
                if self.current_empl.current_work.position == 'hourly':
                    new_hourly_rate = (self.inp_new_hourly_rate.text())
                    new_time = self.inp_new_time.text()
                    if Check.check_hourly_rate(
                            new_hourly_rate
                    ) and Check.check_time(new_time):
                        self.current_empl.current_work.set_salary(int(new_hourly_rate), int(new_time))
                        self.controlsystem.save_json()
                        self.new_salary_window.close()
                    else:
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Critical)
                        error_dialog.setText("УУПС ОШИБОЧКА!")
                        error_dialog.setInformativeText("Возможно, вы ввели некорректные данные")
                        error_dialog.setWindowTitle("ERROR")
                        error_dialog.exec_()
                        error_dialog.close()


                else:
                    new_salary = self.inp_new_salary.text()
                    if Check.check_salary(new_salary):
                        self.current_empl.current_work.set_salary(int(new_salary))
                        self.controlsystem.save_json()
                        self.new_salary_window.close()
                    else:
                        error_dialog = QMessageBox()
                        error_dialog.setIcon(QMessageBox.Critical)
                        error_dialog.setText("УУПС ОШИБОЧКА!")
                        error_dialog.setInformativeText("Возможно, вы ввели некорректные данные")
                        error_dialog.setWindowTitle("ERROR")
                        error_dialog.exec_()
                        error_dialog.close()


    def retranslateUi(self, new_salary_window):
        _translate = QtCore.QCoreApplication.translate
        new_salary_window.setWindowTitle(_translate("new_empl_window", "Dialog"))
        self.text_label_salary.setText(_translate("new_empl_window", "    Введите, пожалуйста, новую зарплату"))
        self.text_new_salary.setText(_translate("new_empl_window", "Новая зарплата:"))
        self.text_new_hourly_rate.setText(_translate("new_empl_window", "Новая почасовая ставка"))
        self.text_new_time.setText(_translate("new_empl_window", "Новое время работы"))