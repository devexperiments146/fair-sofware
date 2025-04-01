
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

class AppController:
  def __init__(self,window,store):
    self.window = window
    self.store = store

  def displayRoomsAndExponents(self):
    self.selectedProject = self.store.getSelectedProject()
    return self.selectedProject != None
  
  def displayTableGroupsAndDoors(self):
    return self.displayRoomsAndExponents() and len(self.selectedProject.rooms) > 0
  
  def displayTables(self):
    return self.displayTableGroupsAndDoors() and len(self.selectedProject.tableGroups) > 0
    
  def displayAssignExponents(self):
    self.selectedProject = self.store.getSelectedProject()
    return self.displayTables() and len(self.selectedProject.rooms[0].tables) > 0 and len(self.selectedProject.exponents) > 0
  
  def printPdf(self,views,exponent = None):
    usecase = PrintPdf(views,exponent)
    usecase.execute()

  def goBack(self):
    self.window.displayDrawer("controller")



