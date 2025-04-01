from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt

from PyQt6.QtCore import  Qt

from view.drawer.tableView import TableView
from view.drawer.tableLineView import TableLineView
from view.drawer.roomView import RoomView
from view.drawer.doorView import DoorView
from view.drawer.groupView import GroupView
from view.drawer.zoneView import ZoneView
from view.drawer.unusableSpaceView import UnusableSpaceView 
from view.drawer.platformView import PlatformView
class Viewport(QGraphicsView):


    def __init__(self,parent,store,tableController=None,tableLineController=None,doorController=None,room=None,unusableSpaceController = None,zoneController = None,platformController = None):
        super(Viewport, self).__init__(parent)
        self.tableController = tableController
        self.tableLineController = tableLineController
        self.doorController = doorController
        self.zoneController = zoneController
        self.unusableSpaceController = unusableSpaceController
        self.platformController = platformController
        self.displayExponent = store.getDisplayExponent()

        multiplier = store.getMultiplier()
        self.scene = QGraphicsScene(self)
        
        roomView = RoomView(room.x, room.y, room.width*multiplier, room.length*multiplier)
        self.scene.addItem(roomView)

        if store.getDisplayTables():
            self.drawTables(room,multiplier)

        if store.getDisplayDoors():
            self.drawDoors(room,multiplier)

        if store.getDisplayTableLines():
            self.drawTableLines(room,multiplier)

        if store.getDisplayUnusableSpaces():
            self.drawUnusableSpaces(room,multiplier)

        if store.getDisplayPlatforms():
            self.drawPlatforms(room,multiplier)

        if store.getDisplayZones():
            self.drawZones(room,multiplier,store)

        if store.getDisplayMeasurements():
            self.drawHorizontalMeasurements(room,multiplier)
            self.drawVerticalMeasurements(room,multiplier)

        # self.setTransformationAnchor(self.ViewportAnchor.AnchorUnderMouse)
        # self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        # self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        # self.setResizeAnchor(self.ViewportAnchor.AnchorUnderMouse)

        #width = 2600
        #height = 2600
        # if  len(rooms) > 0:
        #   room = rooms[0]
        #   width = room.width*self.multiplicateur
        #   height = room.length*self.multiplicateur

        # self.setSceneRect(0, 0, width, height)
        # self.setFixedSize( width, height)
        #self.fitInView(scene.itemsBoundingRect(),Qt.AspectRatioMode.KeepAspectRatio)
        self.fitInView(self.scene.itemsBoundingRect())

        self.setScene(self.scene)
        self.setRenderHints(
            QPainter.RenderHint.Antialiasing
            | QPainter.RenderHint.SmoothPixmapTransform
        )

    def drawTableLines(self,room,multiplier):
        tableLines = self.tableLineController.getTableLines(room)
        for i in range(0,len(tableLines),1):
            item = TableLineView(tableLines[i].id,tableLines[i].x,tableLines[i].y,tableLines[i].width*multiplier,tableLines[i].orientation,self.tableLineController,room)
            self.scene.addItem(item)

    def drawDoors(self,room,multiplier):
        doors = self.doorController.getDoors(room)
        for i in range(0,len(doors),1):
            item = DoorView(doors[i].id,doors[i].x,doors[i].y,doors[i].width*multiplier,doors[i].orientation,self.doorController,room)
            self.scene.addItem(item)       

    def drawZones(self,room,mulitplier,store):
        zones = self.zoneController.getZones(room)
        for i in range(0,len(zones),1):
            index = i
            if room.name == "Polyvalente":
                index=i+3
            item = ZoneView(index,zones[i].x,zones[i].y,zones[i].width*mulitplier,zones[i].length*mulitplier,store)
            self.scene.addItem(item)     
            text = QGraphicsSimpleTextItem(zones[i].name)
            font = QFont()
            font.setPixelSize(24)
            font.setBold(True)
            text.setFont(font)
            text.setX(zones[i].x+zones[i].width*mulitplier/2)
            text.setY(zones[i].y+zones[i].length*mulitplier/2)
            text.setOpacity(0.5)
            self.scene.addItem(text)     
           

    def drawUnusableSpaces(self,room,multiplier):
        unusableSpaces = self.unusableSpaceController.getUnusableSpaces(room)
        for i in range(0,len(unusableSpaces),1):
            item = UnusableSpaceView(unusableSpaces[i].id,unusableSpaces[i].x,unusableSpaces[i].y,float(unusableSpaces[i].width)*multiplier,float(unusableSpaces[i].length)*multiplier,unusableSpaces[i].orientation,self.unusableSpaceController,room)
            self.scene.addItem(item)     
           

    def drawPlatforms(self,room,multiplier):
        platforms = self.platformController.getPlatforms(room)
        for i in range(0,len(platforms),1):
            item = PlatformView(platforms[i].id,platforms[i].x,platforms[i].y,float(platforms[i].width)*multiplier,float(platforms[i].length)*multiplier,platforms[i].orientation,self.platformController,room)
            self.scene.addItem(item)     

    def drawHorizontalMeasurements(self,room,multiplier):
         pen = QPen()
         pen.setWidth(1)
         
         line1 = QGraphicsLineItem(-50,0,-10,0)
         line1.setPen(pen)
         self.scene.addItem(line1)    

         line2 = QGraphicsLineItem(-50,room.length*multiplier,-10,room.length*multiplier)
         line2.setPen(pen)
         self.scene.addItem(line2)  

         line3 = QGraphicsLineItem(-40,0,-40,room.length*multiplier) 
         line3.setPen(pen)
         self.scene.addItem(line3)  

         sortedTableLines = sorted([x for x in room.tableLines if x.orientation == "Horizontal"] , key=lambda x: x.reelY)
         for i in range(0,len(sortedTableLines),1):
            tableLine = sortedTableLines[i]
            y = tableLine.y
            if room.name == "Omnisport":
                if i%2 == 0:
                    maxWidth = self.getMaxWidth(tableLine)*multiplier
                    y += maxWidth
                else:
                    precTableLine = sortedTableLines[i-1]
                    maxWidth = self.getMaxWidth(precTableLine)
                    reelWidth = round(tableLine.reelY-(precTableLine.reelY+maxWidth),2)
                    textWidth = QGraphicsSimpleTextItem(str(reelWidth))
                    font = QFont()
                    font.setPixelSize(12)
                    font.setBold(False)
                    textWidth.setFont(font)
                    textWidth.setRotation(-90)
                    textWidth.setX(-55)
                    textWidth.setY(y-((reelWidth*multiplier)/2))
                    self.scene.addItem(textWidth)  
            else:
                if i%2 == 0:
                    precTableLine = sortedTableLines[i-1]
                    maxWidth = self.getMaxWidth(precTableLine)
                    reelWidth = round(tableLine.reelY-(precTableLine.reelY+maxWidth),2)
                    if(reelWidth>0):
                        textWidth = QGraphicsSimpleTextItem(str(reelWidth))
                        font = QFont()
                        font.setPixelSize(12)
                        font.setBold(False)
                        textWidth.setFont(font)
                        textWidth.setRotation(-90)
                        textWidth.setX(-55)
                        textWidth.setY(y-((reelWidth*multiplier)/2))
                        self.scene.addItem(textWidth)  
                else:
                    maxWidth = self.getMaxWidth(tableLine)*multiplier
                    y += maxWidth
            line = QGraphicsLineItem(-50,y,-30,y) 
            line.setPen(pen)
            self.scene.addItem(line)  

    def drawVerticalMeasurements(self,room,multiplier):
         pen = QPen()
         pen.setWidth(1)
         
         line1 = QGraphicsLineItem(0,-50,0,-10)
         line1.setPen(pen)
         self.scene.addItem(line1)    

         line2 = QGraphicsLineItem(room.width*multiplier,-50,room.width*multiplier,-10)
         line2.setPen(pen)
         self.scene.addItem(line2)    

         line3 = QGraphicsLineItem(0,-40,room.width*multiplier,-40) 
         line3.setPen(pen)
         self.scene.addItem(line3)  

         sortedHorizontalTableLines = sorted([x for x in room.tableLines if x.orientation == "Horizontal"] , key=lambda x: x.reelY)
         sortedHorizontalTableLines.pop(len(sortedHorizontalTableLines)-1)
         sortedHorizontalTableLines.pop(len(sortedHorizontalTableLines)-1)
         sortedHorizontalTableLines.pop(0)

         
         minTableLine = sortedHorizontalTableLines[0]
         maxTableLine = sortedHorizontalTableLines[0]
         for i in range(0,len(sortedHorizontalTableLines),1):
             tableLine = sortedHorizontalTableLines[i]
             if minTableLine.x>tableLine.x:
                 minTableLine = tableLine
             if maxTableLine.x+maxTableLine.width<tableLine.x+tableLine.width:
                 maxTableLine = tableLine


         sortedVerticalTableLines = sorted([x for x in room.tableLines if x.orientation == "Vertical"] , key=lambda x: x.reelX)

         firstTableLine = sortedVerticalTableLines[0]

         line = QGraphicsLineItem(firstTableLine.x,-50,firstTableLine.x,-30) 
         line.setPen(pen)
         self.scene.addItem(line)  
            
         textWidth = QGraphicsSimpleTextItem(str(round(firstTableLine.reelX,2)))
         font = QFont()
         font.setPixelSize(12)
         font.setBold(False)
         textWidth.setFont(font)
         textWidth.setY(-55)
         textWidth.setX((firstTableLine.x)/2)
         self.scene.addItem(textWidth)  

         maxWidth = self.getMaxWidth(firstTableLine)

         line = QGraphicsLineItem(firstTableLine.x+maxWidth*multiplier,-50,firstTableLine.x+maxWidth*multiplier,-30) 
         line.setPen(pen)
         self.scene.addItem(line)  

         line = QGraphicsLineItem(minTableLine.x,-50,minTableLine.x,-30) 
         line.setPen(pen)
         self.scene.addItem(line)  

         width = minTableLine.x  - (firstTableLine.x+maxWidth*multiplier)      
         textWidth = QGraphicsSimpleTextItem(str(round(width/multiplier,2)))
         font = QFont()
         font.setPixelSize(12)
         font.setBold(False)
         textWidth.setFont(font)
         textWidth.setY(-55)
         textWidth.setX(firstTableLine.x+maxWidth*multiplier+(width/2))
         self.scene.addItem(textWidth)  

         line = QGraphicsLineItem(maxTableLine.x+maxTableLine.width*multiplier,-50,maxTableLine.x+maxTableLine.width*multiplier,-30) 
         line.setPen(pen)
         self.scene.addItem(line)  
         
         if len(sortedVerticalTableLines) > 2:
            lastTableLine = sortedVerticalTableLines[2]

            line = QGraphicsLineItem(lastTableLine.x,-50,lastTableLine.x,-30) 
            line.setPen(pen)
            self.scene.addItem(line)  

            width = lastTableLine.x  - (maxTableLine.x+maxTableLine.width*multiplier)      
            textWidth = QGraphicsSimpleTextItem(str(round(width/multiplier,2)))
            font = QFont()
            font.setPixelSize(12)
            font.setBold(False)
            textWidth.setFont(font)
            textWidth.setY(-55)
            textWidth.setX(maxTableLine.x+maxTableLine.width*multiplier+(width/2))
            self.scene.addItem(textWidth)  

            maxWidth = self.getMaxWidth(lastTableLine)

            line = QGraphicsLineItem(lastTableLine.x+maxWidth*multiplier,-50,lastTableLine.x+maxWidth*multiplier,-30) 
            line.setPen(pen)
            self.scene.addItem(line)  

            width = room.width*multiplier  - (lastTableLine.x+maxWidth*multiplier)      
            textWidth = QGraphicsSimpleTextItem(str(round(width/multiplier,2)))
            font = QFont()
            font.setPixelSize(12)
            font.setBold(False)
            textWidth.setFont(font)
            textWidth.setY(-55)
            textWidth.setX(lastTableLine.x+maxWidth*multiplier+(width/2))
            self.scene.addItem(textWidth)  

    def getMaxWidth(self,tableLine):
        maxWidth = 0
        for i in range(0,len(tableLine.tables),1):
            table = tableLine.tables[i]
            if(table.tableGroup.width >maxWidth):
                maxWidth = table.tableGroup.width
        return maxWidth

    def drawTables(self,room,multiplier):
        tables = self.tableController.getTables(room)
        for i in range(0,len(tables),1):
            if tables[i].orientation == "Vertical" :
                width = tables[i].tableGroup.width*multiplier
                height = tables[i].tableGroup.length*multiplier
            else:
                width = tables[i].tableGroup.length*multiplier
                height = tables[i].tableGroup.width*multiplier
            new_x = tables[i].x
            new_y = tables[i].y

            item = TableView(new_x, new_y, width, height,i,tables[i].tableGroup.color,self.tableController)

            text = QGraphicsSimpleTextItem(tables[i].name)
            font = QFont()
            font.setPixelSize(14)
            font.setBold(True)
            brush = QBrush()
            brush.setColor(QColor('gray'))
            brush.setStyle(Qt.BrushStyle.SolidPattern)
            text.setBrush(brush)
            text.setFont(font)

            if tables[i].orientation == "Vertical" :
                text.setX((tables[i].x+tables[i].tableGroup.width*multiplier/2)-5)
                text.setY((tables[i].y+tables[i].tableGroup.length*multiplier/2)-5)
            else:
                text.setX((tables[i].x+tables[i].tableGroup.length*multiplier/2)-5)
                text.setY((tables[i].y+tables[i].tableGroup.width*multiplier/2)-5)
            self.scene.addItem(text) 
            


            if tables[i].exponent and tables[i].exponent.endOfTable:
                bubble = QGraphicsEllipseItem(tables[i].x+1,tables[i].y+1,20,20)
                brush = QBrush()
                brush.setColor(QColor('white'))
                brush.setStyle(Qt.BrushStyle.SolidPattern)
                bubble.setBrush(brush)
                img = self.scene.addPixmap(QPixmap("./hanger.png"))
                img.setPos(tables[i].x+3,tables[i].y+3)


            if tables[i].exponent and tables[i].exponent.nextWall:
                if tables[i].exponent.endOfTable:
                    add = 20
                else:
                    add = 0
                bubble2 = QGraphicsEllipseItem(tables[i].x+1+add,tables[i].y+1,20,20)
                brush = QBrush()
                brush.setColor(QColor('white'))
                brush.setStyle(Qt.BrushStyle.SolidPattern)
                bubble2.setBrush(brush)
                img2 = self.scene.addPixmap(QPixmap("./brickwall.png"))
                img2.setPos(tables[i].x+3+add,tables[i].y+3)


            group = GroupView(i,self.tableController,room)
            group.addToGroup(item)
            group.addToGroup(text)
            if tables[i].exponent and tables[i].exponent.endOfTable:
                group.addToGroup(bubble)
                group.addToGroup(img)
            if tables[i].exponent and tables[i].exponent.nextWall:
                group.addToGroup(bubble2)
                group.addToGroup(img2)            

            if tables[i].exponent and (self.displayExponent == None or self.displayExponent.id == tables[i].exponent.id):
                textLastname = tables[i].exponent.lastname
                textFistname = tables[i].exponent.firstname
                text1 = QGraphicsSimpleTextItem(textLastname)
                text2 = QGraphicsSimpleTextItem(textFistname)
                font = QFont()
                font.setPixelSize(12)
                font.setBold(False)
                text1.setFont(font)
                text2.setFont(font)
                if tables[i].orientation == "Vertical" :
                    if(tables[i].side == "left"):
                        text1.setX(new_x+tables[i].tableGroup.width*multiplier-40-multiplier)
                        text2.setX(new_x+tables[i].tableGroup.width*multiplier-40-multiplier)
                    else:
                        text1.setX(new_x+tables[i].tableGroup.width*multiplier+10)
                        text2.setX(new_x+tables[i].tableGroup.width*multiplier+10)
                    text1.setY(new_y)
                    text2.setY(new_y+20)
                else:
                    text1.setX(new_x)
                    text2.setX(new_x)
                    if(tables[i].side == "left"):
                        text1.setY(new_y+tables[i].tableGroup.width*multiplier-10-multiplier)
                        text2.setY(new_y+tables[i].tableGroup.width*multiplier-30-multiplier)
                    else:
                        text1.setY(new_y+tables[i].tableGroup.width*multiplier+10)
                        text2.setY(new_y+tables[i].tableGroup.width*multiplier+30)
                group.addToGroup(text1)
                group.addToGroup(text2)
            self.scene.addItem(group)
            

    
    # def resizeEvent(self, event):
        # super().resizeEvent(event)

