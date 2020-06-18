from maps.hums_map import walls
from maps.hums_map import doors
from maps.hums_map import entrances
from towns.town import Town
from settings import *

class Hums(Town):

	def __init__(self):
		self.walls = self.set_walls(walls)
		self.doors = self.set_doors(walls, doors, entrances)
