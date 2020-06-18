import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	
	def __init__(self, game, x, y):
		self.x = x
		self.y = y
		self.game = game
		self.dx = 0
		self.dy = 0
		self.rect = pygame.Rect(x, y, WIDTH / TILESIZE, WIDTH / TILESIZE)

	def draw(self):
		pygame.draw.rect(pygame.display.get_surface(), GREEN, self.rect) 

	def update_position(self, x, y):
		self.x = x
		self.y = y

	def move(self, dx, dy):
		self.dx = dx
		self.dy = dy
		temp_x = self.x
		self.x += self.dx
		temp_y = self.y
		self.y += self.dy
		self.check_collision(temp_x, temp_y)

	def update(self):
		self.rect.x = self.x * TILESIZE
		self.rect.y = self.y * TILESIZE	

	def check_collision(self, tx, ty):
		self.check_boundaries()
		self.check_walls(tx, ty)
		self.check_doors()

	def check_boundaries(self):
		if self.x < 0:
			self.x = 0
		elif self.x > (WIDTH - TILESIZE) / TILESIZE:
			self.x = (WIDTH - TILESIZE) / TILESIZE
		if self.y < 0: 
			self.y = 0
		elif self.y > (HEIGHT - TILESIZE) / TILESIZE:
			self.y = (HEIGHT - TILESIZE) / TILESIZE

	def check_walls(self, tx, ty):
		walls = self.game.walls
		for i in range(len(walls)):
			if self.x == walls[i].x and self.y == walls[i].y:
				self.x = tx
				self.y = ty

	def check_doors(self):
		doors = self.game.doors
		for i in range(len(doors)):
			if self.x == doors[i].x and self.y == doors[i].y:
				self.game.map_handler.change_map(doors[i].exit)
				self.update_position(doors[i].entrance_x, doors[i].entrance_y)