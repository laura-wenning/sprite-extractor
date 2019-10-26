from os import path
from pygame import image

fileTypes = ["rxgc", "face", "character", "profile", "sprite"]
rawImageTypes = ["face", "character"]
processedImageTypes = ["profile", "sprite"]

rawFolder = "raw/"
processedFolder = ""

class Character:
  """
  A character object for containing character information and running various 
  processes on the rxgc and images
  """
  __baseFilepath__ = ""
  __filename__ = ""

  # Status of each type of image
  __update__ = {
    "face":False,
    "character":False,
    "profile":False,
    "sprite":False,
  }

  # The last touched at time
  __lastEditedAt__ = {
    "rxgc":None,
    "face":None,
    "character":None,
    "profile":None,
    "sprite":None,
  }

  # All filepaths to the various files
  __filepaths__ = {
    "rxgc":"",
    "face":"",
    "character":"",
    "profile":"",
    "sprite":"",
  }

  # Messages to output to the user. 
  __messages__ = []
  
  def __init__(self, dirpath, filename):
    """
    Initializes the character class and all of the data therein

    param dirpath - the directory path of the file
    param filename - the filename of the rxgc file to build off of
    """
    self.__baseFilepath__ = dirpath
    self.__filename__ = filename

    self.__buildAllFilepaths__()
    self.__determineFileEditTimes__()
    self.__determineFileUpdates__()
    return

  def __buildAllFilepaths__(self):
    """
    Builds all filepaths for each target file
    """
    global rawImageTypes
    global processedImageTypes

    global rawFolder
    global processedFolder

    basePath = self.__baseFilepath__ + "/"

    # Builds the rxgc filepath
    self.__filepaths__["rxgc"] = basePath + self.__filename__ + ".rxgc"

    # Builds the raw image file paths
    for imageType in rawImageTypes:
      self.__filepaths__[imageType] = basePath + rawFolder + self.__filename__ + "_" + imageType + ".png"

    # Builds the processed image file paths
    for imageType in processedImageTypes:
      self.__filepaths__[imageType] = basePath + processedFolder + self.__filename__ + "_" + imageType + ".png"

  def __determineFileEditTimes__(self):
    """
    Determines the last edit times of each file
    """

    # Loops through each file type to determine if the file doesn't exist
    for fileType in self.__filepaths__.keys():
      # Checks that this file exists. Skip if it doesn't
      if not path.exists(self.__filepaths__[fileType]):
        continue
    
      self.__lastEditedAt__[fileType] = path.getmtime(self.__filepaths__[fileType])

  def __determineFileUpdates__(self):
    """
    Determines the file updates, if they need to be re-rendered or exported
    """

    global rawImageTypes
    global processedImageTypes

    # Processed
    for index in range(0, len(rawImageTypes)):
      rawType = rawImageTypes[index]
      processedType = processedImageTypes[index]

      # Create a new processed image if one doesn't exist
      if self.__lastEditedAt__[processedType] is None:
        self.__update__[processedType] = True

      # Create new raw and processed images if the rxgc is newer
      elif (
        self.__lastEditedAt__["rxgc"] is not None and 
        self.__lastEditedAt__["rxgc"] > self.__lastEditedAt__[processedType]
      ):
        self.__update__[rawType] = True
        self.__update__[processedType] = True

      # Create a new processed image if the raw image is newer
      elif (
        self.__lastEditedAt__[rawType] is not None and 
        self.__lastEditedAt__[rawType] > self.__lastEditedAt__[processedType]
      ):
        self.__update__[processedType] = True

      # Otherwise, we don't need to update the processed image
      else:
        self.__update__[processedType] = False

      # Create a new raw file if it doesn't exist
      if self.__lastEditedAt__[rawType] is None:
        self.__update__[rawType] = True

      # Create a new raw file if it is older than the RXGC
      elif (
        self.__lastEditedAt__["rxgc"] is not None and 
        self.__lastEditedAt__["rxgc"] > self.__lastEditedAt__[rawType]
      ):
        self.__update__[rawType] = True

      # Otherwise, we don't need to update the raw image
      else:
        self.__update__[rawType] = False

  def print(self):
    """
    A simple function for debugging purposes
    """
    print(self.__filename__)
    print(self.__update__)
    print(self.__filepaths__)

  def exportRawImages(self):
    """
    Exports raw images from the RXGC
    """
    global rawImageTypes

    for imageType in rawImageTypes:
      # Skips this if we don't need to update it
      if self.__update__[imageType] == False:
        continue

      self.exportRawImage(imageType)

    return

  def exportRawImage(self, imageType):
    """
    Exports a raw image
    """

    return

  def processImages(self):
    """
    Processes raw images and exports into processed images
    """
    global rawImageTypes
    global processedImageTypes

    for index in range(len(rawImageTypes)):
      rawType = rawImageTypes[index]
      processedType = processedImageTypes[index]

      # Skip if this doesn't need an update
      if self.__update__[processedType] == False:
        continue

      self.processImage(rawType, processedType)

    return

  def processImage(self, rawType, processedType):
    """
    Processes a single raw image into a single processed image. 
    It does not check if it needs to update

    param rawType - the raw type to process
    param processedType - the image type to be processed to

    Returns true on success, false otherwise
    """

    # grab file with pygame
    if path.exists(self.__filepaths__[rawType]) == False:
      self.__addMessage__("Image doesn't exist")
      return False
    
    rawImage = image.load(self.__filepaths__[rawType])

    # Yank image based on size
    processedImage = self.__yankImage__(rawImage)

    # Save file
    image.save(processedImage, self.__filepaths__[processedType])

    # Store message

    return True

  def __yankImage__(self, rawImage):
    """
    Yanks the processed image from the given raw image

    param rawImage - the raw image to process

    Returns a processed pygame image
    """
    size = rawImage.get_size()

    if size[0] == 576 and size[1] == 384:
    	return rawImage.subsurface(48, 0, 48, 48)
    elif size[0] == 576 and size[1] == 288:
    	return rawImage.subsurface(0, 0, 144, 144)
    return rawImage

      



