import pygame
from entities.entity import Entity
from settings import *

class NPC(Entity):

	def __init__(self, gsm, name, x, y, direction, hail_range=1):
		self.gsm = gsm
		self.x = x
		self.y = y
		self.name = name
		self.direction = direction
		self.hail_range = hail_range
		self.text = 'Hello traveller!'
		self.image = pygame.image.load('res/sprites/player/player.png')
		self.rect = pygame.Rect(x, y, WIDTH / TILESIZE, WIDTH / TILESIZE)