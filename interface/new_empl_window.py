
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog

from controlsystem import Check

from PyQt5 import QtCore, QtGui, QtWidgets


class NewEmplWindow(QDialog):
    def setupUi(self, new_empl_window,obj_cntrlsystem):
        new_empl_window.setObjectName("new_empl_window")
        new_empl_window.resize(400, 300)
        new_empl_window.setStyleSheet("background-color: rgb(229, 224, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 2px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"\n"
"")
        self.new_empl_window=new_empl_window
        self.controlsystem=obj_cntrlsystem
        self.btn_OK = QtWidgets.QDialogButtonBox(new_empl_window)
        self.btn_OK.setGeometry(QtCore.QRect(10, 230, 361, 51))
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
        self.label = QtWidgets.QLabel(new_empl_window)
        self.label.setGeometry(QtCore.QRect(20, 30, 261, 41))
        self.label.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.label.setObjectName("label")
        self.candy_pctr = QtWidgets.QLabel(new_empl_window)
        self.candy_pctr.setGeometry(QtCore.QRect(290, 10, 91, 61))
        self.candy_pctr.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 20px; /* Закругление углов */\n"
"")
        self.candy_pctr.setText("")
        self.candy_pctr.setPixmap(QtGui.QPixmap("./img/candy.jpg"))
        self.candy_pctr.setObjectName("candy_pctr")
        self.inp_name = QtWidgets.QLineEdit(new_empl_window)
        self.inp_name.setGeometry(QtCore.QRect(131, 90, 144, 26))
        self.inp_name.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.inp_name.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.inp_name.setObjectName("inp_name")
        self.inp_surname = QtWidgets.QLineEdit(new_empl_window)
        self.inp_surname.setGeometry(QtCore.QRect(131, 126, 144, 26))
        self.inp_surname.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.inp_surname.setObjectName("inp_surname")
        self.inp_age = QtWidgets.QLineEdit(new_empl_window)
        self.inp_age.setGeometry(QtCore.QRect(131, 162, 144, 26))
        self.inp_age.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.inp_age.setObjectName("inp_age")
        self.inp_position = QtWidgets.QLineEdit(new_empl_window)
        self.inp_position.setGeometry(QtCore.QRect(131, 198, 144, 26))
        self.inp_position.setStyleSheet("background-color: rgb(247, 242, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 0px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"")
        self.inp_position.setObjectName("inp_position")
        self.text_name = QtWidgets.QLabel(new_empl_window)
        self.text_name.setGeometry(QtCore.QRect(10, 90, 111, 26))
        self.text_name.setObjectName("text_name")
        self.text_surname = QtWidgets.QLabel(new_empl_window)
        self.text_surname.setGeometry(QtCore.QRect(10, 126, 111, 26))
        self.text_surname.setObjectName("text_surname")
        self.text_age = QtWidgets.QLabel(new_empl_window)
        self.text_age.setGeometry(QtCore.QRect(10, 162, 111, 26))
        self.text_age.setObjectName("text_age")
        self.text_position = QtWidgets.QLabel(new_empl_window)
        self.text_position.setGeometry(QtCore.QRect(10, 198, 111, 26))
        self.text_position.setObjectName("text_position")

        self.retranslateUi(new_empl_window)
        self.btn_OK.accepted.connect(self.mod_empl_accept) # type: ignore
        self.btn_OK.rejected.connect(new_empl_window.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(new_empl_window)
    def mod_empl_accept(self):
            self.user_name = self.inp_name.text()
            self.user_surname=self.inp_surname.text()
            self.user_age=self.inp_age.text()
            self.user_position=self.inp_position.text()
            if Check.check(self.user_age, self.user_name, self.user_surname) :
                    if Check.check_position_answer(self.user_position):
                                self.controlsystem.add_employee(self.user_age,self.user_name,self.user_surname,self.user_position)
                                self.controlsystem.save_json()
                                self.new_empl_window.close()
                    else:
                            error_dialog = QMessageBox()
                            error_dialog.setIcon(QMessageBox.Critical)
                            error_dialog.setText("УУПС!")
                            error_dialog.setInformativeText("Такой должности нет в данной компании\n"
"Вот список всех должностей:\n"
                                                            ""
"1. наемный\n"
"2. почасовой\n"
"3. менеджер\n"
"4. руководитель\n")
                            error_dialog.setWindowTitle("ERROR")
                            error_dialog.exec_()
                            error_dialog.close()




            else:
                    #app = QApplication(sys.argv)
                    error_dialog = QMessageBox()
                    error_dialog.setIcon(QMessageBox.Critical)
                    error_dialog.setText("УУПС!")
                    error_dialog.setInformativeText("Возможно, ваши данные не настоящие")
                    error_dialog.setWindowTitle("ERROR")
                    error_dialog.exec_()
                    error_dialog.close()
                    #sys.exit(app.exec_())
    def retranslateUi(self, new_empl_window):
        _translate = QtCore.QCoreApplication.translate
        new_empl_window.setWindowTitle(_translate("new_empl_window", "Dialog"))
        self.label.setText(_translate("new_empl_window", "Введите, пожалуйста, данные"))
        self.text_name.setText(_translate("new_empl_window", "Имя:"))
        self.text_surname.setText(_translate("new_empl_window", "Фамилия:"))
        self.text_age.setText(_translate("new_empl_window", "Возраст:"))
        self.text_position.setText(_translate("new_empl_window", "Должность:"))




