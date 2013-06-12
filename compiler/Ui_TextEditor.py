# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator.PC-20120516GWLZ\Desktop\TextEditor-master\TextEditor.ui'
#
# Created: Wed Jun 12 18:10:37 2013
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
        self.openButton = QtGui.QPushButton(self.centralWidget)
        self.openButton.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.codein = QtGui.QTextEdit(self.centralWidget)
        self.codein.setGeometry(QtCore.QRect(10, 20, 481, 411))
        self.codein.setObjectName(_fromUtf8("codein"))
        self.saveButton = QtGui.QPushButton(self.centralWidget)
        self.saveButton.setGeometry(QtCore.QRect(90, 0, 75, 23))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.console = QtGui.QTextBrowser(self.centralWidget)
        self.console.setGeometry(QtCore.QRect(10, 430, 981, 181))
        self.console.setObjectName(_fromUtf8("console"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 0, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 0, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.codeout = QtGui.QTextBrowser(self.centralWidget)
        self.codeout.setGeometry(QtCore.QRect(490, 20, 501, 411))
        self.codeout.setObjectName(_fromUtf8("codeout"))
        self.runButton = QtGui.QPushButton(self.centralWidget)
        self.runButton.setGeometry(QtCore.QRect(330, 0, 75, 23))
        self.runButton.setObjectName(_fromUtf8("runButton"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.openButton.setText(_translate("MainWindow", "Open", None))
        self.saveButton.setText(_translate("MainWindow", "Save", None))
        self.pushButton.setText(_translate("MainWindow", "compile", None))
        self.pushButton_2.setText(_translate("MainWindow", "disassemble", None))
        self.runButton.setText(_translate("MainWindow", "run", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

