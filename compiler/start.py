import sys, os
from PyQt4 import QtCore, QtGui
from Ui_TextEditor import Ui_MainWindow
from os.path import isfile
import assemble, disassemble
import codecs

class Start(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.openButton,  QtCore.SIGNAL("clicked()"),  self.file_dialog)
        QtCore.QObject.connect(self.ui.saveButton, QtCore.SIGNAL("clicked()"), self.file_save)
        
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.compile)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.disassemble)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.run)        
                
        QtCore.QObject.connect(self.ui.codein,QtCore.SIGNAL("textChanged()"),self.enable_save)
    def file_dialog(self):
        fd=QtGui.QFileDialog(self)
        self.filename=fd.getOpenFileName()
        if(isfile(self.filename)):
            #text=open(self.filename).read()
            text=codecs.open(self.filename, 'r', 'utf-8').read()
            self.ui.codein.setPlainText(text)
            self.ui.saveButton.setEnabled(False)
            
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
        reply = QtGui.QMessageBox.question(self, 'Warning',text, 'OK')
        return    

    
    
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=Start()
    myapp.show()
    sys.exit(app.exec_())

