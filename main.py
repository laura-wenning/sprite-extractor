import pygame # Used for extracting the sprite easily with built-in surfaces 
import os
import sys 

def main():
	# Read args
	print(sys.argv)
	if(len(sys.argv) == 1):
		print("A spritesheet filename is required.")
		return

	if(len(sys.argv) >= 2):
		filename = sys.argv[1]

		if(filename == "--help"):
			print("To do - Help")
			return

	outputName = ""
	if(len(sys.argv) >= 3):
		outputName = sys.argv[2]

	# Load sprite
	if(os.path.isfile(filename) == False):
		print("The given file '" + filename + "' doesn't exist.")
		return

	spritesheet = pygame.image.load(filename)
	yankFunction = determineYankFunction(spritesheet)

	if(yankFunction == "face"):
		sprite = yankFace(spritesheet)
	
	else:
		sprite = yankSprite(spritesheet)

	if(outputName == ""):
		outputName = yankFunction + '.png'

	pygame.image.save(sprite, outputName)


	# Create subsurface
	# Save sprite (do not overwrite)

def determineYankFunction(spritesheet):
	size = spritesheet.get_size()
	# print(size)
	# print(size[0])

	if(size[0] == 576 and size[1] == 384):
		return "sprite"

	if(size[0] == 576 and size[1] == 288):
		return "face"

	return "sprite"


def parseArgs():
	"""
	Parses arguments into specific categories
	"""

	state = 1
	



	arguments = {
		outputFile:"output.png",
		spriteFile:"",
		faceFile:"",
		fileName:"",
		printHelp:False
	}

	return 
	

def yankSprite(spritesheet):
	"""
	Yanks and isolates the face from the RPG generator output

	arg faceimage - the image containing the face

	Returns the subsurface of the face
	"""
	# Error checking?
	return spritesheet.subsurface(48, 0, 48, 48)

def yankFace(faceimage):
	"""
	Yanks and isolates the face from the RPG generator output

	arg faceimage - the image containing the face

	Returns the subsurface of the face
	"""
	# Error checking?
	return faceimage.subsurface(0, 0, 144, 144)


main()