
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from infrastructure.entities.base import Base

class ParameterEntity(Base):
    __tablename__ = "parameter"
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name : Mapped[str] = mapped_column(String(50))
    value : Mapped[str] = mapped_column(String(50))

    def __init__(self, name,value):
        self.name = name
        self.value = value

    def __repr__(self):
        return "Parameter(%r)" % (self.name)
