from model.objects.zone import Zone
from model.objects.tableLineExponentGroup import TableLineExponentGroup

class ReturnNextWallExponentGroupUsecase:
    def __init__(self, exponentGroups):
        self.exponentGroups = exponentGroups

    def execute(self):
        nextWallExponentGroups = []
        for exponentName in self.exponentGroups.keys():
            exponentGroup = self.exponentGroups.get(exponentName)
            if exponentGroup.nextWall:
                nextWallExponentGroups.append(exponentName)
        return nextWallExponentGroups