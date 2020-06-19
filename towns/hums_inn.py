from maps.hums_inn_map import *
from towns.inn import Inn
from settings import * 

class HumsInn(Inn):

	def __init__(self):
		self.walls = self.set_walls(walls)
		self.doors = self.set_doors(walls, doors, entrances)
		self.npcs = self.set_npcs(npcs)