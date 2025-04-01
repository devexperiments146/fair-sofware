from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from view.tableModel import TableModel
import pandas as pd

class DisplayZoneView(QWidget):
    
    def __init__(self,store,appController,zoneController):
        super().__init__()
        self.store = store
        self.appController = appController
        self.zoneController = zoneController
        self.selectedZone = None
        label = QLabel("Zones")
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(label)
        self.zones = []
        for room in store.getSelectedProject().rooms:
            self.zones += room.zones


        self.deleteButton =  QPushButton("Supprimer")
        self.deleteButton.clicked.connect(self.delete)
        self.deleteButton.setEnabled(False)
        layout.addWidget(self.deleteButton)


        table = QtWidgets.QTableView()

        rows = []
        datas = []
        for i in range(0,len(self.zones),1):
            datas.append([self.zones[i].name,self.zones[i].room.getName(),self.zones[i].width,self.zones[i].length,self.zones[i].reelX,self.zones[i].reelY])
            rows.append(self.zones[i].id)
         
        data = pd.DataFrame(datas, columns = ['Name', 'Salle','Width', 'Length', 'x', 'y'], index=rows)   
        self.model = TableModel(data)
        table.setModel(self.model)

        table.clicked.connect(self.select_zone)

        layout.addWidget(table)
        table.resizeRowsToContents()
        
        bouton = QPushButton("Fermer")
        bouton.clicked.connect(self.close)
        layout.addWidget(bouton)

        self.setLayout(layout)
        table.doubleClicked.connect(self.updateZone)

        
    def close(self):
        self.appController.goBack()

    def select_zone(self, mi):
        if mi :
            self.deleteButton.setEnabled(True)
            self.selectedZone = self.zones[mi.row()]
        else : 
            self.deleteButton.setEnabled(False)
            self.selectedZone = None

    def delete(self):
        if self.selectedZone:
            self.zoneController.deleteZone(self.selectedZone.id,self.selectedZone.room)

    def updateZone(self, mi):
        if mi :
            selectedZone = self.zones[mi.row()]
            self.zoneController.displayUpdateZone(selectedZone)