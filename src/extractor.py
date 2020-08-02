import os
import pygame

from src.helpers import confirm
from src.image import get_image_type, load_image

def _extract_image(image, extraction_type):
  """
  Extracts an image, if at all possible
  """
  extracted_image = None
  if extraction_type == "character":
    extracted_image = image.subsurface(48, 0, 48, 48)
  elif extraction_type == "face":
    extracted_image = image.subsurface(0, 0, 144, 144)
  
  if extracted_image == None:
    log.warning("Image failed to extract for type %s", extraction_type)
    extracted_image = image

  return extracted_image


def _get_extracted_filename(filename, game = "", image_type=""):
  """
  Builds the name for the extracted file from the original filename and image type
  """
  extracted_filename = filename.replace(".png", "")
  extracted_filename = extracted_filename.replace("_character", "")
  extracted_filename = extracted_filename.replace("_face", "")

  # Remove the game name to ensure it's not there
  if game != "" and game != None:
    extracted_filename = extracted_filename.replace("_" + game, "")
    extracted_filename += "_" + game 

  if image_type == "character":
    extraction_type = "sprite"
  elif image_type == "face":
    extraction_type = "profile"
  else:
    log.critical("An invalid image_type (%s) was given to _get_extracted_filename", image_type)
  
  extracted_filename += "_" + extraction_type + ".png"

  return extracted_filename


def handle_extraction(args):
  """
  Handles the full extraction process for all given images
  """
  resizing_files = []

  for filename in args.files:
    
    # Does exist
    image = load_image(filename)
    if image == None:
      continue

    # Get extraction type, continue if we can't extract
    image_type = get_image_type(image)
    if not (image_type == "face" or image_type == "character"):
      resizing_files.append(filename)
      continue

    # Get target filename
    extracted_filename = _get_extracted_filename(filename, args.game, image_type)
    resizing_files.append(extracted_filename)

    # Ensure we don't overwrite, unless we want to
    if (os.path.exists(extracted_filename)):
      if(args.confirm or confirm("Are you sure you want to overwrite " + extracted_filename)):
        pass    
      else:
        continue  

    # Extract and save
    extracted_image = _extract_image(image, image_type)
    pygame.image.save(extracted_image, extracted_filename)
  
  return resizing_files