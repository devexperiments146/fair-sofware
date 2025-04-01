class ExponentGroup:
  def __init__(self):
    self.exponents = []
    self.width = 0
    self.nextWall = None
    self.tableLineChoiceId = None
    self.tableLinePosition = None
    self.endOfTable = None

  def addExponent(self,exponent,tableGroup):
    self.exponents.append(exponent)
    self.width+=tableGroup.length
    self.updateExponentGroup(exponent)

  def merge(self,exponentGroup):
    for exponent in exponentGroup.exponents : 
      self.exponents.append(exponent)
      self.updateExponentGroup(exponent)
    self.width+=exponentGroup.width

  def updateExponentGroup(self,exponent):
    if exponent.nextWall != None:
      self.nextWall = exponent.nextWall
    if exponent.tableLineChoiceId != None:
      self.tableLineChoiceId = exponent.tableLineChoiceId
    if exponent.tableLinePosition != None:
      self.tableLinePosition = exponent.tableLinePosition
    if exponent.endOfTable != None:
      self.endOfTable = exponent.endOfTable
