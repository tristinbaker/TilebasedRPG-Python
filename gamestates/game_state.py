from settings import *
from entities.wall import Wall
from entities.door import Door
from entities.npc  import NPC

class GameState():

	def __init__(self, gsm):
		self.gsm = gsm 

	def initialize_state(self, walls, doors, entrances, npcs):
		self.walls = self.set_walls(walls)
		self.doors = self.set_doors(walls, doors, entrances)
		self.npcs  = self.set_npcs(npcs)

	def set_walls(self, walls):
		wall_array = []
		for x in range(int(WIDTH / TILESIZE)):
			for y in range(int(HEIGHT / TILESIZE)):
				if walls[y][x] == 1:
					wall_array.append(Wall(self.gsm, x, y))
		return wall_array

	def set_doors(self, walls, doors, entrances):
		door_array = []
		door = 0
		for x in range(int(WIDTH / TILESIZE)):
			for y in range(int(HEIGHT / TILESIZE)):
				if walls[y][x] == 2:
					door_array.append(Door(self.gsm, x, y, doors[door], entrances[door][0], entrances[door][1]))
					door += 1
		return door_array

	def set_npcs(self, npcs):
		npc_array = []
		for npc, stats in npcs.items():
			npc_array.append(NPC(self.gsm, npc, stats["x"], stats["y"], stats["direction"], stats["hail_range"]))
		return npc_array
		