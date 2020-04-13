# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 't_l_c_gui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject,)

from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: WhiteSmoke;\n"
"}\n"
"QTextEdit {\n"
"	background-color:WhiteSmoke;\n"
"	border: none;\n"
"	font-size: 13px;\n"
"}\n"
"QLineEdit {\n"
"	background-color: White;\n"
"	border: none;\n"
"	wight: 50px;\n"
"	height: 30px;\n"
"}\n"
"QLabel {\n"
"	wight: 50px;\n"
"	height: 20px;\n"
"	font-size: 11px;\n"
"	font-weight: bold;\n"
"	border: none;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color:silver;\n"
"	wight: 75px;\n"
"	height: 50px;\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"	border: none;\n"
"	text-align: center;\n"
"	text-color:#36393F;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: Lavender;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:DimGrey;\n"
"}\n"
"QToolButton {\n"
"	background-color:silver;\n"
"	text-color: White;\n"
"	font-size: 13px;\n"
"	font-weight: bold;\n"
"	border: none;\n"
"	text-align: center;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color:  Lavender;\n"
"}\n"
"QToolButton:pressed {\n"
"	background-color: DimGrey;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_for_log_file = QLineEdit(self.centralwidget)
        self.lineEdit_for_log_file.setObjectName(u"lineEdit_for_log_file")

        self.horizontalLayout.addWidget(self.lineEdit_for_log_file)

        self.toolButton_forlog_file = QToolButton(self.centralwidget)
        self.toolButton_forlog_file.setObjectName(u"toolButton_forlog_file")

        self.horizontalLayout.addWidget(self.toolButton_forlog_file)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.lineEdit_SteamID = QLineEdit(self.centralwidget)
        self.lineEdit_SteamID.setObjectName(u"lineEdit_SteamID")

        self.verticalLayout.addWidget(self.lineEdit_SteamID)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.Button_with_chek_SteamId = QPushButton(self.centralwidget)
        self.Button_with_chek_SteamId.setObjectName(u"Button_with_chek_SteamId")

        self.verticalLayout.addWidget(self.Button_with_chek_SteamId)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.pushButton_for_all_death = QPushButton(self.centralwidget)
        self.pushButton_for_all_death.setObjectName(u"pushButton_for_all_death")

        self.verticalLayout.addWidget(self.pushButton_for_all_death)

        self.pushButton_for_global_chat = QPushButton(self.centralwidget)
        self.pushButton_for_global_chat.setObjectName(u"pushButton_for_global_chat")

        self.verticalLayout.addWidget(self.pushButton_for_global_chat)

        self.pushButton_all_chat = QPushButton(self.centralwidget)
        self.pushButton_all_chat.setObjectName(u"pushButton_all_chat")

        self.verticalLayout.addWidget(self.pushButton_all_chat)

        self.pushButton_all_lpg = QPushButton(self.centralwidget)
        self.pushButton_all_lpg.setObjectName(u"pushButton_all_lpg")

        self.verticalLayout.addWidget(self.pushButton_all_lpg)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Trouble Log Check", u"Trouble Log Check v 0.5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438 log. \u0444\u0430\u0439\u043b", None))
        self.toolButton_forlog_file.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u043a\u043d\u0443\u0442\u044c \u043f\u043e SteamID:", None))
        self.Button_with_chek_SteamId.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0436\u043d\u043e \u0447\u0435\u043a\u043d\u0443\u0442\u044c \u0438 \u043d\u0435  \u043f\u043e SteamID.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u043e:", None))
        self.pushButton_for_all_death.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0432\u0441\u0435 \u0441\u043c\u0435\u0440\u0442\u0438", None))
        self.pushButton_for_global_chat.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0433\u043b\u043e\u0431\u0430\u043b \u0447\u0430\u0442", None))
        self.pushButton_all_chat.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0432\u0435\u0441\u044c \u0447\u0430\u0442", None))
        self.pushButton_all_lpg.setText(QCoreApplication.translate("MainWindow", u"Посмотреть ВСЁ", None))
    # retranslateUi

