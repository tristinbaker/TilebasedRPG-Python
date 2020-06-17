import sys

import pygame
from settings import * 
from handlers.game import Game
from entities.player import Player
from towns.hums import Hums

game = Game()
player = Player(game, 5, 8)

walls = Hums().walls
doors = Hums().doors
game.set_walls(walls)
game.set_doors(doors)
input_handler = game.input_handler

while True:
	game.clear_screen()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		input_handler.handle_input(event, player)
	
	game.draw_grid()
	game.draw_map()
	player.update()
	player.draw()

	pygame.display.flip()