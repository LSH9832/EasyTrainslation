# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'translation.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(467, 371)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textoutput = QtWidgets.QTextBrowser(self.centralwidget)
        self.textoutput.setEnabled(True)
        self.textoutput.setGeometry(QtCore.QRect(10, 40, 451, 321))
        self.textoutput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textoutput.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.textoutput.setStyleSheet("")
        self.textoutput.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textoutput.setObjectName("textoutput")
        self.floatWindowMode = QtWidgets.QCheckBox(self.centralwidget)
        self.floatWindowMode.setGeometry(QtCore.QRect(10, 2, 131, 31))
        self.floatWindowMode.setStyleSheet("")
        self.floatWindowMode.setObjectName("floatWindowMode")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(410, 10, 51, 25))
        self.exit.setStyleSheet("")
        self.exit.setObjectName("exit")
        self.deepColorMode = QtWidgets.QCheckBox(self.centralwidget)
        self.deepColorMode.setGeometry(QtCore.QRect(130, 2, 92, 31))
        self.deepColorMode.setObjectName("deepColorMode")
        MainWindow.setCentralWidget(self.centralwidget)
        self.autoGetText = QtWidgets.QAction(MainWindow)
        self.autoGetText.setCheckable(True)
        self.autoGetText.setObjectName("autoGetText")
        self.autoTranslate = QtWidgets.QAction(MainWindow)
        self.autoTranslate.setCheckable(True)
        self.autoTranslate.setObjectName("autoTranslate")
        self.floatWindow = QtWidgets.QAction(MainWindow)
        self.floatWindow.setCheckable(True)
        self.floatWindow.setObjectName("floatWindow")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "简易翻译"))
        self.textoutput.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.floatWindowMode.setText(_translate("MainWindow", "浮窗跟随模式"))
        self.exit.setText(_translate("MainWindow", "退出"))
        self.deepColorMode.setText(_translate("MainWindow", "深色模式"))
        self.autoGetText.setText(_translate("MainWindow", "自动获取选中文本"))
        self.autoTranslate.setText(_translate("MainWindow", "自动翻译"))
        self.floatWindow.setText(_translate("MainWindow", "浮窗模式（开发中）"))
