from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class CreateTableView(QWidget):


    def __init__(self,store,appController,tableController):
        super().__init__()
        self.store = store
        self.appController = appController
        self.tableController = tableController

        selectedProject = store.getSelectedProject()

        label = QLabel("Créer table")   
        layout = QFormLayout()
        layout.addWidget(label)

        self.name = QLineEdit()
        layout.addRow("Nom:", self.name)

        comboboxExponents = []

        #search which does'nt have a table
        tableExponents = []
        self.exponents  = []
        for room in selectedProject.rooms:
            for table in room.tables:
                if(table.exponent != None):
                    tableExponents.append(table.exponent)     
        for exponent in selectedProject.exponents:
            freeExponents = [x for x in tableExponents if x.id == exponent.id]
            if(len(freeExponents)==0):  
                self.exponents.append(exponent)      
        if(len(self.exponents)>0):
            for i in range(0,len(self.exponents),1):
                comboboxExponents.append(self.exponents[i].getName())
            self.nextExponent = QComboBox()
            self.nextExponent.addItems(comboboxExponents)
            self.nextExponent.activated.connect(self.check_index_exponents)
            self.selectedExponent = self.exponents[0]
            layout.addRow("Exposant:", self.nextExponent)
        else:
            self.selectedExponent = None
        comboboxRooms = []
        self.rooms = selectedProject.rooms
        for i in range(0,len(self.rooms),1):
            comboboxRooms.append(self.rooms[i].getName())
        self.room = QComboBox()
        self.room.addItems(comboboxRooms)
        self.room.activated.connect(self.check_index_table_room)
        layout.addRow("Salle:", self.room )
        self.selectedRoom = self.rooms[0]

        comboboxTableGroups = []
        self.tableGroups = selectedProject.tableGroups
        for i in range(0,len(self.tableGroups),1):
            comboboxTableGroups.append(self.tableGroups[i].getName())
        self.tableGroup = QComboBox()
        self.tableGroup.addItems(comboboxTableGroups)
        self.tableGroup.activated.connect(self.check_index_table_group)
        layout.addRow("Groupe de table:", self.tableGroup )
        self.selectedTableGroup = self.tableGroups[0]

        self.orientation = QComboBox()
        self.orientation.addItems(self.store.getOrientations())
        self.orientation.activated.connect(self.check_index_orientation)
        layout.addRow("Orientation:", self.orientation )
        self.selectedOrientation=self.store.getOrientations()[0]

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validTable)
        layout.addRow(cancelButton, validButton)
        self.setLayout(layout)


    def check_index_table_room(self, index):
        self.selectedRoom = self.rooms[index]

    def check_index_table_group(self, index):
        self.selectedTableGroup = self.tableGroups[index]

    def check_index_orientation(self, index):
        self.selectedOrientation=self.store.getOrientations()[index]

    def validTable(self):
        self.tableController.addTable(self.name.text(),self.selectedRoom,self.selectedTableGroup,self.selectedOrientation,self.selectedExponent) 

    def check_index_exponents(self, index):
        self.selectedExponent = self.exponents[index]


    def close(self):
        self.appController.goBack()