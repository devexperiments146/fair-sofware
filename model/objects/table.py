class Table:
  def __init__(self, id,name, room,tableGroup,x,y,reelX,reelY,orientation,exponent = None,side = None):
    self.id = id
    self.name = name
    self.room = room
    self.tableGroup = tableGroup
    self.x = x
    self.y = y
    self.reelX = reelX
    self.reelY = reelY
    self.orientation = orientation
    self.exponent = exponent
    self.side = side

  def getName(self):
    return self.name + " [" + self.tableGroup.getName() + "]"