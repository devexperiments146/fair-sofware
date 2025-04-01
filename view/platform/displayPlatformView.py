from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from view.tableModel import TableModel
import pandas as pd

class DisplayPlatformView(QWidget):

    def __init__(self,store,appController,platformController):
        super().__init__()
        self.appController = appController
        self.platformController = platformController
        
        label = QLabel("Estrades")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.appController = appController

        self.platforms  = []
        for room in store.getSelectedProject().rooms:
           self.platforms += room.platforms

        self.deleteButton =  QPushButton("Supprimer")
        self.deleteButton.clicked.connect(self.delete)
        self.deleteButton.setEnabled(False)
        layout.addWidget(self.deleteButton)

        project = QtWidgets.QTableView()
        
        rows = []
        datas = []
        for i in range(0,len(self.platforms),1):
            currentPlatform = self.platforms[i]
            datas.append([currentPlatform.name,currentPlatform.x,currentPlatform.y,currentPlatform.reelX,currentPlatform.reelY,currentPlatform.width,currentPlatform.length,currentPlatform.orientation])
            rows.append(currentPlatform.id)
         
        data = pd.DataFrame(datas, columns = ['Name','x','y','x (reel)','y (Reel)','Width','Length','Orientation'], index=rows)   
        self.model = TableModel(data)
        
        project.setModel(self.model)
        
        project.clicked.connect(self.select_platform)

        layout.addWidget(project)
        project.resizeRowsToContents()
        
        bouton = QPushButton("Fermer")
        bouton.clicked.connect(self.close)
        layout.addWidget(bouton)
        
        self.setLayout(layout)

    def close(self):
        self.appController.goBack()


    def select_platform(self, mi):
        if mi :
            self.deleteButton.setEnabled(True)
            self.selectedPlatform = self.platforms[mi.row()]
        else : 
            self.deleteButton.setEnabled(False)
            self.selectedPlatform = None

    def delete(self):
        if self.selectedPlatform:
            self.platformController.deletePlatform(self.selectedPlatform.id,self.selectedPlatform.room)
