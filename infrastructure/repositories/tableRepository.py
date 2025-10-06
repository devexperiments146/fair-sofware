
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

class TableRepository:
  def __init__(self,session):
    self.session = session

  def addTable(self,project,table):
    maxValue = self.session.query(func.max(TableEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    tableEntity = TableEntity(project.id,newId,table.name,table.x,table.y,table.reelX,table.reelY,table.orientation,table.room.id)
    tableEntity.side = table.side
    tableGroupEntity = self.session.query(TableGroupEntity).filter_by(id=table.tableGroup.id).one()
    tableEntity.tableGroup = tableGroupEntity
    roomEntity = self.session.query(RoomEntity).filter_by(id=table.room.id).one()
    tableEntity.room = roomEntity
    if(table.exponent):
      exponentEntity = self.session.query(ExponentEntity).filter_by(id=table.exponent.id).one()
      tableEntity.exponent = exponentEntity
    self.session.add(tableEntity)
    self.session.commit()
    return newId

  def updateTable(self,table):
    self.session.query(TableEntity).filter_by(id=table.id).update({"x":table.x,"y":table.y,"reelX":table.reelX,"reelY":table.reelY,"name":table.name,"side":table.side})
    self.session.commit()

  def updateExponentTable(self,table):
    if(table.exponent):
      self.session.query(TableEntity).filter_by(id=table.id).update({"exponent_id":table.exponent.id})
      self.session.commit()
  
  def deleteTable(self,id):
    tableEntities = self.session.query(TableEntity).filter_by(id=id).all()
    self.session.delete(tableEntities[0])
    self.session.commit()

  
  def deleteAllTablesOfRoom(self,room_id):
    self.session.query(TableEntity).filter_by(room_id=room_id).delete()
    self.session.commit()