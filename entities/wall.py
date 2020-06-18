import pygame
from settings import *

class Wall(pygame.sprite.Sprite): 

	def __init__(self, x, y):
		self.x = x
		self.y = y 
		self.rect = pygame.Rect(x, y, WIDTH / TILESIZE, WIDTH / TILESIZE)

	def update(self):
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE

	def draw(self, color):
		pygame.draw.rect(pygame.display.get_surface(), color, self.rect)