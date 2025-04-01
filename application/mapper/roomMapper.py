
from model.objects.room import Room


from application.mapper.doorMapper import DoorMapper
from application.mapper.tableMapper import TableMapper
from application.mapper.tableLineMapper import TableLineMapper


class RoomMapper:
  
  def jsonToDomain(self,json):
    room = Room(json.id,json.name,json.width,json.length,json.x,json.y)
    doors = []
    if json.doors:
        doorMapper = DoorMapper()
        for i in range(0,len(json.doors),1):
            jsonDoor = json.doors[i]
            doors.append(doorMapper.jsonToDomain(jsonDoor,room)) 
    tables = []
    if json.tables:
        tableMapper = TableMapper()
        for i in range(0,len(json.tables),1):
            jsonTables = json.tables[i]
            tables.append(tableMapper.jsonToDomain(jsonTables,room))
    tableLines = []
    if json.tableLines:
        tableLineMapper = TableLineMapper()
        for i in range(0,len(json.tableLines),1):
            jsonTableLine = json.tableLines[i]
            tableLines.append(tableLineMapper.jsonToDomain(jsonTableLine,room))    
    return room