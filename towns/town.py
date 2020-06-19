from entities.wall import Wall
from entities.door import Door
from entities.npc import NPC
from settings import *

class Town:

	def __init__(self):
		self.map = 0
		self.walls = set_walls(self.map)
		self.doors = set_doors(self.map)
		self.npcs = set_npcs(self.map)

	def set_walls(self, walls):
		wall_array = []
		for x in range(int(WIDTH / TILESIZE)):
			for y in range(int(HEIGHT / TILESIZE)):
				if walls[y][x] == 1:
					wall_array.append(Wall(x, y))
		return wall_array

	def set_doors(self, walls, doors, entrances):
		door_array = []
		door = 0
		for x in range(int(WIDTH / TILESIZE)):
			for y in range(int(HEIGHT / TILESIZE)):
				if walls[y][x] == 2:
					door_array.append(Door(x, y, doors[door], entrances[door][0], entrances[door][1]))
					door += 1
		return door_array

	def set_npcs(self, npcs):
		npc_array = []
		for x, y in npcs.items():
			npc_array.append(NPC(y[0], y[1], y[2], x))
		return npc_array
		