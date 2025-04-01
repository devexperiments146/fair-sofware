from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from view.tableModel import TableModel
import pandas as pd

class DisplayTableLineView(QWidget):

    def __init__(self,store,appController,tableLineController):
        super().__init__()
        self.appController = appController
        self.tableLineController = tableLineController
        
        label = QLabel("Lignes de table")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.appController = appController

        self.tableLines  = []
        for room in store.getSelectedProject().rooms:
           self.tableLines += room.tableLines

        self.deleteButton =  QPushButton("Supprimer")
        self.deleteButton.clicked.connect(self.delete)
        self.deleteButton.setEnabled(False)
        layout.addWidget(self.deleteButton)

        project = QtWidgets.QTableView()
        
        rows = []
        datas = []
        for i in range(0,len(self.tableLines),1):
            currentTableLine = self.tableLines[i]
            datas.append([currentTableLine.name,currentTableLine.x,currentTableLine.y,currentTableLine.reelX,currentTableLine.reelY,currentTableLine.width,currentTableLine.orientation])
            rows.append(currentTableLine.id)
         
        data = pd.DataFrame(datas, columns = ['Name','x','y','x (reel)','y (Reel)','Length','Orientation'], index=rows)   
        self.model = TableModel(data)
        
        project.setModel(self.model)
        
        project.clicked.connect(self.select_table_line)

        layout.addWidget(project)
        project.resizeRowsToContents()
        
        bouton = QPushButton("Fermer")
        bouton.clicked.connect(self.close)
        layout.addWidget(bouton)
        
        self.setLayout(layout)
        project.doubleClicked.connect(self.updateTableLine)

    def close(self):
        self.appController.goBack()


    def select_table_line(self, mi):
        if mi :
            self.deleteButton.setEnabled(True)
            self.selectedTableLine = self.tableLines[mi.row()]
        else : 
            self.deleteButton.setEnabled(False)
            self.selectedTableLine = None

    def delete(self):
        if self.selectedTableLine:
            self.tableLineController.deleteTableLine(self.selectedTableLine.id,self.selectedTableLine.room)

    def updateTableLine(self, mi):
        if mi :
            selectedTableLine = self.tableLines[mi.row()]
            self.tableLineController.displayUpdateTableLine(selectedTableLine)