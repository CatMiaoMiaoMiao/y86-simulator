# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import PyQt4, PyQt4.QtGui, sys
from Simulator import *
import time

from Ui_y86 import Ui_Y86Simulator

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

opentxt=None
savetxt=None

'''class Thread(QtCore.QThread):

    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.exiting = False

    def __del__(self):
        self.exiting = True
        self.wait()

    def render(self,sim,pos=0.1):
        self.interval=pos
        self.sim=sim
        self.start()

    def run(self):
        while self.sim.isGoing:
            self.emit(QtCore.SIGNAL("update()"))
            time.sleep(self.interv)
'''
class Dialog(QDialog, Ui_Y86Simulator):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.simulator=Simulator()
        #self.thread = Thread()
        self.connect(self.loadButton,SIGNAL("clicked()"),self.openFile)
        self.connect(self.saveButton,SIGNAL("clicked()"),self.saveFile)
        self.connect(self.runButton,SIGNAL("clicked()"),self.run)
    
    def openFile(self):
        global opentxt
        opentxt=QFileDialog.getOpenFileName(self,"Open file","/")  
        self.loadAdd.setText(str(opentxt))
        try:
            file=open(opentxt)
            data=file.read()
            self.Code.setText(data)
        except:
            pass

    def saveFile(self):
        global savetxt
        savetxt=QFileDialog.getSaveFileName(self,"Save file","/")  
        self.saveAdd.setText(str(savetxt))

    def run(self):
        global opentxt, savetxt
        pos = self.Slider.value()/100.0
        #self.thread.render(self.simulator, interval = pos)
        self.simulator.interval = pos
        self.simulator.isGoing = True
        try:
            infile=open(str(opentxt))
        except:
            self.openFile()
            return
        try:
            outfile = open(str(savetxt), 'w')
        except:
            outfile = None
        self.simulator.load(infile, outfile)
        self.runButton.setEnabled(False)
        self.simulator.run()
        self.runButton.setEnabled(True)
        
    
    def pause(self):
        self.simulator.isGoing = False

    def step(self):
        self.simulator.step()

    def on_Slider_valueChanged(self):
        pos = self.Slider.value()/100.0
        self.frequency.setText(str(pos) + 's')


if __name__ == "__main__":    
    
    app = PyQt4.QtGui.QApplication(sys.argv)     
    dlg = Dialog()     
    dlg.show()     
    sys.exit(app.exec_())
