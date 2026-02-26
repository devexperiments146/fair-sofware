class TableLine:
  def __init__(self, id, name, room,x,y,reelX,reelY,orientation,width,tableSide,tables = []):
    self.id = id
    self.name = name
    self.room = room
    self.x = x
    self.y = y
    self.reelX = reelX
    self.reelY = reelY
    self.orientation = orientation
    self.width = width
    self.tableSide = tableSide
    self.tables = tables
    self.maxStart = 0
    self.totalUsedWidth = 0
    if self.orientation  == "Vertical":
      self.maxStart =  self.y
    else :
      self.maxStart = self.x

  def addTable(self,table,multiplier):    
    self.tables.append(table)
    self.totalUsedWidth = self.totalUsedWidth +table.tableGroup.length*multiplier

  def addGap(self,gap,multiplier):    
    self.totalUsedWidth = self.totalUsedWidth + gap*multiplier

  def canAddNewTableWithoutExponent(self,tableGroup,multiplier):    
    totalWidth = 0
    if len(self.tables) >0 :
      if self.orientation  == "Vertical":
        maxWidth = self.y+self.width*multiplier
        maxStart = self.y
      else :
        maxWidth = self.x+self.width*multiplier
        maxStart = self.x
      for table in self.tables:  
        if self.orientation  == "Vertical":
          newMaxStart = table.y+table.tableGroup.length*multiplier
          if(newMaxStart>maxStart):
            maxStart = newMaxStart
        else:
          newMaxStart = table.x+table.tableGroup.length*multiplier
          if(newMaxStart>maxStart):
            maxStart = newMaxStart
      totalWidth = maxWidth - maxStart
    else:
      totalWidth = self.width*multiplier
    newTableLineWidth = totalWidth-(tableGroup.length*multiplier)
    if newTableLineWidth >= 0:
      return True
    return False

  def canAddNewTable(self, exponentGroup, multiplier):
    totalAvailableWidth = self.width * multiplier - self.totalUsedWidth
    requiredWidth = exponentGroup.width * multiplier + 0.5 * multiplier
    return totalAvailableWidth >= requiredWidth
  
  def getStartOfExponentGroup(self,exponentGroup,multiplier,gap):
    if(exponentGroup.tableLinePosition == 100):
      if self.orientation  == "Vertical":
        start = self.y+self.width*multiplier-exponentGroup.width*multiplier
      else:
        start = self.x+self.width*multiplier-exponentGroup.width*multiplier
    else:
      if(len(self.tables)>0):
        start = self.maxStart+gap*multiplier
        if self.orientation  == "Vertical" :
          if self.maxStart ==  self.y :
            start = self.maxStart
        else :
          if self.maxStart ==  self.x :
            start = self.maxStart
      else:
        start = self.maxStart
      self.maxStart = start+exponentGroup.width*multiplier
    return start
 
  def getMaxStart(self,multiplier):
    sortedTableLines = []
    maxWidth = 0
    maxStart = 0

    #Initialization
    if self.orientation  == "Vertical":
      sortedTableLines = sorted(self.tables, key=lambda x: x.reelY,  reverse = True)
      maxWidth = self.y+self.width*multiplier
      maxStart = self.y
    else :
      sortedTableLines = sorted(self.tables, key=lambda x: x.reelX,  reverse = True)
      maxWidth = self.x+self.width*multiplier
      maxStart = self.x
    #Parcours des tables
    for table in sortedTableLines:  
      #Vertical
      if self.orientation  == "Vertical":
          #Calcul de la largeur maximum en partant des table qui on le y le plus long
          #On met a jour le maxWWidth 
          if(maxWidth == table.y+table.tableGroup.length*multiplier):
            maxWidth = maxWidth - table.tableGroup.length*multiplier
          else:
            #Calcul de la largeur maximum en partant des table qui on le y le plus long
            newMaxStart = table.y+table.tableGroup.length*multiplier
            if(newMaxStart>maxStart):
              maxStart = newMaxStart
      #Horizontal
      else:
          #Calcul de la largeur maximum en partant des table qui on le y le plus long
          #On met a jour le maxWWidth 
          if(maxWidth == table.x+table.tableGroup.length*multiplier):
            maxWidth = maxWidth - table.tableGroup.length*multiplier
          else:
            #Calcul de la largeur maximum en partant des table qui on le x le plus long
            newMaxStart = table.x+table.tableGroup.length*multiplier
            if(newMaxStart>maxStart):
              maxStart = newMaxStart
    return maxStart


  def getName(self):
    return " [" + str(self.x) + "," + str(self.y) + "]" + self.name