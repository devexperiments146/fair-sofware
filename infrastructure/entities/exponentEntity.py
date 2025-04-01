
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

from infrastructure.entities.projectEntity import ProjectEntity

class ExponentEntity(Base):
    __tablename__ = "exponent"
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"),primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname : Mapped[str] = mapped_column(String(50))
    lastname : Mapped[str] = mapped_column(String(50))
    date : Mapped[str] = mapped_column(String(50), nullable=True)
    tableType : Mapped[str] = mapped_column(String(50), nullable=True)
    description : Mapped[str] = mapped_column(String(300), nullable=True)
    project: Mapped["ProjectEntity"] = relationship(back_populates="exponents")
    
    room_choice_id: Mapped[int] = mapped_column(ForeignKey("room.id"), nullable=True)
    next_door_id: Mapped[int] = mapped_column(ForeignKey("door.id"), nullable=True)
    next_exponent_id: Mapped[int] = mapped_column(ForeignKey("exponent.id"), nullable=True)
    table_line_choice_id: Mapped[int] = mapped_column(ForeignKey("table_line.id"), nullable=True)
    table_line_position : Mapped[str] = mapped_column(Integer(), nullable=True)

    next_wall: Mapped[bool] = mapped_column(Boolean(), nullable=True)
    end_of_table: Mapped[bool] = mapped_column(Boolean(), nullable=True)

    def __init__(self,project_id,id,firstname,lastname,date = None,tableType = None,description = None):
        self.project_id = project_id
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.date = date
        self.tableType = tableType
        self.description = description

    def __repr__(self):
        return "Exponent(%r)" %  (self.lastname)
