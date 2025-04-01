from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class UpdateTableLineView(QWidget):

    def __init__(self,tableLine,appController,tableLineController):
        super().__init__()
        self.appController = appController
        self.tableLineController = tableLineController
        self.currentTableLine = tableLine
        label = QLabel("Modifier Ligne de table")   
        layout = QFormLayout()
        layout.addWidget(label)

        self.tableLineWidth = QLineEdit()
        layout.addRow("Longueur (m):", self.tableLineWidth )
        self.tableLineWidth.setValidator(QDoubleValidator(0,999,2,self))
        self.tableLineWidth.setText(str(tableLine.width))

        self.tableLineX= QLineEdit()
        layout.addRow("X (m):", self.tableLineX )
        self.tableLineX.setValidator(QDoubleValidator(0,999,2,self))
        self.tableLineX.setText(str(tableLine.reelX))

        
        self.tableLineY = QLineEdit()
        layout.addRow("Y (m):", self.tableLineY )
        self.tableLineY.setValidator(QDoubleValidator(0,999,2,self))
        self.tableLineY.setText(str(tableLine.reelY))
        
        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validTableLine)
        layout.addRow(cancelButton, validButton)
        self.setLayout(layout)
        
    def validTableLine(self):
        self.tableLineController.updateTableLine(self.currentTableLine,self.tableLineWidth.text(),self.tableLineX.text(),self.tableLineY.text())

    def close(self):
        self.appController.goBack()