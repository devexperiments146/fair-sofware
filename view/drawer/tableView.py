
from PyQt6.QtWidgets import (
    QGraphicsItem,QGraphicsRectItem
)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt


class TableView(QGraphicsRectItem):
    
    
    def __init__(self, x,y,w,h,index,color,tableController):
        super().__init__(x,y,w,h)
        self.tableController = tableController
        self.index = index
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor('black'))
        
        brush = QBrush()
        brush.setColor(QColor(color))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        self.setPen(pen)
        self.setBrush(brush)
