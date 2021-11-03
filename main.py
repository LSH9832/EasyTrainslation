from packages.translation_ui2py import Ui_MainWindow as MAIN

from sys             import argv, exit

from PyQt5           import QtCore, QtGui, Qt
from PyQt5.QtCore    import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui     import QIcon

from packages.translate import *
from pymouse import PyMouse as mouse

import os
# from PyQt5           import *
# import multiprocessing as mp

# 主窗口
#######################################################################################################################
class MainWindow(QMainWindow, MAIN):

    # 初始化函数
    ###################################################################################################################
    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)
        super(MainWindow, self).setupUi(self)
        # loadUi('main.ui', self)

        # 加载图标
        self.loadIcon()

        self.exit.clicked.connect(self.closeFun)
        self.deepColorMode.clicked.connect(self.setColorMode)
        self.floatWindowMode.clicked.connect(self.setFloatWindow)

        self.timer = QTimer()  # 定时器，或者计时器， whatever
        self.timer.timeout.connect(self.timeoutFun)  # 每2000毫秒自动运行一次的函数
        self.timer.start(300)

        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.timeoutFun2)
        self.timer2.start(1)


        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumSize(300, 300)


        self.highlightText = ''
        self.originText = ''
        self.mouse = mouse()
        self.updatePos = False
        self.waitingForChange = False
        self.moveEnable = False
        self.changeSizeEnable = False
        self.dx = 0
        self.dy = 0
        self.dx2 = 0
        self.dy2 = 0
        self.screenRect = QApplication.desktop().screenGeometry()



        self.highlightText = os.popen('echo $(xsel -o)').read()
        if self.highlightText.endswith('\n'):
            self.highlightText = self.highlightText[:-1]

    def closeFun(self):
        self.close()
        exit(0)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.dx = self.geometry().x() - self.mouse.position()[0]
        self.dy = self.geometry().y() - self.mouse.position()[1]
        dx2 = self.dx + self.geometry().width()
        dy2 = self.dy + self.geometry().height()

        if dx2 <= 10 and dy2 <= 10:
            self.changeSizeEnable = True
            self.dx2 = dx2
            self.dy2 = dy2
        else:
            self.moveEnable = True


    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.changeSizeEnable = False
        self.moveEnable = False

    @staticmethod
    def preprocess(text):
        return text.replace('-\r', '').replace('-\n', '').replace('\n', ' ').replace('\r',' ')

    # 翻译按钮
    def translate(self, text):
        # print("你按了 " + self.translate.text() + " 这个按钮")
        text = self.preprocess(text)

        result = baidu_translate(text)['trans_result'][0]['dst']

        # print(text, result)
        self.originText = text
        self.textoutput.setText(result)


    def setFloatWindow(self):
        pass

    def setColorMode(self):
        if self.deepColorMode.isChecked():
            styleSheet = '''QMainWindow{background-color:black;}
QTextBrowser{background-color:rgb(50,50,50);color:rgb(180,180,180);}
QCheckBox{color:rgb(150,150,150);}
QPushButton{background-color:rgb(80,80,80);color:white}'''
        else:
            styleSheet = ''

        self.setStyleSheet(styleSheet)

    # 自动运行的函数
    def timeoutFun(self):
        # print('123')
        this_highlightText = os.popen('echo $(xsel -o)').read()
        if this_highlightText.endswith('\n'):
            this_highlightText = this_highlightText[:-1]


        if len(this_highlightText) and not self.highlightText == this_highlightText:
            # print('changed from "%s" to "%s"' % (self.highlightText, this_highlightText))
            self.highlightText = this_highlightText
            self.waitingForChange = True

        elif len(this_highlightText) and self.highlightText == this_highlightText:
            if self.waitingForChange:
                self.waitingForChange = False
                if len(self.highlightText) and not self.preprocess(self.highlightText) == self.originText:
                    self.translate(self.highlightText)
                    self.originText = self.preprocess(self.highlightText)
                    self.updatePos = True

    def timeoutFun2(self):
        g = self.geometry()
        x,y,w,h = g.x(),g.y(),g.width(),g.height()

        # print(self.changeSizeEnable)

        self.textoutput.setGeometry(10,40, w-20, h-50)
        ew, eh = self.exit.geometry().width(),self.exit.geometry().height()
        self.exit.setGeometry(w - ew - 10, 8, ew, eh)
        fw, fh = self.floatWindowMode.geometry().width(), self.floatWindowMode.geometry().height()
        self.floatWindowMode.setGeometry(10, 4, fw, fh)
        dw, dh = self.deepColorMode.geometry().width(), self.deepColorMode.geometry().height()
        self.deepColorMode.setGeometry(fw, 4, dw, dh)


        if self.moveEnable:
            x = self.mouse.position()[0] + self.dx
            y = self.mouse.position()[1] + self.dy
            self.setGeometry(x, y, w, h)

        elif self.changeSizeEnable:
            # print(x, y, w, h, self.mouse.position()[0], self.mouse.position()[1])
            w = min(self.mouse.position()[0] + self.dx2 - x, self.screenRect.width() - x - 1)
            h = min(self.mouse.position()[1] + self.dy2 - y, self.screenRect.height() - y - 1)
            self.setGeometry(x, y, w, h)

        elif self.floatWindowMode.isChecked() and self.updatePos:
            # print(666)
            self.updatePos = False
            x = self.mouse.position()[0] + 30
            y = self.mouse.position()[1] + 50
            self.setGeometry(x,y,w,h)

    # 加载图标
    def loadIcon(self):
        self.setWindowIcon(QIcon('icon.png'))

def main():
    app = QApplication(argv)
    w = MainWindow()
    w.show()
    exit(app.exec())


if __name__ == '__main__':
    # mp.freeze_support()
    # sudo apt install xsel python3-xlib
    # pip3 install pyqt5 pyqt5-tools pymouse PyUserInput
    main()