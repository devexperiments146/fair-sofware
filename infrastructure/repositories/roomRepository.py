from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import func


from infrastructure.entities.tableEntity import TableEntity
from infrastructure.entities.tableGroupEntity import TableGroupEntity
from infrastructure.entities.roomEntity import RoomEntity
from infrastructure.entities.exponentEntity import ExponentEntity
from infrastructure.entities.projectEntity import ProjectEntity
from infrastructure.entities.doorEntity import DoorEntity 
from infrastructure.entities.unusableSpaceEntity import UnusableSpaceEntity

from model.objects.table import Table
from model.objects.tableGroup import TableGroup
from model.objects.room import Room
from model.objects.exponent import Exponent
from model.objects.project import Project
from model.objects.door import Door
from model.objects.unusableSpace import UnusableSpace

from infrastructure.entities.base import Base

class RoomRepository:
  def __init__(self,session,store):
    self.session = session
    self.store = store

  def addRoom(self,room):
    maxValue = self.session.query(func.max(RoomEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    roomEntity = RoomEntity(self.store.getSelectedProject().id,newId,room.name,room.x,room.y,room.width,room.length)
    self.session.add(roomEntity)
    self.session.commit()
    return newId

  def copyRoom(self,room):
    maxValue = self.session.query(func.max(RoomEntity.id)).scalar()
    if(maxValue):
      roomId=int(maxValue)+1
    else:
      roomId=1
    roomEntity = RoomEntity(self.store.getSelectedProject().id,roomId,room.name,room.x,room.y,room.width,room.length)
    self.session.add(roomEntity)
    maxValue = self.session.query(func.max(UnusableSpaceEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    for unusableSpace in room.unusableSpaces:
      unusableSpaceEntity = UnusableSpaceEntity(self.store.getSelectedProject().id,newId,unusableSpace.name,unusableSpace.x,unusableSpace.y,unusableSpace.width,unusableSpace.length,unusableSpace.reelX,unusableSpace.reelY,unusableSpace.orientation,roomId)
      newId = newId + 1
      self.session.add(unusableSpaceEntity)
    maxValue = self.session.query(func.max(DoorEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    for door in room.doors:
      doorEntity = DoorEntity(self.store.getSelectedProject().id,newId,door.name,roomId,door.width,door.x,door.y,door.reelX, door.reelY,door.orientation)
      self.session.add(doorEntity)
      newId = newId + 1
    self.session.commit()
    return newId
  
  def loadRooms(self):
    roomEntities = self.session.query(RoomEntity).all()
    doorEntities = self.session.query(DoorEntity).all()
    unusableSpaceEntities = self.session.query(UnusableSpaceEntity).all()
    rooms = []
    for roomEntity in roomEntities:
      room = Room(roomEntity.id,roomEntity.name,roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y)
      roomDoorEntities = [x for x in doorEntities if x.room_id == roomEntity.id]
      for doorEntity in roomDoorEntities:
        roomDoor = Room(roomEntity.id,roomEntity.name,roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y)
        room.doors.append(Door(doorEntity.id,doorEntity.name,roomDoor,doorEntity.width,doorEntity.orientation,doorEntity.x,doorEntity.y,doorEntity.reelX,doorEntity.reelY)) 
      roomUnusableSpaceEntities = [x for x in unusableSpaceEntities if x.room_id == roomEntity.id]
      for unusableSpaceEntity in roomUnusableSpaceEntities:
        roomUnusableSpace = Room(roomEntity.id,roomEntity.name,roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y)
        unusableSpace = UnusableSpace(unusableSpaceEntity.id,unusableSpaceEntity.name,roomUnusableSpace,unusableSpaceEntity.x,
                                            unusableSpaceEntity.y,unusableSpaceEntity.reelX,unusableSpaceEntity.reelY,
                                            unusableSpaceEntity.orientation,unusableSpaceEntity.width,unusableSpaceEntity.length)
        room.unusableSpaces.append(unusableSpace)
      rooms.append(room)
    return rooms