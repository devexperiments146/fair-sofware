
from model.objects.room import Room
from model.objects.door import Door
from model.objects.exponent import Exponent
from model.objects.project import Project
from model.objects.tableGroup import TableGroup
from model.objects.table import Table
from model.objects.platform import Platform
from model.objects.structure import Structure

from model.usecases.shareExponentsUsecase import ShareExponentsUsecase
from model.usecases.regroupExponentsUsecase import RegroupExponentsUsecase

from model.usecases.returnNextWallTableLineUsecase import ReturnNextWallTableLineUsecase


from model.usecases.printPdf import PrintPdf

from infrastructure.repositories.doorRepository import DoorRepository
from infrastructure.repositories.exponentRepository import ExponentRepository
from infrastructure.repositories.projectRepository import ProjectRepository
from infrastructure.repositories.roomRepository import RoomRepository
from infrastructure.repositories.tableGroupRepository import TableGroupRepository
from infrastructure.repositories.tableLineRepository import TableLineRepository
from infrastructure.repositories.platformRepository import PlatformRepository
from infrastructure.repositories.structureRepository import StructureRepository

from application.mapper.projectMapper import ProjectMapper

import csv
import json 

class StructureController:
  def __init__(self,window,store,session):
    self.window = window
    self.store = store
    self.structureRepository = StructureRepository(session)

  def addStructure(self,room,name,length,width,orientation,structureType):
    structure = Structure(0,name,room,0,0,0,0,orientation,float(width.replace(",",".")),float(length.replace(",",".")),structureType)
    id = self.structureRepository.addStructure(self.store.getSelectedProject(),structure)
    structure.id = id
    structures = self.getStructures(room)
    structures.append(structure)  
    self.window.displayDrawer("controller")
    
  def getStructures(self,room):
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    return rooms[0].structures
  
  def updatePositionStructure(self,id,x,y,room):
    structures =  [x for x in room.structures if x.id ==id]
    structure = structures[0]
    structure.x = x
    structure.y = y
    structure.reelX = structure.x/self.store.getMultiplier()
    structure.reelY = structure.y /self.store.getMultiplier()
    self.structureRepository.updateStructure(structure)

  def deleteStructure(self,id,room):
    self.structureRepository.deleteStructure(id)
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    structures = [x for x in rooms[0].structures if x.id == id]
    rooms[0].structures.remove(structures[0])
    self.window.displayDrawer("controller")

  def updateStructure(self,structure,reelX,reelY,structureType):
    structure.reelX = float(reelX.replace(",","."))
    structure.reelY = float(reelY.replace(",","."))
    structure.x = structure.reelX*self.store.getMultiplier()  
    structure.y = structure.reelY *self.store.getMultiplier()  
    structure.structureType = structureType
    self.structureRepository.updateStructure(structure)
    self.window.displayDrawer("controller")

  def displayUpdateStructure(self,structure):
    self.window.displayUpdateStructure(structure)