# cube([2,6,2]);
# translate([10,0,0]) cube([2,6,2]);
import json
import replit


STRUCT_HEIGHT = 2
STRUCT_WIDTH = 6
STRUCT_DEPTH = 2
def structure1():
  return 'cube([{0},{1},{2}])'.format(STRUCT_HEIGHT, STRUCT_WIDTH, STRUCT_DEPTH)

struct_map = {
  'structure1': structure1
}

CELL_WIDTH = 10
CELL_HEIGHT = 10
def translate(coords):
  (x, y) = coords
  cell_x = CELL_WIDTH * x
  cell_y = CELL_HEIGHT * y
  return 'translate([{0},{1}])'.format(cell_x, cell_y)
def rotate(rotation_coords):
  (x, y) = rotation_coords
  return 'rotate([{0},{1}])'.format(x, y)



def load_model(model_name):
  f = open(model_name,"r") 
  model = json.loads(f.read())
  
  f.close()
  return model

def generate_output(model):
  output = ''
  for cell in model['grid']:
    rotation_coords = cell['rotation']
    
    rotation = rotate(rotation_coords)
    coords = cell['coords']
    translation = translate(coords)
    struct_fn = struct_map[cell['type']]
    struct = struct_fn() 
    output += '{0} {1} {2};'.format(translation, rotation, struct)
  return output

def write_output_file(model_name):
  model = load_model(model_name)
  generated_output = generate_output(model)
  replit.clear()
  print(generated_output)
  f = open(model["metadata"]["name"]+".scad", "w+")
  f.write(generated_output)
  f.close()