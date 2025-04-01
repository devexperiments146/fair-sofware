from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class CreateZoneView(QWidget):


    def __init__(self,store,appController,zoneController):
        super().__init__()
        self.appController = appController
        self.zoneController = zoneController

        label = QLabel("Créer Zones")   
        layout = QFormLayout()

        selectedProject = store.getSelectedProject()

        comboboxRooms = []
        self.rooms = selectedProject.rooms
        for i in range(0,len(self.rooms),1):
            comboboxRooms.append(self.rooms[i].getName())
        self.room = QComboBox()
        self.room.addItems(comboboxRooms)
        self.room.activated.connect(self.check_index_rooms)
        self.selectedRoom = self.rooms[0]
        layout.addRow("Salle:", self.room )

        self.numberOfZones = QLineEdit()
        layout.addRow("Nombre de zones:", self.numberOfZones )
        self.numberOfZones.setValidator(QIntValidator(0, 100, self))

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validZone)
        layout.addRow(cancelButton, validButton)
        self.setLayout(layout)

    def check_index_rooms(self, index):
        self.selectedRoom = self.rooms[index]

    def validZone(self):
        self.zoneController.createZones(self.selectedRoom,self.numberOfZones.text())

    def close(self):
        self.appController.goBack()