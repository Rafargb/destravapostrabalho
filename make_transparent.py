from PIL import Image
import numpy as np

# Load the image
img = Image.open('hero_antes_depois.jpg').convert("RGBA")
data = np.array(img)

# Find the background color (e.g. top-left pixel or just light pixels)
# Let's make all pixels that are very close to white/light-grey transparent.
# The AI image probably has a gradient.
# Actually, the best way without AI is to just use the image's own background color and feather it.
# But wait, a simple floodfill or color replacement looks jagged.
