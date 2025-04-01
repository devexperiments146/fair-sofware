from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from view.tableModel import TableModel
import pandas as pd

class DisplayDoorView(QWidget):

    doors = []
    selectedDoor = None

    def __init__(self,store,appController,doorController):
        super().__init__()
        self.appController = appController
        self.doorController = doorController
        label = QLabel("Portes")
        layout = QVBoxLayout()
        layout.addWidget(label)

        self.deleteButton =  QPushButton("Supprimer")
        self.deleteButton.clicked.connect(self.delete)
        self.deleteButton.setEnabled(False)
        layout.addWidget(self.deleteButton)

        rooms = store.getSelectedProject().rooms
        for i in range(0,len(rooms),1):
            self.doors += rooms[i].doors

        table = QtWidgets.QTableView()
        rows = []
        datas = []
        for i in range(0,len(self.doors),1):
            door = self.doors[i]
            datas.append([door.name,door.room.getName(),door.width,door.orientation,door.x,door.y])
            rows.append(door.id)

        data = pd.DataFrame(datas,columns = ['Name','Room','Width','Orientation','X','Y'], index=rows)   
        self.model = TableModel(data)
        table.setModel(self.model)

        table.clicked.connect(self.select_door)

        layout.addWidget(table)
        table.resizeRowsToContents()

        bouton = QPushButton("Fermer")
        bouton.clicked.connect(self.close)
        layout.addWidget(bouton)

        self.setLayout(layout)

    def select_door(self, mi):
        if mi :
            self.deleteButton.setEnabled(True)
            self.selectedDoor = self.doors[mi.row()]
        else : 
            self.deleteButton.setEnabled(False)
            self.selectedDoor = None

    def delete(self):
        if self.selectedDoor:
            self.doorController.deleteDoor(self.selectedDoor.id,self.selectedDoor.room)

    def close(self):
        self.appController.goBack()