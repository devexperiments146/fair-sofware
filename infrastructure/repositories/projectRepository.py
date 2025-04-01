
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import func

from datetime import datetime

from infrastructure.entities.tableEntity import TableEntity
from infrastructure.entities.tableGroupEntity import TableGroupEntity
from infrastructure.entities.roomEntity import RoomEntity
from infrastructure.entities.exponentEntity import ExponentEntity
from infrastructure.entities.projectEntity import ProjectEntity
from infrastructure.entities.doorEntity import DoorEntity 
from infrastructure.entities.tableLineEntity import TableLineEntity 
from infrastructure.entities.zoneEntity import ZoneEntity 
from infrastructure.entities.unusableSpaceEntity import UnusableSpaceEntity 
from infrastructure.entities.platformEntity import PlatformEntity 


from model.objects.table import Table
from model.objects.tableGroup import TableGroup
from model.objects.room import Room
from model.objects.exponent import Exponent
from model.objects.project import Project
from model.objects.door import Door
from model.objects.tableLine import TableLine
from model.objects.zone import Zone
from model.objects.unusableSpace import UnusableSpace
from model.objects.platform import Platform


from infrastructure.entities.base import Base

class ProjectRepository:
  def __init__(self,session):
    self.session = session

  def getProjects(self):
    projectEntities = self.session.query(ProjectEntity).all()
    projects = []
    for i in range(0,len(projectEntities),1):
      projectEntity = projectEntities[i]
      project = Project(projectEntity.id,projectEntity.name)
      projects.append(project)
    return projects
  
  def getProject(self,project):
    projectEntities= self.session.query(ProjectEntity).filter_by(id=project.id).join(TableGroupEntity, isouter=True).join(ExponentEntity, isouter=True).join(RoomEntity, isouter=True).all()
    projectEntity = projectEntities[0]
    doorEntities = self.session.query(DoorEntity).filter_by(project_id=project.id).join(RoomEntity).all()
    tableEntities = self.session.query(TableEntity).filter_by(project_id=project.id).join(RoomEntity, onclause=(TableEntity.room_id == RoomEntity.id)).join(TableGroupEntity, onclause=(TableEntity.table_group_id == TableGroupEntity.id)).join(ExponentEntity,onclause=(TableEntity.exponent_id == ExponentEntity.id), isouter=True).all()
    tableLineEntities = self.session.query(TableLineEntity).filter_by(project_id=project.id).join(RoomEntity).all()  
    zoneEntities = self.session.query(ZoneEntity).filter_by(project_id=project.id).join(RoomEntity).all()
    unusableSpaceEntities = self.session.query(UnusableSpaceEntity).filter_by(project_id=project.id).join(RoomEntity).all()
    platformEntities = self.session.query(PlatformEntity).filter_by(project_id=project.id).join(RoomEntity).all()
    exponents = []
    for exponentEntity in projectEntity.exponents:
      exponentDate = exponentEntity.date[:10]
      date = datetime.strptime(exponentDate,'%d/%m/%Y').date()
      exponents.append(Exponent(exponentEntity.id,exponentEntity.firstname,exponentEntity.lastname,date,exponentEntity.tableType,exponentEntity.description,exponentEntity.room_choice_id,exponentEntity.next_door_id,exponentEntity.next_exponent_id,exponentEntity.next_wall,exponentEntity.table_line_choice_id,exponentEntity.table_line_position,exponentEntity.end_of_table))
    tableGroups = []
    for tableGroupEntity in projectEntity.tableGroups:
      tableGroups.append(TableGroup(tableGroupEntity.id,tableGroupEntity.width,tableGroupEntity.length,tableGroupEntity.color,tableGroupEntity.maxQuantity,tableGroupEntity.tableType))
    rooms = self.getRooms(projectEntity,doorEntities,tableEntities,tableLineEntities,zoneEntities,unusableSpaceEntities,platformEntities)
    completeProject = Project(projectEntities[0].id,projectEntities[0].name,rooms,tableGroups,exponents)
    return completeProject
  
  
  def getRooms(self,projectEntity,doorEntities,tableEntities,tableLineEntities,zoneEntities,unusableSpaceEntities,platformEntities):
    rooms = []
    for roomEntity in projectEntity.rooms:
      doors = []
      roomDoorEntities = [x for x in doorEntities if x.room_id == roomEntity.id]
      for doorEntity in roomDoorEntities:
        roomEntity = doorEntity.room
        room = Room(roomEntity.id,roomEntity.name,roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y)
        doors.append(Door(doorEntity.id,doorEntity.name,room,doorEntity.width,doorEntity.orientation,doorEntity.x,doorEntity.y,doorEntity.reelX,doorEntity.reelY)) 
      #Zones
      zones = []   
      roomZoneEntities = [x for x in zoneEntities if x.room_id == roomEntity.id]
      for zoneEntity in roomZoneEntities:
        roomEntity = zoneEntity.room
        room = Room(roomEntity.id,roomEntity.name,roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y)
        zone = Zone(zoneEntity.id,zoneEntity.name,room,zoneEntity.width,zoneEntity.length,zoneEntity.x,zoneEntity.y,zoneEntity.reelX,zoneEntity.reelY)
        zones.append(zone)
      #Unusable spaces
      unusableSpaces = []   
      roomUnusableSpacesEntities = [x for x in unusableSpaceEntities if x.room_id == roomEntity.id]
      for unusableSpaceEntity in roomUnusableSpacesEntities:
        roomEntity = unusableSpaceEntity.room
        room = Room(roomEntity.id,roomEntity.name,roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y)
        unusableSpace = UnusableSpace(unusableSpaceEntity.id,unusableSpaceEntity.name,room,unusableSpaceEntity.x,
                                            unusableSpaceEntity.y,unusableSpaceEntity.reelX,unusableSpaceEntity.reelY,
                                            unusableSpaceEntity.orientation,unusableSpaceEntity.width,unusableSpaceEntity.length)
        unusableSpaces.append(unusableSpace)
      #Platforms
      platforms = []   
      roomPlatformEntities = [x for x in platformEntities if x.room_id == roomEntity.id]
      for platformEntity in roomPlatformEntities:
        roomEntity = platformEntity.room
        room = Room(roomEntity.id,roomEntity.name,roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y)
        platform = Platform(platformEntity.id,platformEntity.name,room,platformEntity.x,
                                            platformEntity.y,platformEntity.reelX,platformEntity.reelY,
                                            platformEntity.orientation,platformEntity.width,platformEntity.length)
        platforms.append(platform)
      #Tables
      tables = self.getTables(tableEntities,roomEntity)
      tableLines = []
      roomTableLineEntities = [x for x in tableLineEntities if x.room_id == roomEntity.id]
      for tableLineEntity in roomTableLineEntities:
        roomEntity = tableLineEntity.room
        room = Room(roomEntity.id,roomEntity.name,roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y)
        tableLine = TableLine(tableLineEntity.id,tableLineEntity.name,room,tableLineEntity.x,tableLineEntity.y,tableLineEntity.reelX,tableLineEntity.reelY,tableLineEntity.orientation,tableLineEntity.width,tableLineEntity.tableSide,[])
        tableLines.append(tableLine)
      rooms.append(Room(roomEntity.id,roomEntity.name,roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y,tables,doors,tableLines,zones,unusableSpaces,platforms))
    return rooms
  
  def getTables(self,tableEntities,roomEntity):
    tables = []
    roomTableEntities = [x for x in tableEntities if x.room_id == roomEntity.id]
    for tableEntity in roomTableEntities:
      roomEntity = tableEntity.room
      room = Room(roomEntity.id,roomEntity.name,roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y)
      tableGroupEntity = tableEntity.tableGroup
      tableGroup = TableGroup(tableGroupEntity.id,tableGroupEntity.width,tableGroupEntity.length,tableGroupEntity.color,tableGroupEntity.maxQuantity,tableGroupEntity.tableType)
      exponentEntity = tableEntity.exponent
      exponent = None
      if exponentEntity:
        exponentDate = exponentEntity.date[:10]
        date = datetime.strptime(exponentDate,'%d/%m/%Y').date()
        exponent = Exponent(exponentEntity.id,exponentEntity.firstname,exponentEntity.lastname,date,exponentEntity.tableType,exponentEntity.description,exponentEntity.room_choice_id,exponentEntity.next_door_id,exponentEntity.next_exponent_id,exponentEntity.next_wall,exponentEntity.table_line_choice_id,exponentEntity.table_line_position,exponentEntity.end_of_table)
      table = Table(tableEntity.id,tableEntity.name,room,tableGroup,tableEntity.x,tableEntity.y,tableEntity.reelX,tableEntity.reelY,tableEntity.orientation,exponent)
      table.side = tableEntity.side
      tables.append(table)  
    return tables

  
  def addProject(self,project):
    projectEntity = ProjectEntity(project.name)
    self.session.add(projectEntity)
    self.session.commit()
    return projectEntity.id
