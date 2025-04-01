
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
from infrastructure.repositories.parameterRepository import ParameterRepository

from application.mapper.projectMapper import ProjectMapper

import csv
import json 

class ParameterController:
  def __init__(self,window,store,session):
    self.window = window
    self.store = store
    self.parameterRepository = ParameterRepository(session)
   
  def loadParameters(self):
    parameters = self.parameterRepository.getParameters()
    self.store.setParameters(parameters)
    
  def updateParameter(self,name,value):
    self.parameterRepository.updateParameterValue(name,value)
