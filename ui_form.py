# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setKerning(True)
        Widget.setFont(font)
        icon = QIcon()
        icon.addFile(u"url.ico", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        Widget.setStyleSheet(u"background-color: rgb(44, 62, 80);")
        self.longUrlBox = QPlainTextEdit(Widget)
        self.longUrlBox.setObjectName(u"longUrlBox")
        self.longUrlBox.setGeometry(QRect(170, 140, 280, 30))
        font1 = QFont()
        font1.setFamilies([u"Cascadia Mono SemiLight"])
        font1.setPointSize(10)
        self.longUrlBox.setFont(font1)
        self.longUrlBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.generateButton = QPushButton(Widget)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setGeometry(QRect(270, 200, 100, 30))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setBold(True)
        self.generateButton.setFont(font2)
        self.generateButton.setStyleSheet(u"background-color: rgb(52, 152, 219);\n"
"color: rgb(236, 240, 241);")
        self.copyButton = QPushButton(Widget)
        self.copyButton.setObjectName(u"copyButton")
        self.copyButton.setGeometry(QRect(270, 320, 100, 30))
        self.copyButton.setFont(font2)
        self.copyButton.setStyleSheet(u"background-color: rgb(52, 152, 219);\n"
"color: rgb(236, 240, 241);")
        self.copyButton.setFlat(False)
        self.shortUrlBox = QPlainTextEdit(Widget)
        self.shortUrlBox.setObjectName(u"shortUrlBox")
        self.shortUrlBox.setGeometry(QRect(170, 260, 280, 30))
        font3 = QFont()
        font3.setFamilies([u"Fira Code"])
        font3.setPointSize(10)
        self.shortUrlBox.setFont(font3)
        self.shortUrlBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 10, 201, 61))
        self.label.setStyleSheet(u"background-color: rgb(44, 62, 80);\n"
"color: rgb(236, 240, 241);\n"
"font: 22pt \"Arial\";")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.generateButton.setText(QCoreApplication.translate("Widget", u"Generate", None))
        self.copyButton.setText(QCoreApplication.translate("Widget", u"Copy", None))
        self.label.setText(QCoreApplication.translate("Widget", u"URL Shortener", None))
    # retranslateUi

