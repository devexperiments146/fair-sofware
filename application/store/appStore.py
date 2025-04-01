class AppStore:
  def __init__(self):
    self.projects = []
    self.parameters = []
    self.orientations = ['Vertical','Horizontal']
    self.tableTypes = ['Petite table','Grande table']
    self.colors = ['green','purple','orange','black','yellow','black','red']
    self.sides = ['right','left']
    self.selectedProject = None
    self.multiplier = 40
    self.displayTableLines = True
    self.displayDoors = True
    self.displayTables = True
    self.displayZones = False
    self.displayUnusableSpaces = True
    self.displayMeasurements = False
    self.displayExponent = None
    self.displayPlatforms = True
    self.rooms = []

  def setProjects(self,projects):
    self.projects = projects
    
  def getProjects(self):
    return self.projects
  
  def setSelectedProject(self,selectedProject):
    self.selectedProject = selectedProject
    
  def getSelectedProject(self):
    return self.selectedProject
    
  def getColors(self):
    return self.colors
      
  def getMultiplier(self):
    return self.multiplier
  
  def getOrientations(self):
    return self.orientations
  
  def getTableTypes(self):
    return self.tableTypes
  
  def setParameters(self,parameters):
    self.parameters = parameters
  
  def getParameters(self):
    return self.parameters
  
  def getParameter(self,name):
    parameters = [x for x in self.parameters if x.name == name]
    if len(parameters) > 0 and parameters[0]:
      return parameters[0]
    return None
  
  def setDisplayDoors(self,displayDoors):
    self.displayDoors = displayDoors
    
  def getDisplayDoors(self):
    return self.displayDoors
  
  def setDisplayTableLines(self,displayTableLines):
    self.displayTableLines = displayTableLines
    
  def getDisplayTableLines(self):
    return self.displayTableLines
  
  def setDisplayTables(self,displayTables):
    self.displayTables = displayTables
    
  def getDisplayTables(self):
    return self.displayTables
  
  def getDisplayUnusableSpaces(self):
    return self.displayUnusableSpaces
  
  def setDisplayUnusableSpaces(self,displayUnusableSpaces):
    self.displayUnusableSpaces = displayUnusableSpaces
  
  def setDisplayZones(self,displayZones):
    self.displayZones = displayZones
    
  def getDisplayZones(self):
    return self.displayZones
  
  def setDisplayMeasurements(self,displayMeasurements):
    self.displayMeasurements = displayMeasurements
    
  def getDisplayMeasurements(self):
    return self.displayMeasurements
  
  def setDisplayExponent(self,displayExponent):
    self.displayExponent = displayExponent
    
  def getDisplayExponent(self):
    return self.displayExponent
  
  def getColors(self):
    return self.colors
    
  def getSides(self):
    return self.sides
  
  def getDisplayPlatforms(self):
    return self.displayPlatforms
  
  def setDisplayPlatforms(self,displayPlatforms):
    self.displayPlatforms = displayPlatforms

  def setRooms(self,rooms):
    self.rooms = rooms
    
  def getRooms(self):
    return self.rooms
  