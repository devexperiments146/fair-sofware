from model.objects.door import Door

class DoorMapper:
  
  def jsonToDomain(self,json,room):
    return Door(json.id,json.name,room,json.width,json.orientation,json.x,json.y,json.reelX,json.reelY)
  
