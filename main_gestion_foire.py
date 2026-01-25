import sys

from view.room.createRoomView import CreateRoomView
from view.room.displayRoomView import DisplayRoomView
from view.room.importRoomView import ImportRoomView


from view.door.createDoorView import CreateDoorView
from view.door.displayDoorView import DisplayDoorView


from view.exponent.printForExponentView  import PrintForExponentView

from view.zone.createZoneView import CreateZoneView
from view.zone.displayZoneView import DisplayZoneView
from view.zone.updateZoneView import UpdateZoneView


from view.unusableSpace.createUnusableSpaceView import CreateUnusableSpaceView
from view.unusableSpace.displayUnusableSpaceView import DisplayUnusableSpaceView


from view.tableGroup.displayTableGroupView import DisplayTableGroupView
from view.tableGroup.createTableGroupView import CreateTableGroupView
from view.room.fillRoomView import FillRoomView

from view.table.displayTableView import DisplayTableView
from view.table.createTableView import CreateTableView
from view.table.updateTableView  import UpdateTableView

from view.project.displayProjectView import DisplayProjectView
from view.project.createProjectView import CreateProjectView
from view.project.exportProjectView import ExportProjectView
from view.project.importProjectView import ImportProjectView

from view.tableLine.createTableLineView import CreateTableLineView
from view.tableLine.displayTableLineView import DisplayTableLineView
from view.tableLine.fillTableLinesView import  FillTableLinesView
from view.tableLine.updateTableLineView import UpdateTableLineView
from view.tableLine.fillTableLinesWithoutExponentsView import FillTableLinesWithoutExponentsView


from view.exponent.displayExponentView import DisplayExponentView
from view.exponent.createExponentView import CreateExponentView
from view.exponent.updateExponentView import UpdateExponentView
from view.exponent.importFileView import ImportFileView

from view.platform.displayPlatformView import DisplayPlatformView
from view.platform.createPlatformView import CreatePlatformView

from view.structure.displayStructureView import DisplayStructureView
from view.structure.createStructureView import CreateStructureView
from view.structure.updateStructureView import UpdateStructureView


from view.drawer.drawerView import DrawerView
from view.table.fillTablesView import FillTablesView

from application.controller.appController import AppController
from application.controller.doorController import DoorController
from application.controller.exponentController import ExponentController
from application.controller.projectController import ProjectController
from application.controller.roomController import RoomController
from application.controller.tableController import TableController
from application.controller.tableGroupController import TableGroupController
from application.controller.tableLineController import TableLineController
from application.controller.parameterController import ParameterController
from application.controller.zoneController import ZoneController
from application.controller.unusableSpaceController import UnusableSpaceController
from application.controller.platformController import PlatformController
from application.controller.structureController import StructureController

from application.store.appStore import AppStore

from infrastructure.repositories.databaseRepository import DatabaseRepository

