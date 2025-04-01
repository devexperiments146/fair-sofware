from model.objects.zone import Zone
from model.objects.exponentGroup import ExponentGroup

class ReturnNextWallTableLineUsecase:
    def __init__(self, store,sortedTableLines):
        self.store = store
        self.sortedTableLines = sortedTableLines

    def execute(self):
        #0 Gauche, 1 Droite , 2 Haut ,3 Bas
        nextWallTableLine = []
        for i in range(0,4,1):
            for tableLine in self.sortedTableLines:
                if i < 2 and tableLine.orientation == "Vertical":
                    if len(nextWallTableLine) < i+1:
                        nextWallTableLine.append(tableLine)
                    else:
                        currentSelectedTableLine = nextWallTableLine[i]
                        if i == 0 and tableLine.x < currentSelectedTableLine.x:
                            nextWallTableLine[i] =  tableLine
                        if i == 1 and tableLine.x > currentSelectedTableLine.x:
                            nextWallTableLine[i] =  tableLine
                if i > 1 and tableLine.orientation == "Horizontal":
                    if len(nextWallTableLine) < i+1:
                        nextWallTableLine.append(tableLine)
                    else:
                        currentSelectedTableLine = nextWallTableLine[i]
                        if i == 0 and tableLine.y < currentSelectedTableLine.y:
                            nextWallTableLine[i] =  tableLine
                        if i == 1 and tableLine.y > currentSelectedTableLine.y:
                            nextWallTableLine[i] =  tableLine
        return nextWallTableLine