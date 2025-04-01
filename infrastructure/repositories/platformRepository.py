from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import func

from infrastructure.entities.roomEntity import RoomEntity
from infrastructure.entities.platformEntity import PlatformEntity

from infrastructure.entities.base import Base

class PlatformRepository:
  def __init__(self,session):
    self.session = session

  def addPlatform(self,project,platform):
    maxValue = self.session.query(func.max(PlatformEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    platformEntity = PlatformEntity(project.id,newId,platform.name,platform.x,platform.y,platform.width,platform.length,platform.reelX,platform.reelY,platform.orientation,platform.room.id)
    roomEntity = self.session.query(RoomEntity).filter_by(id=platform.room.id).one()
    platformEntity.room = roomEntity
    self.session.add(platformEntity)
    self.session.commit()
    return newId

  def updatePlatform(self,platform):
    self.session.query(PlatformEntity).filter_by(id=platform.id).update({"x":platform.x,"y":platform.y,"reelX":platform.reelX,"reelY":platform.reelY})
    self.session.commit()
  
  def deletePlatform(self,id):
    platformEntities = self.session.query(PlatformEntity).filter_by(id=id).all()
    self.session.delete(platformEntities[0])
    self.session.commit()
