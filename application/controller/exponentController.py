
from model.objects.room import Room
from model.objects.door import Door
from model.objects.exponent import Exponent
from model.objects.project import Project
from model.objects.tableGroup import TableGroup
from model.objects.table import Table
from model.objects.tableLine import TableLine

from PyQt6.QtPrintSupport  import QPrinter
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from model.usecases.printPdf import PrintPdf

from infrastructure.repositories.doorRepository import DoorRepository
from infrastructure.repositories.exponentRepository import ExponentRepository
from infrastructure.repositories.projectRepository import ProjectRepository
from infrastructure.repositories.roomRepository import RoomRepository
from infrastructure.repositories.tableGroupRepository import TableGroupRepository
from infrastructure.repositories.tableLineRepository import TableLineRepository
from infrastructure.repositories.tableRepository import TableRepository

from application.mapper.projectMapper import ProjectMapper


from view.drawer.drawerView import DrawerView

from datetime import datetime

import csv
import json 

class ExponentController:
  def __init__(self,window,store,session):
    self.window = window
    self.store = store
    self.exponentRepository = ExponentRepository(session,store)

  def addExponent(self,firstName,lastName,tableType):
    exponent = Exponent(0,firstName,lastName)
    exponent.tableType = tableType
    exponent.date = datetime.today().strftime('%d/%m/%Y %H:%M')
    id = self.exponentRepository.addExponent(exponent)  
    exponent.id = id
    self.store.getSelectedProject().exponents.append(exponent)  
    self.window.displayDrawer("controller")

  def deleteAllExponents(self):
    self.exponentRepository.deleteAllExponents()  
    self.store.getSelectedProject().exponents = []
    self.window.displayDrawer("controller")
                


  def importExponents(self,filename):
    importedExponents = []
    
    with open(filename,'r',encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[2]== "Validé":
                  importedExponents.append(Exponent(len(importedExponents)+1,row[3],row[4],row[1],row[12],row[21]))
                  line_count += 1
    csv_file.close()
    for exponent in importedExponents:
      self.exponentRepository.addExponent(exponent)  
      self.store.getSelectedProject().exponents.append(exponent)
    self.window.displayDrawer("controller")

  def updateExponent(self,exponent,firstname,lastname,tableType,roomChoice = None, nextExponent = None,nextDoor= None, nextWall = None, tableLineChoice = None, tableLinePosition = None,endOfTable = None):
    if roomChoice:
      exponent.roomChoiceId = roomChoice.id
    if nextExponent:
      exponent.nextExponentId = nextExponent.id
    if nextDoor:
      exponent.nextDoorId = nextDoor.id
    if tableLineChoice and tableLinePosition != None:
      exponent.tableLineChoiceId = tableLineChoice.id
      exponent.tableLinePosition = int(tableLinePosition)
    exponent.nextWall = nextWall
    exponent.endOfTable = endOfTable
    exponent.firstname = firstname
    exponent.lastname = lastname
    exponent.tableType = tableType
    self.exponentRepository.updateExponent(exponent)  
    self.window.displayDrawer("controller")
    
  def displayUpdateExponent(self,exponent):
    self.window.displayUpdateExponent(exponent)



  def printExponent(self,exponent):
    self.window.displayExponentPDF(exponent)
