from model.objects.table import Table

class TableMapper:
  
  def jsonToDomain(self,json,room,tableGroup,exponent = None):
    return Table(json.id,json.name,room,tableGroup,json.x,json.y,json.reelX,json.reelY,json.orientation,exponent)
  
