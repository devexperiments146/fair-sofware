
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
        self._drag_start_scene_pos = None


    def mouseReleaseEvent(self, event):
        new_position = self.scenePos()
        if self._drag_start_scene_pos is not None:
            self.structureController.updatePositionStructure(self.index,  new_position.x(), new_position.y(),  self.room)
        self._drag_start_scene_pos = None
        super().mouseReleaseEvent(event)

    def mousePressEvent(self, event):
        self._drag_start_scene_pos = self.scenePos()
        super().mousePressEvent(event)
