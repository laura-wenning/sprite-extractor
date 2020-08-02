import logging
import os
import pygame

log = logging.getLogger(__name__)

def get_image_type(image):
  """
  Takes a pygame image and uses the size to determine which image type it is. 
  Returns unknown if it is not sure
  """
  size = image.get_size()

  if (size[0] == 576 and size[1] == 384):
    return "character"

  elif (size[0] == 576 and size[1] == 288):
    return "face"

  elif (size[0] == 144 and size[1] == 144):
    return "profile"

  elif (size[0] == 48 and size[1] == 48):
    return "sprite"

  return "unknown"

def load_image(filename):
  """
  Loads an image via pygame. Logs an error if the file does not exist and returns none.
  """
  if (not os.path.exists(filename)):
    log.warning("%s does not exist", filename)
    return None
  return pygame.image.load(filename)