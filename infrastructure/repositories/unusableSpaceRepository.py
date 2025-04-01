from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import func

from infrastructure.entities.roomEntity import RoomEntity
from infrastructure.entities.unusableSpaceEntity import UnusableSpaceEntity

from infrastructure.entities.base import Base

class UnusableSpaceRepository:
  def __init__(self,session):
    self.session = session

  def addUnusableSpace(self,project,unusableSpace):
    maxValue = self.session.query(func.max(UnusableSpaceEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    unusableSpaceEntity = UnusableSpaceEntity(project.id,newId,unusableSpace.name,unusableSpace.x,unusableSpace.y,unusableSpace.width,unusableSpace.length,unusableSpace.reelX,unusableSpace.reelY,unusableSpace.orientation,unusableSpace.room.id)
    roomEntity = self.session.query(RoomEntity).filter_by(id=unusableSpace.room.id).one()
    unusableSpaceEntity.room = roomEntity
    self.session.add(unusableSpaceEntity)
    self.session.commit()
    return newId

  def updateUnusableSpace(self,unusableSpace):
    self.session.query(UnusableSpaceEntity).filter_by(id=unusableSpace.id).update({"x":unusableSpace.x,"y":unusableSpace.y,"reelX":unusableSpace.reelX,"reelY":unusableSpace.reelY})
    self.session.commit()
  
  def deleteUnusableSpace(self,id):
    UnusableSpaceEntities = self.session.query(UnusableSpaceEntity).filter_by(id=id).all()
    self.session.delete(UnusableSpaceEntities[0])
    self.session.commit()
