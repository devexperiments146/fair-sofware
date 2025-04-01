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

class TableGroupRepository:
  def __init__(self,session,store):
    self.session = session
    self.store = store

  def addTableGroup(self,tableGroup):
    maxValue = self.session.query(func.max(TableGroupEntity.id)).scalar()   
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    tableGroupEntity = TableGroupEntity(self.store.getSelectedProject().id,newId,tableGroup.width,tableGroup.length,tableGroup.color,tableGroup.maxQuantity,tableGroup.tableType)
    self.session.add(tableGroupEntity)
    self.session.commit()
    return newId