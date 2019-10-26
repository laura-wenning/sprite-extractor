def buildFilepath(character: dict, fileType: str):
  """
  Builds the standard filepath for a given character and filetype

  param character - character information
  param fileType - the type of file we're building a filepath for

  Returns a filepath as a string
  """
  path = character["dirpath"] + "/"

  if fileType == "rxgc":
    path += character["baseFilename"] + ".rxgc"
  elif fileType == "face":
    path += "raw/" + character["baseFilename"] +  "_face.png"
  elif fileType == "character":
    path += "raw/" + character["baseFilename"] + "_character.png"
  elif fileType == "profile":
    path += character["baseFilename"] + "_profile.png"
  elif fileType == "sprite":
    path += character["baseFilename"] + "_sprite.png"

  return path

