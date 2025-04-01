from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class PrintForExponentView(QWidget):

    def __init__(self,store,appController,exponentController):
        super().__init__()
        self.appController = appController
        self.exponentController = exponentController
        label = QLabel("Imprimer pour exposant")   
        layout = QFormLayout()
        layout.addWidget(label)

        selectedProject = store.getSelectedProject()

        comboboxExponents = []
        self.exponents = sorted(selectedProject.exponents, key=lambda x: x.lastname) 
        for i in range(0,len(self.exponents),1):
            comboboxExponents.append(self.exponents[i].getName())
        self.nextExponent = QComboBox()
        self.nextExponent.addItems(comboboxExponents)
        self.nextExponent.activated.connect(self.check_index_exponents)
        self.selectedExponent = None
        layout.addRow("Exposant:", self.nextExponent)

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.printPdf)
        layout.addRow(cancelButton, validButton)
        self.setLayout(layout)
        
    def printPdf(self):
        self.exponentController.printExponent(self.selectedExponent)

    def check_index_exponents(self, index):
        if index > 0:
            self.selectedExponent = self.exponents[index]
        else:
            self.selectedExponent = None

    def close(self):
        self.appController.goBack()