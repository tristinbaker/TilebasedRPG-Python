from entities.entity import Entity
from entities.inventory import Inventory
from settings import *

import pygame

class Player(Entity):
	
	def __init__(self, gsm, x, y, hp, strength, defense):
		self.gsm = gsm
		self.hp = 100
		self.strength = strength 
		self.defense = defense 
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.direction = NORTH
		self.rect = pygame.Rect(x, y, WIDTH / TILESIZE, WIDTH / TILESIZE)
		self.inventory = Inventory({"Sword": 1, "Shield": 1})
		self.image = pygame.image.load('res/sprites/player/player-south.png')

	def move(self, dx, dy):
		self.dx = dx
		self.dy = dy
		temp_x = self.x
		self.x += self.dx
		temp_y = self.y
		self.y += self.dy
		self.check_collision(temp_x, temp_y)

	def show_inventory(self):
		for item, count in self.inventory.items.items():
			print(item + ' ' + str(count))

	def update_sprite(self):
		if self.direction == SOUTH:
			self.image = pygame.image.load('res/sprites/player/player-south.png')
		elif self.direction == NORTH:
			self.image = pygame.image.load('res/sprites/player/player-north.png')
		elif self.direction == WEST:
			self.image = pygame.image.load('res/sprites/player/player-west.png')
		elif self.direction == EAST:
			self.image = pygame.image.load('res/sprites/player/player-east.png')

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
		walls = self.gsm.states[self.gsm.current_state].walls
		for i in range(len(walls)):
			if self.x == walls[i].x and self.y == walls[i].y:
				self.x = tx
				self.y = ty

	def check_doors(self):
		doors = self.gsm.states[self.gsm.current_state].doors
		for i in range(len(doors)):
			if self.x == doors[i].x and self.y == doors[i].y:
				self.gsm.change_state(doors[i].exit)
				self.update_position(doors[i].entrance_x, doors[i].entrance_y)

	def check_npcs(self, tx, ty):
		npcs = self.gsm.states[self.gsm.current_state].npcs
		for i in range(len(npcs)):
			if self.x == npcs[i].x and self.y == npcs[i].y:
				self.x = tx 
				self.y = ty 

	def check_dialog(self):
		npcs = self.gsm.states[self.gsm.current_state].npcs
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

