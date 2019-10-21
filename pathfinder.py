from PIL import Image

# image = Image.new('RGBA', (600, 600), 'black')

# image.show()

# draw = ImageDraw.Draw(image)

with open('elevation_small.txt', 'r') as file:
  content = file.read().split()
  integer_list = [int(i) for i in content]

min_elevation = 3139
max_elevation = 5648

class Map:
  def __init__(self, integer_list):
    self.integer_list = integer_list
    self.min_elevation = min(self.integer_list)
    self.max_elevation = max(self.integer_list)
    

  def read_file(self):
    with open('elevation_small.txt', 'r') as file:
      content = file.read().split()
      integer_list = [int(i) for i in content]
      # print(integer_list)

  
  def make_brightness(self, elevation):
    brightness = (elevation - self.min_elevation) / (self.max_elevation - self.min_elevation)
    color = int(brightness * 255)
    return (255, 255, 255, brightness) 
    print(map.make_brightness)

  def create_brightness_list(self):
    brightness_list = []
    for elevation in content:
      pixel = self.make_brightness(elevation)
      self.brightness_list.append(pixel)

# my_data = content

my_map = Map(integer_list)

my_map.create_brightness_list()

# my_map.read_file()




  

  


