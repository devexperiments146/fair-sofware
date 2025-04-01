from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class FillTablesView(QWidget):

    def __init__(self,store,appController,tableController):
        super().__init__()
        self.store = store
        self.appController = appController
        self.tableController = tableController
        label = QLabel("Remplir salle de tables")   
        layout = QFormLayout()
        layout.addWidget(label)

        comboboxRooms = []
        self.rooms = store.getSelectedProject().rooms
        if(len(self.rooms)>0):
            self.selectedRoom = self.rooms[0]
        for i in range(0,len(self.rooms),1):
            comboboxRooms.append(self.rooms[i].getName())
        self.room = QComboBox()
        self.room.addItems(comboboxRooms)
        self.room.activated.connect(self.check_index_table_room)
        layout.addRow("Salle:", self.room )

        bouton = QPushButton("Valider")
        bouton.clicked.connect(self.fillTables)
        layout.addWidget(bouton)
        self.setLayout(layout)

    def check_index_table_room(self, index):
        self.selectedRoom = self.rooms[index]

    def fillTables(self):
        self.tableController.fillTables(self.selectedRoom)