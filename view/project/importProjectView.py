
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from view.tableModel import TableModel
import pandas as pd

class ImportProjectView(QWidget):

    def __init__(self,appController,projectController):
        super().__init__()
        self.appController = appController
        self.projectController = projectController
        label = QLabel("Importer peoject")
        layout = QVBoxLayout()
        layout.addWidget(label)

        bouton = QPushButton("Importer")
        bouton.clicked.connect(self.open)
        layout.addWidget(bouton)

        bouton = QPushButton("Fermer")
        bouton.clicked.connect(self.close)
        layout.addWidget(bouton)

        self.setLayout(layout)
        
    def close(self):
        self.appController.goBack()


    def open(self):
        qfd = QFileDialog()
        path = "C:\\"
        filter = "*.json"
        filename, _  = QFileDialog.getOpenFileName(qfd, "Importer projet", path, filter)
        self.projectController.importProject(filename)