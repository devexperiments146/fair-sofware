
from PyQt6.QtWidgets import (
    QGraphicsItem,QGraphicsRectItem
)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt


class RoomView(QGraphicsRectItem):
    
    def __init__(self, x,y,w,h):
        super().__init__(x,y,w,h)
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor('black'))
        self.setPen(pen)

