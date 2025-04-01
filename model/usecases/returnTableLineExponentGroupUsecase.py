from model.objects.zone import Zone
from model.objects.tableLineExponentGroup import TableLineExponentGroup

class ReturnTableLineExponentGroupUsecase:
    def __init__(self, exponentGroups):
        self.exponentGroups = exponentGroups

    def execute(self):
        tableLineExponentGroups = {}
        for exponentName in self.exponentGroups.keys():
            exponentGroup = self.exponentGroups.get(exponentName)
            if exponentGroup.tableLineChoiceId:
                tableLineExponentGroup = tableLineExponentGroups.get(exponentGroup.tableLineChoiceId)
                if tableLineExponentGroup:
                    tableLineExponentGroup.addExponentGroupName(exponentName)
                else:
                    tableLineExponentGroups[exponentGroup.tableLineChoiceId] = TableLineExponentGroup()
                    tableLineExponentGroup = tableLineExponentGroups.get(exponentGroup.tableLineChoiceId)
                    tableLineExponentGroup.addExponentGroupName(exponentName)
        return tableLineExponentGroups