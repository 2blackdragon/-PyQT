# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plan.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 300)
        Form.setStyleSheet("*{\n"
"    font-size: 12pt;\n"
"    font-family: sans-serif;\n"
"    background-color: #2a323b;\n"
"    color: #ff9900;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #3b3b3b;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #20252b;\n"
"}")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 240, 281, 22))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.time = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.time.setObjectName("time")
        self.horizontalLayout_4.addWidget(self.time)
        self.alarm = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.alarm.setObjectName("alarm")
        self.horizontalLayout_4.addWidget(self.alarm)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 270, 281, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.stopwatch = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stopwatch.setObjectName("stopwatch")
        self.horizontalLayout_6.addWidget(self.stopwatch)
        self.timer = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.timer.setObjectName("timer")
        self.horizontalLayout_6.addWidget(self.timer)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 16))
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 30, 281, 61))
        self.lcdNumber.setObjectName("lcdNumber")
        self.start_btn = QtWidgets.QPushButton(Form)
        self.start_btn.setGeometry(QtCore.QRect(230, 100, 61, 21))
        self.start_btn.setObjectName("start_btn")
        self.circle_btn = QtWidgets.QPushButton(Form)
        self.circle_btn.setGeometry(QtCore.QRect(90, 100, 61, 21))
        self.circle_btn.setObjectName("circle_btn")
        self.stop_btn = QtWidgets.QPushButton(Form)
        self.stop_btn.setGeometry(QtCore.QRect(160, 100, 61, 21))
        self.stop_btn.setObjectName("stop_btn")
        self.reset_btn = QtWidgets.QPushButton(Form)
        self.reset_btn.setGeometry(QtCore.QRect(20, 100, 61, 21))
        self.reset_btn.setObjectName("reset_btn")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 130, 281, 101))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.time.setText(_translate("Form", "Время"))
        self.alarm.setText(_translate("Form", "Будильник"))
        self.stopwatch.setText(_translate("Form", "Секундомер"))
        self.timer.setText(_translate("Form", "Таймер"))
        self.label.setText(_translate("Form", "                       Секундомер"))
        self.start_btn.setText(_translate("Form", "Старт"))
        self.circle_btn.setText(_translate("Form", "Круг"))
        self.stop_btn.setText(_translate("Form", "Стоп"))
        self.reset_btn.setText(_translate("Form", "Сброс"))
