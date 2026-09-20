from PIL import Image
import numpy as np

img = Image.open('hero_antes_depois.jpg').convert("RGBA")
data = np.array(img)

# The background is a blurry office (light greys, greens). 
# A simple threshold won't work well because the man's shirt is also light blue/grey.
