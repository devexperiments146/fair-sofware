
from model.objects.room import Room
from model.objects.door import Door
from model.objects.exponent import Exponent
from model.objects.project import Project
from model.objects.tableGroup import TableGroup
from model.objects.table import Table
from model.objects.tableLine import TableLine

from model.usecases.printPdf import PrintPdf

from infrastructure.repositories.doorRepository import DoorRepository
from infrastructure.repositories.exponentRepository import ExponentRepository
from infrastructure.repositories.projectRepository import ProjectRepository
from infrastructure.repositories.roomRepository import RoomRepository
from infrastructure.repositories.tableGroupRepository import TableGroupRepository
from infrastructure.repositories.tableLineRepository import TableLineRepository
from infrastructure.repositories.tableRepository import TableRepository

from application.mapper.projectMapper import ProjectMapper

import csv
import json 

class TableGroupController:
  def __init__(self,window,store,session):
    self.window = window
    self.store = store
    self.tableGroupRepository = TableGroupRepository(session,store)
    
  def addTableGroup(self,tableWidth,tableLength,color,maxQuantity,tableType):
    tableGroup = TableGroup(0,float(tableWidth.replace(",",".")),float(tableLength.replace(",",".")),color,maxQuantity,tableType)
    id = self.tableGroupRepository.addTableGroup(tableGroup)
    tableGroup.id = id
    selectedProject = self.store.getSelectedProject()
    selectedProject.tableGroups.append(tableGroup)   
    self.window.refreshMenu()
    self.window.displayDrawer("controller")