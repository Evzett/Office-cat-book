import sys

from PyQt5 import QtWidgets

from interface import MainWindow
from controlsystem import ControlSystem

def main():
    if __name__ == "__main__":

        base_empl=ControlSystem()
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        mainwindow = MainWindow()
        mainwindow.setupUi(window,base_empl)
        mainwindow.controlsystem.load_json()
        mainwindow.view_cntrlSystem()

        window.show()
        sys.exit(app.exec_())
main()