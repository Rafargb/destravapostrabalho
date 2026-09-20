from PIL import Image

input_path = '/Users/apple/.gemini/antigravity/brain/39592a43-d40d-4ed6-aa98-e4346ea14f46/.user_uploaded/media_1789869843073.png'
output_path = 'bonus_mockup_alpha.png'

img = Image.open(input_path).convert("RGBA")
datas = img.getdata()

new_data = []
for item in datas:
    # Checkerboard is usually exactly 204,204,204 or 255,255,255
    # Or sometimes 254, 254, 254 etc.
    # Let's check for near-white and near-204
    is_white = item[0] > 250 and item[1] > 250 and item[2] > 250
    is_grey = 195 < item[0] < 215 and 195 < item[1] < 215 and 195 < item[2] < 215
    
    if is_white or is_grey:
        new_data.append((255, 255, 255, 0)) # transparent
    else:
        new_data.append(item)

img.putdata(new_data)
img.save(output_path, "PNG")
