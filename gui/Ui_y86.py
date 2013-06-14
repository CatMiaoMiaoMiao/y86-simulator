# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\github\y86-simulator\gui\y86.ui'
#
# Created: Fri Jun 14 23:29:52 2013
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

class Ui_Y86Simulator(object):
    def setupUi(self, Y86Simulator):
        Y86Simulator.setObjectName(_fromUtf8("Y86Simulator"))
        Y86Simulator.resize(982, 692)
        Y86Simulator.setStyleSheet(_fromUtf8("QDialog\n"
"{\n"
"background:white;\n"
"}\n"
"QTextBrowser\n"
"{\n"
"border:white;\n"
"}"))
        self.label_23 = QtGui.QLabel(Y86Simulator)
        self.label_23.setGeometry(QtCore.QRect(320, 420, 21, 16))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(Y86Simulator)
        self.label_24.setGeometry(QtCore.QRect(390, 420, 21, 16))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_37 = QtGui.QLabel(Y86Simulator)
        self.label_37.setGeometry(QtCore.QRect(440, 420, 21, 16))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.frame = QtGui.QFrame(Y86Simulator)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 991, 691))
        self.frame.setStyleSheet(_fromUtf8("QFrame {background-color: rgba(255, 255, 255, 0%);\n"
"        border-image: url(\'bg1.jpg\');}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.Slider = QtGui.QSlider(self.frame)
        self.Slider.setGeometry(QtCore.QRect(640, 30, 160, 22))
        self.Slider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Slider.setStyleSheet(_fromUtf8("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 white, stop:1 rgb(222, 222, 222));\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(162, 162, 162), stop:1 rgb(222, 222, 222));\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 20px;\n"
"    margin: -2px 0;\n"
"    border-radius: 3px;\n"
"}"))
        self.Slider.setMinimum(1)
        self.Slider.setMaximum(100)
        self.Slider.setProperty("value", 100)
        self.Slider.setSliderPosition(100)
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Slider.setObjectName(_fromUtf8("Slider"))
        self.frequency = QtGui.QLineEdit(self.frame)
        self.frequency.setGeometry(QtCore.QRect(820, 30, 113, 20))
        self.frequency.setStyleSheet(_fromUtf8("QLineEdit{\n"
"background-color:none;\n"
"border-color: none;\n"
"border-width: none;\n"
"border-radius: 10px;}"))
        self.frequency.setObjectName(_fromUtf8("frequency"))
        self.resetButton = QtGui.QPushButton(self.frame)
        self.resetButton.setGeometry(QtCore.QRect(370, 70, 61, 31))
        self.resetButton.setStyleSheet(_fromUtf8("QPushButton,\n"
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
"}\n"
""))
        self.resetButton.setText(_fromUtf8(""))
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.backButton = QtGui.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(300, 70, 51, 31))
        self.backButton.setStyleSheet(_fromUtf8("QPushButton,\n"
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
"}\n"
""))
        self.backButton.setText(_fromUtf8(""))
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.stepButton = QtGui.QPushButton(self.frame)
        self.stepButton.setGeometry(QtCore.QRect(230, 70, 51, 31))
        self.stepButton.setStyleSheet(_fromUtf8("QPushButton,\n"
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
"}\n"
""))
        self.stepButton.setText(_fromUtf8(""))
        self.stepButton.setObjectName(_fromUtf8("stepButton"))
        self.pauseButton = QtGui.QPushButton(self.frame)
        self.pauseButton.setGeometry(QtCore.QRect(160, 80, 61, 31))
        self.pauseButton.setStyleSheet(_fromUtf8("QPushButton,\n"
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
"}\n"
""))
        self.pauseButton.setText(_fromUtf8(""))
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.runButton = QtGui.QPushButton(self.frame)
        self.runButton.setEnabled(True)
        self.runButton.setGeometry(QtCore.QRect(110, 70, 41, 41))
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
"}\n"
""))
        self.runButton.setText(_fromUtf8(""))
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.saveButton = QtGui.QPushButton(self.frame)
        self.saveButton.setGeometry(QtCore.QRect(580, 110, 71, 21))
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
"}\n"
""))
        self.saveButton.setText(_fromUtf8(""))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.loadButton = QtGui.QPushButton(self.frame)
        self.loadButton.setGeometry(QtCore.QRect(580, 80, 61, 21))
        self.loadButton.setStyleSheet(_fromUtf8("QPushButton,\n"
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
"}\n"
""))
        self.loadButton.setText(_fromUtf8(""))
        self.loadButton.setDefault(False)
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.loadAdd = QtGui.QLineEdit(self.frame)
        self.loadAdd.setGeometry(QtCore.QRect(650, 80, 141, 20))
        self.loadAdd.setStyleSheet(_fromUtf8("QLineEdit{\n"
"background-color:rgb(0,0,0,0%);\n"
"border-color: none;\n"
"border-width: none;\n"
"border-radius: 1px;}"))
        self.loadAdd.setObjectName(_fromUtf8("loadAdd"))
        self.saveAdd = QtGui.QLineEdit(self.frame)
        self.saveAdd.setGeometry(QtCore.QRect(650, 110, 141, 21))
        self.saveAdd.setStyleSheet(_fromUtf8("QLineEdit{\n"
"background-color:rgb(0,0,0,0%);\n"
"border-color: none;\n"
"border-width: none;\n"
"border-radius: 1px;}"))
        self.saveAdd.setObjectName(_fromUtf8("saveAdd"))
        self.edi = QtGui.QLineEdit(self.frame)
        self.edi.setGeometry(QtCore.QRect(390, 620, 101, 20))
        self.edi.setStyleSheet(_fromUtf8("QLineEdit{\n"
"background-color:rgb(0,0,0,0%);\n"
"border-color: none;\n"
"border-width: none;\n"
"border-radius: 1px;}"))
        self.edi.setObjectName(_fromUtf8("edi"))
        self.eax = QtGui.QLineEdit(self.frame)
        self.eax.setGeometry(QtCore.QRect(200, 590, 91, 20))
        self.eax.setStyleSheet(_fromUtf8("QLineEdit{\n"
"background-color:rgb(0,0,0,0%);\n"
"border-color: none;\n"
"border-width: none;\n"
"border-radius: 1px;}"))
        self.eax.setText(_fromUtf8(""))
        self.eax.setObjectName(_fromUtf8("eax"))
        self.ebx = QtGui.QLineEdit(self.frame)
        self.ebx.setGeometry(QtCore.QRect(200, 620, 91, 20))
        self.ebx.setStyleSheet(_fromUtf8("QLineEdit{\n"
"background-color:rgb(0,0,0,0%);\n"
"border-color: none;\n"
"border-width: none;\n"
"border-radius: 1px;}"))
        self.ebx.setObjectName(_fromUtf8("ebx"))
        self.ecx = QtGui.QLineEdit(self.frame)
        self.ecx.setGeometry(QtCore.QRect(200, 640, 91, 20))
        self.ecx.setStyleSheet(_fromUtf8("QLineEdit{\n"
"background-color:rgb(0,0,0,0%);\n"
"border-color: none;\n"
"border-width: none;\n"
"border-radius: 1px;}"))
        self.ecx.setObjectName(_fromUtf8("ecx"))
        self.edx = QtGui.QLineEdit(self.frame)
        self.edx.setGeometry(QtCore.QRect(210, 670, 81, 20))
        self.edx.setStyleSheet(_fromUtf8("QLineEdit{\n"
"background-color:rgb(0,0,0,0%);\n"
"border-color: none;\n"
"border-width: none;\n"
"border-radius: 1px;}"))
        self.edx.setObjectName(_fromUtf8("edx"))
        self.ebp = QtGui.QLineEdit(self.frame)
        self.ebp.setGeometry(QtCore.QRect(390, 660, 101, 20))
        self.ebp.setStyleSheet(_fromUtf8("QLineEdit{\n"
"background-color:rgb(0,0,0,0%);\n"
"border-color: none;\n"
"border-width: none;\n"
"border-radius: 1px;}"))
        self.ebp.setObjectName(_fromUtf8("ebp"))
        self.esp = QtGui.QLineEdit(self.frame)
        self.esp.setGeometry(QtCore.QRect(390, 640, 101, 20))
        self.esp.setStyleSheet(_fromUtf8("QLineEdit{\n"
"background-color:rgb(0,0,0,0%);\n"
"border-color: none;\n"
"border-width: none;\n"
"border-radius: 1px;}"))
        self.esp.setObjectName(_fromUtf8("esp"))
        self.cycle = QtGui.QLineEdit(self.frame)
        self.cycle.setGeometry(QtCore.QRect(660, 650, 171, 21))
        self.cycle.setStyleSheet(_fromUtf8("QLineEdit{\n"
"background-color:rgb(0,0,0,0%);\n"
"border-color: none;\n"
"border-width: none;\n"
"border-radius: 1px;}"))
        self.cycle.setObjectName(_fromUtf8("cycle"))
        self.esi = QtGui.QLineEdit(self.frame)
        self.esi.setGeometry(QtCore.QRect(390, 590, 101, 20))
        self.esi.setStyleSheet(_fromUtf8("QLineEdit{\n"
"background-color:rgb(0,0,0,0%);\n"
"border-color: none;\n"
"border-width: none;\n"
"border-radius: 1px;}"))
        self.esi.setObjectName(_fromUtf8("esi"))
        self.label_41 = QtGui.QLabel(Y86Simulator)
        self.label_41.setGeometry(QtCore.QRect(120, 120, 41, 31))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.W_stat = QtGui.QTextBrowser(Y86Simulator)
        self.W_stat.setGeometry(QtCore.QRect(110, 150, 41, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.W_stat.sizePolicy().hasHeightForWidth())
        self.W_stat.setSizePolicy(sizePolicy)
        self.W_stat.setBaseSize(QtCore.QSize(70, 20))
        self.W_stat.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.W_stat.setObjectName(_fromUtf8("W_stat"))
        self.label_2 = QtGui.QLabel(Y86Simulator)
        self.label_2.setGeometry(QtCore.QRect(160, 121, 31, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.W_icode = QtGui.QTextBrowser(Y86Simulator)
        self.W_icode.setGeometry(QtCore.QRect(160, 150, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.W_icode.sizePolicy().hasHeightForWidth())
        self.W_icode.setSizePolicy(sizePolicy)
        self.W_icode.setBaseSize(QtCore.QSize(70, 20))
        self.W_icode.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.W_icode.setObjectName(_fromUtf8("W_icode"))
        self.label_3 = QtGui.QLabel(Y86Simulator)
        self.label_3.setGeometry(QtCore.QRect(210, 120, 41, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.W_valE = QtGui.QTextBrowser(Y86Simulator)
        self.W_valE.setGeometry(QtCore.QRect(200, 150, 71, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.W_valE.sizePolicy().hasHeightForWidth())
        self.W_valE.setSizePolicy(sizePolicy)
        self.W_valE.setBaseSize(QtCore.QSize(70, 20))
        self.W_valE.setStyleSheet(_fromUtf8("background:rgb(255,255,255,10%)"))
        self.W_valE.setObjectName(_fromUtf8("W_valE"))
        self.label_4 = QtGui.QLabel(Y86Simulator)
        self.label_4.setGeometry(QtCore.QRect(300, 120, 31, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.W_valM = QtGui.QTextBrowser(Y86Simulator)
        self.W_valM.setGeometry(QtCore.QRect(280, 152, 81, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.W_valM.sizePolicy().hasHeightForWidth())
        self.W_valM.setSizePolicy(sizePolicy)
        self.W_valM.setBaseSize(QtCore.QSize(70, 20))
        self.W_valM.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.W_valM.setObjectName(_fromUtf8("W_valM"))
        self.label_5 = QtGui.QLabel(Y86Simulator)
        self.label_5.setGeometry(QtCore.QRect(363, 120, 41, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.W_dstE = QtGui.QTextBrowser(Y86Simulator)
        self.W_dstE.setGeometry(QtCore.QRect(370, 150, 61, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.W_dstE.sizePolicy().hasHeightForWidth())
        self.W_dstE.setSizePolicy(sizePolicy)
        self.W_dstE.setBaseSize(QtCore.QSize(70, 20))
        self.W_dstE.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.W_dstE.setObjectName(_fromUtf8("W_dstE"))
        self.label_6 = QtGui.QLabel(Y86Simulator)
        self.label_6.setGeometry(QtCore.QRect(443, 121, 51, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.W_dstM = QtGui.QTextBrowser(Y86Simulator)
        self.W_dstM.setGeometry(QtCore.QRect(440, 150, 51, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.W_dstM.sizePolicy().hasHeightForWidth())
        self.W_dstM.setSizePolicy(sizePolicy)
        self.W_dstM.setBaseSize(QtCore.QSize(70, 20))
        self.W_dstM.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.W_dstM.setObjectName(_fromUtf8("W_dstM"))
        self.label_42 = QtGui.QLabel(Y86Simulator)
        self.label_42.setGeometry(QtCore.QRect(120, 220, 41, 20))
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.M_stat = QtGui.QTextBrowser(Y86Simulator)
        self.M_stat.setGeometry(QtCore.QRect(110, 240, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_stat.sizePolicy().hasHeightForWidth())
        self.M_stat.setSizePolicy(sizePolicy)
        self.M_stat.setBaseSize(QtCore.QSize(70, 20))
        self.M_stat.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.M_stat.setObjectName(_fromUtf8("M_stat"))
        self.label_13 = QtGui.QLabel(Y86Simulator)
        self.label_13.setGeometry(QtCore.QRect(160, 210, 41, 41))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.M_icode = QtGui.QTextBrowser(Y86Simulator)
        self.M_icode.setGeometry(QtCore.QRect(150, 240, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_icode.sizePolicy().hasHeightForWidth())
        self.M_icode.setSizePolicy(sizePolicy)
        self.M_icode.setBaseSize(QtCore.QSize(70, 20))
        self.M_icode.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.M_icode.setObjectName(_fromUtf8("M_icode"))
        self.label_17 = QtGui.QLabel(Y86Simulator)
        self.label_17.setGeometry(QtCore.QRect(200, 200, 41, 61))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.M_bch = QtGui.QTextBrowser(Y86Simulator)
        self.M_bch.setGeometry(QtCore.QRect(190, 240, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_bch.sizePolicy().hasHeightForWidth())
        self.M_bch.setSizePolicy(sizePolicy)
        self.M_bch.setBaseSize(QtCore.QSize(70, 20))
        self.M_bch.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.M_bch.setObjectName(_fromUtf8("M_bch"))
        self.label_16 = QtGui.QLabel(Y86Simulator)
        self.label_16.setGeometry(QtCore.QRect(250, 210, 24, 41))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.M_valE = QtGui.QTextBrowser(Y86Simulator)
        self.M_valE.setGeometry(QtCore.QRect(230, 240, 70, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_valE.sizePolicy().hasHeightForWidth())
        self.M_valE.setSizePolicy(sizePolicy)
        self.M_valE.setBaseSize(QtCore.QSize(70, 20))
        self.M_valE.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.M_valE.setObjectName(_fromUtf8("M_valE"))
        self.label_12 = QtGui.QLabel(Y86Simulator)
        self.label_12.setGeometry(QtCore.QRect(330, 210, 24, 41))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.M_valA = QtGui.QTextBrowser(Y86Simulator)
        self.M_valA.setGeometry(QtCore.QRect(309, 240, 61, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_valA.sizePolicy().hasHeightForWidth())
        self.M_valA.setSizePolicy(sizePolicy)
        self.M_valA.setBaseSize(QtCore.QSize(70, 20))
        self.M_valA.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.M_valA.setObjectName(_fromUtf8("M_valA"))
        self.label_14 = QtGui.QLabel(Y86Simulator)
        self.label_14.setGeometry(QtCore.QRect(390, 210, 31, 41))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.M_dstE = QtGui.QTextBrowser(Y86Simulator)
        self.M_dstE.setGeometry(QtCore.QRect(380, 240, 61, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_dstE.sizePolicy().hasHeightForWidth())
        self.M_dstE.setSizePolicy(sizePolicy)
        self.M_dstE.setBaseSize(QtCore.QSize(70, 20))
        self.M_dstE.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.M_dstE.setObjectName(_fromUtf8("M_dstE"))
        self.label_15 = QtGui.QLabel(Y86Simulator)
        self.label_15.setGeometry(QtCore.QRect(450, 210, 51, 41))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.M_dstM = QtGui.QTextBrowser(Y86Simulator)
        self.M_dstM.setGeometry(QtCore.QRect(449, 240, 41, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_dstM.sizePolicy().hasHeightForWidth())
        self.M_dstM.setSizePolicy(sizePolicy)
        self.M_dstM.setBaseSize(QtCore.QSize(70, 20))
        self.M_dstM.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.M_dstM.setObjectName(_fromUtf8("M_dstM"))
        self.label_44 = QtGui.QLabel(Y86Simulator)
        self.label_44.setGeometry(QtCore.QRect(120, 330, 41, 20))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.E_stat = QtGui.QTextBrowser(Y86Simulator)
        self.E_stat.setGeometry(QtCore.QRect(110, 350, 40, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_stat.sizePolicy().hasHeightForWidth())
        self.E_stat.setSizePolicy(sizePolicy)
        self.E_stat.setBaseSize(QtCore.QSize(70, 20))
        self.E_stat.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.E_stat.setObjectName(_fromUtf8("E_stat"))
        self.label_29 = QtGui.QLabel(Y86Simulator)
        self.label_29.setGeometry(QtCore.QRect(160, 330, 30, 16))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.E_icode = QtGui.QTextBrowser(Y86Simulator)
        self.E_icode.setGeometry(QtCore.QRect(159, 350, 21, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_icode.sizePolicy().hasHeightForWidth())
        self.E_icode.setSizePolicy(sizePolicy)
        self.E_icode.setBaseSize(QtCore.QSize(70, 20))
        self.E_icode.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.E_icode.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.E_icode.setObjectName(_fromUtf8("E_icode"))
        self.label_26 = QtGui.QLabel(Y86Simulator)
        self.label_26.setGeometry(QtCore.QRect(200, 330, 24, 16))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.E_ifun = QtGui.QTextBrowser(Y86Simulator)
        self.E_ifun.setGeometry(QtCore.QRect(190, 350, 21, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_ifun.sizePolicy().hasHeightForWidth())
        self.E_ifun.setSizePolicy(sizePolicy)
        self.E_ifun.setBaseSize(QtCore.QSize(70, 20))
        self.E_ifun.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.E_ifun.setObjectName(_fromUtf8("E_ifun"))
        self.label_30 = QtGui.QLabel(Y86Simulator)
        self.label_30.setGeometry(QtCore.QRect(230, 310, 31, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.E_valC = QtGui.QTextBrowser(Y86Simulator)
        self.E_valC.setGeometry(QtCore.QRect(260, 320, 61, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_valC.sizePolicy().hasHeightForWidth())
        self.E_valC.setSizePolicy(sizePolicy)
        self.E_valC.setBaseSize(QtCore.QSize(70, 20))
        self.E_valC.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.E_valC.setObjectName(_fromUtf8("E_valC"))
        self.label_31 = QtGui.QLabel(Y86Simulator)
        self.label_31.setGeometry(QtCore.QRect(330, 310, 24, 12))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.E_valA = QtGui.QTextBrowser(Y86Simulator)
        self.E_valA.setGeometry(QtCore.QRect(360, 320, 61, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_valA.sizePolicy().hasHeightForWidth())
        self.E_valA.setSizePolicy(sizePolicy)
        self.E_valA.setBaseSize(QtCore.QSize(70, 20))
        self.E_valA.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.E_valA.setObjectName(_fromUtf8("E_valA"))
        self.label_27 = QtGui.QLabel(Y86Simulator)
        self.label_27.setGeometry(QtCore.QRect(420, 310, 24, 12))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.E_valB = QtGui.QTextBrowser(Y86Simulator)
        self.E_valB.setGeometry(QtCore.QRect(440, 320, 51, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_valB.sizePolicy().hasHeightForWidth())
        self.E_valB.setSizePolicy(sizePolicy)
        self.E_valB.setBaseSize(QtCore.QSize(70, 20))
        self.E_valB.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.E_valB.setObjectName(_fromUtf8("E_valB"))
        self.label_28 = QtGui.QLabel(Y86Simulator)
        self.label_28.setGeometry(QtCore.QRect(220, 350, 31, 20))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.E_dstE = QtGui.QTextBrowser(Y86Simulator)
        self.E_dstE.setGeometry(QtCore.QRect(250, 350, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_dstE.sizePolicy().hasHeightForWidth())
        self.E_dstE.setSizePolicy(sizePolicy)
        self.E_dstE.setBaseSize(QtCore.QSize(70, 20))
        self.E_dstE.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.E_dstE.setObjectName(_fromUtf8("E_dstE"))
        self.label_25 = QtGui.QLabel(Y86Simulator)
        self.label_25.setGeometry(QtCore.QRect(290, 350, 31, 20))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.E_dstM = QtGui.QTextBrowser(Y86Simulator)
        self.E_dstM.setGeometry(QtCore.QRect(320, 350, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_dstM.sizePolicy().hasHeightForWidth())
        self.E_dstM.setSizePolicy(sizePolicy)
        self.E_dstM.setBaseSize(QtCore.QSize(70, 20))
        self.E_dstM.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.E_dstM.setObjectName(_fromUtf8("E_dstM"))
        self.label_32 = QtGui.QLabel(Y86Simulator)
        self.label_32.setGeometry(QtCore.QRect(350, 350, 31, 20))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.E_srcA = QtGui.QTextBrowser(Y86Simulator)
        self.E_srcA.setGeometry(QtCore.QRect(390, 350, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_srcA.sizePolicy().hasHeightForWidth())
        self.E_srcA.setSizePolicy(sizePolicy)
        self.E_srcA.setBaseSize(QtCore.QSize(70, 20))
        self.E_srcA.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.E_srcA.setObjectName(_fromUtf8("E_srcA"))
        self.label_33 = QtGui.QLabel(Y86Simulator)
        self.label_33.setGeometry(QtCore.QRect(430, 350, 31, 20))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.E_srcB = QtGui.QTextBrowser(Y86Simulator)
        self.E_srcB.setGeometry(QtCore.QRect(460, 350, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_srcB.sizePolicy().hasHeightForWidth())
        self.E_srcB.setSizePolicy(sizePolicy)
        self.E_srcB.setBaseSize(QtCore.QSize(70, 20))
        self.E_srcB.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.E_srcB.setObjectName(_fromUtf8("E_srcB"))
        self.label_45 = QtGui.QLabel(Y86Simulator)
        self.label_45.setGeometry(QtCore.QRect(120, 440, 36, 12))
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.D_stat = QtGui.QTextBrowser(Y86Simulator)
        self.D_stat.setGeometry(QtCore.QRect(120, 470, 40, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_stat.sizePolicy().hasHeightForWidth())
        self.D_stat.setSizePolicy(sizePolicy)
        self.D_stat.setMinimumSize(QtCore.QSize(0, 20))
        self.D_stat.setMaximumSize(QtCore.QSize(40, 24))
        self.D_stat.setBaseSize(QtCore.QSize(70, 20))
        self.D_stat.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.D_stat.setObjectName(_fromUtf8("D_stat"))
        self.label_34 = QtGui.QLabel(Y86Simulator)
        self.label_34.setGeometry(QtCore.QRect(170, 440, 30, 12))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.D_icode = QtGui.QTextBrowser(Y86Simulator)
        self.D_icode.setGeometry(QtCore.QRect(170, 470, 20, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_icode.sizePolicy().hasHeightForWidth())
        self.D_icode.setSizePolicy(sizePolicy)
        self.D_icode.setMinimumSize(QtCore.QSize(0, 20))
        self.D_icode.setMaximumSize(QtCore.QSize(20, 24))
        self.D_icode.setBaseSize(QtCore.QSize(70, 20))
        self.D_icode.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.D_icode.setObjectName(_fromUtf8("D_icode"))
        self.label_38 = QtGui.QLabel(Y86Simulator)
        self.label_38.setGeometry(QtCore.QRect(210, 440, 24, 12))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.D_ifun = QtGui.QTextBrowser(Y86Simulator)
        self.D_ifun.setGeometry(QtCore.QRect(210, 470, 20, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_ifun.sizePolicy().hasHeightForWidth())
        self.D_ifun.setSizePolicy(sizePolicy)
        self.D_ifun.setMinimumSize(QtCore.QSize(0, 20))
        self.D_ifun.setMaximumSize(QtCore.QSize(20, 24))
        self.D_ifun.setBaseSize(QtCore.QSize(70, 20))
        self.D_ifun.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.D_ifun.setObjectName(_fromUtf8("D_ifun"))
        self.label_39 = QtGui.QLabel(Y86Simulator)
        self.label_39.setGeometry(QtCore.QRect(260, 440, 12, 12))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.D_rA = QtGui.QTextBrowser(Y86Simulator)
        self.D_rA.setGeometry(QtCore.QRect(290, 430, 20, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_rA.sizePolicy().hasHeightForWidth())
        self.D_rA.setSizePolicy(sizePolicy)
        self.D_rA.setMinimumSize(QtCore.QSize(0, 20))
        self.D_rA.setMaximumSize(QtCore.QSize(20, 24))
        self.D_rA.setBaseSize(QtCore.QSize(70, 20))
        self.D_rA.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.D_rA.setObjectName(_fromUtf8("D_rA"))
        self.label_40 = QtGui.QLabel(Y86Simulator)
        self.label_40.setGeometry(QtCore.QRect(260, 470, 12, 12))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.D_rB = QtGui.QTextBrowser(Y86Simulator)
        self.D_rB.setGeometry(QtCore.QRect(290, 470, 20, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_rB.sizePolicy().hasHeightForWidth())
        self.D_rB.setSizePolicy(sizePolicy)
        self.D_rB.setMinimumSize(QtCore.QSize(0, 20))
        self.D_rB.setMaximumSize(QtCore.QSize(20, 24))
        self.D_rB.setBaseSize(QtCore.QSize(70, 20))
        self.D_rB.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.D_rB.setObjectName(_fromUtf8("D_rB"))
        self.label_35 = QtGui.QLabel(Y86Simulator)
        self.label_35.setGeometry(QtCore.QRect(340, 450, 24, 12))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.D_valC = QtGui.QTextBrowser(Y86Simulator)
        self.D_valC.setGeometry(QtCore.QRect(330, 470, 70, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_valC.sizePolicy().hasHeightForWidth())
        self.D_valC.setSizePolicy(sizePolicy)
        self.D_valC.setMinimumSize(QtCore.QSize(70, 20))
        self.D_valC.setMaximumSize(QtCore.QSize(70, 24))
        self.D_valC.setBaseSize(QtCore.QSize(70, 20))
        self.D_valC.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.D_valC.setObjectName(_fromUtf8("D_valC"))
        self.label_36 = QtGui.QLabel(Y86Simulator)
        self.label_36.setGeometry(QtCore.QRect(430, 450, 24, 12))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.D_valP = QtGui.QTextBrowser(Y86Simulator)
        self.D_valP.setGeometry(QtCore.QRect(420, 470, 70, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_valP.sizePolicy().hasHeightForWidth())
        self.D_valP.setSizePolicy(sizePolicy)
        self.D_valP.setMinimumSize(QtCore.QSize(70, 20))
        self.D_valP.setMaximumSize(QtCore.QSize(70, 24))
        self.D_valP.setBaseSize(QtCore.QSize(70, 20))
        self.D_valP.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.D_valP.setObjectName(_fromUtf8("D_valP"))
        self.label_46 = QtGui.QLabel(Y86Simulator)
        self.label_46.setGeometry(QtCore.QRect(120, 550, 36, 12))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.F_stat = QtGui.QTextBrowser(Y86Simulator)
        self.F_stat.setGeometry(QtCore.QRect(170, 539, 61, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.F_stat.sizePolicy().hasHeightForWidth())
        self.F_stat.setSizePolicy(sizePolicy)
        self.F_stat.setBaseSize(QtCore.QSize(70, 20))
        self.F_stat.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.F_stat.setObjectName(_fromUtf8("F_stat"))
        self.label_43 = QtGui.QLabel(Y86Simulator)
        self.label_43.setGeometry(QtCore.QRect(310, 550, 36, 12))
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.F_predPC = QtGui.QTextBrowser(Y86Simulator)
        self.F_predPC.setGeometry(QtCore.QRect(380, 540, 91, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.F_predPC.sizePolicy().hasHeightForWidth())
        self.F_predPC.setSizePolicy(sizePolicy)
        self.F_predPC.setBaseSize(QtCore.QSize(70, 20))
        self.F_predPC.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.F_predPC.setObjectName(_fromUtf8("F_predPC"))
        self.Code = QtGui.QTextBrowser(Y86Simulator)
        self.Code.setGeometry(QtCore.QRect(570, 180, 321, 131))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.Code.sizePolicy().hasHeightForWidth())
        self.Code.setSizePolicy(sizePolicy)
        self.Code.setBaseSize(QtCore.QSize(70, 20))
        self.Code.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0)"))
        self.Code.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.Code.setObjectName(_fromUtf8("Code"))
        self.Author = QtGui.QTextBrowser(Y86Simulator)
        self.Author.setGeometry(QtCore.QRect(560, 550, 341, 71))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.Author.sizePolicy().hasHeightForWidth())
        self.Author.setSizePolicy(sizePolicy)
        self.Author.setBaseSize(QtCore.QSize(70, 20))
        self.Author.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0)"))
        self.Author.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.Author.setObjectName(_fromUtf8("Author"))
        self.Memory = QtGui.QTextBrowser(Y86Simulator)
        self.Memory.setGeometry(QtCore.QRect(560, 380, 331, 101))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.Memory.sizePolicy().hasHeightForWidth())
        self.Memory.setSizePolicy(sizePolicy)
        self.Memory.setBaseSize(QtCore.QSize(70, 20))
        self.Memory.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0)"))
        self.Memory.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.Memory.setObjectName(_fromUtf8("Memory"))
        self.ZF = QtGui.QTextBrowser(Y86Simulator)
        self.ZF.setGeometry(QtCore.QRect(350, 420, 21, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.ZF.sizePolicy().hasHeightForWidth())
        self.ZF.setSizePolicy(sizePolicy)
        self.ZF.setBaseSize(QtCore.QSize(70, 20))
        self.ZF.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.ZF.setObjectName(_fromUtf8("ZF"))
        self.SF = QtGui.QTextBrowser(Y86Simulator)
        self.SF.setGeometry(QtCore.QRect(410, 420, 21, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.SF.sizePolicy().hasHeightForWidth())
        self.SF.setSizePolicy(sizePolicy)
        self.SF.setBaseSize(QtCore.QSize(70, 20))
        self.SF.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.SF.setObjectName(_fromUtf8("SF"))
        self.OF = QtGui.QTextBrowser(Y86Simulator)
        self.OF.setGeometry(QtCore.QRect(460, 420, 21, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.OF.sizePolicy().hasHeightForWidth())
        self.OF.setSizePolicy(sizePolicy)
        self.OF.setBaseSize(QtCore.QSize(70, 20))
        self.OF.setStyleSheet(_fromUtf8("background:rgb(243, 221, 255,0%)"))
        self.OF.setObjectName(_fromUtf8("OF"))

        self.retranslateUi(Y86Simulator)
        QtCore.QMetaObject.connectSlotsByName(Y86Simulator)

    def retranslateUi(self, Y86Simulator):
        Y86Simulator.setWindowTitle(_translate("Y86Simulator", "Y86 Simulator", None))
        self.label_23.setText(_translate("Y86Simulator", " ZF", None))
        self.label_24.setText(_translate("Y86Simulator", "SF", None))
        self.label_37.setText(_translate("Y86Simulator", "OF", None))
        self.label_41.setText(_translate("Y86Simulator", "W_stat", None))
        self.label_2.setText(_translate("Y86Simulator", "iCode", None))
        self.label_3.setText(_translate("Y86Simulator", " valE", None))
        self.label_4.setText(_translate("Y86Simulator", "valM", None))
        self.label_5.setText(_translate("Y86Simulator", " dstE", None))
        self.label_6.setText(_translate("Y86Simulator", "  dstM", None))
        self.label_42.setText(_translate("Y86Simulator", "M_stat", None))
        self.label_13.setText(_translate("Y86Simulator", "iCode", None))
        self.label_17.setText(_translate("Y86Simulator", "Bch", None))
        self.label_16.setText(_translate("Y86Simulator", "valE", None))
        self.label_12.setText(_translate("Y86Simulator", "valA", None))
        self.label_14.setText(_translate("Y86Simulator", " dstE", None))
        self.label_15.setText(_translate("Y86Simulator", " dstM", None))
        self.label_44.setText(_translate("Y86Simulator", "E_stat", None))
        self.label_29.setText(_translate("Y86Simulator", "iCode", None))
        self.label_26.setText(_translate("Y86Simulator", "iFun", None))
        self.label_30.setText(_translate("Y86Simulator", "valC", None))
        self.label_31.setText(_translate("Y86Simulator", "valA", None))
        self.label_27.setText(_translate("Y86Simulator", "valB", None))
        self.label_28.setText(_translate("Y86Simulator", "dstE", None))
        self.label_25.setText(_translate("Y86Simulator", "dstM", None))
        self.label_32.setText(_translate("Y86Simulator", " srcA", None))
        self.label_33.setText(_translate("Y86Simulator", "srcB", None))
        self.label_45.setText(_translate("Y86Simulator", "D_stat", None))
        self.label_34.setText(_translate("Y86Simulator", "iCode", None))
        self.label_38.setText(_translate("Y86Simulator", "iFun", None))
        self.label_39.setText(_translate("Y86Simulator", "rA", None))
        self.label_40.setText(_translate("Y86Simulator", "rB", None))
        self.label_35.setText(_translate("Y86Simulator", "valC", None))
        self.label_36.setText(_translate("Y86Simulator", "valP", None))
        self.label_46.setText(_translate("Y86Simulator", "F_stat", None))
        self.label_43.setText(_translate("Y86Simulator", "predPC", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Y86Simulator = QtGui.QDialog()
    ui = Ui_Y86Simulator()
    ui.setupUi(Y86Simulator)
    Y86Simulator.show()
    sys.exit(app.exec_())

