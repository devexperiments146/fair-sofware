from model.objects.exponentGroup import ExponentGroup

class RegroupExponentsUsecase:

    def __init__(self, store,room):
        self.store = store
        self.tableGroups = store.getSelectedProject().tableGroups
        self.room = room

    def execute(self):
        tables = []
        filteredExponents = []

        for room in self.store.getSelectedProject().rooms:
            for tableLine in room.tableLines:
                tables = tables + tableLine.tables
        sortedByDateExponents  = sorted(self.store.getSelectedProject().exponents, key=lambda x: x.date)

        for exponent in sortedByDateExponents:
            alreadyAssigned = False
            filteredTables = [x for x in tables  if x.exponent.id == exponent.id]
            if len(filteredTables)>0:
                alreadyAssigned = True
            if not alreadyAssigned:
                if exponent.roomChoiceId:
                    if exponent.roomChoiceId == self.room.id:
                        filteredExponents.append(exponent)
                else:
                    filteredExponents.append(exponent)
        exponents  = sorted(filteredExponents, key=lambda x: (x.roomChoiceId or 0,x.tableLineChoiceId or 0),  reverse = True)

        exponentGroups = self.regroupExponents(exponents)
        nextExponentGroups =self.regroupNextExponents(exponentGroups,exponents)
        
        return nextExponentGroups 
  
    def getTableGroup(self, exponent):
        tableGroups = [x for x in self.tableGroups  if x.tableType == exponent.tableType.strip()]
        return tableGroups[0]
  
    def regroupExponents(self,exponents):
        exponentTableGroups = {}
        for exponent in exponents: 
            tableGroup = self.getTableGroup(exponent)
            lowerExponentName = exponent.getName().lower().strip()
            if lowerExponentName in exponentTableGroups:
                exponentGroup = exponentTableGroups.get(lowerExponentName)
                exponentGroup.addExponent(exponent,tableGroup)
            else:
                exponentGroup = ExponentGroup()
                exponentGroup.addExponent(exponent,tableGroup)
                exponentTableGroups[lowerExponentName] = exponentGroup
        return exponentTableGroups
    

    def regroupNextExponents(self,exponentGroups,exponents):
        nextExponentGroups = {}
        for exponentName in exponentGroups.keys():
            if exponentName not in nextExponentGroups:
                exponentGroup = exponentGroups.get(exponentName)
                exponent = exponentGroup.exponents[0]
                if exponent.nextExponentId:
                    nextExponent = [x for x in exponents  if x.id == exponent.nextExponentId]
                    lowerExponentName = nextExponent[0].getName().lower().strip()
                    #Add the next exponent
                    if lowerExponentName not in nextExponentGroups:
                        nextExponentGroups[lowerExponentName] = exponentGroups.get(lowerExponentName)
                    nextExponentGroup = nextExponentGroups.get(lowerExponentName)
                    #Merge exponent with the nest exponent
                    nextExponentGroup.merge(exponentGroup)
                else:
                    #No next exponent we add the exponent
                    lowerExponentName = exponent.getName().lower().strip()
                    nextExponentGroups[lowerExponentName] = exponentGroup
        return nextExponentGroups

