from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class CreateStructureView(QWidget):


    def __init__(self,store,appController,structureController):
        super().__init__()
        self.appController = appController
        self.structureController = structureController

        label = QLabel("Créer une structure")   
        layout = QFormLayout()
        self.name = QLineEdit()

        layout.addWidget(label)
        layout.addRow("Nom:", self.name)

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

        self.lineLength = QLineEdit()
        layout.addRow("Longueur (m):", self.lineLength )
        self.lineLength.setValidator(QDoubleValidator(0,999,2,self))
        
        self.lineWidth = QLineEdit()
        layout.addRow("Largeur (m):", self.lineWidth )
        self.lineWidth.setValidator(QDoubleValidator(0,999,2,self))

        comboboxOrientations = ['Vertical','Horizontal']
        self.orientation = QComboBox()
        self.orientation.addItems(comboboxOrientations)
        self.orientation.activated.connect(self.check_index_orientation)
        self.selectedOrientation="Vertical"
        layout.addRow("Orientation:", self.orientation )

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validStructure)
        layout.addRow(cancelButton, validButton)
        self.setLayout(layout)

    def check_index_orientation(self, index):
        self.selectedOrientation=  "Vertical" if index == 0 else "Horizontal"

    def check_index_rooms(self, index):
        self.selectedRoom = self.rooms[index]

    def validStructure(self):
        self.structureController.addStructure(self.selectedRoom,self.name.text(),self.lineLength.text(),self.lineWidth.text(),self.selectedOrientation)

    def close(self):
        self.appController.goBack()