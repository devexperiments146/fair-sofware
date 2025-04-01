
from PyQt6.QtWidgets import (
    QGraphicsItem,QGraphicsRectItem
)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt


class ZoneView(QGraphicsRectItem):
    
    def __init__(self,index, x,y,w,h,store):
        super().__init__(x,y,w,h)
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor('black'))
        self.setPen(pen)
        brush = QBrush()
        brush.setColor(QColor(store.getColors()[index]))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        self.setPen(pen)
        self.setBrush(brush)
        self.setOpacity(0.5)

