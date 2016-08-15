__author__ = 'SufferProgrammer'

from PyQt4 import QtGui
from PyQt4 import QtCore
from design import *
from design import design
from database import *
from database import dbcontroller
import sys

class App(QtGui.QWidget,  design.Ui_Form):
    def __init__(self):
        super(App,  self).__init__()
        self.setupUi(self)
        self.dataViewer()
        self.lineEdit.returnPressed.connect(self.InsertData)
        self.lineEdit_2.returnPressed.connect(self.DelData)
        
    def dataViewer(self):
        dataServedToGui = dbcontroller.DBase()
        res = dataServedToGui.retrDataRow()
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setHorizontalHeaderLabels(['Message'])
        for i,  item in enumerate(dataServedToGui.retrData()):
            Message = QtGui.QTableWidgetItem(str(item[1]))
            self.tableWidget.setItem(i, 0,  Message)
            closeDB = dbcontroller.DBase()
            closeDB.closeConnection()
            
        QtCore.QTimer.singleShot(1000, self.dataViewer)
        
    def InsertData(self):
        data = self.lineEdit.text()
        if data != '':
            control = dbcontroller.DBase()
            control.addData(data)
            self.lineEdit.setText('')
            
        else:
            self.lineEdit.setText('')
            QtGui.QMessageBox.critical(self,  'Failed',  'Insert message first!!')
        
    def DelData(self):
        dataTarget = self.lineEdit_2.text()
        if dataTarget != '':
            dataAction = dbcontroller.DBase()
            dataAction.delData(dataTarget)
            self.lineEdit_2.setText('')
            QtGui.QMessageBox.warning(self,  'Success',  'Message has been deleted!!')

        else:
            self.lineEdit_2.setText('')
            QtGui.QMessageBox.critical(self, 'Failed',  'Insert Message to delete!!')
    
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    gui = App()
    gui.show()
    sys.exit(app.exec_())
