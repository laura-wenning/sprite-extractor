from os import path, walk

import src.character as character

def run(history, config):
  """
  Runs the main function of going through each file, 
  seeing what needs updating, updating it, and returning 
  the resulting information

  param history - the previously altered information
  param config - the configuration data
  """
  # Read all folders from the config
  characterList = __listCharacters__(config)
  print(characterList)

  for char in characterList:
    char.print()
    char.processImages()
  # characterList = __processRXGCs__(characterList, config)
  # characterList = rawProcessor.processAll(characterList, config)

  return history

def __listCharacters__(config):
  """
  Generates a list of all characters with their 
  """
  characters = []
  # file: {lastTouched: [timestamp], processType: [raw, img, none]}
  if config["readFolders"] == None:
    return characters

  for folder in config["readFolders"]:
    for (dirpath, dirnames, filenames) in walk(folder):
      if __isCharacterFolder__(filenames) == False:
        continue

      # Extract target filename
      baseFilename = __getCharacterFilename__(filenames)
      newCharacter = character.Character(dirpath, baseFilename)
      
      characters.append(newCharacter)

  return characters
      

def __isCharacterFolder__(filenames):
  """
  Determines if this is a character folder by checking if there is a .rxgc file present
  Returns true if it is a character folder, false otherwise
  """
  return len(__getCharacterFilename__(filenames)) > 0

def __getCharacterFilename__(filenames):
  """
  Extracts the character filename from the rxgc file
  Returns the character name
  """
  for filename in filenames:
    if filename.find(".rxgc") != -1:
      return filename.replace(".rxgc", "")

  return ""

def __determineSteps__(dirpath, baseFilename, config):
  """
  Determines which files need to be re-exported and re-rendered

  param dirpath - the directory of the current rxgc
  param baseFilename - the base filename to build additional files
  param config - the config dict

  Returns a dict containing profile and sprite updates required
  """
  rxgcTime = path.getmtime(dirpath + "/" + baseFilename + ".rxgc")

  return (
    __determineProfileStep__(dirpath, baseFilename, rxgcTime, config),
    __determineSpriteStep__(dirpath, baseFilename, rxgcTime, config)
  )

def __determineProfileStep__(dirpath, baseFilename, rxgcTime, config):
  """
  Determines which step in the profile extraction process to start from

  param dirpath - the path of the current directory 
  param baseFilename - the base filename for building filenames
  param rxgcTime - the last edit time of the rxgc file
  param config - the config dict

  Returns the step
  """
  # Determines the last time the raw face image was edited
  rawFaceImageTime = None
  rawFaceImagePath = dirpath + "/raw/" + baseFilename + "_face.png"
  if path.isfile(rawFaceImagePath):
    rawFaceImageTime = path.getmtime(rawFaceImagePath)

  # Determines the last time the profile image was edited
  profileImageTime = None
  profileImagePath = dirpath + "/" + baseFilename + "_profile.png"
  if path.isfile(profileImagePath):
    profileImageTime = path.getmtime(profileImagePath)

  # If we need to export RXGC to images
  if __getRXGCStep__(rxgcTime, rawFaceImageTime, profileImageTime, config):
    return "rxgc"

  # If we need to process raw images
  elif __getRawStep__(rawFaceImageTime, profileImageTime):
    return "raw"

  return "none"

def __determineSpriteStep__(dirpath, baseFilename, rxgcTime, config):
  """
  Determines which step in the sprite extraction process to start from

  param dirpath - the path of the current directory 
  param baseFilename - the base filename for building filenames
  param rxgcTime - the last edit time of the rxgc file
  param config - the config dict

  Returns the step
  """
  # Determines the last time the raw character image was edited
  rawCharacterImageTime = None
  rawCharacterImagePath = dirpath + "/raw/" + baseFilename + "_character.png"
  if path.isfile(rawCharacterImagePath):
    rawCharacterImageTime = path.getmtime(rawCharacterImagePath)
  
  # Determines the last time the processed sprite was edited
  spriteImageTime = None
  spriteImagePath = dirpath + "/" + baseFilename + "_sprite.png"
  if path.isfile(spriteImagePath):
    spriteImageTime = path.getmtime(spriteImagePath)

  # If we need to export RXGC to images
  if __getRXGCStep__(rxgcTime, rawCharacterImageTime, spriteImageTime, config):
    return "rxgc"

  # If we need to process raw images
  elif __getRawStep__(rawCharacterImageTime, spriteImageTime):
    return "raw"

  return "none"

def __getRXGCStep__(rxgcTime, rawTime, processedTime, config):
  """
  Determines if we need to run the RXGC export step

  param rxgcTime - the last edit time of the rxgc file
  param rawTime - the last edit time of the raw file
  param processedTime - the last edit time of the processed file
  param config - the config settings

  Returns true if we want to run the rxgc step
  """

  # We can't do the RXGC step if false
  # TODO - do we want to inform the user?
  # if config["exportRXGC"] == False:
  #   return False

  # If the raw image exists and is newer than rxgcTime, we don't need to export
  if rawTime != None and rawTime > rxgcTime: 
    return False

  # If the processedImage exists and is newer than rxgcTime, we don't need to export
  # Catches case where the raw image got deleted
  if processedTime != None and processedTime > rxgcTime:
    return False

  return True

def __getRawStep__(rawTime, processedTime):
  """
  Determines if we need to process the raw image
  
  param rawTime - the last edit time of the raw image
  param processedTime - the last edit time of the processed image

  Returns true if we need to reprocess the image
  """
  # Prevents possible errors where the rxgc might not handle both
  # in case of no export rxgc
  if processedTime == None and rawTime == None:
    return False

  # If processed doesn't exist while raw time does, we need to process
  if rawTime != None and processedTime == None:
    return True

  # If processed exists and is older than raw time, reprocess
  if (
    processedTime != None and 
    rawTime != None and 
    rawTime > processedTime
  ):
    return True

  return False
  
def __processRXGCs__(characterList, config):
  for character in characterList:
    if character["profileStep"] == "rxgc":
      character["profileStep"] = "raw"
    if character["spriteStep"] == "rxgc":
      character["spriteStep"] = "raw"

  return characterList

def __processRXGC__(character, config):
  return

def __processRaws__(characterList, config):
  return

def __processRaw__(character, imageType, config):
  # Does image exist? 
  # Determine type of image

  return