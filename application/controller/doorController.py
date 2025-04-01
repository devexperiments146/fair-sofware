
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

class DoorController:
  def __init__(self,window,store,session):
    self.window = window
    self.store = store
    self.doorRepository = DoorRepository(session,store)
   
  def addDoor(self,name,room,width,orientation):
    door = Door(0,name,room,float(width.replace(",",".")),orientation,0,0,0,0)
    id = self.doorRepository.addDoor(door)
    door.id = id
    room.doors.append(door)
    self.window.displayDrawer("controller")
  
  def deleteDoor(self,id,room):
    self.doorRepository.deleteDoor(id)
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    doors = [x for x in rooms[0].doors if x.id == id]
    rooms[0].doors.remove(doors[0])
    self.window.displayDrawer("controller")

  def getDoors(self,room):
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    return rooms[0].doors

  def updatePositionDoor(self,id,shiftX,shiftY,room):
    doors =  [x for x in room.doors if x.id ==id]
    door = doors[0]
    door.x = door.x + shiftX
    door.y = door.y + shiftY
    door.reelX = door.x/self.store.getMultiplier()
    door.reelY = door.y /self.store.getMultiplier()
    self.doorRepository.updateDoor(door)
