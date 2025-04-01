
from model.objects.room import Room
from model.objects.door import Door
from model.objects.exponent import Exponent
from model.objects.project import Project
from model.objects.tableGroup import TableGroup
from model.objects.table import Table
from model.objects.tableLine import TableLine

from model.usecases.printPdf import PrintPdf


from PyQt6.QtPrintSupport  import QPrinter
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from model.usecases.returnNextWallTableLineUsecase import ReturnNextWallTableLineUsecase
from model.usecases.returnEndTableExponentGroupUsecase import ReturnEndTableExponentGroupUsecase
from model.usecases.returnNextWallExponentGroupUsecase import ReturnNextWallExponentGroupUsecase
from model.usecases.returnTableLineExponentGroupUsecase import ReturnTableLineExponentGroupUsecase

from model.usecases.shareExponentsUsecase import ShareExponentsUsecase
from model.usecases.regroupExponentsUsecase import RegroupExponentsUsecase

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

class TableController:
  def __init__(self,window,store,session):
    self.window = window
    self.store = store
    self.tableRepository = TableRepository(session)

  def addTable(self,name,room,tableGroup,orientation,exponent = None):
    table = Table(0,name,room,tableGroup,0,0,0,0,orientation)
    table.exponent = exponent
    id = self.tableRepository.addTable(self.store.getSelectedProject(),table)
    table.id = id
    self.getTables(room).append(table)       
    self.window.displayDrawer("controller")
    
  def updatePositionTable(self,index,shiftX,shiftY,room):
    table = room.tables[index]
    table.x = table.x + shiftX
    table.y = table.y + shiftY
    table.reelX = table.x/self.store.getMultiplier()
    table.reelY = table.y /self.store.getMultiplier()
    self.tableRepository.updateTable(table)

  def getTables(self,room):
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    return rooms[0].tables
  

  def fillTableLinesWithoutExponents(self,room):
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    multiplier = self.store.getMultiplier()
    tableLines = rooms[0].tableLines
    tableGroup =  self.store.getSelectedProject().tableGroups[2]
    for tableLine in tableLines:
        while tableLine.canAddNewTableWithoutExponent(tableGroup,multiplier): 
            newX = tableLine.x
            newY = tableLine.y
            if len(tableLine.tables) > 0:
              maxTable = tableLine.tables[len(tableLine.tables)-1]
              if tableLine.orientation  == "Vertical":
                newX = tableLine.x
                newY = maxTable.y+maxTable.tableGroup.length*multiplier
              else:
                newY = tableLine.y
                newX = maxTable.x+maxTable.tableGroup.length*multiplier
            else:
              newX = tableLine.x
              newY = tableLine.y
            table = Table(0,"",room,tableGroup,newX,newY,newX/multiplier,newY/multiplier,tableLine.orientation)
            tableLine.tables.append(table)
    tables = []
    for tableLine in tableLines:
      tables = tables + tableLine.tables
    rooms[0].tables = tables
    self.window.displayDrawer("controller")

  
  def fillTableLines(self,room):
    sortedTableLines = sorted(room.tableLines, key=lambda x: x.reelY)

    regroupExponentsUsecase = RegroupExponentsUsecase(self.store,room)
    exponentGroups =  regroupExponentsUsecase.execute()
    
    returnNextWallTableLineUsecase = ReturnNextWallTableLineUsecase(room,sortedTableLines)
    nextWallTableLines = returnNextWallTableLineUsecase.execute()

    returnEndTableExponentGroupUsecase = ReturnEndTableExponentGroupUsecase(exponentGroups)
    endTableExponentGroup = returnEndTableExponentGroupUsecase.execute()

    returnNextWallExponentGroupUsecase = ReturnNextWallExponentGroupUsecase(exponentGroups)
    nextWallExponentGroup = returnNextWallExponentGroupUsecase.execute()
   
    returnTableLineExponentGroupUsecase = ReturnTableLineExponentGroupUsecase(exponentGroups)
    tableLineExponentGroup = returnTableLineExponentGroupUsecase.execute() 

    shareExponentsUsecase = ShareExponentsUsecase(self.store,room,exponentGroups,sortedTableLines,nextWallTableLines,endTableExponentGroup,nextWallExponentGroup,tableLineExponentGroup)
    tableLines = shareExponentsUsecase.execute()

    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    rooms[0].tableLines = tableLines
    tables = []
    for tableLine in tableLines:
      for table in tableLine.tables:
        self.tableRepository.addTable(self.store.getSelectedProject(),table)
      tables = tables + tableLine.tables
    rooms[0].tables = tables
    self.window.displayDrawer("controller")

  def updateTable(self,table,reelX,reelY,name = None,side = None):
    table.reelX = float(reelX.replace(",","."))
    table.reelY = float(reelY.replace(",","."))
    table.x = table.reelX*self.store.getMultiplier()  
    table.y = table.reelY *self.store.getMultiplier()  
    if(side != None):
      table.side = side
    if(name != None):
      table.name = name
    self.tableRepository.updateTable(table)  
    self.window.displayDrawer("controller")

  def deleteAllTables(self):
    self.tableRepository.deleteAllTables()
    for room in self.store.getSelectedProject().rooms:
      for tableLine in room.tableLines:
          tableLine.tables = []
      room.tables = []
    self.window.displayDrawer("controller")

  def deleteTable(self,id,room):
    self.tableRepository.deleteTable(id)
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    table = [x for x in rooms[0].tables if x.id ==id]
    rooms[0].tables.remove(table[0])
    for tableLine in rooms[0].tableLines:
      for table in tableLine.tables:
        if table.id == id:
          tableLine.remove(table)
    self.window.displayDrawer("controller")
    
  def displayUpdateTable(self,table):
    self.window.displayUpdateTableView(table)

  def exportTables(self,store):
      qfd = QFileDialog()
      path = "C:\\"
      filter = "*.csv"
      filename, _  = QFileDialog.getSaveFileName(qfd, "Exporter tables", path, filter)
      with open(filename, 'w') as f:
        tables  = []
        for room in store.getSelectedProject().rooms:
          tables += room.tables
        for table in tables:
          if table.exponent:
            f.write(table.name+";"+table.exponent.firstname+";"+table.exponent.lastname+"\n")
      self.window.displayDrawer("controller")
