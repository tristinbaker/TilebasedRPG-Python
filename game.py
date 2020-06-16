import pygame
from wall import Wall
from settings import * 

class Game:

	def __init__(self):
		pygame.init()
		pygame.display.set_mode([WIDTH, HEIGHT])
		pygame.display.set_caption("Pygame Tilebased RPG")
		pygame.key.set_repeat(100)

	def draw_grid(self):
		for x in range(0, WIDTH, TILESIZE):
			pygame.draw.line(pygame.display.get_surface(), LIGHTGREY, (x, 0), (x, HEIGHT))

		for y in range(0, HEIGHT, TILESIZE):
			pygame.draw.line(pygame.display.get_surface(), LIGHTGREY, (0, y), (WIDTH, y))

	def clear_screen(self):
		pygame.display.get_surface().fill((0, 0, 0))

	def set_walls(self):
		self.walls = []
		for x in range(10, 15):
			self.walls.append(Wall(x, 10))

	def draw_walls(self):
		for x in range(len(self.walls)):
			self.walls[x].update()
			self.walls[x].draw()