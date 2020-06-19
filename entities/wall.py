from settings import *
from entities.entity import Entity
import pygame

class Wall(Entity): 

	def __init__(self, x, y):
		self.x = x
		self.y = y 
		self.rect = pygame.Rect(x, y, WIDTH / TILESIZE, WIDTH / TILESIZE)

	def draw(self, color):
		pygame.draw.rect(pygame.display.get_surface(), color, self.rect)