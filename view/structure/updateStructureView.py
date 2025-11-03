from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class UpdateStructureView(QWidget):

    def __init__(self,store,structure,appController,structureController):
        super().__init__()
        self.appController = appController
        self.structureController = structureController
        self.currentStructure = structure
        label = QLabel("Modifier structure")   
        layout = QFormLayout()
        layout.addWidget(label)

        selectedProject = store.getSelectedProject()

        self.structureX= QLineEdit()
        layout.addRow("X (m):", self.structureX )
        self.structureX.setValidator(QDoubleValidator(0,999,2,self))
        self.structureX.setText(str(structure.reelX))

        self.structureY = QLineEdit()
        layout.addRow("Y (m):", self.structureY )
        self.structureY.setValidator(QDoubleValidator(0,999,2,self))
        self.structureY.setText(str(structure.reelY))

        self.structureType = QComboBox()
        self.structureType.addItems(store.getStructureTypes())
        self.structureType.activated.connect(self.check_index_structure_type)
        self.selectedStructureType=structure.structureType
        layout.addRow("Type de structure:", self.structureType )

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validStructure)
        layout.addRow(cancelButton, validButton)
        self.setLayout(layout)
        
    def check_index_structure_type(self, index):
        self.selectedStructureType = index

    def validStructure(self):
        self.structureController.updateStructure(self.currentStructure,self.structureX.text(),self.structureY.text(),self.selectedStructureType)

    def close(self):
        self.appController.goBack()