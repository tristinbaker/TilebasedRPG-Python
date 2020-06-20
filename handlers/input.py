import pygame
from settings import *

class InputHandler:

	def __init__(self):
		pass

	def handle_input(self, event, player):
		dx = 0
		dy = 0
		direction = player.direction 
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_w:
				direction = NORTH
				dy = -MOVEMENT_FACTOR
			if event.key==pygame.K_s:
				direction = SOUTH
				dy = MOVEMENT_FACTOR
			if event.key==pygame.K_a:
				direction = WEST
				dx = -MOVEMENT_FACTOR
			if event.key==pygame.K_d:
				direction = EAST
				dx = MOVEMENT_FACTOR
			if event.key==pygame.K_SPACE:
				player.check_dialog()
			if event.key==pygame.K_i:
				player.show_inventory()
		if event.type == pygame.KEYUP:
			if event.key==pygame.K_w:
				dy = 0
			if event.key==pygame.K_s:
				dy = 0
			if event.key==pygame.K_a:
				dx = 0
			if event.key==pygame.K_d:
				dx = 0
			if event.key==pygame.K_SPACE:
				pass
			if event.key==pygame.K_i:
				pass
		player.update_direction(direction)
		player.move(dx, dy)
