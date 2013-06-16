# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\github\y86-simulator\compiler\TextEditor.ui'
#
# Created: Sat Jun 15 23:22:39 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1002, 627)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1001, 621))
        self.frame.setStyleSheet(_fromUtf8("QFrame {background-color: rgba(255, 255, 255, 0%);\n"
"        border-image: url(\'bg2.jpg\');}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.openButton = QtGui.QPushButton(self.frame)
        self.openButton.setGeometry(QtCore.QRect(70, 72, 81, 41))
        self.openButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.openButton.setStyleSheet(_fromUtf8("QPushButton,\n"
"QToolButton {\n"
"    selection-color: none;\n"
"    background-color:none;\n"
"  \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover,\n"
"QToolButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222,222,222,5%), stop:1 rgb(222,222,222,10%));\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QToolButton:pressed,\n"
"QPushButton:on,\n"
"QToolButton:on {\n"
"    qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,0,0,18%), stop:1 rgb(0,0,0,25%));\n"
"}"))
        self.openButton.setText(_fromUtf8(""))
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.saveButton = QtGui.QPushButton(self.frame)
        self.saveButton.setGeometry(QtCore.QRect(250, 72, 75, 41))
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveButton.setStyleSheet(_fromUtf8("QPushButton,\n"
"QToolButton {\n"
"    selection-color: none;\n"
"    background-color:none;\n"
"  \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover,\n"
"QToolButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222,222,222,5%), stop:1 rgb(222,222,222,10%));\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QToolButton:pressed,\n"
"QPushButton:on,\n"
"QToolButton:on {\n"
"    qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,0,0,18%), stop:1 rgb(0,0,0,25%));\n"
"}"))
        self.saveButton.setText(_fromUtf8(""))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(410, 70, 111, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton,\n"
"QToolButton {\n"
"    selection-color: none;\n"
"    background-color:none;\n"
"  \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover,\n"
"QToolButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222,222,222,5%), stop:1 rgb(222,222,222,10%));\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QToolButton:pressed,\n"
"QPushButton:on,\n"
"QToolButton:on {\n"
"    qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,0,0,18%), stop:1 rgb(0,0,0,25%));\n"
"}"))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 70, 141, 31))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton,\n"
"QToolButton {\n"
"    selection-color: none;\n"
"    background-color:none;\n"
"  \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover,\n"
"QToolButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222,222,222,5%), stop:1 rgb(222,222,222,10%));\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QToolButton:pressed,\n"
"QPushButton:on,\n"
"QToolButton:on {\n"
"    qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,0,0,18%), stop:1 rgb(0,0,0,25%));\n"
"}"))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.runButton = QtGui.QPushButton(self.frame)
        self.runButton.setGeometry(QtCore.QRect(804, 80, 71, 23))
        self.runButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.runButton.setStyleSheet(_fromUtf8("QPushButton,\n"
"QToolButton {\n"
"    selection-color: none;\n"
"    background-color:none;\n"
"  \n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover,\n"
"QToolButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222,222,222,5%), stop:1 rgb(222,222,222,10%));\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QToolButton:pressed,\n"
"QPushButton:on,\n"
"QToolButton:on {\n"
"    qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,0,0,18%), stop:1 rgb(0,0,0,25%));\n"
"}"))
        self.runButton.setText(_fromUtf8(""))
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.codeout = QtGui.QTextBrowser(self.centralWidget)
        self.codeout.setGeometry(QtCore.QRect(520, 140, 411, 211))
        self.codeout.setAutoFillBackground(False)
        self.codeout.setStyleSheet(_fromUtf8("QTextEdit {\n"
"font-size : 15px;\n"
"    font: 9pt \"å®‹ä½“\";\n"
"background:none;\n"
"border:none;\n"
"}"))
        self.codeout.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.codeout.setObjectName(_fromUtf8("codeout"))
        self.codein = QtGui.QTextEdit(self.centralWidget)
        self.codein.setGeometry(QtCore.QRect(70, 140, 411, 241))
        self.codein.setStyleSheet(_fromUtf8("QTextEdit {\n"
"font-size : 15px;\n"
"    font: 9pt \"å®‹ä½“\";\n"
"background:none;\n"
"border:none;\n"
"}"))
        self.codein.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.codein.setObjectName(_fromUtf8("codein"))
        self.console = QtGui.QTextBrowser(self.centralWidget)
        self.console.setGeometry(QtCore.QRect(70, 460, 831, 111))
        self.console.setStyleSheet(_fromUtf8("QTextEdit {\n"
"font-size : 15px;\n"
"    font: 9pt \"å®‹ä½“\";\n"
"background:none;\n"
"border:none;\n"
"}"))
        self.console.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.console.setObjectName(_fromUtf8("console"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

