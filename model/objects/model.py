from room import Room
from door import Door
from exponent import Exponent
from table import Table
from tableGroup import TableGroup

class Model:
  def __init__(self):
    self.doors = []
    self.exponents = []
    self.selectedExponent : Exponent
    self.tableGroups = []
    self.selectedTableGroup : TableGroup
    self.tables = []
    self.selectedTable : Table
    self.rooms = []
    self.selectedRoom : Room