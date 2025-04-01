from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class CreateProjectView(QWidget):

    def __init__(self,store,appController,projectController,parameterController):
        super().__init__()
        self.store = store
        self.appController = appController
        self.projectController = projectController
        self.parameterController = parameterController
        label = QLabel("Créer projet")   
        layout = QFormLayout()
        layout.addWidget(label)
        self.name = QLineEdit()
        layout.addRow("Nom:", self.name)
       
        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validProject)
        layout.addRow(cancelButton, validButton)

        self.setLayout(layout)
    
    def validProject(self):
        self.projectController.addProject(self.name.text())
        self.parameterController.updateParameter("CURRENT_PROJECT",str(self.store.getSelectedProject().id))
        
    def close(self):
        self.appController.goBack()