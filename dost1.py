# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dostop.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:#f8f8ff")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, 0, 241, 601))
        self.widget.setStyleSheet("background-color:#b0c4de")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(70, 10, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 111, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("глобус2.png"))
        self.label_2.setObjectName("label_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.widget)
        self.commandLinkButton.setGeometry(QtCore.QRect(40, 200, 185, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setStyleSheet("background-color:#b0c4de;\n"
"border-radius:30;\n"
"color:white")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.widget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(40, 270, 185, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setStyleSheet("background-color:#b0c4de;\n"
"border-radius:30;\n"
"color:white")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.verxnee = QtWidgets.QLineEdit(self.centralwidget)
        self.verxnee.setGeometry(QtCore.QRect(280, 120, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.verxnee.setFont(font)
        self.verxnee.setStyleSheet("background-color:#f0fff0;\n"
"border:2px solid#b0c4de;\n"
"border-radius:30;\n"
"color:gray")
        self.verxnee.setObjectName("verxnee")
        self.dostoprim = QtWidgets.QLabel(self.centralwidget)
        self.dostoprim.setGeometry(QtCore.QRect(270, 40, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        self.dostoprim.setFont(font)
        self.dostoprim.setObjectName("dostoprim")
        self.nizhnee = QtWidgets.QLineEdit(self.centralwidget)
        self.nizhnee.setGeometry(QtCore.QRect(280, 210, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(20)
        self.nizhnee.setFont(font)
        self.nizhnee.setStyleSheet("background-color:#f0fff0;\n"
"border:2px solid#b0c4de;\n"
"border-radius:30;\n"
"color:gray")
        self.nizhnee.setObjectName("nizhnee")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 400, 151, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("карта.png"))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 300, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#778899;\n"
"border-radius:30;\n"
"color:white")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 80, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:blue")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MENU"))
        self.commandLinkButton.setText(_translate("MainWindow", "Страна(wiki)"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "О городе(wiki)"))
        self.dostoprim.setText(_translate("MainWindow", "Достопримечательности"))
        self.pushButton.setText(_translate("MainWindow", "Узнать, что нужно посетить!"))
        self.label_4.setText(_translate("MainWindow", "Введите город"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
