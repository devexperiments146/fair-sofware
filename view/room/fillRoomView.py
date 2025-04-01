from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class FillRoomView(QWidget):

    def __init__(self,store,appController,roomController):
        super().__init__()
        self.store = store
        self.appController = appController
        self.roomController = roomController

        super().__init__()
        label = QLabel("Remplir salle de tables")   
        layout = QFormLayout()
        layout.addWidget(label)

        selectedProject = store.getSelectedProject();

        comboboxRooms = []
        self.rooms = selectedProject.rooms
        for i in range(0,len(self.rooms),1):
            comboboxRooms.append(self.rooms[i].getName())
        self.room = QComboBox()
        self.room.addItems(comboboxRooms)
        self.room.activated.connect(self.check_index_table_room)
        layout.addRow("Salle:", self.room )

        comboboxTableGroups = []
        self.tableGroups =  selectedProject.rooms.tableGroups
        for i in range(0,len(self.tableGroups),1):
            comboboxTableGroups.append(self.tableGroups[i].getName())
        self.tableGroup = QComboBox()
        self.tableGroup.addItems(comboboxTableGroups)
        self.tableGroup.activated.connect(self.check_index_table_group)
        layout.addRow("Groupe de table:", self.tableGroup )

        self.distanceFromTheWall = QLineEdit()
        self.distanceFromTheWall.setValidator(QIntValidator(1, 999, self))
        layout.addRow("Distance du mur:", self.distanceFromTheWall)
        
        self.numberOfAlleys = QLineEdit()
        self.numberOfAlleys.setValidator(QIntValidator(1, 999, self))
        layout.addRow("Nombre d'allées:", self.numberOfAlleys)

        self.widthAlley = QLineEdit()
        self.widthAlley.setValidator(QIntValidator(1, 999, self))
        layout.addRow("Largeur des allées:", self.widthAlley)
    
        bouton = QPushButton("Valider")
        bouton.clicked.connect(self.fillRoom)
        layout.addWidget(bouton)
        self.setLayout(layout)

    def check_index_table_room(self, index):
        self.selectedRoom = self.rooms[index]

    def check_index_table_group(self, index):
        self.selectedTableGroup = self.tableGroups[index]

    def fillRoom(self):
        self.roomController.fillRoom(self.selectedRoom,self.selectedTableGroup,self.distanceFromTheWall.text(),self.numberOfAlleys.text(),self.widthAlley.text())