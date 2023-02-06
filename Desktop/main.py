from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, \
    QLabel, QSlider, QStyle, QSizePolicy, QFileDialog, QMainWindow
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QDir, Qt, QUrl

from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer

from dotenv import load_dotenv
import requests
import sys
import os

from utils.Navigation import Navigation
from services.api import RequestsBack
import images_rc as images_rc


class LoginScreen(QMainWindow):
    def __init__(self, parent=None):
        super(LoginScreen, self).__init__(parent)
        self.setStyle()
        self.setUi()

    def setUi(self):
        self.setObjectName("MainWindow")
        self.resize(500, 600)
        self.setMinimumSize(QtCore.QSize(500, 600))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Images/Icon.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("color: rgb(200, 200, 200);\n"
                           "background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_error = QtWidgets.QFrame(self.top_bar)
        self.frame_error.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_error.setStyleSheet("background-color: rgb(255, 85, 127);\n"
                                       "border-radius: 5px;")
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setStyleSheet("color: rgb(35, 35, 35);")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error)
        self.pushButton_close_popup = QtWidgets.QPushButton(self.frame_error)
        self.pushButton_close_popup.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_close_popup.setStyleSheet("QPushButton {\n"
                                                  "    border-radius: 5px;    \n"
                                                  "    background-position: center;    \n"
                                                  "    background-image: url(:/assets/cil-x.png);\n"
                                                  "    background-color: rgb(60, 60, 60);\n"
                                                  "}\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: rgb(50, 50, 50);    \n"
                                                  "    color: rgb(200, 200, 200);\n"
                                                  "}\n"
                                                  "QPushButton:pressed {\n"
                                                  "    background-color: rgb(35, 35, 35);    \n"
                                                  "    color: rgb(200, 200, 200);\n"
                                                  "}")
        self.pushButton_close_popup.setText("")
        self.pushButton_close_popup.setObjectName("pushButton_close_popup")
        self.horizontalLayout_3.addWidget(self.pushButton_close_popup)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet("border-radius: 10px;")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.logo = QtWidgets.QFrame(self.login_area)
        self.logo.setGeometry(QtCore.QRect(90, 100, 271, 131))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.logo.setMouseTracking(False)
        self.logo.setStyleSheet("background-repeat: cover;\n"
                                "background-image: url(:/assets/logobranco.webp);\n"
                                "background-position: center;\n"
                                "\n"
                                "\n"
                                "\n"
                                "")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.lineEdit_user = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_user.setGeometry(QtCore.QRect(85, 288, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setStyleSheet("QLineEdit {\n"
                                         "    border: 2px solid rgb(45, 45, 45);\n"
                                         "    border-radius: 5px;\n"
                                         "    padding: 15px;\n"
                                         "    background-color: rgb(30, 30, 30);    \n"
                                         "    color: rgb(100, 100, 100);\n"
                                         "}\n"
                                         "QLineEdit:hover {\n"
                                         "    border: 2px solid rgb(55, 55, 55);\n"
                                         "}\n"
                                         "QLineEdit:focus {\n"
                                         "    border: 2px solid rgb(255, 207, 0);    \n"
                                         "    color: rgb(200, 200, 200);\n"
                                         "}")
        self.lineEdit_user.setMaxLength(32)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_password.setGeometry(QtCore.QRect(85, 340, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("QLineEdit {\n"
                                             "    border: 2px solid rgb(45, 45, 45);\n"
                                             "    border-radius: 5px;\n"
                                             "    padding: 15px;\n"
                                             "    background-color: rgb(30, 30, 30);    \n"
                                             "    color: rgb(100, 100, 100);\n"
                                             "}\n"
                                             "QLineEdit:hover {\n"
                                             "    border: 2px solid rgb(55, 55, 55);\n"
                                             "}\n"
                                             "QLineEdit:focus {\n"
                                             "    border: 2px solid rgb(255, 207, 0);    \n"
                                             "    color: rgb(200, 200, 200);\n"
                                             "}")
        self.lineEdit_password.setMaxLength(16)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_login = QtWidgets.QPushButton(self.login_area)
        self.pushButton_login.setGeometry(QtCore.QRect(85, 425, 280, 50))
        self.pushButton_login.setStyleSheet("QPushButton {    \n"
                                            "    background-color: rgb(50, 50, 50);\n"
                                            "    border: 2px solid rgb(60, 60, 60);\n"
                                            "    border-radius: 5px;\n"
                                            "}\n"
                                            "QPushButton:hover {    \n"
                                            "    background-color: rgb(60, 60, 60);\n"
                                            "    border: 2px solid rgb(70, 70, 70);\n"
                                            "}\n"
                                            "QPushButton:pressed {    \n"
                                            "    background-color: rgb(250, 230, 0);\n"
                                            "    border: 2px solid rgb(255, 165, 24);    \n"
                                            "    color: rgb(35, 35, 35);\n"
                                            "}")
        self.pushButton_login.setObjectName("pushButton_login")
        self.lineEdit_user.raise_()
        self.lineEdit_password.raise_()
        self.pushButton_login.raise_()
        self.logo.raise_()
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom.setStyleSheet("background-color: rgb(15, 15, 15)")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_credits = QtWidgets.QLabel(self.bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(75, 75, 75);")
        self.label_credits.setText("")
        self.label_credits.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout_2.addWidget(self.label_credits)
        self.verticalLayout.addWidget(self.bottom)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        # FUNCTIONS ###############################################
        self.frame_error.hide()

        # BT CLOSE POPUP
        self.pushButton_close_popup.clicked.connect(
            lambda: self.frame_error.hide())

        # BT LOGIN
        self.pushButton_login.clicked.connect(self.checkFields)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def setStyle(self):
        self.styleLineEditOk = ("QLineEdit {\n"
                                "    border: 2px solid rgb(45, 45, 45);\n"
                                "    border-radius: 5px;\n"
                                "    padding: 15px;\n"
                                "    background-color: rgb(30, 30, 30);    \n"
                                "    color: rgb(100, 100, 100);\n"
                                "}\n"
                                "QLineEdit:hover {\n"
                                "    border: 2px solid rgb(55, 55, 55);\n"
                                "}\n"
                                "QLineEdit:focus {\n"
                                "    border: 2px solid rgb(255, 207, 0);    \n"
                                "    color: rgb(200, 200, 200);\n"
                                "}")

        self.styleLineEditError = ("QLineEdit {\n"
                                   "    border: 2px solid rgb(255, 85, 127);\n"
                                   "    border-radius: 5px;\n"
                                   "    padding: 15px;\n"
                                   "    background-color: rgb(30, 30, 30);    \n"
                                   "    color: rgb(100, 100, 100);\n"
                                   "}\n"
                                   "QLineEdit:hover {\n"
                                   "    border: 2px solid rgb(55, 55, 55);\n"
                                   "}\n"
                                   "QLineEdit:focus {\n"
                                   "    border: 2px solid rgb(255, 207, 0);    \n"
                                   "    color: rgb(200, 200, 200);\n"
                                   "}")

        self.stylePopupError = (
            "background-color: rgb(255, 85, 127); border-radius: 5px;")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_error.setText(_translate("MainWindow", "Error"))
        self.logo.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/assets/cil-x.png\" /></p></body></html>"))
        self.logo.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><img width=\"400\" height=\"300\" src=\":/assets/logobranco.webp\"/></p></body></html>"))
        self.lineEdit_user.setPlaceholderText(_translate("MainWindow", "USER"))
        self.lineEdit_password.setPlaceholderText(
            _translate("MainWindow", "PASSWORD"))
        self.pushButton_login.setText(_translate("MainWindow", "LOGIN"))

    def showMessage(self, message):
        self.frame_error.show()
        self.label_error.setText(message)
        QtCore.QTimer.singleShot(3000, self.frame_error.hide)

    def checkFields(self):
        login = self.lineEdit_user.text()
        password = self.lineEdit_password.text()
        print(login, password)

        # CHECK USER
        if login + password == '':
            self.showMessage('Campos em branco!')
            self.lineEdit_user.setStyleSheet(self.styleLineEditError)
            self.lineEdit_password.setStyleSheet(self.styleLineEditError)
        elif not login:
            self.showMessage('Login em branco!')
            self.lineEdit_user.setStyleSheet(self.styleLineEditOk)
        elif not password:
            self.showMessage('Senha em branco!')
            self.lineEdit_password.setStyleSheet(self.styleLineEditOk)
        else:
            if api.Login(login.strip(), password.strip()):
                navigation.changeScreen('home')
                navigation.SCREENS['home'].displayVideos()
            else:
                self.showMessage('Credenciais inválidas!')


class HomeScrean(QMainWindow):

    def __init__(self, parent=None):
        super(HomeScrean, self).__init__(parent)
        self.setupUi()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def setupUi(self):
        self.setWindowTitle('Gesec Galeria')
        self.resize(822, 568)
        self.setStyleSheet("color: rgb(200, 200, 200);\n"
                           "background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(15, -1, 15, 15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setMinimumSize(QtCore.QSize(0, 50))
        self.homeButton.setMaximumSize(QtCore.QSize(250, 16777215))
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton.setStyleSheet("QPushButton {    \n"
                                      "    background-color: rgb(50, 50, 50);\n"
                                      "    border: 2px solid rgb(60, 60, 60);\n"
                                      "    border-radius: 5px;\n"
                                      "font-weight: 900;\n"
                                      "}\n"
                                      "QPushButton:hover {    \n"
                                      "    background-color: rgb(60, 60, 60);\n"
                                      "    border: 2px solid rgb(70, 70, 70);\n"
                                      "}\n"
                                      "")
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout.addWidget(self.homeButton)
        self.addVideoButton = QtWidgets.QPushButton(self.centralwidget)
        self.addVideoButton.setMinimumSize(QtCore.QSize(0, 50))
        self.addVideoButton.setMaximumSize(QtCore.QSize(250, 16777215))
        self.addVideoButton.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addVideoButton.setStyleSheet("QPushButton {    \n"
                                          "    background-color: rgb(50, 50, 50);\n"
                                          "    border: 2px solid rgb(60, 60, 60);\n"
                                          "    border-radius: 5px;\n"
                                          "font-weight: 900;\n"
                                          "\n"
                                          "}\n"
                                          "QPushButton:hover {    \n"
                                          "    background-color: rgb(60, 60, 60);\n"
                                          "    border: 2px solid rgb(70, 70, 70);\n"
                                          "}\n"
                                          "")
        self.addVideoButton.setObjectName("addVideoButton")
        self.horizontalLayout.addWidget(self.addVideoButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.contentEdit = QtWidgets.QFrame(self.centralwidget)
        self.contentEdit.setMinimumSize(QtCore.QSize(781, 411))
        self.contentEdit.setMaximumSize(QtCore.QSize(781, 411))
        self.contentEdit.setStyleSheet("background-color: rgb(61, 56, 70);\n"
                                       "border-radius: 15px;\n"
                                       "")
        self.contentEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentEdit.setObjectName("contentEdit")
        self.label = QtWidgets.QLabel(self.contentEdit)
        self.label.setGeometry(QtCore.QRect(30, 10, 91, 41))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.contentEdit)
        self.scrollArea.setGeometry(QtCore.QRect(50, 70, 671, 320))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 320))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 300))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 1260, 306))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(
            self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMaximumSize(QtCore.QSize(50, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setMinimumSize(QtCore.QSize(600, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(600, 290))
        self.frame_2.setStyleSheet("    background-color: rgb(50, 50, 50);\n"
                                   "    border: 2px solid rgb(60, 60, 60);\n"
                                   "    border-radius: 5px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 571, 31))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setGeometry(QtCore.QRect(385, 51, 191, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(353, 50, 20, 221))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.frame_2, 0, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.add_video = QtWidgets.QFrame(self.contentEdit)
        self.add_video.setGeometry(QtCore.QRect(0, 0, 781, 411))
        self.add_video.setStyleSheet("background-color: rgb(61, 56, 70);\n"
                                     "border-radius: 15px;\n"
                                     "")
        self.add_video.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_video.setObjectName("add_video")
        self.label_6 = QtWidgets.QLabel(self.add_video)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 211, 41))
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        self.groupBox = QtWidgets.QGroupBox(self.add_video)
        self.groupBox.setGeometry(QtCore.QRect(30, 70, 381, 61))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 30, 361, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "    border-radius: 0px;\n"
                                      "")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.add_video)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 160, 371, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.input_video = QtWidgets.QLineEdit(self.groupBox_2)
        self.input_video.setGeometry(QtCore.QRect(0, 30, 251, 30))
        self.input_video.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.input_video.setObjectName("input_video")
        self.searchVideo = QtWidgets.QPushButton(self.groupBox_2)
        self.searchVideo.setGeometry(QtCore.QRect(260, 30, 100, 31))
        self.searchVideo.setMinimumSize(QtCore.QSize(0, 31))
        self.searchVideo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.searchVideo.setStyleSheet("QPushButton {    \n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "    border: 2px solid rgb(60, 60, 60);\n"
                                       "    border-radius: 5px;\n"
                                       "font-weight: 900;\n"
                                       "}\n"
                                       "QPushButton:hover {    \n"
                                       "    background-color: rgb(60, 60, 60);\n"
                                       "    border: 2px solid rgb(70, 70, 70);\n"
                                       "}\n"
                                       "")
        self.searchVideo.setObjectName("searchVideo")
        self.groupBox_3 = QtWidgets.QGroupBox(self.add_video)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 240, 371, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.input_capa = QtWidgets.QLineEdit(self.groupBox_3)
        self.input_capa.setGeometry(QtCore.QRect(0, 30, 251, 30))
        self.input_capa.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(0, 0, 0);")
        self.input_capa.setObjectName("input_capa")
        self.searchCapa = QtWidgets.QPushButton(self.groupBox_3)
        self.searchCapa.setGeometry(QtCore.QRect(260, 30, 100, 31))
        self.searchCapa.setMinimumSize(QtCore.QSize(0, 31))
        self.searchCapa.setMaximumSize(QtCore.QSize(100, 16777215))
        self.searchCapa.setStyleSheet("QPushButton {    \n"
                                      "    background-color: rgb(50, 50, 50);\n"
                                      "    border: 2px solid rgb(60, 60, 60);\n"
                                      "    border-radius: 5px;\n"
                                      "font-weight: 900;\n"
                                      "}\n"
                                      "QPushButton:hover {    \n"
                                      "    background-color: rgb(60, 60, 60);\n"
                                      "    border: 2px solid rgb(70, 70, 70);\n"
                                      "}\n"
                                      "")
        self.searchCapa.setObjectName("searchCapa")
        self.groupBox_4 = QtWidgets.QGroupBox(self.add_video)
        self.groupBox_4.setGeometry(QtCore.QRect(450, 70, 301, 251))
        self.groupBox_4.setObjectName("groupBox_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 30, 291, 221))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "color: rgb(0, 0, 0);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.buttonClear = QtWidgets.QPushButton(self.add_video)
        self.buttonClear.setGeometry(QtCore.QRect(40, 350, 95, 39))
        self.buttonClear.setMaximumSize(QtCore.QSize(95, 45))
        self.buttonClear.setStyleSheet("QPushButton {    \n"
                                       "color: rgb(192, 28, 40);\n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "    border: 2px solid rgb(60, 60, 60);\n"
                                       "    border-radius: 5px;\n"
                                       "font-weight: 800;\n"
                                       "}\n"
                                       "QPushButton:hover {    \n"
                                       "    background-color: rgb(60, 60, 60);\n"
                                       "    border: 2px solid rgb(70, 70, 70);\n"
                                       "}\n"
                                       "")
        self.buttonClear.setObjectName("buttonClear")
        self.buttonSend = QtWidgets.QPushButton(self.add_video)
        self.buttonSend.setGeometry(QtCore.QRect(170, 350, 95, 39))
        self.buttonSend.setMaximumSize(QtCore.QSize(95, 45))
        self.buttonSend.setStyleSheet("QPushButton {    \n"
                                      "    color: rgb(87, 227, 137);\n"
                                      "    background-color: rgb(50, 50, 50);\n"
                                      "    border: 2px solid rgb(60, 60, 60);\n"
                                      "    border-radius: 5px;\n"
                                      "font-weight: 800;\n"
                                      "}\n"
                                      "QPushButton:hover {    \n"
                                      "    background-color: rgb(60, 60, 60);\n"
                                      "    border: 2px solid rgb(70, 70, 70);\n"
                                      "}")
        self.buttonSend.setObjectName("buttonSend")
        self.gridLayout.addWidget(self.contentEdit, 1, 0, 1, 1)
        self.contentEdit.raise_()
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(self)
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        # actions
        self.add_video.hide()
        self.homeButton.clicked.connect(self.showHome)
        self.addVideoButton.clicked.connect(lambda: self.add_video.show())

        self.searchVideo.clicked.connect(
            lambda: self.openFileVideo("Selecionar Video", self.input_video))
        self.searchCapa.clicked.connect(
            lambda: self.openFileImage("Selecionar Capa", self.input_capa))

        self.buttonClear.clicked.connect(self.clearAddVideo)
        self.buttonSend.clicked.connect(self.sendNewVideo)

    def showHome(self):
        self.displayVideos()
        self.add_video.hide()

    def displayVideos(self):
        itens = api.AllVideos()
        print(itens)

        n = 0
        for item in itens:
            n += 1
            card = self.createCard(item)
            self.gridLayout_2.addWidget(card, 0, n, 1, 1)

    def createCard(self, item):
        url_video = os.getenv('URL_BACK') + '/' + item['video']
        url_image = os.getenv('URL_BACK') + '/' + item['thumbnail']

        card = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        card.setMinimumSize(QtCore.QSize(620, 0))
        card.setMaximumSize(QtCore.QSize(600, 290))
        card.setStyleSheet("border: 2px solid ;\n"
                           "border-color: rgb(50, 50, 50);\n"
                           "border-radius: 15px;\n"
                           "color: rgb(143, 240, 164);\n"
                           "background-color: rgb(50, 50, 50);\n"
                           "")
        card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        card.setFrameShadow(QtWidgets.QFrame.Raised)
        card.setObjectName("frame_3")
        label_4 = QtWidgets.QLabel(card)
        label_4.setGeometry(QtCore.QRect(30, 10, 561, 31))
        label_4.setObjectName("label_4")
        textBrowser_3 = QtWidgets.QTextBrowser(card)
        textBrowser_3.setGeometry(QtCore.QRect(400, 50, 201, 221))
        textBrowser_3.setStyleSheet("color: rgb(255, 255, 255);")
        textBrowser_3.setObjectName("textBrowser_3")
        line_4 = QtWidgets.QFrame(card)
        line_4.setGeometry(QtCore.QRect(370, 50, 16, 221))
        line_4.setStyleSheet("border-color: rgb(119, 118, 123);")
        line_4.setFrameShape(QtWidgets.QFrame.VLine)
        line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        line_4.setObjectName("line_4")

        # image video
        image = QImage()
        image.height = 80
        image.width = 90
        image.loadFromData(requests.get(url_image).content)
        imageLabel = QtWidgets.QLabel(card)
        imageLabel.setGeometry(QtCore.QRect(20, 50, 341, 181))
        imageLabel.setStyleSheet("border-color: rgb(94, 92, 100);")
        imageLabel.setObjectName("imageLabel")
        imageLabel.setPixmap(QPixmap(image))
        imageLabel.show()

        horizontalLayoutWidget = QtWidgets.QWidget(card)
        horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 240, 341, 41))
        horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        horizontalLayout_2 = QtWidgets.QHBoxLayout(
            horizontalLayoutWidget)
        horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        buttonDisplayVideo = QtWidgets.QPushButton(horizontalLayoutWidget)
        buttonDisplayVideo.setMaximumSize(QtCore.QSize(95, 45))
        buttonDisplayVideo.setStyleSheet("QPushButton {    \n"
                                         "    color: rgb(87, 227, 137);\n"
                                         "    background-color: rgb(50, 50, 50);\n"
                                         "    border: 2px solid rgb(60, 60, 60);\n"
                                         "    border-radius: 5px;\n"
                                         "font-weight: 800;\n"
                                         "}\n"
                                         "QPushButton:hover {    \n"
                                         "    background-color: rgb(60, 60, 60);\n"
                                         "    border: 2px solid rgb(70, 70, 70);\n"
                                         "}")
        buttonDisplayVideo.setObjectName("buttonDisplayVideo")
        horizontalLayout_2.addWidget(buttonDisplayVideo)
        pushButton_2 = QtWidgets.QPushButton(horizontalLayoutWidget)
        pushButton_2.setMaximumSize(QtCore.QSize(95, 45))
        pushButton_2.setStyleSheet("QPushButton {    \n"
                                   "color: rgb(192, 28, 40);\n"
                                   "    background-color: rgb(50, 50, 50);\n"
                                   "    border: 2px solid rgb(60, 60, 60);\n"
                                   "    border-radius: 5px;\n"
                                   "font-weight: 800;\n"
                                   "}\n"
                                   "QPushButton:hover {    \n"
                                   "    background-color: rgb(60, 60, 60);\n"
                                   "    border: 2px solid rgb(70, 70, 70);\n"
                                   "}\n"
                                   "")
        pushButton_2.setObjectName("pushButton_2")
        horizontalLayout_2.addWidget(pushButton_2)

        _translate = QtCore.QCoreApplication.translate
        label_4.setText(_translate(
            "MainWindow", f'''<html><head/><body><p align="center"><span style= "font-size:14pt"\>{item['title']}</span></p></body></html>'''))
        textBrowser_3.setHtml(_translate("MainWindow", f'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
                                         <html><head><meta name="qrichtext" content="1" /><style type="text/css">'''+"p, li { white-space: pre-wrap; }" +
                                         f'''</style></head><body style=" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
                                         <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">{item['description']}</p></body></html>'''))
        buttonDisplayVideo.setText(_translate("MainWindow", "Assistir"))
        pushButton_2.setText(_translate("MainWindow", "Excluir"))

        # actions
        buttonDisplayVideo.clicked.connect(
            lambda: self.showVideo(url_video, item['title']))
        pushButton_2.clicked.connect(self.deleteVideo)

        return card

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.homeButton.setText(_translate("MainWindow", "HOME"))
        self.addVideoButton.setText(_translate("MainWindow", "ADD VIDEOS"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Galeria</span></p></body></html>"))
        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">NOME DO VIDEO</span></p></body></html>"))
        self.label_6.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Adicionar Video</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Nome do Video"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Selecionar Video"))
        self.searchVideo.setText(_translate("MainWindow", "Procurar"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Selecionar Capa"))
        self.searchCapa.setText(_translate("MainWindow", "Procurar"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Descrição"))
        self.buttonClear.setText(_translate("MainWindow", "Limpar"))
        self.buttonSend.setText(_translate("MainWindow", "Enviar"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    def openFileImage(self, title, obj):
        file_path, _ = QFileDialog.getOpenFileName(self, title,
                                                   QDir.homePath(), filter="Imagens (*.png *.jpeg *.jpg *.gif);;Todos os arquivos (*)")
        obj.setText(file_path)

        return file_path

    def openFileVideo(self, title, obj):
        file_path, _ = QFileDialog.getOpenFileName(self, title,
                                                   QDir.homePath(), filter="Vídeos (*.mp4 *.avi *.mkv);;Todos os arquivos (*)")
        obj.setText(file_path)

        return file_path

    def clearAddVideo(self):
        self.input_video.setText('')
        self.input_capa.setText('')
        self.lineEdit_2.setText('')
        self.plainTextEdit.setPlainText('')

    def sendNewVideo(self):
        video_path = self.input_video.text()
        thumbnail_path = self.input_capa.text()
        title = self.lineEdit_2.text()
        description = self.plainTextEdit.toPlainText()
        if video_path and thumbnail_path and title and description:
            api.CreateVideo(title, thumbnail_path, video_path, description)
            self.clearAddVideo()
        

    def deleteVideo(self):
        print('delete')

    def showVideo(self, url, name):
        navigation.changeScreen('video_play', False)
        navigation.SCREENS['video_play'].showVideo(url, name)


class VideoPlayer(QMainWindow):
    def __init__(self):
        super(VideoPlayer, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(640, 480)
        self.setStyleSheet("color: rgb(200, 200, 200);\n"
                           "background-color: rgb(10, 10, 10);")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.error = QLabel()
        self.error.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)

        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.error)

        # Set widget to contain window contents
        wid.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

    def showVideo(self, urllink: str, name: str):
        self.setWindowTitle(name)
        url = QUrl(urllink)
        self.media_content = QMediaContent(url)
        self.mediaPlayer.setMedia(self.media_content)
        self.playButton.setEnabled(True)

    def exitCall(self):
        sys.exit(app.exec_())

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.error.setText("Error: " + self.mediaPlayer.errorString())

    def closeEvent(self, event):
        self.mediaPlayer.pause()


if __name__ == '__main__':
    load_dotenv()

    app = QApplication(sys.argv)
    api = RequestsBack()

    # Create user - for testing purposes
    #api.Register('admin', '123456')

    navigation = Navigation()
    navigation.addScreen('login', LoginScreen)
    navigation.addScreen('home', HomeScrean)
    navigation.addScreen('video_play', VideoPlayer)

    navigation.showScreen('login')

    sys.exit(app.exec_())
