# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacevXnDZF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(648, 351)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #09102a;\n"
"}\n"
"#sideMenuMainCont, #header, #mainBody, #widget, #notification > QFrame {\n"
"	background-color: #171d3c;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	text-align: left;\n"
"	background-color: #08112a;\n"
"	padding: 10px 2px;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit{\n"
"	padding: 5px;\n"
"	background: transparent;\n"
"}\n"
"#searchInput{\n"
"	border-radius: 20px;\n"
"	border: 2px solid #fd7012;\n"
"}\n"
"#pushButton_8, #pushButton{\n"
"	background: none;\n"
"	padding: 0;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideMenuMainCont = QCustomSlideMenu(self.centralwidget)
        self.sideMenuMainCont.setObjectName(u"sideMenuMainCont")
        self.sideMenuMainCont.setMaximumSize(QSize(40, 16777215))
        self.verticalLayout = QVBoxLayout(self.sideMenuMainCont)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.sideMenuMainCont)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(6, 10, 10, 10)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.pushButton)


        self.verticalLayout_7.addWidget(self.frame, 0, Qt.AlignTop)

        self.sideMenuSubCont = QWidget(self.widget)
        self.sideMenuSubCont.setObjectName(u"sideMenuSubCont")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sideMenuSubCont.sizePolicy().hasHeightForWidth())
        self.sideMenuSubCont.setSizePolicy(sizePolicy)
        self.sideMenuSubCont.setMinimumSize(QSize(200, 301))
        self.sideMenuSubCont.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.sideMenuSubCont)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.sideMenuSubCont)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 301))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/dollar-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/pie-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/message-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.pushButton_7)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.sideMenuSubCont, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.sideMenuMainCont)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.notification = QCustomSlideMenu(self.widget_2)
        self.notification.setObjectName(u"notification")
        self.horizontalLayout_4 = QHBoxLayout(self.notification)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_3 = QFrame(self.notification)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)

        self.verticalLayout_9.addWidget(self.label_5)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_9.addWidget(self.label_4)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.pushButton_2 = QPushButton(self.notification)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon6)

        self.horizontalLayout_4.addWidget(self.pushButton_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.notification, 0, Qt.AlignHCenter)

        self.header = QWidget(self.widget_2)
        self.header.setObjectName(u"header")
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.searchInput = QFrame(self.header)
        self.searchInput.setObjectName(u"searchInput")
        self.searchInput.setFrameShape(QFrame.StyledPanel)
        self.searchInput.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.searchInput)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.searchInput)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit, 0, Qt.AlignHCenter)

        self.pushButton_8 = QPushButton(self.searchInput)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pushButton_8, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.searchInput, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.header)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignRight)

        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/images/images/logo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.header, 0, Qt.AlignTop)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.mainBody = QWidget(self.widget_4)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout_5 = QVBoxLayout(self.mainBody)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.mainBody)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.label_6 = QLabel(self.mainBody)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777214, 16777215))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_6)


        self.verticalLayout_4.addWidget(self.mainBody)


        self.verticalLayout_3.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.widget_2.raise_()
        self.sideMenuMainCont.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Investments", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Connection timeout. Please check your internet connection. ", None))
        self.pushButton_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Am looking for...", None))
        self.pushButton_8.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">SPINN TV</span><br>Creative UI</p></body></html>", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt;\">The </span><span style=\" font-size:28pt; font-weight:600;\">Main</span><span style=\" font-size:28pt;\"> Bo</span><span style=\" font-size:28pt; font-style:italic;\">d</span><span style=\" font-size:28pt;\">y</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#09102a;\">QT </span><span style=\" font-size:28pt; font-weight:600; color:#09102a; vertical-align:super;\">CUSTOM</span><span style=\" font-size:28pt; font-weight:600; color:#09102a;\"> WIDGETS</span></p></body></html>", None))
    # retranslateUi

