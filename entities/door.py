import pygame

from entities.wall import Wall
from settings import *

class Door(Wall):

	def __init__(self, x, y, exit):
		self.x = x
		self.y = y
		self.rect = pygame.Rect(x, y, WIDTH / TILESIZE, WIDTH / TILESIZE)
		self.exit = exit

	def draw(self):
		pygame.draw.rect(pygame.display.get_surface(), BLUE, self.rect)