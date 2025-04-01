from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import func


from infrastructure.entities.tableEntity import TableEntity
from infrastructure.entities.tableGroupEntity import TableGroupEntity
from infrastructure.entities.roomEntity import RoomEntity
from infrastructure.entities.exponentEntity import ExponentEntity
from infrastructure.entities.projectEntity import ProjectEntity
from infrastructure.entities.doorEntity import DoorEntity 
from infrastructure.entities.tableLineEntity import TableLineEntity
from infrastructure.entities.zoneEntity import ZoneEntity

from model.objects.table import Table
from model.objects.tableGroup import TableGroup
from model.objects.room import Room
from model.objects.exponent import Exponent
from model.objects.project import Project
from model.objects.door import Door
from model.objects.tableLine import TableLine

from infrastructure.entities.base import Base

class ZoneRepository:
  def __init__(self,session):
    self.session = session

  def addZone(self,project,zone):
    maxValue = self.session.query(func.max(ZoneEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    zoneEntity = ZoneEntity(project.id,newId,zone.name,zone.room.id,zone.x,zone.y,zone.reelX,zone.reelY,zone.width,zone.length)
    self.session.add(zoneEntity)
    self.session.commit()
    return newId
  
  def deleteZone(self,id):
    zoneEntities = self.session.query(ZoneEntity).filter_by(id=id).all()
    self.session.delete(zoneEntities[0])
    self.session.commit()


  def updateZone(self,zone):
    self.session.query(ZoneEntity).filter_by(id=zone.id).update({"name":zone.name,"length":zone.length,"width":zone.width,"x":zone.x,"y":zone.y,"reelX":zone.reelX,"reelY":zone.reelY})
    self.session.commit()