from model.objects.tableGroup import TableGroup

class TableGroupMapper:
  
  def jsonToDomain(self,json):
    return TableGroup(json.id,json.width,json.length,json.color)
  
