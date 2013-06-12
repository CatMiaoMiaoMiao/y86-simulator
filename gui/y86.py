# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import PyQt4, PyQt4.QtGui, sys
from PyQt4 import QtGui
from Simulator import *
import time

from Ui_y86 import Ui_Y86Simulator

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

opentxt=None
savetxt=None

class Thread(QtCore.QThread):

    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.exiting = False

    def __del__(self):
        self.exiting = True
        self.wait()

    def render(self,sim, interval=0.1):
        self.sim=sim
        self.interval=interval
        self.start()

    def run(self):
        while self.sim.isTerminated == False:
            self.emit(QtCore.SIGNAL("next()"))
            time.sleep(self.interval)

class Dialog(QDialog, Ui_Y86Simulator):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.simulator=Simulator()
        self.thread = Thread()
        self.connect(self.thread, SIGNAL("next()"), self.step)
        self.connect(self.loadButton,SIGNAL("clicked()"),self.openFile)
        self.connect(self.saveButton,SIGNAL("clicked()"),self.saveFile)
        self.connect(self.runButton,SIGNAL("clicked()"),self.run)
        self.connect(self.pauseButton,SIGNAL("clicked()"),self.pause)
        self.connect(self.begin,SIGNAL("clicked()"),self.loadFile)
        self.connect(self.stepButton,SIGNAL("clicked()"),self.step)
        self.connect(self.backButton,SIGNAL("clicked()"),self.back)
        self.connect(self.resetButton,SIGNAL("clicked()"),self.reset)
        self.frequency.setText('1.0s')
    
    def showerror(self):
        reply = QtGui.QMessageBox.question(self, 'Error',"invalid format input file", 'OK')
        return

    
    def openFile(self):
        global opentxt
        opentxt=QFileDialog.getOpenFileName(self,"Open file","/")  
        try:
            self.loadAdd.setText(str(opentxt))
        except UnicodeEncodeError:
            self.showerror()
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

    def loadFile(self):
        global opentxt, savetxt
        
        try:
            infile=open(str(opentxt))
        except:
            self.openFile()
            return
        try:
            if savetxt != None:
                outfile = open(str(savetxt), 'w')
            else:
                outfile = None
        except:
            pass
        try:
            self.simulator.load(infile, outfile)
        except:
            self.showerror()
            self.openFile()
        
    def run(self):
        pos = self.Slider.value()/100.0
        self.thread.render(self.simulator, pos)
        self.runButton.setEnabled(False)
    
    def pause(self):
        self.runButton.setEnabled(True)
        self.thread.terminate()

    def step(self):
        if self.simulator.isTerminated == False:
            try:
                self.simulator.step()
            except:
                self.showerror()
            self.showtxt()


    def showtxt(self):
        if self.simulator.M_Cnd:
            self.M_bch.setText('1')
        else:
            self.M_bch.setText('0')
            
        my=[self.ZF, self.SF, self.OF, 
                self.F_stat, self.F_predPC, 
                self.D_stat,self.D_icode,self.D_ifun, self.D_rA, self.D_rB, self.D_valC, self.D_valP, 
                self.E_stat,self.E_icode, self.E_ifun,self.E_valC, self.E_valA, self.E_valB, self.E_srcA, self.E_srcB, self.E_dstE, self.E_dstM, 
                self.M_stat,self.M_icode, self.M_valE, self.M_valA, self.M_dstE, self.M_dstM, 
                self.W_stat, self.W_icode, self.W_valE, self.W_valM, self.W_dstE, self.W_dstM, 
                self.eax, self.ecx, self.edx, self.ebx, self.esp, self.ebp, self.esi, self.edi, self.cycle]
            
        his=[self.simulator.condcode['ZF'], self.simulator.condcode['SF'], self.simulator.condcode['OF'], 
                self.simulator.F_stat, self.simulator.F_predPC, 
                self.simulator.D_stat,self.simulator.D_icode,self.simulator.D_ifun, self.simulator.D_rA, self.simulator.D_rB, self.simulator.D_valC, self.simulator.D_valP, 
                self.simulator.E_stat,self.simulator.E_icode, self.simulator.E_ifun,self.simulator.E_valC, self.simulator.E_valA, self.simulator.E_valB, self.simulator.E_srcA, self.simulator.E_srcB, self.simulator.E_dstE, self.simulator.E_dstM, 
                self.simulator.M_stat,self.simulator.M_icode,self.simulator.M_valE, self.simulator.M_valA, self.simulator.M_dstE, self.simulator.M_dstM, 
                self.simulator.W_stat, self.simulator.W_icode, self.simulator.W_valE, self.simulator.W_valM, self.simulator.W_dstE, self.simulator.W_dstM, 
                self.simulator.register[0x0],  self.simulator.register[0x1],  self.simulator.register[0x2],  self.simulator.register[0x3], 
                self.simulator.register[0x4],  self.simulator.register[0x5],  self.simulator.register[0x6],  self.simulator.register[0x7], 
                self.simulator.cycle-1]
        
        for (myname, hisname) in zip(my, his):
            myname.setText(str(hisname))

    def on_Slider_valueChanged(self):
        pos = self.Slider.value()/100.0
        self.frequency.setText(str(pos) + 's')
    
    def back(self):
        self.simulator.back()
        self.showtxt()
        
    def reset(self):
        self.simulator=Simulator()
        self.loadFile()
        for item in [self.ZF, self.SF, self.OF, 
                self.F_stat, self.F_predPC, 
                self.D_stat,self.D_icode,self.D_ifun, self.D_rA, self.D_rB, self.D_valC, self.D_valP, 
                self.E_stat,self.E_icode, self.E_ifun,self.E_valC, self.E_valA, self.E_valB, self.E_srcA, self.E_srcB, self.E_dstE, self.E_dstM, 
                self.M_stat,self.M_icode,self.M_bch,  self.M_valE, self.M_valA, self.M_dstE, self.M_dstM, 
                self.W_stat, self.W_icode, self.W_valE, self.W_valM, self.W_dstE, self.W_dstM, 
                self.eax, self.ecx, self.edx, self.ebx, self.esp, self.ebp, self.esi, self.edi, self.cycle]:
            item.clear()
        
            
if __name__ == "__main__":    
    
    app = PyQt4.QtGui.QApplication(sys.argv)     
    dlg = Dialog()     
    dlg.show()     
    sys.exit(app.exec_())
