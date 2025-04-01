
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

class ExponentRepository:
  def __init__(self,session,store):
    self.session = session
    self.store = store

  def addExponent(self,exponent):
    maxValue = self.session.query(func.max(ExponentEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    exponentEntity = ExponentEntity(self.store.getSelectedProject().id,newId,exponent.firstname,exponent.lastname,exponent.date,exponent.tableType,exponent.description)
    self.session.add(exponentEntity)
    self.session.commit()
    return exponentEntity.id
  
  def deleteAllExponents(self):  
    self.session.query(ExponentEntity).delete()
    self.session.commit()
  
  def updateExponent(self,exponent):    
    self.session.query(ExponentEntity).filter_by(id=exponent.id).update({"firstname":exponent.firstname,"lastname":exponent.lastname,"tableType":exponent.tableType,"room_choice_id":exponent.roomChoiceId,"next_door_id":exponent.nextDoorId,"next_exponent_id":exponent.nextExponentId,"next_wall":exponent.nextWall,"table_line_choice_id":exponent.tableLineChoiceId,"table_line_position":exponent.tableLinePosition,"end_of_table":exponent.endOfTable})
    self.session.commit()
  

