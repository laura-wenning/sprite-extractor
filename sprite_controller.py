#! /usr/bin/python3
import argparse
import logging
import os
import pygame # Used for extracting the sprite easily with built-in surfaces 
import sys

from src.extractor import handle_extraction
from src.image import get_image_type
from src.shrink import can_shrink, handle_shrink

log = logging.getLogger(__name__)

def handle_args(args):
  # Default action if no other args are given is to extract so drag/drop still works 
  if (can_shrink(args) == False and args.extract == False):
    args.extract = True

  if args.game != None:
    args.game = args.game[0]

  if args.extract == True:
    args.files = handle_extraction(args)

  handle_shrink(args)

def main():
  parser = argparse.ArgumentParser(description="Extracts and optionally resizes sprites for D&D")
  parser.add_argument("files", metavar="file", nargs="+", help="the file or files to parse")
  parser.add_argument(
    "--extract", 
    "-e", 
    action="store_true", 
    help="Extract the sprite or profile from the given files"
  )
  parser.add_argument(
    "--dwarf", 
    "-d",
    action="store_true",
    help="pads a sprite to resize to a dwarf--slightly shorter but wider"
  )
  parser.add_argument(
    "--small",
    "-s",
    action="store_true",
    help="pads a sprite to resize to a proportionally smaller character"
  )
  parser.add_argument(
    "--tiny",
    "-t",
    action="store_true",
    help="pads a sprite to resize to a proprotionally tiny character"
  )
  parser.add_argument(
    "--reset-size",
    "-r",
    action="store_true",
    help="removes additional padding and ensures the sprite is non-destructively back at normal size"
  )
  parser.add_argument(
    "--game",
    "-g",
    metavar="game",
    nargs=1,
    help="sets the current game these sprites belong to. Recommended but not required"
  )
  parser.add_argument(
    "-y",
    dest="confirm",
    action="store_true",
    help="forces automatic confirmation"
  )
  parser.add_argument(
    "-n",
    dest="preserve",
    action="store_true",
    help="prevents any overwriting extracted images"
  )
  args = parser.parse_args()
  handle_args(args)
  

if __name__ == "__main__":
  main()