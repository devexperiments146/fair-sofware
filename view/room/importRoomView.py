from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class ImportRoomView(QWidget):

    def __init__(self,store,appController,roomController):
        super().__init__()
        self.store = store
        self.appController = appController
        self.roomController = roomController

        super().__init__()
        label = QLabel("Importer salle")   
        layout = QFormLayout()
        layout.addWidget(label)

        comboboxRooms = []
        self.rooms = store.getRooms()
        for i in range(0,len(self.rooms),1):
            comboboxRooms.append(self.rooms[i].getName())
        if(len(self.rooms)>0):
            self.selectedRoom = self.rooms[0]
        self.room = QComboBox()
        self.room.addItems(comboboxRooms)
        self.room.activated.connect(self.check_index_table_room)
        layout.addRow("Salle:", self.room)

        bouton = QPushButton("Valider")
        bouton.clicked.connect(self.importRoom)
        layout.addWidget(bouton)
        self.setLayout(layout)

    def check_index_table_room(self, index):
        self.selectedRoom = self.rooms[index]

    def importRoom(self):
        self.roomController.importRoom(self.selectedRoom)