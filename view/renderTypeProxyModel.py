from PyQt6 import QtCore
from PyQt6.QtCore import Qt

class RenderTypeProxyModel (QtCore.QSortFilterProxyModel): #Custom Proxy Model
    def __init__(self, type, parent=None):
        super(RenderTypeProxyModel,self).__init__(parent)
        self.__type = type

    def filterAcceptsRow(self, row, parent):
        model = self.sourceModel()
        index = model.index(row, 0, parent)
        if model.data(index,QtCore.Qt.DisplayRole) == type:
            return True
        else:
            return False
