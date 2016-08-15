__author__ = 'SufferProgrammer'

import mysql.connector as mariaDBConnector

class DBase:
    def __init__(self):
        self.conn = mariaDBConnector.connect(host = '192.168.8.101',  user = 'developer',  database = 'crud_trial',  password='')
        self.cur = self.conn.cursor()
        
    def execute(self,  command):
        self.cur.execute(command)
        
    def addData(self, data):
        command = "INSERT INTO gui_trial(data) VALUES('%s')" %(data)
        self.execute(command)
        self.commit()
        
    def delData(self,  DropTarget):
        command = "DELETE FROM gui_trial WHERE data=('%s')" %(DropTarget)
        self.execute(command)
        self.commit()
    
    def commit(self):
        return self.conn.commit()
        
    def retrDataRow(self):
        command = "SELECT * FROM gui_trial"
        self.execute(command)
        dataListRow = self.cur.fetchall()
        return dataListRow
        
    def retrData(self):
        command = "SELECT * FROM gui_trial"
        self.execute(command)
        dataList = self.cur.fetchall()
        return dataList
        
    def closeConnection(self):
        return self.conn.close()
