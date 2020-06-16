import pygame
from settings import *

class InputHandler:

	def __init__(self):
		pass

	def handle_input(self, event, player):
		dx = 0
		dy = 0
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_w:
				dy = -MOVEMENT_FACTOR
			if event.key==pygame.K_s:
				dy = MOVEMENT_FACTOR
			if event.key==pygame.K_a:
				dx = -MOVEMENT_FACTOR
			if event.key==pygame.K_d:
				dx = MOVEMENT_FACTOR
		if event.type == pygame.KEYUP:
			if event.key==pygame.K_w:
				dy = 0
			if event.key==pygame.K_s:
				dy = 0
			if event.key==pygame.K_a:
				dx = 0
			if event.key==pygame.K_d:
				dx = 0
		player.move(dx, dy)
