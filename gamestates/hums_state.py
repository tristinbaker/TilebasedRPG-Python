from maps.hums_map import *
from gamestates.game_state import GameState

class HumsState(GameState):

	def __init__(self, gsm):
		self.gsm = gsm 
		self.initialize_state(walls, doors, entrances, npcs)