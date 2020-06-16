from settings import * 
from game import Game
from player import Player
from input import InputHandler
import pygame
import sys

game = Game()
player = Player(game, 5, 8)
input_handler = InputHandler()

game.set_walls()

while True:
	game.clear_screen()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()	
			sys.exit()
		input_handler.handle_input(event, player)
	
	game.draw_grid()
	game.draw_walls()
	player.update()
	player.draw()

	pygame.display.flip()