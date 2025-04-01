class UnusableSpace:
  def __init__(self, id, name, room,x,y,reelX,reelY,orientation,width,length):
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

  def getName(self):
    return self.name