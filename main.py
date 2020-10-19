from PIL import Image
from PIL import ImageFilter

baby = Image.open('baby.jpeg')

edge = baby.filter(ImageFilter.EDGE_ENHANCE)

edge.show()