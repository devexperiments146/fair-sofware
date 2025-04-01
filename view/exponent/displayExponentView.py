from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from view.tableModel import TableModel
import pandas as pd
import sys

class DisplayExponentView(QWidget):

    def __init__(self,store,appController,exponentController):
        super().__init__()
        self.appController = appController
        self.exponentController = exponentController
        self.store = store
        label = QLabel("Exposants")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.exponents = self.store.getSelectedProject().exponents


        self.deleteButton =  QPushButton("Tout supprimer")
        self.deleteButton.clicked.connect(self.deleteAll)
        layout.addWidget(self.deleteButton)

        table = QtWidgets.QTableView()
        rows = []
        datas = []
        for i in range(0,len(self.exponents),1):
            currentExponent = self.exponents[i]
            date = ""
            if currentExponent.date:
                date = currentExponent.date.strftime('%d/%m/%Y')
            tableType = ""
            if currentExponent.tableType:
                tableType = currentExponent.tableType
            description = ""
            if currentExponent.description:
                description = currentExponent.description
            nextExponent = ""
            if currentExponent.nextExponentId:
                exponents = [x for x in self.store.getSelectedProject().exponents if x.id == currentExponent.nextExponentId]
                if exponents[0]:
                    nextExponent = exponents[0].getName()
            roomChoice = ""
            nextDoor = ""
            tableLineChoice = ""
            tableLinePosition = ""
            if currentExponent.roomChoiceId:
                rooms = [x for x in self.store.getSelectedProject().rooms if x.id == currentExponent.roomChoiceId]
                if rooms[0]:
                    roomChoice = rooms[0].getName()    
                    if currentExponent.nextDoorId: 
                        doors = [x for x in rooms[0].doors if x.id == currentExponent.nextDoorId]
                        if doors[0]:
                            nextDoor = doors[0].getName()
                    if currentExponent.tableLineChoiceId: 
                        tableLines = [x for x in rooms[0].tableLines if x.id == currentExponent.tableLineChoiceId]
                        if tableLines[0]:
                            tableLineChoice = tableLines[0].getName()
                            if currentExponent.tableLinePosition != None: 
                                tableLinePosition = currentExponent.tableLinePosition
            nextWall = ""
            if currentExponent.nextWall != None:
                if currentExponent.nextWall:
                    nextWall = "Oui"
                else: 
                    nextWall = "Non"
            endOfTable = ""
            if currentExponent.endOfTable != None:
                if currentExponent.endOfTable:
                    endOfTable = "Oui"
                else: 
                    endOfTable = "Non"
            datas.append([currentExponent.firstname,currentExponent.lastname,date,tableType,description,nextExponent,roomChoice,nextDoor,nextWall,tableLineChoice,tableLinePosition,endOfTable])
            rows.append(currentExponent.id)

        self.data = pd.DataFrame(datas, columns = ['Firstname', 'Lastname','Date inscription','Type table','Description','A coté exposant','Choix salle', 'A coté porte', 'A coté mur',"Ligne de table","Position sur ligne de table","Bout de table"], index=rows)   
        self.model = TableModel(self.data)
        self.proxy_model = QSortFilterProxyModel(self.model)
        self.proxy_model.setSourceModel(self.model)
        table.setModel(self.proxy_model)

        layout.addWidget(table)
        table.resizeRowsToContents()



        self.search = QLineEdit()
        self.search.returnPressed.connect(self.searchExponent)
        layout.addWidget(self.search)

        bouton = QPushButton("Fermer")
        bouton.clicked.connect(self.close)
        layout.addWidget(bouton)

        self.setLayout(layout)
        table.doubleClicked.connect(self.updateExponent)
    
    def searchExponent(self):
        self.proxy_model.setFilterRegularExpression(QRegularExpression(self.search.text()))
        
    def deleteAll(self):
        self.exponentController.deleteAllExponents()

    def updateExponent(self, mi):
        if mi :
            selectedExponent = self.exponents[mi.row()]
            self.exponentController.displayUpdateExponent(selectedExponent)

        
    def close(self):
        self.appController.goBack()