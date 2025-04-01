from model.objects.project import Project
from application.mapper.roomMapper import RoomMapper
from application.mapper.exponentMapper import ExponentMapper
from application.mapper.tableGroupMapper import TableGroupMapper

class ProjectMapper:
  
  def jsonToDomain(self,json):
    rooms = []
    if json.rooms:
        roomMapper = RoomMapper()
        for i in range(0,len(json.rooms),1):
            jsonRoom = json.rooms[i]
            rooms.append(roomMapper.jsonToDomain(jsonRoom))  
    exponents = []
    if json.exponents:
        exponentMapper = ExponentMapper()
        for i in range(0,len(json.exponents),1):
            jsonExponent = json.exponents[i]
            exponents.append(exponentMapper.jsonToDomain(jsonExponent))
    tableGroups = []
    if json.tableGroups:
        tableGroupMapper = TableGroupMapper()
        for i in range(0,len(json.tableGroups),1):
            jsonTableGroup = json.tableGroups[i]
            tableGroups.append(tableGroupMapper.jsonToDomain(jsonTableGroup))    
    return Project(json.id,json.name,rooms,tableGroups,exponents)