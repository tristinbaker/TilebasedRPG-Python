import pygame
from settings import *

class Entity(pygame.sprite.Sprite):

	def __init__(self, game, x, y):
		self.game = game
		self.x = x
		self.y = y
		self.rect = pygame.Rect(x, y, WIDTH / TILESIZE, WIDTH / TILESIZE)

	def update(self):
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE	

	def update_position(self, x, y):
		self.x = x
		self.y = y

	def update_direction(self, direction):
		self.direction = direction