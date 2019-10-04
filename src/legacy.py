import pygame
import os
import sys

def main():
	# Read args
	argumentDict = parseArguments(sys.argv)

	# Renders help before exiting
	# TODO - replace with actual help. Maybe keep Ragnarok reference as easter egg deal? 
	if argumentDict["renderHelp"] == True:
		print("GET HELP!")
		print("My brother, he's hurt!")
		print("Help him!")
		print("*Throws brother*")
		return

	# Exit if we recieve an error
	elif argumentDict["error"] != None:
		print(argumentDict["error"])
		return

	filepath = ""
	characterName = ""
	characterGame = ""

	if argumentDict["filepath"] != None:
		filepath = argumentDict["filepath"]

	if argumentDict["characterName"] != None:
		characterName = argumentDict["characterName"]

	if argumentDict["characterGame"] != None:
		characterGame = argumentDict["characterGame"]

	# TODO - make this loop, unless we have more than one argument
	while(True):
		image = getImage(filepath)
		
		if(characterName == ''):
			characterName = getFilePart("character name")

		if(characterGame == ''):
			characterGame = getFilePart("character game")

		sheetType = determineImageType(image)
		
		targetFile = buildFilename(sheetType, characterName, characterGame)

		croppedImage = yank(image, sheetType)

		# TODO - add option to overwrite or save to a new file
		pygame.image.save(croppedImage, targetFile)

		return

	# print(argumentDict)
	# return
	# print(sys.argv)
	# if(len(sys.argv) == 1):
	# 	print("A spritesheet filename is required.")
	# 	return

	# if(len(sys.argv) >= 2):
	# 	filename = sys.argv[1]

	# 	if(filename == "--help"):
	# 		print("To do - Help")
	# 		return

	# outputName = ""
	# if(len(sys.argv) >= 3):
	# 	outputName = sys.argv[2]

	# # Load sprite
	# if(os.path.isfile(filename) == False):
	# 	print("The given file '" + filename + "' doesn't exist.")
	# 	return

	# spritesheet = pygame.image.load(filename)
	# yankFunction = determineImageType(spritesheet)

	# if(yankFunction == "profile"):
	# 	sprite = yankFace(spritesheet)
	
	# else:
	# 	sprite = yankSprite(spritesheet)

	# if(outputName == ""):
	# 	outputName = yankFunction + '.png'

	# pygame.image.save(sprite, outputName)


	# Create subsurface
	# Save sprite (do not overwrite)

def getFilePart(requestText):
	# TODO - add character checking. 
	name = 	input("Enter the " + requestText + ": ")
	return name

def yank(image, sheetType):
	if(sheetType == "profile"):
		return yankFace(image)
	
	else:
		return yankSprite(image)

def buildFilename(sheetType, characterName, characterGame):
	# waals_fate_profile
	filename = ""
	if characterName != "":
		filename += characterName + "_"

	if characterGame != "":
		filename += characterGame + "_"

	filename += sheetType + ".png"
	print(filename)
	return filename

def getImage(filepath):
	"""
	Loads the image and returns it
	"""
	# TODO - handle missing files better (loop and ask for input)
	if(os.path.isfile(filepath) == False):
		print("Error: The given file '" + filepath + "' doesn't exist.")
		sys.exit()

	return pygame.image.load(filepath)

def parseArguments(argValues):
	# Easily parsable struct for determining which actions to take after returning
	readableValuesDict = {
		"renderHelp":False,
		"characterName":None,
		"characterGame":None,
		"filepath":None,
		"sheetType":None,
		"error":None
	}

	# Patterns the inputs may match
	patterns = [
		["filepath"],
		["filepath", "characterName"],
		["filepath", "characterName", "characterGame"]
	]

	# Dict for easily identifying and parsing flags. Can be later stuffed into a JSON file
	flags = {
		"--help":{
			"next":None,
			"set":{"renderHelp": True}
		},
		"-h":{
			"next":None,
			"set":{"renderHelp": True}
		},
		"--name":{
			"next":"characterName",
			"set":{}
		},
		"--game":{
			"next":"characterGame",
			"set":{}
		},
		"--file":{
			"next":"filepath",
			"set":{}
		},
		"--sheetType":{
			"next":"sheetType",
			"set":{}
		}
	}

	nextKey = None

	argCount = len(argValues) # The number of values

	# Does pattern match?
	matchingPattern = None
	for pattern in patterns:
		if len(pattern) + 1 != argCount:
			continue

		# Set the matching pattern off the bat and remove if it doesn't match
		# TODO - handle this better, maybe a boolean flag? 
		matchingPattern = pattern

		# Loop through all arguments
		for i in range(1, argCount):
			value = argValues[i]

			# Patterns don't accept flags. Exit if one is found
			if value in flags:
				matchingPattern = None
				break

		# Stop looping if a matching pattern is found
		if matchingPattern != None:
			break

	# Parse the pattern if a matching pattern is found
	if matchingPattern != None:
		for i in range(1, argCount):
			readableValuesDict[matchingPattern[i-1]] = argValues[i]

		return readableValuesDict
		
	# Loop through by index to utilize default patterns
	# Start at 1 since first arg is always program
	for i in range(1, argCount):
		value = argValues[i]

		# If the previous key indicates what this value is
		if nextKey != None:
			readableValuesDict[nextKey] = value
			nextKey = None
			continue

		# If this argument is a flag
		elif value in flags:
			flag = flags[value]

			# Sets the next key
			nextKey = flag["next"]

			# Loops through all set flags (if any) and sets them in the readable
			for key in flag["set"]:
				readableValuesDict[key] = flag["set"][key]

		# If we don't know what this is
		else:
			readableValuesDict["error"] = "There was an error parsing your input string starting at '" + value + "'."
			break 

	return readableValuesDict

def determineImageType(spritesheet):
	"""
	Determines which function we should use for yanking the image, since the 
	different kinds of spritesheets have different sizes

	arg spritesheet - the image passed in by the user

	Returns the type of image
	"""
	size = spritesheet.get_size()

	if(size[0] == 576 and size[1] == 384):
		return "sprite"

	if(size[0] == 576 and size[1] == 288):
		return "profile"

	return "sprite"


def parseArgs():
	"""
	Parses arguments into specific categories

	TODO!!
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
