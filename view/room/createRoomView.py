from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class CreateRoomView(QWidget):

    def __init__(self,appController,roomController):
        super().__init__()
        self.appController = appController
        self.roomController = roomController
        super().__init__()
        label = QLabel("Créer salle")   
        layout = QFormLayout()
        layout.addWidget(label)
        self.name = QLineEdit()
        layout.addRow("Nom:", self.name)
        self.width = QLineEdit()
        self.width.setValidator(QDoubleValidator(0,999,2,self))
        layout.addRow("Largeur (m):", self.width)
        self.height = QLineEdit()
        self.height.setValidator(QDoubleValidator(0,999,2,self))
        layout.addRow("Longueur (m):", self.height)

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validRoom)
        layout.addRow(cancelButton, validButton)

        self.setLayout(layout)
    
    def validRoom(self):
        self.roomController.addRoom(self.name.text(),self.width.text(),self.height.text())
        
    def close(self):
        self.appController.goBack()