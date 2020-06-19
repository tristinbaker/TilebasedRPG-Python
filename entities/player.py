from entities.entity import Entity
from settings import *

import pygame

class Player(Entity):
	
	def __init__(self, game, x, y, direction):
		self.game = game
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.direction = NORTH
		self.rect = pygame.Rect(x, y, WIDTH / TILESIZE, WIDTH / TILESIZE)

	def draw(self):
		pygame.draw.rect(pygame.display.get_surface(), GREEN, self.rect) 

	def move(self, dx, dy):
		self.dx = dx
		self.dy = dy
		temp_x = self.x
		self.x += self.dx
		temp_y = self.y
		self.y += self.dy
		self.check_collision(temp_x, temp_y)

	def check_collision(self, tx, ty):
		self.check_boundaries()
		self.check_walls(tx, ty)
		self.check_doors()
		self.check_npcs(tx, ty)

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

	def check_npcs(self, tx, ty):
		npcs = self.game.npcs
		for i in range(len(npcs)):
			if self.x == npcs[i].x and self.y == npcs[i].y:
				self.x = tx 
				self.y = ty 

	def check_dialog(self):
		npcs = self.game.npcs
		for i in range(len(npcs)):
			if self.direction == NORTH:
				if self.x == npcs[i].x and self.y - 1 == npcs[i].y:
					print(npcs[i].text)
			elif self.direction == WEST: 
				if self.x - 1 == npcs[i].x and self.y == npcs[i].y:
					print(npcs[i].text)
			elif self.direction == SOUTH:
				if self.x == npcs[i].x and self.y + 1 == npcs[i].y:
					print(npcs[i].text)
			elif self.direction == EAST:
				if self.x + 1 == npcs[i].x and self.y == npcs[i].y:
					print(npcs[i].text)

