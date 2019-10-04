import yaml

def readConfig():
  """
  Reads in the configuration yaml file
  Returns a dict with the configuration data
  # TODO - include default configuration information
  """
  config = {}

  with open("./config.yaml", "r") as stream:
    try:
      config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)

  return config

def readHistory():
  """
  Reads in the previously accessed history
  Returns a dict containing the files and their last accessed dates
  """
  history = {}

  with open("./.history", "r") as stream:
    try:
      history = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)

  return history

def writeHistory(history):
  """
  Writes the given history to a yaml file
  """
  with open("./.history", "w") as ostream:
    try:
      yaml.dump(history, ostream)
    except yaml.YAMLError as exc:
      print(exc)
    