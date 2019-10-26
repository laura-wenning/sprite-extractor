# TODO - remove PyGame and handle image extraction using a lighter library or on our own
import pygame # Used for extracting the sprite easily with built-in surfaces 
import os
import sys 

import src.core as core
import src.io as io
import src.legacy as legacy

def main():
	# Handles case where we want to use the legacy functionality (drag and drop)
	if len(sys.argv) >= 2:
		legacy.main()
		return
	
	# Load config
	config = io.readConfig()

	# Load history
	history = io.readHistory()

	while(True):
		userInput = input("> ")

		userInput = userInput.lower()
		print("user input:", userInput)

		if userInput == "quit":
			print("Thanks for using the Sprite Extractor")
			sys.exit()

		elif userInput == "run":
			history = core.run(history, config)
			print("Ran")

		elif userInput == "help":
			print("GET HELP!")
			print("My brother, he's hurt!")
			print("Help him!")
			print("*Throws brother*")

		else:
			print("Invalid command", userInput)

	return 

main()