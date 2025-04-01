from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from view.tableModel import TableModel
import pandas as pd

class DisplayRoomView(QWidget):
    
    def __init__(self,store,appController):
        super().__init__()
        self.store = store
        self.appController = appController
        label = QLabel("Salles")
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(label)
        rooms = store.getSelectedProject().rooms

        table = QtWidgets.QTableView()

        rows = []
        datas = []
        for i in range(0,len(rooms),1):
            datas.append([rooms[i].name,rooms[i].width,rooms[i].length,rooms[i].x,rooms[i].y,len(rooms[i].tables)])
            rows.append(rooms[i].id)
         
        data = pd.DataFrame(datas, columns = ['Name', 'Width', 'Length', 'x', 'y','Tables'], index=rows)   
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