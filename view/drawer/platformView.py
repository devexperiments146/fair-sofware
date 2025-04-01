
from PyQt6.QtWidgets import (
    QGraphicsItem,QGraphicsRectItem
)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt


class PlatformView(QGraphicsRectItem):
    
    def __init__(self,id, x,y,width,length,orientation,platformController,room):
        self.id = id
        self.room = room
        super().__init__(x,y,width,length)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.platformController = platformController
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor('black'))
        
        brush = QBrush()
        brush.setColor(QColor('black'))
        brush.setStyle(Qt.BrushStyle.Dense6Pattern)
        self.setPen(pen)
        self.setBrush(brush)

    def mouseReleaseEvent(self, event):
        new_position = self.scenePos()
        self.platformController.updatePlatform(self.id,new_position.x(),new_position.y(),self.room)
        super().mouseReleaseEvent(event)
