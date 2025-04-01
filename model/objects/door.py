class Door:
  def __init__(self, id,name,room, width,orientation,x,y,reelX,reelY):
    self.id = id
    self.name = name
    self.room = room
    self.width = float(width)
    self.orientation = orientation
    self.x = x
    self.y = y
    self.reelX = reelX
    self.reelY = reelY

  def getName(self):
    return self.name + " [" + self.room.name + "]"
