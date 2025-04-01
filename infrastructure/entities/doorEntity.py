
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from infrastructure.entities.roomEntity import RoomEntity

from infrastructure.entities.base import Base

class DoorEntity(Base):
    __tablename__ = "door"
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"),primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(50))
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
    room: Mapped[RoomEntity] = relationship(
        lazy="joined"
    )
    width : Mapped[float]
    x : Mapped[float]
    y : Mapped[float]
    reelX : Mapped[float]
    reelY : Mapped[float]
    orientation: Mapped[str] = mapped_column(String(30))
    def __init__(self,project_id,id,name,room_id,width, x, y,reelX,reelY,orientation):
        self.project_id = project_id
        self.id = id
        self.name = name
        self.room_id = room_id
        self.width = width
        self.x = x
        self.y = y
        self.reelX = reelX
        self.reelY = reelY
        self.orientation = orientation

    def __repr__(self):
        return "Door(%r)" % (self.name)

