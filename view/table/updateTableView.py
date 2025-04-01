from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class UpdateTableView(QWidget):

    def __init__(self,store,table,appController,tableController):
        super().__init__()
        self.appController = appController
        self.tableController = tableController
        self.currentTable = table
        label = QLabel("Modifier table")   
        layout = QFormLayout()
        layout.addWidget(label)

        self.tableName = QLineEdit()
        layout.addRow("Nom:", self.tableName)
        self.tableName.setText(table.name)


        self.tableX= QLineEdit()
        layout.addRow("X (m):", self.tableX )
        self.tableX.setValidator(QDoubleValidator(0,999,2,self))
        self.tableX.setText(str(table.reelX))

        self.tableY = QLineEdit()
        layout.addRow("Y (m):", self.tableY )
        self.tableY.setValidator(QDoubleValidator(0,999,2,self))
        self.tableY.setText(str(table.reelY))


        self.sides = store.getSides()
        self.side = QComboBox()
        self.side.addItems(self.sides)
        self.side.activated.connect(self.check_index_side)
        self.selectedSide = self.sides[0]
        layout.addRow("Texte:", self.side )

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validTable)
        layout.addRow(cancelButton, validButton)
        self.setLayout(layout)
        
    def validTable(self):
        self.tableController.updateTable(self.currentTable,self.tableX.text(),self.tableY.text(),self.tableName.text(),self.selectedSide)

    def check_index_side(self, index):
        self.selectedSide = self.sides[index]

    def close(self):
        self.appController.goBack()