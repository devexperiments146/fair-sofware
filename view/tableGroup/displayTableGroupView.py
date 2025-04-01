from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from view.tableModel import TableModel
import pandas as pd

class DisplayTableGroupView(QWidget):

    def __init__(self,store,appController):
        super().__init__()
        self.appController = appController
        label = QLabel("Groupes de table")
        layout = QVBoxLayout()
        layout.addWidget(label)

        table = QtWidgets.QTableView()
        tableGroups = store.getSelectedProject().tableGroups
        rows = []
        datas = []
        for i in range(0,len(tableGroups),1):
            tableType = ""
            if tableGroups[i].tableType:
                tableType = tableGroups[i].tableType

            datas.append([tableGroups[i].width,tableGroups[i].length,tableGroups[i].color,tableGroups[i].maxQuantity,tableType])
            rows.append(tableGroups[i].id)
         
        data = pd.DataFrame(datas, columns = ['Width', 'Length', 'Color',"Quantité max",'Type de table'], index=rows)   
        self.model = TableModel(data)
        table.setModel(self.model)

        layout.addWidget(table)
        table.resizeRowsToContents()
        
        
        bouton = QPushButton("Fermer")
        bouton.clicked.connect(self.close)
        layout.addWidget(bouton)

        self.setLayout(layout)

        
    def close(self):
        self.appController.goBack()