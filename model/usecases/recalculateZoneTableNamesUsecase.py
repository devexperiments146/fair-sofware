
class RecalculateZoneTableNamesUsecase:
  def __init__(self, store,room):
    self.store = store
    self.room = room
    self.zoneCounters = {}
    self.multiplier = self.store.getMultiplier()


  def execute(self):
    for table in self.room.tables:
        if(len(self.room.zones)>0):
            for zone in self.room.zones :
                if table.x >= zone.x and table.x<= zone.x+zone.width*self.multiplier and table.y >= zone.y and table.y <= zone.y+zone.length*self.multiplier:
                    counter = self.zoneCounters.get(zone.id)
                    if counter is None:
                        counter = 0
                    counter+=1
                    name = zone.name+str(counter)  
                    self.zoneCounters[zone.id] = counter  
                    table.name = name  