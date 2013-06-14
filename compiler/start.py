import sys, os
from os.path import isfile
from PyQt4 import QtCore, QtGui
from Ui_TextEditor import Ui_MainWindow
import assemble, disassemble
import codecs
from highlighter import MyHighlighter1

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\gui')
import y86


class Start(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.callflag = False
        self.ui.runButton.setEnabled(False)
        QtCore.QObject.connect(self.ui.openButton,  QtCore.SIGNAL("clicked()"),  self.file_dialog)
        QtCore.QObject.connect(self.ui.saveButton, QtCore.SIGNAL("clicked()"), self.file_save)
        
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.compile)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.disassemble)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.run) 
        QtCore.QObject.connect(self.ui.runButton, QtCore.SIGNAL("clicked()"), self.runfile) 
        
       
         
        QtCore.QObject.connect(self.ui.codein,QtCore.SIGNAL("textChanged()"),self.enable_save)

        MyHighlighter1( self.ui.codein, "Classic" )
    
    def runfile(self):
        if self.callflag == True:
            self.callerDia.opentxt = self.callfile.replace('.ys', '.yo') 
            self.callerDia.loadFile()
        else:
            try:
                self.Dialog = QtGui.QDialog(self)
                self.Dialog.ui = y86.Dialog(self)
                self.Dialog.ui.opentxt = self.filename.replace('.ys', '.yo') 
                self.Dialog.ui.loadFile()
                fin = open(str(self.Dialog.ui.opentxt))
                self.Dialog.ui.loadAdd.setText(str(self.Dialog.ui.opentxt))
                self.Dialog.ui.displaytext = fin.read()
                self.Dialog.ui.Code.setText(self.Dialog.ui.displaytext)
                fin.close()
                self.Dialog.ui.show()   
            except:
                self.showtext('Unable to run file')
    
    def create(self, filename, callerDia):
        self.callfile = filename
        self.callflag = True
        text=codecs.open(self.callfile, 'r', 'utf-8').read()
        self.ui.codein.setPlainText(text)
        self.ui.saveButton.setEnabled(False)
        self.callerDia = callerDia
        
        return
                
    def file_dialog(self):
        fd=QtGui.QFileDialog(self)
        self.filename=fd.getOpenFileName()
        if(isfile(self.filename)):
            #text=open(self.filename).read()
            text=codecs.open(self.filename, 'r', 'utf-8').read()
            self.ui.codein.setPlainText(text)
            self.ui.saveButton.setEnabled(False)
        if self.filename[-3:] =='.yo':
            self.ui.runButton.setEnabled(True)
        else:
            self.ui.runButton.setEnabled(False)
    
    def enable_save(self):
        self.ui.saveButton.setEnabled(True)
            
    def file_save(self):
        try:
            if(isfile(self.filename)):
                    file=codecs.open(self.filename, 'w', 'utf-8')
                    file.write(unicode(self.ui.codein.toPlainText()))
                    file.close()
                    text='Save success in   %s' %(self.filename)
                    self.ui.console.setPlainText(text)
                    self.ui.saveButton.setEnabled(False)
        except:
            pass
            
    def compile(self):
        self.ui.console.clear()
        infile = str(self.filename)
        out = os.path.splitext(infile)
        if out[1] != '.ys':
            self.showtext('Unable to compile %s' % infile)
            self.ui.console.setPlainText('Invalid file to compile')
            return
        outfile = out[0] + '.yo'
        infile = open(infile, 'r')
        outfile = open(outfile, 'w')
        assemble.assemble(infile, outfile)

        outfile.close()
        outfile = open(out[0]+'.yo', 'r')
        
        error = assemble.error
        if error != '':
            self.ui.console.setPlainText(error)
            self.ui.codeout.clear()
        else:
            self.ui.console.setPlainText('Compile success')
            text = outfile.read()
            self.ui.codeout.setPlainText(text)
        self.ui.runButton.setEnabled(True)
        return
    
    def disassemble(self):
        infile = str(self.filename)
        out = os.path.splitext(infile)
        if out[1] != '.yo':
            self.showtext('Unable to disassemble %s' % infile)
            self.ui.console.setPlainText('Invalid file to discompile')
            return
        outfile = out[0] + '.ys'
        infile = open(infile, 'r')
        outfile = open(outfile, 'w')
        disassemble.disassemble(infile, outfile)
        
        outfile.close()
        outfile = open(out[0]+'.ys', 'r')
        
        error = disassemble.error
        if error != '':
            self.ui.console.setPlainText(error)
            self.ui.codeout.setPlainText('')
        else:
            self.ui.console.setPlainText('disassemble success')
            text = outfile.read()
            self.ui.codeout.setPlainText(text)
        return
    
    def run(self):
        return
    
    def showtext(self, text):
        reply = QtGui.QMessageBox.warning(self, 'Warning',text, 'OK')
        return    

    
    
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Start()
    myapp.show()
    sys.exit(app.exec_())
