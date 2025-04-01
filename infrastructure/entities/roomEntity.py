
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import String
from typing import List

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from infrastructure.entities.base import Base

from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class RoomEntity(Base):
    __tablename__ = "room"
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"),primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(50))
    x : Mapped[float]
    y : Mapped[float]
    width : Mapped[float]
    length : Mapped[float]
    project: Mapped["ProjectEntity"] = relationship(back_populates="rooms")


    def __init__(self,project_id,id,name,x,y,width,length):
        self.project_id = project_id
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.length = length

    def __repr__(self):
        return "Room(%r)" % (self.name)
