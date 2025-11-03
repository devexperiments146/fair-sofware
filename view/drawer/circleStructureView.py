
from PyQt6.QtWidgets import (
    QGraphicsItem,QGraphicsRectItem
)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt


class CircleStructureView(QGraphicsEllipseItem):
    
    def __init__(self,id, x,y,width,length,orientation,structureController,room):
        self.id = id
        self.room = room

        structureWidth = width
        structureLength = length
        if orientation == "Horizontal" :
            structureWidth = length
            structureLength = width
    
        super().__init__(x,y,structureWidth,structureLength)
        self.structureController = structureController
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor('black'))
        
        brush = QBrush()
        brush.setColor(QColor('lightgray'))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        self.setPen(pen)
        self.setBrush(brush)

