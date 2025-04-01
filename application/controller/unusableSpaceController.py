
from model.objects.room import Room
from model.objects.door import Door
from model.objects.exponent import Exponent
from model.objects.project import Project
from model.objects.tableGroup import TableGroup
from model.objects.table import Table
from model.objects.unusableSpace import UnusableSpace

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
from infrastructure.repositories.unusableSpaceRepository import UnusableSpaceRepository

from application.mapper.projectMapper import ProjectMapper

import csv
import json 

class UnusableSpaceController:
  def __init__(self,window,store,session):
    self.window = window
    self.store = store
    self.unusableSpaceRepository = UnusableSpaceRepository(session)

  def addUnusableSpace(self,room,name,length,width,orientation):
    unusableSpace = UnusableSpace(0,name,room,0,0,0,0,orientation,float(width.replace(",",".")),float(length.replace(",",".")))
    id = self.unusableSpaceRepository.addUnusableSpace(self.store.getSelectedProject(),unusableSpace)
    unusableSpace.id = id
    unusableSpaces = self.getUnusableSpaces(room)
    unusableSpaces.append(unusableSpace)  
    self.window.displayDrawer("controller")
    
  def getUnusableSpaces(self,room):
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    return rooms[0].unusableSpaces
  
  def updateUnusableSpace(self,id,shiftX,shiftY,room):
    unusableSpaces =  [x for x in room.unusableSpaces if x.id ==id]
    unusableSpace = unusableSpaces[0]
    unusableSpace.x = unusableSpace.x + shiftX
    unusableSpace.y = unusableSpace.y + shiftY
    unusableSpace.reelX = unusableSpace.x/self.store.getMultiplier()
    unusableSpace.reelY = unusableSpace.y /self.store.getMultiplier()
    self.unusableSpaceRepository.updateUnusableSpace(unusableSpace)

  def deleteUnusableSpace(self,id,room):
    self.unusableSpaceRepository.deleteUnusableSpace(id)
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    unusableSpaces = [x for x in rooms[0].unusableSpaces if x.id == id]
    rooms[0].unusableSpaces.remove(unusableSpaces[0])
    self.window.displayDrawer("controller")

