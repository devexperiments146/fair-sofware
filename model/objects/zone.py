class Zone:
  def __init__(self, id,name,room, width,length,x,y,reelX,reelY):
    self.id = id
    self.name = name
    self.room = room
    self.width = int(width)
    self.length = int(length)
    self.x = x
    self.y = y
    self.reelX = reelX
    self.reelY = reelY

  def getName(self):
    return self.name
