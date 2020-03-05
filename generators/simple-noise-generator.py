import random
import json

model = {
  "metadata": {
    "name": "simple-noise-model",
    "noise_type": "noise"
  }
}

def write_model(grid_height, grid_width):
  grid = []

  for col in range(grid_height):
    for row in range(grid_width):
      cell = {
        "type": "structure1",
        "coords": [row, col],
        "rotation": [random.choice([0, 90]), random.choice([0, -90])] 
      }
      grid.append(cell)

  model["grid"] = grid

  f = open(model["metadata"]["name"]+".json", "w")
  f.write(json.dumps(model))
  f.close()