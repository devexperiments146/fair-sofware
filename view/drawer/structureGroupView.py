
from PyQt6.QtWidgets import (
    QGraphicsItem,QGraphicsRectItem
)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt

class StructureGroupView(QGraphicsItemGroup):
        
    def __init__(self,index,structureController,room):
        super().__init__()
        self.structureController = structureController
        self.index = index
        self.room = room
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        new_position = self.scenePos()
        self.structureController.updatePositionStructure(self.index,  new_position.x(), new_position.y(),  self.room)
