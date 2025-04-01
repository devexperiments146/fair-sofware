from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from view.tableModel import TableModel
import pandas as pd

class DisplayTableView(QWidget):


    def __init__(self,store,appController,tableController):
        super().__init__()
        self.store = store
        self.appController = appController
        self.tableController = tableController
        
        label = QLabel("Tables")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.tables  = []
        for room in store.getSelectedProject().rooms:
           self.tables += room.tables

        self.deleteAllButton =  QPushButton("Tout supprimer")
        self.deleteAllButton.clicked.connect(self.deleteAll)
        layout.addWidget(self.deleteAllButton)

        self.deleteButton =  QPushButton("Supprimer")
        self.deleteButton.clicked.connect(self.delete)
        self.deleteButton.setEnabled(False)
        layout.addWidget(self.deleteButton)

        self.selectedTable = None
    
        table = QtWidgets.QTableView()
        
        rows = []
        datas = []
        for i in range(0,len(self.tables),1):
            exponent = ""
            if hasattr(self.tables[i],"exponent") and self.tables[i].exponent:
                exponent = self.tables[i].exponent.getName()
            textSide = ""
            if self.tables[i].side:
                textSide = self.tables[i].side
            datas.append([self.tables[i].name,self.tables[i].room.getName(),self.tables[i].tableGroup.getName(),self.tables[i].x,self.tables[i].y,self.tables[i].orientation,exponent,textSide])
            rows.append(self.tables[i].id)
         
        data = pd.DataFrame(datas, columns = ['Name','Room','Table Group','X','Y','Orientation','Exponent','Texte'], index=rows)   
        self.model = TableModel(data)
        table.setModel(self.model)
        
        table.clicked.connect(self.select_table)
        layout.addWidget(table)
        table.resizeRowsToContents()
        
        bouton = QPushButton("Fermer")
        bouton.clicked.connect(self.close)
        layout.addWidget(bouton)

        self.setLayout(layout)

        table.doubleClicked.connect(self.updateTable)
        
    def close(self):
        self.appController.goBack()

    def select_table(self, mi):
        if mi :
            self.deleteButton.setEnabled(True)
            self.selectedTable = self.tables[mi.row()]
        else : 
            self.deleteButton.setEnabled(False)
            self.selectedTable = None

    def deleteAll(self):
        self.tableController.deleteAllTables()

    def delete(self):
        if self.selectedTable:
            self.tableController.deleteTable(self.selectedTable.id,self.selectedTable.room)

    def updateTable(self, mi):
        if mi :
            selectedTable = self.tables[mi.row()]
            self.tableController.displayUpdateTable(selectedTable)