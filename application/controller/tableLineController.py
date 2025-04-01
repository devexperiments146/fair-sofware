
from model.objects.room import Room
from model.objects.door import Door
from model.objects.exponent import Exponent
from model.objects.project import Project
from model.objects.tableGroup import TableGroup
from model.objects.table import Table
from model.objects.tableLine import TableLine


from model.usecases.printPdf import PrintPdf

from infrastructure.repositories.tableLineRepository import TableLineRepository
from application.mapper.projectMapper import ProjectMapper

import csv
import json 

class TableLineController:
  def __init__(self,window,store,session):
    self.window = window
    self.store = store
    self.tableLineRepository = TableLineRepository(session)

  def addTableLine(self,room,name,width,orientation):
    tableLine = TableLine(0,name,room,self.store.getMultiplier(),self.store.getMultiplier(),1,1,orientation,float(width.replace(",",".")),"Right")
    id = self.tableLineRepository.addTableLine(self.store.getSelectedProject(),tableLine)
    tableLine.id = id
    tableLines = self.getTableLines(room)
    tableLines.append(tableLine)  
    self.window.displayDrawer("controller")
    
  def getTableLines(self,room):
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    return rooms[0].tableLines
  
  def updatePositionTableLine(self,id,shiftX,shiftY,room):
    tableLines =  [x for x in room.tableLines if x.id ==id]
    tableLine = tableLines[0]
    tableLine.x = tableLine.x + shiftX
    tableLine.y = tableLine.y + shiftY
    tableLine.reelX = tableLine.x/self.store.getMultiplier()
    tableLine.reelY = tableLine.y /self.store.getMultiplier()
    self.tableLineRepository.updateTableLine(tableLine)



  def deleteTableLine(self,id,room):
    self.tableLineRepository.deleteTableLine(id)
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    tableLines = [x for x in rooms[0].tableLines if x.id == id]
    rooms[0].tableLines.remove(tableLines[0])
    self.window.displayDrawer("controller")


  def updateTableLine(self,tableLine,width,reelX,reelY):
    tableLine.width = float(width.replace(",","."))
    tableLine.reelX = float(reelX.replace(",","."))
    tableLine.reelY = float(reelY.replace(",","."))
    tableLine.x = tableLine.reelX*self.store.getMultiplier()  
    tableLine.y = tableLine.reelY *self.store.getMultiplier()  
    self.tableLineRepository.updateTableLine(tableLine)  
    self.window.displayDrawer("controller")
    
  def displayUpdateTableLine(self,tableLine):
    self.window.displayUpdateTableLine(tableLine)

