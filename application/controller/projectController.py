
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

class ProjectController:
  def __init__(self,window,store,session):
    self.window = window
    self.store = store
    self.projectRepository = ProjectRepository(session)
  
  def addProject(self,name):
    project = Project(0,name)
    id = self.projectRepository.addProject(project)
    project.id = id
    self.store.getProjects().append(project)  
    self.store.setSelectedProject(project)   
    self.window.refreshMenu()
    self.window.displayDrawer("controller")
    
  def loadProjects(self):
    self.store.setProjects(self.projectRepository.getProjects())

  def loadProject(self,project):
    self.store.setSelectedProject(self.projectRepository.getProject(project))
    self.window.refreshMenu()
    self.window.displayDrawer("controller")
  
  def exportProject(self,project,filename):
    with open(filename, 'w') as f:
      simpleProject = self.projectRepository.getProject(project)
      jsonProject = json.dumps(simpleProject,default=vars)
      f.write(jsonProject)
    self.window.displayDrawer("controller")
 
  def importProject(self,filename):
    with open(filename,'r',encoding="utf8") as json_file:
      jsonProject = json.load(json_file) 
      mapper = ProjectMapper()
      self.selectedProject = mapper.jsonToDomain(jsonProject)
    self.window.displayDrawer("controller")
