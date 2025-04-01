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

class TableLineRepository:
  def __init__(self,session):
    self.session = session

  def addTableLine(self,project,tableLine):
    maxValue = self.session.query(func.max(TableLineEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    tableLineEntity = TableLineEntity(project.id,newId,tableLine.name,tableLine.x,tableLine.y,tableLine.width,tableLine.reelX,tableLine.reelY,tableLine.orientation,tableLine.room.id,tableLine.tableSide)
    roomEntity = self.session.query(RoomEntity).filter_by(id=tableLine.room.id).one()
    tableLineEntity.room = roomEntity
    self.session.add(tableLineEntity)
    self.session.commit()
    return newId

  def updateTableLine(self,tableLine):
    self.session.query(TableLineEntity).filter_by(id=tableLine.id).update({"width":tableLine.width,"x":tableLine.x,"y":tableLine.y,"reelX":tableLine.reelX,"reelY":tableLine.reelY})
    self.session.commit()

  
  def deleteTableLine(self,id):
    tableLineEntities = self.session.query(TableLineEntity).filter_by(id=id).all()
    self.session.delete(tableLineEntities[0])
    self.session.commit()
