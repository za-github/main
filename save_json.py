import world
import json
def save_to_json(filename, world):
  with open(filename, 'w') as f:
    json.dump(world.serialize(),f)

def read_from_json():
  return 0