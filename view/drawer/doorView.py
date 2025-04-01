
from PyQt6.QtWidgets import (
    QGraphicsItem,QGraphicsRectItem
)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt


class DoorView(QGraphicsLineItem):
    
    def __init__(self,id, x,y,width,orientation,doorController,room):
        self.id = id
        self.room = room
        x2 = 0
        y2 = 0
        if orientation == "Vertical":
            x2 = x
            y2 = y + width
        else:
            x2 = x + width
            y2 = y

        super().__init__(x,y,x2,y2)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.doorController = doorController
        pen = QPen()
        pen.setWidth(6)
        pen.setColor(QColor('black'))
        self.setPen(pen)

    def mouseReleaseEvent(self, event):
        new_position = self.scenePos()
        self.doorController.updatePositionDoor(self.id,new_position.x(),new_position.y(),self.room)
        super().mouseReleaseEvent(event)
