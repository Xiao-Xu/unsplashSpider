# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unsplush_spider.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from unsplash import auto_download
import threading
import globalvar


class Ui_UnsplushDownloader(object):
    def setupUi(self, UnsplushDownloader):
        UnsplushDownloader.setObjectName("UnsplushDownloader")
        UnsplushDownloader.resize(415, 273)
        self.centralwidget = QtWidgets.QWidget(UnsplushDownloader)
        self.centralwidget.setObjectName("centralwidget")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(270, 200, 113, 32))
        self.start_btn.setObjectName("start_btn")
        self.cance_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cance_btn.setGeometry(QtCore.QRect(150, 200, 113, 32))
        self.cance_btn.setObjectName("cance_btn")
        self.keyword_input = QtWidgets.QLineEdit(self.centralwidget)
        self.keyword_input.setGeometry(QtCore.QRect(130, 60, 241, 31))
        self.keyword_input.setInputMask("")

        self.keyword_input.setObjectName("keyword_input")
        self.mount_input = QtWidgets.QLineEdit(self.centralwidget)
        self.mount_input.setGeometry(QtCore.QRect(320, 110, 51, 31))
        self.mount_input.setObjectName("mount_input")
        self.results_lebal = QtWidgets.QLabel(self.centralwidget)
        self.results_lebal.setGeometry(QtCore.QRect(60, 150, 311, 21))
        self.results_lebal.setObjectName("results_lebal")
        self.mount_lable = QtWidgets.QLabel(self.centralwidget)
        self.mount_lable.setGeometry(QtCore.QRect(240, 110, 71, 31))
        self.mount_lable.setObjectName("mount_lable")
        self.keywords_lable = QtWidgets.QLabel(self.centralwidget)
        self.keywords_lable.setGeometry(QtCore.QRect(60, 60, 71, 31))
        self.keywords_lable.setObjectName("keywords_lable")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(40, 20, 151, 21))
        self.title.setObjectName("title")
        UnsplushDownloader.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UnsplushDownloader)
        self.statusbar.setObjectName("statusbar")
        UnsplushDownloader.setStatusBar(self.statusbar)

        self.retranslateUi(UnsplushDownloader)
        QtCore.QMetaObject.connectSlotsByName(UnsplushDownloader)

    def retranslateUi(self, UnsplushDownloader):
        _translate = QtCore.QCoreApplication.translate
        UnsplushDownloader.setWindowTitle(
            _translate("UnsplushDownloader", "MainWindow"))
        self.start_btn.setText(_translate("UnsplushDownloader", "开始"))
        self.cance_btn.setText(_translate("UnsplushDownloader", "取消"))
        self.results_lebal.setText(_translate("UnsplushDownloader", "一切准备就绪"))
        self.mount_lable.setText(_translate("UnsplushDownloader", "抓取数量："))
        self.keywords_lable.setText(_translate("UnsplushDownloader", "关键词："))
        self.title.setText(_translate(
            "UnsplushDownloader", "Unsplush 爬虫 by Sean"))

    def clicked(self):
        self.keywords = self.keyword_input.text()
        self.mount = self.mount_input.text()
        if globalvar.spyderstatu != True:
            self.t1 = threading.Thread(
                target=auto_download, args=(self.mount, self.keywords))
            self.t1.start()
            globalvar.message = '开始抓图'
            self.show_message(globalvar.message)
        else:
            globalvar.message = '已有抓图进程 如有新进程请先取消！'
            self.show_message(globalvar.message)

    def change_statu(self):
        globalvar.spyderstatu = False
        globalvar.message = '已结束'
        self.show_message(globalvar.message)

    def onclick(self):

        self.start_btn.clicked.connect(self.clicked)
        self.cance_btn.clicked.connect(self.change_statu)

    def show_message(self, mes):
        self.results_lebal.setText(mes)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UnsplushDownloader = QtWidgets.QMainWindow()
    ui = Ui_UnsplushDownloader()
    ui.setupUi(UnsplushDownloader)
    UnsplushDownloader.show()
    globalvar.message = '一切准备就绪'
    ui.onclick()
    sys.exit(app.exec_())
