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

  def canAddNewTable(self, exponentGroup,multiplier):
    #Initialization
    totalWidth = 0
    sortedTables = []
    maxWidth = 0
    maxStart = 0
    #if(exponentGroup.exponents[0].lastname.strip() == "Tifenn" or exponentGroup.exponents[0].lastname.strip() == "Tifenn" or exponentGroup.exponents[0].lastname.strip() == "Simon" or exponentGroup.exponents[0].lastname.strip() == "Simon"):
    #  print("HEllo")
    if len(self.tables) >0 :
      #Initialization
      if self.orientation  == "Vertical":
        sortedTables = sorted(self.tables, key=lambda x: x.reelY,  reverse = True)
        maxWidth = self.y+self.width*multiplier
        maxStart = self.y
      else :
        sortedTables = sorted(self.tables, key=lambda x: x.reelX,  reverse = True)
        maxWidth = self.x+self.width*multiplier
        maxStart = self.x
      for table in sortedTables:  
        if self.orientation  == "Vertical":
            if(maxWidth == table.y+table.tableGroup.length*multiplier):
              maxWidth = maxWidth - table.tableGroup.length*multiplier
            else:
              newMaxStart = table.y+table.tableGroup.length*multiplier
              if(newMaxStart>maxStart):
                maxStart = newMaxStart
        else:
            if(maxWidth == table.x+table.tableGroup.length*multiplier):
              maxWidth = maxWidth - table.tableGroup.length*multiplier
            else:
              newMaxStart = table.x+table.tableGroup.length*multiplier
              if(newMaxStart>maxStart):
                maxStart = newMaxStart
      totalWidth = maxWidth-maxStart
    else:
      totalWidth = self.width*multiplier
    newTableLineWidth = totalWidth-(exponentGroup.width*multiplier+0.5*multiplier)
    if newTableLineWidth >= 0:
      return True
    return False
  
  def getStartOfExponentGroup(self,exponentGroup,multiplier,gap):
    if(exponentGroup.tableLinePosition == 100):
      if self.orientation  == "Vertical":
        start = self.y+self.width*multiplier-exponentGroup.width*multiplier
      else:
        start = self.x+self.width*multiplier-exponentGroup.width*multiplier
    else:
      if(len(self.tables)>0):
        maxStart = self.getMaxStart(multiplier)
        start = maxStart+gap*multiplier 
      else:
        if self.orientation  == "Vertical":
            start = self.y
        else:
            start = self.x
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