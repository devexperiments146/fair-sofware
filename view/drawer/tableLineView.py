
from PyQt6.QtWidgets import (
    QGraphicsItem,QGraphicsRectItem
)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt


class TableLineView(QGraphicsLineItem):
    

    def __init__(self,id, x,y,length,orientation,tableLineController,room):
        self.id = id
        self.x = x
        self.y = y
        x2 = 0
        y2 = 0
        self.room = room
        if orientation == "Vertical":
            x2 = float(x)
            y2 = float(y) + float(length)
        else:
            x2 = float(x) + float(length)
            y2 = float(y)

        super().__init__(x,y,x2,y2)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.tableLineController = tableLineController
        pen = QPen()
        pen.setWidth(2)
        pen.setStyle(Qt.PenStyle.DashLine)
        pen.setColor(QColor('gray'))
        self.setPen(pen)

    def mouseReleaseEvent(self, event):
        new_position = self.scenePos()
        self.tableLineController.updatePositionTableLine(self.id,new_position.x(),new_position.y(),self.room)
        super().mouseReleaseEvent(event)
