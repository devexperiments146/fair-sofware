from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from view.tableModel import TableModel
import pandas as pd

class DisplayStructureView(QWidget):

    def __init__(self,store,appController,structureController):
        super().__init__()
        self.appController = appController
        self.structureController = structureController
        
        label = QLabel("Structures")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.appController = appController

        self.structures  = []
        for room in store.getSelectedProject().rooms:
           self.structures += room.structures

        self.deleteButton =  QPushButton("Supprimer")
        self.deleteButton.clicked.connect(self.delete)
        self.deleteButton.setEnabled(False)
        layout.addWidget(self.deleteButton)

        project = QtWidgets.QTableView()
        
        rows = []
        datas = []
        for i in range(0,len(self.structures),1):
            currentStructure = self.structures[i]
            datas.append([currentStructure.name,currentStructure.x,currentStructure.y,currentStructure.reelX,currentStructure.reelY,currentStructure.width,currentStructure.length,currentStructure.orientation])
            rows.append(currentStructure.id)
         
        data = pd.DataFrame(datas, columns = ['Name','x','y','x (reel)','y (Reel)','Width','Length','Orientation'], index=rows)   
        self.model = TableModel(data)
        
        project.setModel(self.model)
        
        project.clicked.connect(self.select_structure)

        layout.addWidget(project)
        project.resizeRowsToContents()
        
        bouton = QPushButton("Fermer")
        bouton.clicked.connect(self.close)
        layout.addWidget(bouton)
        
        self.setLayout(layout)

    def close(self):
        self.appController.goBack()


    def select_structure(self, mi):
        if mi :
            self.deleteButton.setEnabled(True)
            self.selectedStructure = self.structures[mi.row()]
        else : 
            self.deleteButton.setEnabled(False)
            self.selectedStructure = None

    def delete(self):
        if self.selectedStructure:
            self.structureController.deleteStructure(self.selectedStructure.id,self.selectedStructure.room)
