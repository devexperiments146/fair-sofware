
from model.objects.table import Table
from model.objects.exponentGroup import ExponentGroup

class ShareExponentsUsecase:
  def __init__(self, store,room,exponentGroups,sortedTableLines,nextWallTableLines,endTableExponentGroup,nextWallExponentGroup,tableLineExponentGroup):
    self.store = store
    self.room = room
    self.tableGroups = store.getSelectedProject().tableGroups
    self.exponentGroups = exponentGroups
    self.sortedTableLines = sortedTableLines
    self.nextWallTableLines = nextWallTableLines

    self.endTableExponentGroup = endTableExponentGroup
    self.nextWallExponentGroup = nextWallExponentGroup
    self.tableLineExponentGroup = tableLineExponentGroup

    self.tableGroupCounters = {}
    self.zoneCounters = {}

  def execute(self):

    self.initializeCounters()
    addedExponentGroups = []
  
    for tableLine in self.sortedTableLines:
      tableLineExponentGroup = self.tableLineExponentGroup.get(tableLine.id)

      if tableLineExponentGroup:
        endOfTableOfThisTableLine = [element for element in tableLineExponentGroup.exponentGroupNames if element in self.endTableExponentGroup]
        if(len(endOfTableOfThisTableLine)>0):
          #Debut de table et présent dans la ligne
          exponentName = endOfTableOfThisTableLine[0]
          if exponentName not in addedExponentGroups:
            exponentGroup = self.exponentGroups.get(exponentName)
            if tableLine.canAddNewTable(exponentGroup,self.store.getMultiplier()):
              gap = 0.5
              for exponent in exponentGroup.exponents :
                tableGroup = self.getTableGroup(exponent)
                table = self.getTable(tableLine,tableGroup,exponent,self.store.getMultiplier(),gap,self.room.zones)
                tableLine.tables.append(table)
                gap = 0
              addedExponentGroups.append(exponentName)
        else:
          #Debut de table
          endOfTableAdded = False
          if tableLine.orientation == "Horizontal":
            for exponentName in self.endTableExponentGroup:
              if exponentName not in addedExponentGroups and not endOfTableAdded:
                exponentGroup = self.exponentGroups.get(exponentName)
                if tableLine.canAddNewTable(exponentGroup,self.store.getMultiplier()) and exponentGroup.tableLineChoiceId == None:
                  gap = 0.5
                  for exponent in exponentGroup.exponents :
                    tableGroup = self.getTableGroup(exponent)
                    table = self.getTable(tableLine,tableGroup,exponent,self.store.getMultiplier(),gap,self.room.zones)
                    tableLine.tables.append(table)
                    gap = 0
                  addedExponentGroups.append(exponentName)
                  endOfTableAdded = True
       #Présent dans la ligne
        for exponentName in tableLineExponentGroup.exponentGroupNames:
          if exponentName not in addedExponentGroups:
            exponentGroup = self.exponentGroups.get(exponentName)
            if tableLine.canAddNewTable(exponentGroup,self.store.getMultiplier()):
              gap = 0.5
              startTable =  tableLine.getStartOfExponentGroup(exponentGroup,self.store.getMultiplier(),gap)
              for exponent in exponentGroup.exponents :
                tableGroup = self.getTableGroup(exponent)
                table = self.getTable(tableLine,tableGroup,exponent,self.store.getMultiplier(),gap,self.room.zones,startTable)
                startTable = startTable + table.tableGroup.length*self.store.getMultiplier()
                tableLine.tables.append(table)
                gap = 0
              addedExponentGroups.append(exponentName)
      else:
        #Debut de table 
        endOfTableAdded = False
        for exponentName in self.endTableExponentGroup:
          if exponentName not in addedExponentGroups and not endOfTableAdded:
            exponentGroup = self.exponentGroups.get(exponentName)
            if tableLine.canAddNewTable(exponentGroup,self.store.getMultiplier()) and exponentGroup.tableLineChoiceId == None:
              gap = 0.5
              for exponent in exponentGroup.exponents :
                tableGroup = self.getTableGroup(exponent)
                table = self.getTable(tableLine,tableGroup,exponent,self.store.getMultiplier(),gap,self.room.zones)
                tableLine.tables.append(table)
                gap = 0
              addedExponentGroups.append(exponentName)
              endOfTableAdded = True

      selectedNextWallTableLine  = [x for x in self.nextWallTableLines if x.id == tableLine.id]
      if len(selectedNextWallTableLine)>0:
         for exponentName in self.nextWallExponentGroup:
            if exponentName not in addedExponentGroups and exponentName not in self.endTableExponentGroup:
              exponentGroup = self.exponentGroups.get(exponentName)
              if exponentGroup.tableLineChoiceId == None:
                if tableLine.canAddNewTable(exponentGroup,self.store.getMultiplier()):
                  gap = 0.5
                  for exponent in exponentGroup.exponents :
                    tableGroup = self.getTableGroup(exponent)
                    table = self.getTable(tableLine,tableGroup,exponent,self.store.getMultiplier(),gap,self.room.zones)
                    tableLine.tables.append(table)
                    gap = 0
                  addedExponentGroups.append(exponentName)  
      for exponentName in self.exponentGroups:
        if exponentName not in addedExponentGroups and exponentName not in self.endTableExponentGroup:
          exponentGroup = self.exponentGroups.get(exponentName)
          if exponentGroup.tableLineChoiceId == None:      
            if tableLine.canAddNewTable(exponentGroup,self.store.getMultiplier()):
              gap = 0.5
              for exponent in exponentGroup.exponents :
                tableGroup = self.getTableGroup(exponent)
                table = self.getTable(tableLine,tableGroup,exponent,self.store.getMultiplier(),gap,self.room.zones)
                tableLine.tables.append(table)
                gap = 0
              addedExponentGroups.append(exponentName) 
    return self.room.tableLines
  
  def getTable(self, tableLine,tableGroup,exponent,multiplier,gap,zones,startTable=None):
    newY = 0
    if startTable:
      if tableLine.orientation  == "Vertical":
          newX = tableLine.x
          newY = startTable
      else:
          newY = tableLine.y
          newX = startTable
    else:
      if len(tableLine.tables) > 0:
          maxTable = tableLine.tables[len(tableLine.tables)-1]
          if tableLine.orientation  == "Vertical":
              newX = tableLine.x
              newY = tableLine.getMaxStart(multiplier)+gap*multiplier
          else:
              newY = tableLine.y
              newX =  tableLine.getMaxStart(multiplier)+gap*multiplier
      else:
            newX = tableLine.x
            newY = tableLine.y
    name = "" 
    if(len(zones)>0):
      for zone in zones :
        if newX >= zone.x and newX<= zone.x+zone.width*multiplier and newY >= zone.y and newY <= zone.y+zone.length*multiplier:
          counter = self.zoneCounters.get(zone.id)
          counter+=1
          name = zone.name+str(counter)  
          self.zoneCounters[zone.id] = counter    
    return Table(0,name,self.room,tableGroup,newX,newY,newX/multiplier,newY/multiplier,tableLine.orientation,exponent)
         

  def getTableGroup(self, exponent):
    tableGroups = [x for x in self.tableGroups  if x.tableType == exponent.tableType.strip()]
    selectedTableGroup = None
    for tableGroup in tableGroups :
      if not selectedTableGroup:
        counter = self.tableGroupCounters.get(tableGroup.id)
        if (counter+1<=tableGroup.maxQuantity):
          selectedTableGroup = tableGroup
          counter += 1
          self.tableGroupCounters[tableGroup.id] = counter
    return selectedTableGroup
  
  def getTableLine(self, tableLineId):
    tableLines = [x for x in self.room.tableLines  if x.id == tableLineId]
    return tableLines[0]
  

  def initializeCounters(self):
    for tableGroup in self.tableGroups :
      self.tableGroupCounters[tableGroup.id] = 0
    for room in self.store.getSelectedProject().rooms:
      for table in room.tables :
          counter = self.tableGroupCounters.get(table.tableGroup.id)
          counter += 1
          self.tableGroupCounters[table.tableGroup.id] = counter

    for zone in self.room.zones :
      self.zoneCounters[zone.id] = 0


             
           





