from os import walk

def run(history, config):
  # Read all folders from the config
  folderList = __readFolders__(config)

  return history

def __readFolders__(config):
  characters = {}
  # file: {lastTouched: [timestamp], processType: [raw, img, none]}
  if config["readFolders"] == None:
    return characters

  for folder in config["readFolders"]:
    for (dirpath, dirnames, filenames) in walk(folder):
      if __isCharacterFolder__(filenames) == False:
        continue

      # Extract target filename
      baseFilename = __getCharacterFilename__(filenames)
      
      # Find which of the files is newest

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