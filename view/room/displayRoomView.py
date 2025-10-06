from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from view.tableModel import TableModel
import pandas as pd

class DisplayRoomView(QWidget):
    
    def __init__(self,store,appController,roomController):
        super().__init__()
        self.store = store
        self.appController = appController
        self.roomController = roomController
        self.selectedRoom = None
        label = QLabel("Salles")
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(label)
        rooms = store.getSelectedProject().rooms
        self.rooms = rooms;

        self.deleteButton =  QPushButton("Supprimer")
        self.deleteButton.clicked.connect(self.delete)
        self.deleteButton.setEnabled(False)
        layout.addWidget(self.deleteButton)

        table = QtWidgets.QTableView()

        rows = []
        datas = []
        for i in range(0,len(rooms),1):
            datas.append([rooms[i].name,rooms[i].width,rooms[i].length,rooms[i].x,rooms[i].y,len(rooms[i].tables)])
            rows.append(rooms[i].id)
         
        data = pd.DataFrame(datas, columns = ['Name', 'Width', 'Length', 'x', 'y','Tables'], index=rows)   
        self.model = TableModel(data)
        table.setModel(self.model)

        table.clicked.connect(self.selectRoom)

        layout.addWidget(table)
        table.resizeRowsToContents()
        
        bouton = QPushButton("Fermer")
        bouton.clicked.connect(self.close)
        layout.addWidget(bouton)

        self.setLayout(layout)

        
    def close(self):
        self.appController.goBack()

    def selectRoom(self, mi):
        if mi :
            self.deleteButton.setEnabled(True)
            self.selectedRoom = self.rooms[mi.row()]
        else : 
            self.deleteButton.setEnabled(False)
            self.selectedRoom = None

    def delete(self):
        if self.selectedRoom:
            self.roomController.deleteRoom(self.selectedRoom.id)