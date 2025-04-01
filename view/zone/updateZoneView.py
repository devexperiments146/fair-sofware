from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class UpdateZoneView(QWidget):

    def __init__(self,zone,appController,zoneController):
        super().__init__()
        self.appController = appController
        self.zoneController = zoneController
        self.currentZone = zone
        label = QLabel("Modifier Zone")   
        layout = QFormLayout()
        layout.addWidget(label)


        self.zoneName = QLineEdit()
        layout.addRow("Nom:", self.zoneName)
        self.zoneName.setText(zone.name)

        self.zoneLength = QLineEdit()
        layout.addRow("Longueur (m):", self.zoneLength)
        self.zoneLength.setValidator(QIntValidator(0, 100, self))
        self.zoneLength.setText(str(zone.length))


        self.zoneWidth = QLineEdit()
        layout.addRow("Largeur (m):", self.zoneWidth)
        self.zoneWidth.setValidator(QIntValidator(0, 100, self))
        self.zoneWidth.setText(str(zone.width))


        self.zoneX= QLineEdit()
        layout.addRow("X (m):", self.zoneX)
        self.zoneX.setValidator(QDoubleValidator(0,999,2,self))
        self.zoneX.setText(str(zone.reelX))

        
        self.zoneY = QLineEdit()
        layout.addRow("Y (m):", self.zoneY)
        self.zoneY.setValidator(QDoubleValidator(0,999,2,self))
        self.zoneY.setText(str(zone.reelY))

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validZone)
        layout.addRow(cancelButton, validButton)
        self.setLayout(layout)
        
    def validZone(self):
        self.zoneController.updateZone(self.currentZone,self.zoneName.text(),self.zoneLength.text(),self.zoneWidth.text(),self.zoneX.text(),self.zoneY.text())

    def close(self):
        self.appController.goBack()