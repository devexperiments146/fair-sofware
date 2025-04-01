
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import func


from infrastructure.entities.tableEntity import TableEntity
from infrastructure.entities.tableGroupEntity import TableGroupEntity
from infrastructure.entities.roomEntity import RoomEntity
from infrastructure.entities.exponentEntity import ExponentEntity
from infrastructure.entities.projectEntity import ProjectEntity
from infrastructure.entities.doorEntity import DoorEntity 
from infrastructure.entities.parameterEntity import ParameterEntity

from model.objects.table import Table
from model.objects.tableGroup import TableGroup
from model.objects.room import Room
from model.objects.exponent import Exponent
from model.objects.project import Project
from model.objects.door import Door
from model.objects.parameter import Parameter

from infrastructure.entities.base import Base

class ParameterRepository:
  def __init__(self,session):
    self.session = session

  def getParameters(self):
    parameterEntities = self.session.query(ParameterEntity).all()
    parameters = []
    for i in range(0,len(parameterEntities),1):
      projectEntity = parameterEntities[i]
      parameter = Parameter(projectEntity.id,projectEntity.name,projectEntity.value)
      parameters.append(parameter)
    return parameters
  
  def updateParameterValue(self,name,value):
    parameterEntity = self.session.query(ParameterEntity).filter_by(name=name).all()
    if(len(parameterEntity)>0):
      self.session.query(ParameterEntity).filter_by(id=parameterEntity[0].id).update({"value":value})
    else:
      parameterEntity = ParameterEntity(name,value)
      self.session.add(parameterEntity)
    self.session.commit()
