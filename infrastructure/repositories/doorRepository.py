
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

from model.objects.table import Table
from model.objects.tableGroup import TableGroup
from model.objects.room import Room
from model.objects.exponent import Exponent
from model.objects.project import Project
from model.objects.door import Door
from model.objects.tableLine import TableLine

from infrastructure.entities.base import Base

class DoorRepository:
  def __init__(self,session,store):
    self.session = session
    self.store = store

  def addDoor(self,door):
    maxValue = self.session.query(func.max(DoorEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    doorEntity = DoorEntity(self.store.getSelectedProject().id,newId,door.name,door.room.id,door.width,door.x,door.y,door.reelX, door.reelY,door.orientation)
    self.session.add(doorEntity)
    self.session.commit()
    return newId
  
  def deleteDoor(self,id):
    doorEntities = self.session.query(DoorEntity).filter_by(id=id).all()
    self.session.delete(doorEntities[0])
    self.session.commit()
  
  def updateDoor(self,door):
    self.session.query(DoorEntity).filter_by(id=door.id).update({"x":door.x,"y":door.y,"reelX":door.reelX,"reelY":door.reelY})
    self.session.commit()

  