import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class MainWindow(QMainWindow, ):
    databaseRepository = DatabaseRepository()
    store = AppStore()

    def __init__(self):
        super().__init__()

        self.setStatusBar(QStatusBar(self))
        session = self.databaseRepository.getSession()
        self.doorController = DoorController(self,self.store,session)
        self.exponentController = ExponentController(self,self.store,session)
        self.projectController = ProjectController(self,self.store,session)
        self.roomController = RoomController(self,self.store,session)
        self.tableController = TableController(self,self.store,session)
        self.tableGroupController = TableGroupController(self,self.store,session)
        self.tableLineController = TableLineController(self,self.store,session)
        self.appController = AppController(self,self.store)
        self.parameterController = ParameterController(self,self.store,session)
        self.zoneController = ZoneController(self,self.store,session)
        self.unusableSpaceController = UnusableSpaceController(self,self.store,session)
        self.platformController = PlatformController(self,self.store,session)
        self.structureController = StructureController(self,self.store,session)
        
        self.parameterController.loadParameters()
        self.projectController.loadProjects()

        currentProjectParameter = self.store.getParameter("CURRENT_PROJECT")

        self.initMenu()    
        self.roomController.loadRooms()
        if(currentProjectParameter):
            projects = [x for x in self.store.getProjects() if x.id ==int(currentProjectParameter.value)]
            self.projectController.loadProject(projects[0])
        else: 
            self.refreshMenu()
            self.displayDrawer("view")

        
    def initMenu(self):
        menu = self.menuBar()
        self.project_menu = menu.addMenu("&Projets")
        button_action= QAction(QIcon("bug.png"), "&Créer projet", self)
        button_action.triggered.connect(self.displayCreateProject)

        button_action2= QAction(QIcon("bug.png"), "&Projets", self)
        button_action2.triggered.connect(self.displayProjects)

        button_action3= QAction(QIcon("bug.png"), "&Importer projet", self)
        button_action3.triggered.connect(self.displayImportProject)

        button_action4= QAction(QIcon("bug.png"), "&Exporter projet", self)
        button_action4.triggered.connect(self.displayExportProject)
        
        button_action5= QAction(QIcon("bug.png"), "&Export PDF", self)
        button_action5.triggered.connect(self.displayPDF)
               
        self.project_menu.addAction(button_action)
        self.project_menu.addAction(button_action2)
        self.project_menu.addSeparator()
        self.project_menu.addAction(button_action3)
        self.project_menu.addAction(button_action4)
        self.project_menu.addSeparator()
        self.project_menu.addAction(button_action5)


        self.room_menu = menu.addMenu("&Salles")
        self.table_menu = menu.addMenu("&Tables")
        self.exponent_menu = menu.addMenu("&Exposants")
        other_menu = menu.addMenu("&Autres")
        display_menu = menu.addMenu("&Affichage")
        help_menu = menu.addMenu("&Aide")

        button_action = QAction(QIcon("bug.png"), "&Créer salle", self)
        button_action.triggered.connect(self.displayCreateRoom)

        button_action2 = QAction(QIcon("bug.png"), "&Salles", self)
        button_action2.triggered.connect(self.displayRooms)


        button_action9 = QAction(QIcon("bug.png"), "&Importer salle", self)
        button_action9.triggered.connect(self.displayImportRoom)

        button_action3= QAction(QIcon("bug.png"), "&Créer porte", self)
        button_action3.triggered.connect(self.displayCreateDoor)

        button_action4= QAction(QIcon("bug.png"), "&Portes", self)
        button_action4.triggered.connect(self.displayDoors)

        button_action5= QAction(QIcon("bug.png"), "&Créer zones", self)
        button_action5.triggered.connect(self.displayCreateZones)

        button_action6= QAction(QIcon("bug.png"), "&Zones", self)
        button_action6.triggered.connect(self.displayZones)

        
        button_action7= QAction(QIcon("bug.png"), "&Créer espace inutilisables", self)
        button_action7.triggered.connect(self.displayCreateUnusableSpaces)

        button_action8= QAction(QIcon("bug.png"), "&Espace inutilisables", self)
        button_action8.triggered.connect(self.displayUnusableSpaces)

        self.room_menu.addAction(button_action)
        self.room_menu.addAction(button_action2)
        self.room_menu.addAction(button_action9)
        self.room_menu.addSeparator()
        self.room_menu.addAction(button_action3)
        self.room_menu.addAction(button_action4)
        self.room_menu.addSeparator()
        self.room_menu.addAction(button_action5)
        self.room_menu.addAction(button_action6)
        self.room_menu.addSeparator()
        self.room_menu.addAction(button_action7)
        self.room_menu.addAction(button_action8)

        button_action = QAction(QIcon("bug.png"), "&Créer groupe de tables", self)
        button_action.triggered.connect(self.displayCreateTableGroup)

        button_action2 = QAction(QIcon("bug.png"), "&Groupes de tables", self)
        button_action2.triggered.connect(self.displayTableGroups)

        button_action3= QAction(QIcon("bug.png"), "&Créer table", self)
        button_action3.triggered.connect(self.displayCreateTable)

        button_action4= QAction(QIcon("bug.png"), "&Tables", self)
        button_action4.triggered.connect(self.displayTables)


        button_action6= QAction(QIcon("bug.png"), "&Créer ligne de table", self)
        button_action6.triggered.connect(self.displayCreateTableLine)

        button_action7= QAction(QIcon("bug.png"), "&Lignes de table", self)
        button_action7.triggered.connect(self.displayTableLines)

        button_action8= QAction(QIcon("bug.png"), "&Remplir lignes de table", self)
        button_action8.triggered.connect(self.displayFillTableLines)

        button_action10= QAction(QIcon("bug.png"), "&Remplir lignes de table sans exposant", self)
        button_action10.triggered.connect(self.displayFillTableLinesWithoutExponents)

        button_action9= QAction(QIcon("bug.png"), "&Exporter tables", self)
        button_action9.triggered.connect(self.exportTables)

        self.table_menu.addAction(button_action)
        self.table_menu.addAction(button_action2)
        self.table_menu.addSeparator()
        self.table_menu.addAction(button_action3)
        self.table_menu.addAction(button_action4)
        self.table_menu.addSeparator()
        self.table_menu.addAction(button_action6)
        self.table_menu.addAction(button_action7)
        self.table_menu.addSeparator()
        self.table_menu.addAction(button_action8)
        self.table_menu.addAction(button_action10)
        self.table_menu.addAction(button_action9)

        button_action = QAction(QIcon("bug.png"), "&Créer exposant", self)
        button_action.triggered.connect(self.displayCreateExponent)

        button_action2 = QAction(QIcon("bug.png"), "&Exposants", self)
        button_action2.triggered.connect(self.displayExponents)

        button_action3= QAction(QIcon("bug.png"), "&Importer exposant", self)
        button_action3.triggered.connect(self.displayImportExponents)

        button_action4= QAction(QIcon("bug.png"), "&Exporter exposant", self)
        button_action4.triggered.connect(self.displayExportExponents)
        
        button_action5= QAction(QIcon("bug.png"), "&Imprimer pour exposant", self)
        button_action5.triggered.connect(self.displayExportPdfExponent)
        
        self.exponent_menu.addAction(button_action)
        self.exponent_menu.addAction(button_action2)
        self.exponent_menu.addSeparator()
        self.exponent_menu.addAction(button_action3)
        self.exponent_menu.addAction(button_action4)
        self.exponent_menu.addSeparator()
        self.exponent_menu.addAction(button_action5)
        
        
        button_action = QAction(QIcon("bug.png"), "&Créer estrade", self)
        button_action.triggered.connect(self.displayCreatePlatform)

        button_action2 = QAction(QIcon("bug.png"), "&Estrades", self)
        button_action2.triggered.connect(self.displayPlatforms)

        button_action3 = QAction(QIcon("bug.png"), "&Créer structure", self)
        button_action3.triggered.connect(self.displayCreateStructure)

        button_action4 = QAction(QIcon("bug.png"), "&Structures", self)
        button_action4.triggered.connect(self.displayStructures)


        other_menu.addAction(button_action)
        other_menu.addAction(button_action2)
        self.exponent_menu.addSeparator()
        other_menu.addAction(button_action3)
        other_menu.addAction(button_action4)

        button_action = QAction(QIcon("bug.png"), "Tables", self)
        button_action.triggered.connect(self.displayDrawerTables)
        button_action.setCheckable(True)
        button_action.setChecked(True)


        button_action2 = QAction(QIcon("bug.png"), "Lignes de tables", self)
        button_action2.triggered.connect(self.displayDrawerTableLines)
        button_action2.setCheckable(True)
        button_action2.setChecked(True)

        button_action3 = QAction(QIcon("bug.png"), "Portes", self)
        button_action3.triggered.connect(self.displayDrawerDoors)
        button_action3.setCheckable(True)
        button_action3.setChecked(True)

        button_action4 = QAction(QIcon("bug.png"), "Zones", self)
        button_action4.triggered.connect(self.displayDrawerZones)
        button_action4.setCheckable(True)
        button_action4.setChecked(False)

        button_action5 = QAction(QIcon("bug.png"), "Espace inutilisables", self)
        button_action5.triggered.connect(self.displayDrawerUnusableSpaces)
        button_action5.setCheckable(True)
        button_action5.setChecked(True)

        button_action6 = QAction(QIcon("bug.png"), "Mesures", self)
        button_action6.triggered.connect(self.displayMeasurements)
        button_action6.setCheckable(True)
        button_action6.setChecked(False)

        
        button_action6 = QAction(QIcon("bug.png"), "Echelle", self)
        button_action6.triggered.connect(self.displayScale)
        button_action6.setCheckable(True)
        button_action6.setChecked(True)

        display_menu.addAction(button_action)
        display_menu.addAction(button_action2)
        display_menu.addAction(button_action3)
        display_menu.addAction(button_action4)
        display_menu.addAction(button_action5)
        display_menu.addAction(button_action6)

        button_action = QAction(QIcon("bug.png"), "&Contenu", self)
        button_action.setStatusTip("")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)

        button_action2 = QAction(QIcon("bug.png"), "&A propos", self)
        button_action2.setStatusTip("")
        button_action2.triggered.connect(self.displayAbout)
        button_action2.setCheckable(True)

        help_menu.addAction(button_action)
        help_menu.addAction(button_action2)


    def refreshMenu(self):
        displayRoomsAndExponents = self.appController.displayRoomsAndExponents()
        if displayRoomsAndExponents:
            selectedProject = self.store.getSelectedProject()
            self.setWindowTitle("Gestion foire - "+selectedProject.getName())
        else:
            self.setWindowTitle("Gestion foire")
            
        displayTableGroupsAndDoors = self.appController.displayTableGroupsAndDoors()
        actions = self.project_menu.actions()
        actions[4].setEnabled(displayRoomsAndExponents)
        actions =  self.room_menu.actions()     
        for action in actions:
            action.setEnabled(displayRoomsAndExponents)
        actions[3].setEnabled(displayTableGroupsAndDoors)
        actions[4].setEnabled(displayTableGroupsAndDoors)
        actions =  self.table_menu.actions()    
        actions[0].setEnabled(displayTableGroupsAndDoors)
        actions[1].setEnabled(displayTableGroupsAndDoors)
        displayTables = self.appController.displayTables()
        actions[2].setEnabled(displayTables)
        actions[3].setEnabled(displayTables)
        actions[4].setEnabled(displayTables)
        actions[5].setEnabled(displayTables)
        actions[6].setEnabled(displayTables)
        actions[7].setEnabled(displayTables)
        actions[8].setEnabled(displayTables)
        actions =  self.exponent_menu.actions()     
        for action in actions:
            action.setEnabled(displayRoomsAndExponents)
    
    def show_view(self, widget):
        # Replace central widget cleanly: delete previous widget to free resources
        old = self.centralWidget()
        if old is not None:
            try:
                old.deleteLater()
            except Exception:
                pass
        self.setCentralWidget(widget)
      
    def onMyToolBarButtonClick(self, s):
        print("click", s)
 
    def displayCreateRoom(self):  
        widget = CreateRoomView(self.appController,self.roomController)
        self.show_view(widget)

    def displayDrawer(self, s):  
        widget = DrawerView(self.store,self.tableController,self.tableLineController,self.doorController,self.unusableSpaceController,self.zoneController,self.platformController,self.structureController)
        self.show_view(widget)

    def displayRooms(self, s):
        widget = DisplayRoomView(self.store,self.appController,self.roomController)
        self.show_view(widget)

    def displayImportRoom(self,s):
        widget = ImportRoomView(self.store,self.appController,self.roomController)
        self.show_view(widget)

    def displayCreateDoor(self, s):
        widget = CreateDoorView(self.store,self.appController,self.doorController)
        self.show_view(widget)

    def displayDoors(self, s):
        widget = DisplayDoorView(self.store,self.appController,self.doorController)
        self.show_view(widget)

    def displayCreateZones(self, s):
        widget = CreateZoneView(self.store,self.appController,self.zoneController)
        self.show_view(widget)

    def displayZones(self, s):
        widget = DisplayZoneView(self.store,self.appController,self.zoneController)
        self.show_view(widget)

    def displayCreateUnusableSpaces(self, s):
        widget = CreateUnusableSpaceView(self.store,self.appController,self.unusableSpaceController)
        self.show_view(widget)

    def displayUnusableSpaces(self, s):
        widget = DisplayUnusableSpaceView(self.store,self.appController,self.unusableSpaceController)
        self.show_view(widget)

    def displayCreateTableGroup(self, s):
        widget = CreateTableGroupView(self.store,self.appController,self.tableGroupController)
        self.show_view(widget)
  
    def displayTableGroups(self, s):
        widget = DisplayTableGroupView(self.store,self.appController)
        self.show_view(widget)
  
    def displayCreateTable(self, s):
        widget = CreateTableView(self.store,self.appController,self.tableController)
        self.show_view(widget)

    def displayTables(self, s):
        widget = DisplayTableView(self.store,self.appController,self.tableController)
        self.show_view(widget)

    def displayExponents(self, s):
        widget = DisplayExponentView(self.store,self.appController,self.exponentController)
        self.setCentralWidget(widget)           

    def displayCreateExponent(self, s):
        widget = CreateExponentView(self.store,self.appController,self.exponentController)
        self.show_view(widget)

    def displayImportExponents(self, s):
        widget = ImportFileView(self.appController,self.exponentController)
        self.show_view(widget)
  
    def displayUpdateExponent(self, exponent):
        widget = UpdateExponentView(self.store,exponent,self.appController,self.exponentController)
        self.show_view(widget)

    def displayUpdateTableView(self, table):
        widget = UpdateTableView(self.store,table,self.appController,self.tableController)
        self.show_view(widget)

    def displayExportExponents(self, s):
        label = QLabel("Export exponents")
        self.show_view(label)    

    def displayExportPdfExponent(self):
        widget = PrintForExponentView(self.store,self.appController,self.exponentController)
        self.show_view(widget)


    def displayAbout(self, s):
        label = QLabel("About")
        self.show_view(label)    

    def displayCreateProject(self, s):
        widget = CreateProjectView(self.store,self.appController,self.projectController,self.parameterController)
        self.show_view(widget)

    def displayProjects(self, s):
        widget = DisplayProjectView(self.store,self.appController,self.projectController,self.parameterController)
        self.show_view(widget)

    def displayImportProject(self, s):
        widget = ImportProjectView(self.appController,self.projectController)
        self.show_view(widget)

    def displayExportProject(self, s):
        widget = ExportProjectView(self.store,self.appController,self.projectController)
        self.show_view(widget)

    def displayPDF(self,s):
        widget = DrawerView(self.store,self.tableController,self.tableLineController,self.doorController,self.unusableSpaceController,self.zoneController,self.platformController,self.structureController)
        self.appController.printPdf(widget.getViews())

    def displayExponentPDF(self,exponent):
        self.store.setDisplayExponent(exponent)
        widget = DrawerView(self.store,self.tableController,self.tableLineController,self.doorController,self.unusableSpaceController,self.zoneController,self.platformController,self.structureController)
        self.appController.printPdf(widget.getViews())
        self.store.setDisplayExponent(None)
        self.displayDrawer("view")

    def displayCreateTableLine(self, s):
        widget = CreateTableLineView(self.store,self.appController,self.tableLineController)
        self.show_view(widget)

    def displayTableLines(self, s):
        widget = DisplayTableLineView(self.store,self.appController,self.tableLineController)
        self.show_view(widget)
        
    def displayFillTableLines(self, s):
        widget = FillTableLinesView(self.store,self.appController,self.tableController)
        self.show_view(widget)
         
    def displayFillTableLinesWithoutExponents(self, s):
        widget = FillTableLinesWithoutExponentsView(self.store,self.appController,self.tableController)
        self.show_view(widget)
 
    def exportTables(self,s):
        self.tableController.exportTables(self.store)
    
    def displayUpdateTableLine(self, tableLine):
        widget = UpdateTableLineView(tableLine,self.appController,self.tableLineController)
        self.show_view(widget)
 
    def displayUpdateZone(self, zone):
        widget = UpdateZoneView(zone,self.appController,self.zoneController)
        self.show_view(widget)

    def displayDrawerTables(self,s):
        self.store.setDisplayTables(s)
        widget = DrawerView(self.store,self.tableController,self.tableLineController,self.doorController,self.unusableSpaceController,self.zoneController,self.platformController,self.structureController)
        self.show_view(widget)

    def displayDrawerTableLines(self,s):
        self.store.setDisplayTableLines(s)
        widget = DrawerView(self.store,self.tableController,self.tableLineController,self.doorController,self.unusableSpaceController,self.zoneController,self.platformController,self.structureController)
        self.show_view(widget)

    def displayDrawerDoors(self,s):
        self.store.setDisplayDoors(s)
        widget = DrawerView(self.store,self.tableController,self.tableLineController,self.doorController,self.unusableSpaceController,self.zoneController,self.platformController,self.structureController)
        self.show_view(widget)

    def displayDrawerZones(self,s):
        self.store.setDisplayZones(s)
        widget = DrawerView(self.store,self.tableController,self.tableLineController,self.doorController,self.unusableSpaceController,self.zoneController,self.platformController,self.structureController)
        self.show_view(widget)

    def displayDrawerUnusableSpaces(self,s):
        self.store.setDisplayUnusableSpaces(s)
        widget = DrawerView(self.store,self.tableController,self.tableLineController,self.doorController,self.unusableSpaceController,self.zoneController,self.platformController,self.structureController)
        self.show_view(widget)
    
    def displayDrawerPlatforms(self,s):
        self.store.setDisplayPlatforms(s)
        widget = DrawerView(self.store,self.tableController,self.tableLineController,self.doorController,self.unusableSpaceController,self.zoneController,self.platformController,self.structureController)
        self.show_view(widget)

    def displayDrawerStructures(self,s):
        self.store.setDisplayStructures(s)
        widget = DrawerView(self.store,self.tableController,self.tableLineController,self.doorController,self.unusableSpaceController,self.zoneController,self.platformController,self.structureController)
        self.show_view(widget)

    def displayMeasurements(self,s):
        self.store.setDisplayMeasurements(s)
        widget = DrawerView(self.store,self.tableController,self.tableLineController,self.doorController,self.unusableSpaceController,self.zoneController,self.platformController,self.structureController)
        self.show_view(widget)

    def displayScale(self,s):
        self.store.displayScale(s)
        widget = DrawerView(self.store,self.tableController,self.tableLineController,self.doorController,self.unusableSpaceController,self.zoneController,self.platformController,self.structureController)
        self.show_view(widget)

    def displayPlatforms(self, s):
        widget = DisplayPlatformView(self.store,self.appController,self.platformController)
        self.show_view(widget)           

    def displayCreatePlatform(self, s):
        widget = CreatePlatformView(self.store,self.appController,self.platformController)
        self.show_view(widget)

    def displayStructures(self, s):
        widget = DisplayStructureView(self.store,self.appController,self.structureController)
        self.show_view(widget)     

    def displayUpdateStructure(self, structure):
        widget = UpdateStructureView(self.store,structure,self.appController,self.structureController)
        self.show_view(widget)  

    def displayCreateStructure(self, s):
        widget = CreateStructureView(self.store,self.appController,self.structureController)
        self.show_view(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
