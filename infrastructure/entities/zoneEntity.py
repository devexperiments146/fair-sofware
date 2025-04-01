
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from infrastructure.entities.base import Base

from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from infrastructure.entities.roomEntity import RoomEntity

from infrastructure.entities.projectEntity import ProjectEntity

class ZoneEntity(Base):
    __tablename__ = "zone"
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"),primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"), nullable=True)
    room: Mapped[RoomEntity] = relationship(
        lazy="joined"
    )
    name : Mapped[str] = mapped_column(String(50))
    x : Mapped[float]
    y : Mapped[float]
    reelX : Mapped[float]
    reelY : Mapped[float]
    width : Mapped[float]
    length : Mapped[float]

    def __init__(self,project_id,id,name,room_id,x,y,reelX,reelY,width,length):
        self.project_id = project_id
        self.id = id
        self.name = name
        self.room_id = room_id
        self.x = x
        self.y = y
        self.reelX = reelX
        self.reelY = reelY
        self.width = width
        self.length = length

    def __repr__(self):
        return "Zone(%r)" %  (self.name)
