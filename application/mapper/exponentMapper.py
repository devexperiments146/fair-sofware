from model.objects.exponent import Exponent

class ExponentMapper:
  
  def jsonToDomain(self,json):
    return Exponent(json.id,json.firstname,json.lastname)
  
