import os

def confirm(confirmation_message):
  """
  Prints a confirmation message to the user
  """
  while True:
    confirmation = input(confirmation_message + " ([y/N]): ")
    confirmation = confirmation.lower()

    if confirmation == "y":
      return True
    elif confirmation == "n":
      return False
    else:
      print("'%s' is an invalid input.", confirmation_message)

def confirm_overwrite(target_filename, confirm, preserve):
  """
  Asks a standard confirmation for overwriting pre-existing files.
  This confirm may be overwritten with the preserve or confirm flags
  """
  if (os.path.exists(target_filename)):
    if (preserve == True): 
      return False

    if(confirm or confirm("Are you sure you want to overwrite " + target_filename)):
      return True
    else:
      return False
  return True

  