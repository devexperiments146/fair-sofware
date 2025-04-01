
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from sqlalchemy.orm import DeclarativeBase

from infrastructure.entities.tableGroupEntity import TableGroupEntity
from infrastructure.entities.roomEntity import RoomEntity
from infrastructure.entities.exponentEntity import ExponentEntity

from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column



from infrastructure.entities.base import Base


class UnusableSpaceEntity(Base):
    __tablename__ = "unused_space"
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"),primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    x : Mapped[float]
    y : Mapped[float]
    reelX : Mapped[float]
    reelY : Mapped[float]
    width : Mapped[float]
    length: Mapped[float]
    orientation: Mapped[str] = mapped_column(String(30))
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
    room: Mapped[RoomEntity] = relationship(lazy="joined")

    def __init__(self,project_id,id,name, x, y,width,length,reelX,reelY,orientation,room_id):
        self.project_id = project_id
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.reelX = reelX
        self.reelY = reelY
        self.orientation = orientation
        self.room_id = room_id

    def __repr__(self):
        return "Table(%r)" % (self.name)

