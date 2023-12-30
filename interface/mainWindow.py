# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QStringListModel
from PyQt5.QtWidgets import QMessageBox

from interface import new_empl_window, AboutWindow
from interface import new_job_window
from interface import new_position_window
from interface import neww_salary_window



class MainWindow:
    def setupUi(self, MainWindow,controlsystem):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 694)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("font: 9pt \"Sitka\";\n"
"background-color: rgb(239, 242, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateTime = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTime.setGeometry(QtCore.QRect(530, 0, 148, 25))
        self.dateTime.setStyleSheet("")
        self.dateTime.setObjectName("dateTime")
        self.dateTime.setDateTime(QDateTime.currentDateTime())

        self.pages = QtWidgets.QTabWidget(self.centralwidget)
        self.pages.setEnabled(True)
        self.pages.setGeometry(QtCore.QRect(10, 20, 708, 621))
        self.pages.setMinimumSize(QtCore.QSize(0, 0))
        self.pages.setMaximumSize(QtCore.QSize(708, 16777215))
        self.pages.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pages.setMouseTracking(True)
        self.pages.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pages.setAutoFillBackground(False)
        self.pages.setStyleSheet("background-color: rgb(229, 224, 255);\n"
"font: 75 10pt \"System\";\n"
"border: 2px solid #c0b7ff; /* Цвет рамки и ее толщина */\n"
"border-radius: 10px; /* Закругление углов */\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #000000; /* Цвет фона выбранной вкладки */\n"
"    color: #000000; /* Цвет текста выбранной вкладки */\n"
"}")
        self.pages.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pages.setElideMode(QtCore.Qt.ElideLeft)
        self.pages.setUsesScrollButtons(True)
        self.pages.setTabsClosable(False)
        self.pages.setMovable(False)
        self.pages.setTabBarAutoHide(False)
        self.pages.setObjectName("pages")
        self.menu = QtWidgets.QWidget()
        self.menu.setObjectName("menu")
        self.add_new_empl = QtWidgets.QPushButton(self.menu)
        self.add_new_empl.setGeometry(QtCore.QRect(10, 110, 671, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(150)
        sizePolicy.setHeightForWidth(self.add_new_empl.sizePolicy().hasHeightForWidth())
        self.add_new_empl.setSizePolicy(sizePolicy)
        self.add_new_empl.setMinimumSize(QtCore.QSize(100, 50))

        self.show_about_window = QtWidgets.QPushButton(self.menu)
        self.show_about_window.setGeometry(QtCore.QRect(10, 440, 671, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(150)
        sizePolicy.setHeightForWidth(self.show_about_window.sizePolicy().hasHeightForWidth())
        self.show_about_window.setSizePolicy(sizePolicy)
        self.show_about_window.setMinimumSize(QtCore.QSize(100, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.show_about_window.setPalette(palette)
        self.show_about_window.setStyleSheet("QPushButton {\n"
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
        self.show_about_window.setCheckable(True)
        self.show_about_window.setAutoDefault(True)
        self.show_about_window.setDefault(False)
        self.show_about_window.setObjectName("show_about_window")
        self.show_about_window.clicked.connect(self.window_about_program)









        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.add_new_empl.setPalette(palette)
        self.add_new_empl.setStyleSheet("QPushButton {\n"
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
        self.add_new_empl.setCheckable(True)
        self.add_new_empl.setAutoDefault(True)
        self.add_new_empl.setDefault(False)
        self.add_new_empl.setObjectName("add_new_empl")
        self.add_new_job = QtWidgets.QPushButton(self.menu)
        self.add_new_job.setGeometry(QtCore.QRect(10, 220, 671, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(150)
        sizePolicy.setHeightForWidth(self.add_new_job.sizePolicy().hasHeightForWidth())
        self.add_new_job.setSizePolicy(sizePolicy)
        self.add_new_job.setMinimumSize(QtCore.QSize(100, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.add_new_job.setPalette(palette)
        self.add_new_job.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.add_new_job.setStyleSheet("QPushButton {\n"
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
        self.add_new_job.setCheckable(True)
        self.add_new_job.setObjectName("add_new_job")
        self.assign_job = QtWidgets.QPushButton(self.menu)
        self.assign_job.setGeometry(QtCore.QRect(10, 330, 671, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(150)
        sizePolicy.setHeightForWidth(self.assign_job.sizePolicy().hasHeightForWidth())
        self.assign_job.setSizePolicy(sizePolicy)
        self.assign_job.setMinimumSize(QtCore.QSize(100, 50))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.assign_job.setPalette(palette)
        self.assign_job.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.assign_job.setAutoFillBackground(False)
        self.assign_job.setStyleSheet("QPushButton {\n"
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
        self.assign_job.setCheckable(True)
        self.assign_job.setObjectName("assign_job")
        self.assign_job.clicked.connect(self.assign_job_to_staff)
        self.line = QtWidgets.QFrame(self.menu)
        self.line.setGeometry(QtCore.QRect(0, 180, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.menu)
        self.line_2.setGeometry(QtCore.QRect(0, 300, 701, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.menu)
        self.line_3.setGeometry(QtCore.QRect(0, 410, 701, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.catyy_pict = QtWidgets.QLabel(self.menu)
        self.catyy_pict.setGeometry(QtCore.QRect(590, 0, 107, 104))
        self.catyy_pict.setText("")
        self.catyy_pict.setPixmap(QtGui.QPixmap("../../Downloads/img/catyyy.jpg"))
        self.catyy_pict.setObjectName("catyy_pict")
        self.pages.addTab(self.menu, "")
        self.employees = QtWidgets.QWidget()
        self.employees.setObjectName("employees")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.employees)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 86, 691, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.employees_list = QtWidgets.QListView(self.verticalLayoutWidget)
        self.employees_list.setStyleSheet("selection-color: rgb(255, 255, 255);\n"
"background-color: rgb(247, 242, 255);")
        self.employees_list.setObjectName("employees_list")
        self.verticalLayout.addWidget(self.employees_list)
        self.lapa_cat_pict = QtWidgets.QLabel(self.employees)
        self.lapa_cat_pict.setGeometry(QtCore.QRect(0, 0, 101, 91))
        self.lapa_cat_pict.setText("")
        self.lapa_cat_pict.setPixmap(QtGui.QPixmap("../../Downloads/img/lapa_cat.jpg"))
        self.lapa_cat_pict.setObjectName("lapa_cat_pict")
        self.change_position_btn = QtWidgets.QPushButton(self.employees)
        self.change_position_btn.setGeometry(QtCore.QRect(191, 23, 189, 24))
        self.change_position_btn.setStyleSheet("QPushButton {\n"
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
        self.error_occurred=False
        self.change_position_btn.setObjectName("change_position_btn")
        self.change_position_btn.clicked.connect(self.window_new_position)
        self.dismissal_btn = QtWidgets.QPushButton(self.employees)
        self.dismissal_btn.setGeometry(QtCore.QRect(536, 23, 131, 24))
        self.dismissal_btn.setStyleSheet("QPushButton {\n"
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
        self.dismissal_btn.setObjectName("dismissal_btn")
        self.dismissal_btn.clicked.connect(self.remove_selected_item_empl)
        self.raise_salary_btn = QtWidgets.QPushButton(self.employees)
        self.raise_salary_btn.setGeometry(QtCore.QRect(387, 23, 141, 24))
        self.raise_salary_btn.setStyleSheet("QPushButton {\n"
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
        self.raise_salary_btn.setObjectName("raise_salary_btn")
        self.raise_salary_btn.clicked.connect(self.window_new_salary)
        self.pages.addTab(self.employees, "")
        self.jobs = QtWidgets.QWidget()
        self.jobs.setObjectName("jobs")
        self.list_jobs = QtWidgets.QListView(self.jobs)
        self.list_jobs.setGeometry(QtCore.QRect(0, 86, 691, 481))
        self.list_jobs.setStyleSheet("selection-color: rgb(255, 255, 255);\n"
"background-color: rgb(247, 242, 255);\n"
"")
        self.list_jobs.setObjectName("list_jobs")
        self.cat_ghost_pctr = QtWidgets.QLabel(self.jobs)
        self.cat_ghost_pctr.setGeometry(QtCore.QRect(0, 0, 101, 91))
        self.cat_ghost_pctr.setText("")
        self.cat_ghost_pctr.setPixmap(QtGui.QPixmap("../../Downloads/img/caty ghost1.jpg"))
        self.cat_ghost_pctr.setObjectName("cat_ghost_pctr")
        self.del_job_btn = QtWidgets.QPushButton(self.jobs)
        self.del_job_btn.setGeometry(QtCore.QRect(465, 18, 201, 31))
        self.del_job_btn.setStyleSheet("QPushButton {\n"
"border-radius:  10px;\n"
"background-color: rgb(240, 235, 255);\n"
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
        self.del_job_btn.setObjectName("del_job_btn")
        self.del_job_btn.clicked.connect(self.remove_selected_item_job)
        self.pages.addTab(self.jobs, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 27))
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setTitle("")
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu_2.menuAction())
        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(0)
        self.controlsystem = controlsystem
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_new_empl.clicked.connect(self.window_empl_start)
        self.add_new_job.clicked.connect(self.window_job_start)

    def view_cntrlSystem(self):

        self.model_empl = QStringListModel(list(map(str, self.controlsystem.employeess)))
        self.model_jobs = QStringListModel(list(map(str, self.controlsystem.jobs)))
        self.employees_list.setModel(self.model_empl)
        self.list_jobs.setModel(self.model_jobs)

    def assign_job_to_staff(self):
        self.pages.setCurrentIndex(1)
        self.employees_list.clicked.connect(self.on_employee_selected)

    def on_employee_selected(self,index_empl):
            self.selected_empl=index_empl.row()
            self.pages.setCurrentIndex(2)
            self.list_jobs.clicked.connect(self.on_job_selected)

            self.list_jobs.clicked.disconnect()  # Отключаем событие clicked перед подключением
            self.list_jobs.clicked.connect(self.on_job_selected)
    def on_job_selected(self,index):


            current_empl = self.controlsystem.employeess[self.selected_empl]
            current_work = self.controlsystem.jobs[index.row()]
            flag = current_empl.set_work(current_work)
            if index.row() < len(self.controlsystem.jobs) and self.selected_empl < len(self.controlsystem.employeess):
                    if flag:

                            self.controlsystem.save_json()
                            self.remove_selected_item_job()
                            self.view_cntrlSystem()
                    else:

                            self.show_error()

                            self.list_jobs.selectionModel().clearSelection()
                            self.employees_list.selectionModel().clearSelection()
                            self.pages.setCurrentIndex(1)

            else:

                    self.show_error()

                    self.list_jobs.selectionModel().clearSelection()
                    self.employees_list.selectionModel().clearSelection()
                    self.pages.setCurrentIndex(1)





    def show_error(self):

            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setText("УУПС ОШИБОЧКА!")
            error_dialog.setInformativeText("Выбран не тот тип вакансии")
            error_dialog.setWindowTitle("ERROR")
            error_dialog.setStandardButtons(QMessageBox.Cancel)
            self.list_jobs.selectionModel().clearSelection()
            self.employees_list.selectionModel().clearSelection()
            self.pages.setCurrentIndex(0)

            error_dialog.exec_()
            error_dialog.close()
            self.list_jobs.clicked.disconnect()  # Отключаем событие clicked
            self.employees_list.clicked.disconnect()  # Отключаем событие clicked




    def remove_selected_item_empl(self):
        # Получение индекса выбранного элемента
        index = self.employees_list.currentIndex()

        if index.isValid():
            # Удаление выбранной строки из модели данных
            self.model_empl.removeRow(index.row())
            self.controlsystem.dismissal(index.row())
            self.controlsystem.save_json()
            self.view_cntrlSystem()

    def remove_selected_item_job(self):
        # Получение индекса выбранного элемента
        index_job = self.list_jobs.currentIndex()

        if index_job.isValid():
            # Удаление выбранной строки из модели данных
            self.model_jobs.removeRow(index_job.row())
            self.controlsystem.del_job(index_job.row())
            self.controlsystem.save_json()
            self.view_cntrlSystem()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_new_empl.setText(_translate("MainWindow", "Добавить нового сотрудника"))
        self.show_about_window.setText(_translate("MainWindow", "Показать сведения о программе"))

        self.add_new_job.setText(_translate("MainWindow", "Добавить новую вакансию"))
        self.assign_job.setText(_translate("MainWindow", "Назначить вакансию работнику"))
        self.pages.setTabText(self.pages.indexOf(self.menu), _translate("MainWindow", "Меню"))
        self.change_position_btn.setText(_translate("MainWindow", "Изменить должность"))
        self.dismissal_btn.setText(_translate("MainWindow", "Уволить"))
        self.raise_salary_btn.setText(_translate("MainWindow", "Повысить зп"))
        self.pages.setTabText(self.pages.indexOf(self.employees), _translate("MainWindow", "Сотрудники"))
        self.del_job_btn.setText(_translate("MainWindow", "Удалить вакансию"))
        self.pages.setTabText(self.pages.indexOf(self.jobs), _translate("MainWindow", "Вакансии"))

    def window_empl_start(self):
        window = QtWidgets.QDialog()
        ui = new_empl_window.NewEmplWindow()
        ui.setupUi(window, self.controlsystem)
        window.exec_()
        self.view_cntrlSystem()

    def window_new_position(self):
        window = QtWidgets.QDialog()
        ui = new_position_window.NewPositionWindow()
        ui.setupUi(window, self.controlsystem, self.model_empl, self.employees_list)
        window.exec_()
        self.view_cntrlSystem()

    def window_new_salary(self):
        index_empl = self.employees_list.currentIndex()
        if self.controlsystem.employeess[index_empl.row()].current_work:
            window = QtWidgets.QDialog()
            ui = neww_salary_window.NewSalaryWindow()
            ui.setupUi(window, self.controlsystem,self.employees_list)
            window.exec_()
            self.view_cntrlSystem()
        else:

            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setText("УУПС ОШИБОЧКА!")
            error_dialog.setInformativeText("Нельзя изменить зарплату безработному")
            error_dialog.setWindowTitle("ERROR")
            error_dialog.exec_()
            error_dialog.close()

    def window_job_start(self):
        window = QtWidgets.QDialog()
        ui = new_job_window.NewJobWindow()
        ui.setupUi(window, self.controlsystem)
        window.exec_()
        self.view_cntrlSystem()

    def window_about_program(self):
            self.about_window = AboutWindow()
            self.about_window.show()
