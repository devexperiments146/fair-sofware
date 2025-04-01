
from PyQt6.QtWidgets import (
    QGraphicsItem,QGraphicsRectItem
)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt


class UnusableSpaceView(QGraphicsRectItem):
    
    def __init__(self,id, x,y,width,length,orientation,unusableSpaceController,room):
        self.id = id
        self.room = room
        super().__init__(x,y,width,length)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.unusableSpaceController = unusableSpaceController
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor('black'))
        
        brush = QBrush()
        brush.setColor(QColor('black'))
        brush.setStyle(Qt.BrushStyle.BDiagPattern)
        self.setPen(pen)
        self.setBrush(brush)

    def mouseReleaseEvent(self, event):
        new_position = self.scenePos()
        self.unusableSpaceController.updateUnusableSpace(self.id,new_position.x(),new_position.y(),self.room)
        super().mouseReleaseEvent(event)
