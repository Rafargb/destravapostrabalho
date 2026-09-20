from PIL import Image
import numpy as np

# Load image
img = Image.open('/Users/apple/.gemini/antigravity/brain/39592a43-d40d-4ed6-aa98-e4346ea14f46/.user_uploaded/media_1789869843073.png')
img = img.convert("RGBA")
data = np.array(img)

# The checkerboard is likely made of two specific colors.
# Let's just find the colors of the top-left pixels
# top-left corner is usually part of the background.
r, g, b, a = data.T

# We can find the unique colors in the first row
# But simpler: it's a grid of 16x16 or similar.
# Let's just replace exact gray and white from the background with transparent.
# Typical checkerboard gray is #cccccc (204,204,204) and white (255,255,255).
# Let's find the exact colors at (0,0) and (16,0).

# Instead of exact color match, which might fail due to compression artifacts, 
# let's use a flood fill algorithm from the corners.
from skimage.segmentation import flood_fill

# Oops, skimage might not be installed. Let's use pure PIL/numpy.
# Or just install rembg using bypass sandbox?
