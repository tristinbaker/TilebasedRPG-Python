import pygame
from settings import *

class Entity(pygame.sprite.Sprite):

	def __init__(self, gsm, x, y):
		self.gsm = gsm
		self.x = x
		self.y = y
		self.image = pygame.image.load('res/sprites/player/player.png')
		self.rect = pygame.Rect(x, y, WIDTH / TILESIZE, WIDTH / TILESIZE)

	def draw(self):
		self.gsm.SURFACE.blit(self.image, self.rect)

	def update(self):
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE	

	def update_position(self, x, y):
		self.x = x
		self.y = y

	def update_direction(self, direction):
		self.direction = direction