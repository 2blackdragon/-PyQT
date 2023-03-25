# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plan3.ui'
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 270, 281, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stopwatch_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stopwatch_btn.setObjectName("stopwatch_btn")
        self.horizontalLayout_2.addWidget(self.stopwatch_btn)
        self.timer_btn_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.timer_btn_2.setObjectName("timer_btn_2")
        self.horizontalLayout_2.addWidget(self.timer_btn_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 240, 281, 22))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.time_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.time_btn.setObjectName("time_btn")
        self.horizontalLayout_4.addWidget(self.time_btn)
        self.alarm_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.alarm_btn.setObjectName("alarm_btn")
        self.horizontalLayout_4.addWidget(self.alarm_btn)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.stopwatch_btn.setText(_translate("Form", "Секундомер"))
        self.timer_btn_2.setText(_translate("Form", "Таймер"))
        self.time_btn.setText(_translate("Form", "Время"))
        self.alarm_btn.setText(_translate("Form", "Будильник"))
        self.label.setText(_translate("Form", "                          Время"))
        self.pushButton.setText(_translate("Form", "Цифровые"))
