
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

from sqlalchemy.orm import Mapped
from sqlalchemy import String
from sqlalchemy.orm import mapped_column

from infrastructure.entities.base import Base

from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

from infrastructure.entities.projectEntity import ProjectEntity

class TableGroupEntity(Base):
    __tablename__ = "table_group"
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"),primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    width : Mapped[float]
    length : Mapped[float]
    color : Mapped[str] = mapped_column(String(50))
    maxQuantity : Mapped[int]
    tableType : Mapped[str] = mapped_column(String(50), nullable=True)
    project: Mapped["ProjectEntity"] = relationship(back_populates="tableGroups")
    

    def __init__(self,project_id, id, width,length,color,maxQuantity,tableType = None):
        self.project_id = project_id
        self.id = id
        self.width = width
        self.length = length
        self.color = color
        self.maxQuantity = maxQuantity
        self.tableType = tableType
