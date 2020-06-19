from maps import map_list

class MapHandler:

	def __init__(self, map):
		self.map_list = self.set_map_list()
		self.map = self.map_list[map]

	def change_map(self, map):
		self.map = self.map_list[map]

	def set_map_list(self):
		return map_list.map_list