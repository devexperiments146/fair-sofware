from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import func

from infrastructure.entities.roomEntity import RoomEntity
from infrastructure.entities.structureEntity import StructureEntity

from infrastructure.entities.base import Base

class StructureRepository:
  def __init__(self,session):
    self.session = session

  def addStructure(self,project,structure):
    maxValue = self.session.query(func.max(StructureEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    structureEntity = StructureEntity(project.id,newId,structure.name,structure.x,structure.y,structure.width,structure.length,structure.reelX,structure.reelY,structure.orientation,structure.room.id,structure.structureType)
    roomEntity = self.session.query(RoomEntity).filter_by(id=structure.room.id).one()
    structureEntity.room = roomEntity
    self.session.add(structureEntity)
    self.session.commit()
    return newId

  def updateStructure(self,structure):
    self.session.query(StructureEntity).filter_by(id=structure.id).update({"x":structure.x,"y":structure.y,"reelX":structure.reelX,"reelY":structure.reelY,"structure_type":structure.structureType})
    self.session.commit()
  
  def deleteStructure(self,id):
    structureEntities = self.session.query(StructureEntity).filter_by(id=id).all()
    self.session.delete(structureEntities[0])
    self.session.commit()

  def deleteAllStructuresOfRoom(self,room_id):
    self.session.query(StructureEntity).filter_by(room_id=room_id).delete()
    self.session.commit()