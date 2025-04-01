from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class CreateTableGroupView(QWidget):

    def __init__(self,store,appController,tableGroupController):
        super().__init__()
        self.store = store
        self.appController = appController
        self.tableGroupController = tableGroupController
        label = QLabel("Créer groupe de table") 
        layout = QFormLayout()
        self.tableWidth = QLineEdit()
        layout.addWidget(label)
        layout.addRow("Largeur (m):", self.tableWidth )
        self.tableWidth.setValidator(QDoubleValidator(0,999,2,self))
        self.tableLength = QLineEdit()
        layout.addRow("Longueur (m):", self.tableLength )
        self.tableLength.setValidator(QDoubleValidator(0,999,2,self))

        comboboxColors = []
        self.colors = store.getColors()
        for i in range(0,len(self.colors),1):
            comboboxColors.append(self.colors[i])
        self.color = QComboBox()
        self.color.addItems(comboboxColors)
        self.color.activated.connect(self.check_index_color)
        self.selectedColor = self.colors[0]
        layout.addRow("Couleur:", self.color )

        self.maxQuantity = QLineEdit()
        self.maxQuantity.setValidator(QIntValidator(1, 999, self))
        layout.addRow("Quantité max:", self.maxQuantity)

        self.tableType = QComboBox()
        self.tableType.addItems(self.store.getTableTypes())
        self.tableType.activated.connect(self.check_index_tableType)
        self.selectedTableType=self.store.getTableTypes()[0]
        layout.addRow("Type de table:", self.tableType )


        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validGroupTable)
        layout.addRow(cancelButton, validButton)
        self.setLayout(layout)
    
    def check_index_color(self, index):
        self.selectedColor= self.colors[index]
            
    def check_index_tableType(self, index):
        self.selectedTableType= self.store.getTableTypes()[index]

    def validGroupTable(self):
        self.tableGroupController.addTableGroup(self.tableWidth.text(),self.tableLength.text(),self.selectedColor,self.maxQuantity.text(),self.selectedTableType)

    def close(self):
        self.appController.goBack()