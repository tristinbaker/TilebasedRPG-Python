import sys

import pygame
from settings import * 
from handlers.game import Game
from entities.player import Player
from handlers.dialog import DialogHandler

game = Game('hums')
player = Player(game, 18, 18, NORTH)

input_handler = game.input_handler

while True:
	game.clear_screen()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		input_handler.handle_input(event, player)
	
	game.draw_grid()
	game.update_map()
	game.draw_map()
	player.update()
	player.draw()

	pygame.display.flip()