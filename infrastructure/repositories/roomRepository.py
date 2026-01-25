from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import func

from infrastructure.entities.roomEntity import RoomEntity
from infrastructure.entities.doorEntity import DoorEntity 
from infrastructure.entities.unusableSpaceEntity import UnusableSpaceEntity
from infrastructure.entities.tableLineEntity import TableLineEntity

from model.objects.room import Room
from model.objects.door import Door
from model.objects.unusableSpace import UnusableSpace
from model.objects.tableLine import TableLine

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
    
    # Load only the entities related to this specific room
    roomUnusableSpaceEntities = self.session.query(UnusableSpaceEntity).filter_by(room_id=room.id).all()
    roomDoorEntities = self.session.query(DoorEntity).filter_by(room_id=room.id).all()
    roomTableLineEntities = self.session.query(TableLineEntity).filter_by(room_id=room.id).all()
    
    # Unusable space
    maxValue = self.session.query(func.max(UnusableSpaceEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    for unusableSpaceEntity in roomUnusableSpaceEntities:
      newUnusableSpaceEntity = UnusableSpaceEntity(self.store.getSelectedProject().id,newId,unusableSpaceEntity.name,unusableSpaceEntity.x,unusableSpaceEntity.y,unusableSpaceEntity.width,unusableSpaceEntity.length,unusableSpaceEntity.reelX,unusableSpaceEntity.reelY,unusableSpaceEntity.orientation,roomId)
      newId = newId + 1
      self.session.add(newUnusableSpaceEntity)
    # Door
    maxValue = self.session.query(func.max(DoorEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    for doorEntity in roomDoorEntities:
      newDoorEntity = DoorEntity(self.store.getSelectedProject().id,newId,doorEntity.name,roomId,doorEntity.width,doorEntity.x,doorEntity.y,doorEntity.reelX, doorEntity.reelY,doorEntity.orientation)
      self.session.add(newDoorEntity)
      newId = newId + 1
    # Table line
    maxValue = self.session.query(func.max(TableLineEntity.id)).scalar()
    if(maxValue):
      newId=int(maxValue)+1
    else:
      newId=1
    for tableLineEntity in roomTableLineEntities:
      newTableLineEntity = TableLineEntity(self.store.getSelectedProject().id,newId,tableLineEntity.name,tableLineEntity.x,tableLineEntity.y,tableLineEntity.width,tableLineEntity.reelX,tableLineEntity.reelY,tableLineEntity.orientation,roomId,tableLineEntity.tableSide)
      newId = newId + 1
      self.session.add(newTableLineEntity)
    self.session.commit()
    return newId
  
  def loadRooms(self):
    roomEntities = self.session.query(RoomEntity).all()
    doorEntities = self.session.query(DoorEntity).all()
    unusableSpaceEntities = self.session.query(UnusableSpaceEntity).all()
    tableLineEntities = self.session.query(TableLineEntity).all()
    rooms = []
    for roomEntity in roomEntities:
      projectRoom = [x for x in self.store.getProjects() if x.id ==int(roomEntity.project_id)]
      room = Room(roomEntity.id,roomEntity.name +" ["+projectRoom[0].getName()+"]",roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y)
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
      roomTableLineEntities = [x for x in tableLineEntities if x.room_id == roomEntity.id]
      for roomTableLineEntity in roomTableLineEntities:
        roomTableLine  = Room(roomEntity.id,roomEntity.name,roomEntity.width,roomEntity.length,roomEntity.x,roomEntity.y)
        tableLine = TableLine(roomTableLineEntity.id,roomTableLineEntity.name,roomTableLine,roomTableLineEntity.x,
                                            roomTableLineEntity.y,roomTableLineEntity.reelX,roomTableLineEntity.reelY,
                                            roomTableLineEntity.orientation,roomTableLineEntity.width,roomTableLineEntity.tableSide)
        room.tableLines.append(tableLine)
      rooms.append(room)
    return rooms
  
  def deleteRoom(self,id):
    roomEntities = self.session.query(RoomEntity).filter_by(id=id).all()
    self.session.delete(roomEntities[0])
    self.session.commit()
  