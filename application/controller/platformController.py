
from model.objects.room import Room
from model.objects.door import Door
from model.objects.exponent import Exponent
from model.objects.project import Project
from model.objects.tableGroup import TableGroup
from model.objects.table import Table
from model.objects.platform import Platform

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

from application.mapper.projectMapper import ProjectMapper

import csv
import json 

class PlatformController:
  def __init__(self,window,store,session):
    self.window = window
    self.store = store
    self.platformRepository = PlatformRepository(session)

  def addPlatform(self,room,name,length,width,orientation):
    platform = Platform(0,name,room,0,0,0,0,orientation,float(width.replace(",",".")),float(length.replace(",",".")))
    id = self.platformRepository.addPlatform(self.store.getSelectedProject(),platform)
    platform.id = id
    platforms = self.getPlatforms(room)
    platforms.append(platform)  
    self.window.displayDrawer("controller")
    
  def getPlatforms(self,room):
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    return rooms[0].platforms
  
  def updatePlatform(self,id,shiftX,shiftY,room):
    platforms =  [x for x in room.platforms if x.id ==id]
    platform = platforms[0]
    platform.x = platform.x + shiftX
    platform.y = platform.y + shiftY
    platform.reelX = platform.x/self.store.getMultiplier()
    platform.reelY = platform.y /self.store.getMultiplier()
    self.platformRepository.updatePlatform(platform)

  def deletePlatform(self,id,room):
    self.platformRepository.deletePlatform(id)
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    platforms = [x for x in rooms[0].platforms if x.id == id]
    rooms[0].platforms.remove(platforms[0])
    self.window.displayDrawer("controller")

