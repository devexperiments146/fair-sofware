
from PyQt6.QtWidgets import (
    QGraphicsItem,QGraphicsRectItem
)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt




class GroupView(QGraphicsItemGroup):
        
    def __init__(self,index,tableController,room):
        super().__init__()
        self.tableController = tableController
        self.index = index
        self.room = room
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)


    def mouseReleaseEvent(self, event):
        new_position = self.scenePos()
        self.tableController.updatePositionTable(self.index,new_position.x(),new_position.y(),self.room)
        super().mouseReleaseEvent(event)
