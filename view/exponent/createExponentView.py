from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class CreateExponentView(QWidget):

    def __init__(self,store,appController,exponentController):
        super().__init__()
        self.appController = appController
        self.exponentController = exponentController
        self.tableTypes = store.getTableTypes()
        label = QLabel("Création exposant")   
        layout = QFormLayout()
        layout.addWidget(label)
        self.firstName = QLineEdit()
        layout.addRow("Prénom:", self.firstName )
        self.lastName = QLineEdit()
        layout.addRow("Nom:", self.lastName )

        self.tableTypesCB= QComboBox()
        self.tableTypesCB.addItems(self.tableTypes)
        self.tableTypesCB.activated.connect(self.check_index_tableTypes)
        self.selectedTableType = self.tableTypes[0]
        layout.addRow("Type de table:", self.tableTypesCB)
          

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validExponent)
        layout.addRow(cancelButton, validButton)

        self.setLayout(layout)
    
    def validExponent(self):
        self.exponentController.addExponent(self.firstName.text(),self.lastName.text(),self.selectedTableType)

    def close(self):
        self.appController.goBack()

    def check_index_tableTypes(self, index):
        self.selectedTableType = self.tableTypes[index]
