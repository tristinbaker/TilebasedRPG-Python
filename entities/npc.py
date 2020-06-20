import pygame
from entities.entity import Entity
from settings import *

class NPC(Entity):

	def __init__(self, x, y, direction, name):
		self.x = x
		self.y = y
		self.name = name
		self.direction = direction
		self.text = 'Hello traveller!'
		self.rect = pygame.Rect(x, y, WIDTH / TILESIZE, WIDTH / TILESIZE)


	def draw(self):
		pygame.draw.rect(pygame.display.get_surface(), WHITE, self.rect) 
