class TableGroup:
  def __init__(self, id,width, length,color,maxQuantity,tableType = None):
    self.id = id
    self.width = float(width)
    self.length = float(length)
    self.color = color
    self.maxQuantity = int(maxQuantity)
    self.tableType = tableType


  def getName(self):
    return str(self.width) + " x " + str(self.length)
