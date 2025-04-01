from model.objects.zone import Zone
from model.objects.exponentGroup import ExponentGroup
import math 

class CreateZonesUsecase:
  def __init__(self, store,room,numberOfZone):
    self.store = store
    self.room = room
    self.name = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    self.numberOfZone = int(numberOfZone)

  def execute(self):
    zones = []
    multiplier = self.store.getMultiplier()
    division = math.floor(self.numberOfZone/2)
    column = 0
    row = 0
    zoneWidth = math.floor(self.room.width/division)
    zoneLength = math.floor(self.room.length/division)
    for i in range(0,self.numberOfZone,1):
        newWidth = zoneWidth
        newLength = zoneLength
        newX = column*zoneWidth*multiplier
        newY = row*zoneLength*multiplier
        if (i+1)%division == 0 or i == self.numberOfZone-1:
            newWidth = self.room.width-column*zoneWidth
            if row ==  division-1:
                newLength = self.room.length-row*zoneLength
            if (i+1)%division == 0:
              column=0   
              row+=1       
        else:
            if row ==  division-1:
                newLength = self.room.length-row*zoneLength
            column+=1 

        zone = Zone(0,self.name[i],self.room,newWidth,newLength,newX,newY,newX/multiplier,newY/multiplier)
        zones.append(zone) 
    return zones
      

      
    
    

