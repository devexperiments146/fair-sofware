from model.objects.tableLine import TableLine

class TableLineMapper:
  
  def jsonToDomain(self,json,room,tables = []):
    return TableLine(json.id,room,json.x,json.y,json.reelX,json.virtuakY,json.orientation,json.width,json.tableSide,tables)
  
