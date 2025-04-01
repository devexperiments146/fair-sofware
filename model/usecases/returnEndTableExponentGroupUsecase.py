from model.objects.zone import Zone
from model.objects.tableLineExponentGroup import TableLineExponentGroup

class ReturnEndTableExponentGroupUsecase:
    def __init__(self, exponentGroups):
        self.exponentGroups = exponentGroups

    def execute(self):
        endTableExponentGroups = []
        for exponentName in self.exponentGroups.keys():
            exponentGroup = self.exponentGroups.get(exponentName)
            if exponentGroup.endOfTable:
                endTableExponentGroups.append(exponentName)
        return endTableExponentGroups