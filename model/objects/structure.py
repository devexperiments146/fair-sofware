class Structure:
  def __init__(self, id, name, room,x,y,reelX,reelY,orientation,width,length,structureType):
    self.id = id
    self.name = name
    self.room = room
    self.x = x
    self.y = y
    self.reelX = reelX
    self.reelY = reelY
    self.orientation = orientation
    self.width = width
    self.length = length
    self.structureType = structureType

  def getName(self):
    return self.name