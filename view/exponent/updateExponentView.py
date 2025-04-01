from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class UpdateExponentView(QWidget):

    def __init__(self,store,exponent,appController,exponentController):
        super().__init__()
        self.appController = appController
        self.exponentController = exponentController
        self.currentExponent = exponent
        label = QLabel("Modifier exposant")   
        layout = QFormLayout()
        layout.addWidget(label)

        self.tableTypes = store.getTableTypes()
        selectedProject = store.getSelectedProject()

        comboboxRooms = []
        self.rooms = selectedProject.rooms

        self.exponentFirstname = QLineEdit()
        layout.addRow("Prénom:", self.exponentFirstname)
        self.exponentFirstname.setText(exponent.firstname)

        self.exponentLastname = QLineEdit()
        layout.addRow("Nom:", self.exponentLastname)
        self.exponentLastname.setText(exponent.lastname)

        self.tableTypesCB= QComboBox()
        self.tableTypesCB.addItems(self.tableTypes)
        self.tableTypesCB.activated.connect(self.check_index_tableTypes)
        self.tableTypesCB.setCurrentIndex(self.tableTypes.index(exponent.tableType.strip()));
        self.selectedTableType = exponent.tableType
        layout.addRow("Type de table:", self.tableTypesCB)

        comboboxRooms.append("Aucun")
        for i in range(0,len(self.rooms),1):
            comboboxRooms.append(self.rooms[i].getName())
        self.room = QComboBox()
        self.room.addItems(comboboxRooms)
        self.room.activated.connect(self.check_index_rooms)
        self.selectedRoom = None
        layout.addRow("Salle:", self.room )

        comboboxExponents = []
        self.exponents = sorted(selectedProject.exponents, key=lambda x: x.lastname) 
        comboboxExponents.append("Aucun")
        for i in range(0,len(self.exponents),1):
            comboboxExponents.append(self.exponents[i].getName())
        self.nextExponent = QComboBox()
        self.nextExponent.addItems(comboboxExponents)
        self.nextExponent.activated.connect(self.check_index_exponents)
        self.selectedExponent = None
        layout.addRow("A coté exposant:", self.nextExponent)

        comboboxDoors = []
        self.doors  = []
        for room in store.getSelectedProject().rooms:
           self.doors += room.doors

        comboboxDoors.append("Aucun")
        for i in range(0,len(self.doors),1):
            comboboxDoors.append(self.doors[i].getName())
        self.nextDoor= QComboBox()
        self.nextDoor.addItems(comboboxDoors)
        self.nextDoor.activated.connect(self.check_index_doors)
        self.selectedDoor = None
        layout.addRow("A coté porte:", self.nextDoor)

        self.nextWall= QComboBox()
        self.nextWall.addItems(["Pas d'avis","Oui","Non"])
        self.nextWall.activated.connect(self.check_index_wall)
        self.selectedWall= None
        layout.addRow("A coté Mur:", self.nextWall)

        self.endOfTable= QComboBox()
        self.endOfTable.addItems(["Pas d'avis","Oui","Non"])
        self.endOfTable.activated.connect(self.check_index_end_of_wall)
        self.selectedEndOfTable= None
        layout.addRow("Bout de table:", self.endOfTable)

        comboboxTableLines = []
        self.tableLines  = []
        for room in store.getSelectedProject().rooms:
           self.tableLines += room.tableLines

        comboboxTableLines.append("Aucun")
        for i in range(0,len(self.tableLines),1):
            comboboxTableLines.append(self.tableLines[i].getName())
        self.tableLineChoice= QComboBox()
        self.tableLineChoice.addItems(comboboxTableLines)
        self.tableLineChoice.activated.connect(self.check_index_table_lines)
        self.selectedTableLine = None
        layout.addRow("Ligne de table:", self.tableLineChoice)

        self.tableLinePosition = QLineEdit()
        layout.addRow("Position sur ligne de table (%):", self.tableLinePosition )
        self.tableLinePosition.setValidator(QIntValidator(0, 100, self))

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validExponent)
        layout.addRow(cancelButton, validButton)
        self.setLayout(layout)
        
    def validExponent(self):
        self.exponentController.updateExponent(self.currentExponent,self.exponentFirstname.text(),self.exponentLastname.text(),self.selectedTableType,self.selectedRoom,self.selectedExponent,self.selectedDoor,self.selectedWall,self.selectedTableLine,self.tableLinePosition.text(),self.selectedEndOfTable)

    def check_index_rooms(self, index):
        if index > 0:
            self.selectedRoom = self.rooms[index-1]
            self.doors = self.selectedRoom.doors
            self.tableLines = self.selectedRoom.tableLines
            self.selectedDoor = None
            self.selectedTableLine = None
        else:
            self.selectedDoor = None
            self.selectedRoom = None
            self.selectedTableLine = None

    def check_index_exponents(self, index):
        if index > 0:
            self.selectedExponent = self.exponents[index-1]
        else:
            self.selectedExponent = None

    def check_index_doors(self, index):
        if index > 0:
            self.selectedDoor = self.doors[index-1]
        else:
            self.selectedDoor = None

    def check_index_table_lines(self, index):
        if index > 0:
            self.selectedTableLine = self.tableLines[index-1]
        else:
            self.selectedTableLine = None

    def check_index_wall(self, index):
        match index:
            case 1:
                self.selectedWall = True
            case 2:
                self.selectedWall = False
            case _:
                self.selectedWall = None

    def check_index_end_of_wall(self, index):
        match index:
            case 1:
                self.selectedEndOfTable = True
            case 2:
                self.selectedEndOfTable = False
            case _:
                self.selectedEndOfTable = None

    def check_index_tableTypes(self, index):
        self.selectedTableType = self.tableTypes[index]

    def close(self):
        self.appController.goBack()