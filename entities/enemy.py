from entities.entity import Entity
from settings import *

class Enemy(Entity):

	def __init__(self, game, x, y, name, strength, defense):
		self.game = game
		self.x = x 
		self.y = y
		self.name = name 
		self.strength = strength 
		self.defense = defense 
