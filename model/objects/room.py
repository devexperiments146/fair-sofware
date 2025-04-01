class Room:
  def __init__(self, id,name, width,length,x,y,tables = [],doors = [],tableLines = [],zones = [],unusableSpaces = [],platforms = []):
    self.id = id
    self.name = name
    self.width = int(width)
    self.length = int(length)
    self.x = x
    self.y = y
    self.tables = tables
    self.doors = doors 
    self.tableLines = tableLines
    self.zones = zones
    self.unusableSpaces = unusableSpaces
    self.platforms = platforms

  def getName(self):
    return self.name
