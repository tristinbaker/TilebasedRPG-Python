from maps.hums_inn_map import *
from gamestates.game_state import GameState

class HumsInnState(GameState):

	def __init__(self, gsm):
		self.gsm = gsm
		self.initialize_state(walls, doors, entrances, npcs)