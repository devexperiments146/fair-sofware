
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
from infrastructure.entities.tableLineEntity import TableLineEntity

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from infrastructure.entities.base import Base

class TableEntity(Base):
    __tablename__ = "table"
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"),primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    x : Mapped[float]
    y : Mapped[float]
    reelX : Mapped[float]
    reelY : Mapped[float]
    orientation: Mapped[str] = mapped_column(String(30))
    side: Mapped[str] = mapped_column(String(5), nullable=True)
    table_group_id: Mapped[int] = mapped_column(ForeignKey("table_group.id"))
    tableGroup: Mapped[TableGroupEntity] = relationship(
        lazy="joined"
    )
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
    room: Mapped[RoomEntity] = relationship(
        lazy="joined"
    )
    exponent_id: Mapped[int] = mapped_column(ForeignKey("exponent.id"), nullable=True)
    exponent: Mapped[ExponentEntity] = relationship(
        lazy="joined"
    )
    table_line_id: Mapped[int] = mapped_column(ForeignKey("table_line.id"), nullable=True)

    def __init__(self, project_id,id,name, x, y,reelX,reelY,orientation,room_id):
        self.project_id = project_id
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.reelX = reelX
        self.reelY = reelY
        self.orientation = orientation
        self.room_id = room_id

    def __repr__(self):
        return "Table(%r)" % (self.name)


 