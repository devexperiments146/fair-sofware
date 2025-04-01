from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class CreateDoorView(QWidget):

    def __init__(self,store,appController,doorController):
        super().__init__()
        self.appController = appController
        self.doorController = doorController
        self.store = store
        label = QLabel("Créer porte")   
        layout = QFormLayout()
        self.name = QLineEdit()

        layout.addWidget(label)
        layout.addRow("Nom:", self.name)

        comboboxRooms = []
        self.rooms = self.store.getSelectedProject().rooms
        for i in range(0,len(self.rooms),1):
            comboboxRooms.append(self.rooms[i].getName())
        self.room = QComboBox()
        self.room.addItems(comboboxRooms)
        self.room.activated.connect(self.check_index_room)
        self.selectedRoom = self.rooms[0]
        layout.addRow("Salle:", self.room )
        
        self.tableWidth= QLineEdit()
        layout.addRow("Largeur (m):", self.tableWidth )
        self.tableWidth.setValidator(QDoubleValidator(0,999,2,self))

        self.orientation = QComboBox()
        self.orientation.addItems(self.store.getOrientations())
        self.orientation.activated.connect(self.check_index_orientation)
        self.selectedOrientation=self.store.getOrientations()[0]
        layout.addRow("Orientation:", self.orientation )

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validDoor)
        layout.addRow(cancelButton, validButton)
        self.setLayout(layout)

    def check_index_room(self, index):
        self.selectedRoom = self.rooms[index]

    def check_index_orientation(self, index):
        self.selectedOrientation=self.store.getOrientations()[index]

    def validDoor(self):
        self.doorController.addDoor(self.name.text(),self.selectedRoom,self.tableWidth.text(),self.selectedOrientation)

    def close(self):
        self.appController.goBack()