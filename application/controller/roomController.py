
from model.objects.room import Room
from model.objects.door import Door
from model.objects.exponent import Exponent
from model.objects.project import Project
from model.objects.tableGroup import TableGroup
from model.objects.table import Table
from model.objects.tableLine import TableLine

from model.usecases.printPdf import PrintPdf

from infrastructure.repositories.doorRepository import DoorRepository
from infrastructure.repositories.roomRepository import RoomRepository
from infrastructure.repositories.tableLineRepository import TableLineRepository
from infrastructure.repositories.tableRepository import TableRepository
from infrastructure.repositories.zoneRepository import ZoneRepository
from infrastructure.repositories.unusableSpaceRepository import UnusableSpaceRepository
from infrastructure.repositories.platformRepository import PlatformRepository

from application.mapper.projectMapper import ProjectMapper

import csv
import json 

class RoomController:
  def __init__(self,window,store,session):
    self.window = window
    self.store = store
    self.roomRepository = RoomRepository(session,store)
    self.tableRepository = TableRepository(session)
    self.doorRepository = DoorRepository(session,store)
    self.tableLineRepository = TableLineRepository(session)
    self.zoneRepository = ZoneRepository(session)
    self.unusableSpaceRepository = UnusableSpaceRepository(session)
    self.platformRepository = PlatformRepository(session)

  def addRoom(self,name,width,height):
    room = Room(0,name,float(width.replace(",",".")),float(height.replace(",",".")),0,0)
    id = self.roomRepository.addRoom(room)
    room.id = id
    self.store.getSelectedProject().rooms.append(room)
    self.window.refreshMenu()
    self.window.displayDrawer("controller")
 
  def importRoom(self,room):
    id = self.roomRepository.copyRoom(room)
    room.id = id
    self.store.getSelectedProject().rooms.append(room)
    self.window.refreshMenu()
    self.window.displayDrawer("controller")
 
  def loadRooms(self):
    rooms = self.roomRepository.loadRooms()
    print("Salles chargées")
    print(str(len(rooms)))
    self.store.setRooms(rooms)

  def deleteRoom(self,id):
    self.tableRepository.deleteAllTablesOfRoom(id)
    self.doorRepository.deleteAllDoorsOfRoom(id)
    self.tableLineRepository.deleteAllTableLinesOfRoom(id)
    self.zoneRepository.deleteAllZonesOfRoom(id)
    self.unusableSpaceRepository.deleteAllUnusableSpacesOfRoom(id)
    self.platformRepository.deleteAllPlatformsOfRoom(id)
    rooms = self.roomRepository.deleteRoom(id)
    
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==id]
    rooms.remove(rooms[0])
    self.window.displayDrawer("controller")

