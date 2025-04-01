class Exponent:
  def __init__(self, id,firstname, lastname,date = None,tableType = None,description = None,roomChoiceId = None,nextDoorId = None,nextExponentId = None,nextWall = None,tableLineChoiceId = None,tableLinePosition = None,endOfTable = None):
    self.id = id
    self.firstname = firstname
    self.lastname = lastname
    self.date = date
    self.tableType = tableType
    self.description = description
    self.roomChoiceId = roomChoiceId
    self.nextDoorId = nextDoorId
    self.nextExponentId = nextExponentId
    self.nextWall = nextWall
    self.tableLineChoiceId = tableLineChoiceId
    self.tableLinePosition = tableLinePosition
    self.endOfTable = endOfTable

  def getName(self):
    return self.firstname + " " + self.lastname
