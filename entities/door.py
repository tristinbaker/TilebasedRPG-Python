import pygame

from entities.wall import Wall
from settings import *

class Door(Wall):

	def __init__(self, x, y, exit, entrance_x, entrance_y):
		self.x = x
		self.y = y
		self.entrance_x = entrance_x
		self.entrance_y = entrance_y
		self.rect = pygame.Rect(x, y, WIDTH / TILESIZE, WIDTH / TILESIZE)
		self.exit = exit