class DrawerView(QWidget):
    keyPressed = pyqtSignal()

    def __init__(self,store,tableController,tableLineController,doorController,unusableSpaceController,zoneController,platformController):
        super().__init__()
        self.views = []
        tab = QTabWidget(self)
        if(store.getSelectedProject() != None):
            rooms = store.getSelectedProject().rooms
        else:
            rooms = []
        for i in range(0,len(rooms),1):
            room_page = QWidget(self)
            room = rooms[i]
            self.view = Viewport(self,store,tableController,tableLineController,doorController,room,unusableSpaceController,zoneController,platformController)
            self.views.append(self.view)
            gridLayout = QGridLayout()
            gridLayout.addWidget(self.view, 0, 0, 1, 1)
            room_page.setLayout(gridLayout)
            tab.addTab(room_page, room.getName())
        
        mainLayout = QGridLayout(self)
        self.setLayout(mainLayout)
        mainLayout.addWidget(tab)
        self.keyPressed.connect(self.keyPressEvent)


    def keyPressEvent(self, e):  
        if e.key() == Qt.Key.Key_F11.value:
            if self.view.isMaximized():
                self.view.showNormal()
            else:
                self.view.showMaximized()

    def getViews(self,):
        return self.views
    
    def getScene(self,):
        return self.view.scene

