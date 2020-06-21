import pygame

from entities.wall import Wall
from settings import *

class Door(Wall):

	def __init__(self, gsm, x, y, exit, entrance_x, entrance_y):
		self.gsm = gsm
		self.x = x
		self.y = y
		self.entrance_x = entrance_x
		self.entrance_y = entrance_y
		self.rect = pygame.Rect(x, y, WIDTH / TILESIZE, WIDTH / TILESIZE)
		self.image = pygame.image.load('res/sprites/doors/door.png')
		self.exit = exit
