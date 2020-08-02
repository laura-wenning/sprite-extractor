import logging
import os
import pygame

from src.helpers import confirm_overwrite
from src.image import get_image_type, load_image

log = logging.getLogger(__name__)

def _get_shrunk_filename(filename, args):
  """
  Determines the filename of the shrunken image
  """
  shrunk_filename = filename.replace(".png", "")

  if (args.tiny):
    shrunk_filename += "_tiny"
  
  if (args.small):
    shrunk_filename += "_small"

  if (args.dwarf):
    shrunk_filename += "_dwarf"

  shrunk_filename += ".png"
  return shrunk_filename

def _get_target_position(target_size):
  """
  Determines the position of the icon in the larger empty space
  """
  x = 0
  y = 0
  x = (target_size[0] - 48) / 2
  y = target_size[1] - 48

  return (x, y)

def _get_target_size(args):
  """
  Determines the size of the new area given the arguments
  """
  x = 48
  y = 48
  if args.dwarf:
    y += 12

  if args.small:
    y += 12
    x += 12

  if args.tiny:
    y += 24
    x += 24

  return (x, y)

def _resize_image(image, target_size, target_position):
  """
  Creates a resized image by creating a new empty surface and blitting the sprite inside
  """
  resized_image = pygame.Surface(target_size, pygame.SRCALPHA)
  resized_image.blit(image, target_position)
  return resized_image

def can_shrink(args):
  """
  Returns true if any shrink args are true and we can shrink
  """
  return args.dwarf or args.small or args.tiny

def handle_shrink(args):
  """
  Handles shrinking all given images to the given size
  """
  # Checks that we will shrink
  if (not can_shrink(args)):
    return

  target_size = _get_target_size(args)
  target_position = _get_target_position(target_size)

  # For each file
  for filename in args.files:
    # Load in 
    image = load_image(filename)
    if image == None:
      continue

    # Check type
    image_type = get_image_type(image)
    if image_type != "sprite":
      continue

    shrunk_filename = _get_shrunk_filename(filename, args)
    if (confirm_overwrite(shrunk_filename, args.confirm, args.preserve) == False):
      continue

    # Extract and save
    resized_image = _resize_image(image, target_size, target_position)
    pygame.image.save(resized_image, shrunk_filename)

