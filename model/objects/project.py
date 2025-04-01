class Project:
  def __init__(self, id,name,rooms = [],tableGroups = [],exponents = []):
    self.id = id
    self.name = name
    self.rooms = rooms
    self.tableGroups = tableGroups
    self.exponents = exponents
    
  def getName(self):
    return self.name
