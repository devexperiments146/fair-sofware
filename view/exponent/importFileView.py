
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from view.tableModel import TableModel
import pandas as pd

class ImportFileView(QWidget):

    def __init__(self,appController,exponentController):
        super().__init__()
        self.appController = appController
        self.exponentController = exponentController
        label = QLabel("Importer fichier")
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
        filter = "*.csv"
        filename, _  = QFileDialog.getOpenFileName(qfd, "Importer fichier", path, filter)
        self.exponentController.importExponents(filename)