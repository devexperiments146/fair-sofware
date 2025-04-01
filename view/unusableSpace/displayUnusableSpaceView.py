from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from view.tableModel import TableModel
import pandas as pd

class DisplayUnusableSpaceView(QWidget):

    def __init__(self,store,appController,unusableSpaceController):
        super().__init__()
        self.appController = appController
        self.unusableSpaceController = unusableSpaceController
        
        label = QLabel("Espace inutilisables")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.appController = appController

        self.unusableSpaces  = []
        for room in store.getSelectedProject().rooms:
           self.unusableSpaces += room.unusableSpaces

        self.deleteButton =  QPushButton("Supprimer")
        self.deleteButton.clicked.connect(self.delete)
        self.deleteButton.setEnabled(False)
        layout.addWidget(self.deleteButton)

        project = QtWidgets.QTableView()
        
        rows = []
        datas = []
        for i in range(0,len(self.unusableSpaces),1):
            currentUnusableSpace = self.unusableSpaces[i]
            datas.append([currentUnusableSpace.name,currentUnusableSpace.x,currentUnusableSpace.y,currentUnusableSpace.reelX,currentUnusableSpace.reelY,currentUnusableSpace.width,currentUnusableSpace.length,currentUnusableSpace.orientation])
            rows.append(currentUnusableSpace.id)
         
        data = pd.DataFrame(datas, columns = ['Name','x','y','x (reel)','y (Reel)','Width','Length','Orientation'], index=rows)   
        self.model = TableModel(data)
        
        project.setModel(self.model)
        
        project.clicked.connect(self.select_unusable_space)

        layout.addWidget(project)
        project.resizeRowsToContents()
        
        bouton = QPushButton("Fermer")
        bouton.clicked.connect(self.close)
        layout.addWidget(bouton)
        
        self.setLayout(layout)

    def close(self):
        self.appController.goBack()


    def select_unusable_space(self, mi):
        if mi :
            self.deleteButton.setEnabled(True)
            self.selectedUnusableSpace = self.unusableSpaces[mi.row()]
        else : 
            self.deleteButton.setEnabled(False)
            self.selectedUnusableSpace = None

    def delete(self):
        if self.selectedUnusableSpace:
            self.unusableSpaceController.deleteUnusableSpace(self.selectedUnusableSpace.id,self.selectedUnusableSpace.room)
