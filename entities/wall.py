from settings import *
from entities.entity import Entity
import pygame

class Wall(Entity): 

	def __init__(self, gsm, x, y):
		self.gsm = gsm
		self.x = x
		self.y = y 
		self.rect = pygame.Rect(x, y, WIDTH / TILESIZE, WIDTH / TILESIZE)
		self.image = pygame.image.load('res/sprites/walls/wall.png')

	def draw(self, color):
		self.gsm.SURFACE.blit(self.image, self.rect)