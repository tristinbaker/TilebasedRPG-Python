from maps.hums_inn_map import walls
from maps.hums_inn_map import doors
from maps.hums_inn_map import entrances
from towns.inn import Inn
from settings import * 

class HumsInn(Inn):

	def __init__(self):
		self.walls = self.set_walls(walls)
		self.doors = self.set_doors(walls, doors, entrances)