
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from typing import List

from infrastructure.entities.base import Base


class ProjectEntity(Base):
    __tablename__ = "project"
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name : Mapped[str] = mapped_column(String(50))
    rooms: Mapped[List["RoomEntity"]] = relationship(back_populates="project")
    tableGroups: Mapped[List["TableGroupEntity"]] = relationship(back_populates="project")
    exponents: Mapped[List["ExponentEntity"]] = relationship(back_populates="project")
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Project(%r)" % (self.name)
