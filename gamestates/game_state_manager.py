from settings import *
from entities.player import Player
from handlers.input import InputHandler
from gamestates.states import *

import pygame
import gamestates

from gamestates.hums_state import HumsState
from gamestates.hums_inn_state import HumsInnState

class GameStateManager():

	def __init__(self):
		pygame.init()
		pygame.display.set_mode([WIDTH, HEIGHT])
		pygame.display.set_caption("Pygame Tilebased RPG")
		pygame.key.set_repeat(100)
		self.current_state = HUMS_STATE
		self.input_handler = InputHandler()
		self.states = self.create_states()
		self.player = Player(self, 18, 18, 100, 5, 5)
		self.walls = self.states[self.current_state].walls
		self.doors = self.states[self.current_state].doors
		self.npcs = self.states[self.current_state].npcs

	def update(self):
		self.draw_grid()
		self.draw_map()
		self.player.update()
		self.player.draw()

	def change_state(self, state):
		self.current_state = state
		self.walls = self.states[self.current_state].walls
		self.doors = self.states[self.current_state].doors
		self.npcs  = self.states[self.current_state].npcs

	def create_states(self):
		states = [None] * NUM_STATES
		states[HUMS_STATE] = HumsState(self)
		states[HUMS_INN_STATE] = HumsInnState(self)
		return states

	def draw_grid(self):
		for x in range(0, WIDTH, TILESIZE):
			pygame.draw.line(pygame.display.get_surface(), LIGHTGREY, (x, 0), (x, HEIGHT))

		for y in range(0, HEIGHT, TILESIZE):
			pygame.draw.line(pygame.display.get_surface(), LIGHTGREY, (0, y), (WIDTH, y))

	def draw_map(self):
		for x in range(len(self.walls)):
			self.walls[x].update()
			self.walls[x].draw(RED)
		for x in range(len(self.doors)):
			self.doors[x].update()
			self.doors[x].draw(BLUE)
		for x in range(len(self.npcs)):
			self.npcs[x].update()
			self.npcs[x].draw()

	def clear_screen(self):
		pygame.display.get_surface().fill((0, 0, 0))