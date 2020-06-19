import pygame
from handlers.input import InputHandler
from handlers.map import MapHandler
from settings import * 

class Game:

	def __init__(self, map):
		pygame.init()
		pygame.display.set_mode([WIDTH, HEIGHT])
		pygame.display.set_caption("Pygame Tilebased RPG")
		pygame.key.set_repeat(100)
		self.input_handler = InputHandler()
		self.map_handler = MapHandler(map)
		self.walls = self.map_handler.map.walls
		self.doors = self.map_handler.map.doors
		self.npcs = self.map_handler.map.npcs

	def draw_grid(self):
		for x in range(0, WIDTH, TILESIZE):
			pygame.draw.line(pygame.display.get_surface(), LIGHTGREY, (x, 0), (x, HEIGHT))

		for y in range(0, HEIGHT, TILESIZE):
			pygame.draw.line(pygame.display.get_surface(), LIGHTGREY, (0, y), (WIDTH, y))

	def clear_screen(self):
		pygame.display.get_surface().fill((0, 0, 0))

	def set_walls(self, walls):
		self.walls = walls

	def set_doors(self, doors):
		self.doors = doors

	def set_npcs(self, npcs):
		self.npcs = npcs

	def update_map(self):
		self.set_walls(self.map_handler.map.walls)
		self.set_doors(self.map_handler.map.doors)
		self.set_npcs(self.map_handler.map.npcs)

	def draw_map(self):
		for x in range(len(self.walls)):
			self.walls[x].update()
			self.walls[x].draw(RED)
		for x in range(len(self.doors)):
			self.doors[x].update()
			self.doors[x].draw(BLUE)
		for x in range(len(self.npcs)):
			self.npcs[x].update()
			self.npcs[x].draw()
