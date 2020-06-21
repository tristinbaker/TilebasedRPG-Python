import sys

import pygame
from settings import * 
from gamestates.game_state_manager import GameStateManager 

gsm = GameStateManager()

while True:
	gsm.clear_screen()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		gsm.input_handler.handle_input(event, gsm.player)
	
	gsm.update()

	pygame.display.flip()