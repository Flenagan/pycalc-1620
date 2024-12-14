# main file for the program

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from calcgui import Ui_MainCWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainCWindow = QtWidgets.QMainWindow()
    ui = Ui_MainCWindow()
    ui.setupUi(MainCWindow)
    MainCWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
