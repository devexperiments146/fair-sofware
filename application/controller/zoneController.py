from model.objects.zone import Zone

from model.usecases.createZonesUsecase import CreateZonesUsecase
from model.usecases.createZonesUsecase import CreateZonesUsecase
from model.usecases.recalculateZoneTableNamesUsecase import RecalculateZoneTableNamesUsecase
from infrastructure.repositories.zoneRepository import ZoneRepository

class ZoneController:
  def __init__(self,window,store,session):
    self.window = window
    self.store = store
    self.zoneRepository = ZoneRepository(session)

  def createZones(self,room,numberOfZones):
    zone = Zone(0,"",room,0,0,0,0,0,0)
    usecase = CreateZonesUsecase( self.store,room,int(numberOfZones))
    zones = usecase.execute()
    currentZones = self.getZones(room)
    for zone in zones:
        id = self.zoneRepository.addZone(self.store.getSelectedProject(),zone)
        zone.id = id
        currentZones.append(zone)  
    self.window.displayDrawer("controller")

  def getZones(self,room):
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    return rooms[0].zones
  
  def recalculateZoneTableNames(self):
    rooms = self.store.getSelectedProject().rooms
    for i in range(0,len(rooms),1):
      room = rooms[i]
      usecase = RecalculateZoneTableNamesUsecase(self.store,room)
      usecase.execute()

  def deleteZone(self,id,room):
    self.zoneRepository.deleteZone(id)
    rooms = [x for x in self.store.getSelectedProject().rooms if x.id ==room.id]
    zones = [x for x in rooms[0].zones if x.id == id]
    rooms[0].zones.remove(zones[0])
    self.window.displayDrawer("controller")

  def displayUpdateZone(self,zone):
    self.window.displayUpdateZone(zone)

  def updateZone(self,zone,name,length,width,reelX,reelY):
    zone.name = name
    zone.length = float(length.replace(",","."))
    zone.width = float(width.replace(",","."))
    zone.reelX = float(reelX.replace(",","."))
    zone.reelY = float(reelY.replace(",","."))
    zone.x = zone.reelX*self.store.getMultiplier()  
    zone.y = zone.reelY *self.store.getMultiplier()  
    self.zoneRepository.updateZone(zone)  
    self.window.displayDrawer("controller")
