from PIL import Image
import numpy as np
import time
import sys

name = sys.argv[1]
resolution = int(sys.argv[2])
pal = sys.argv[3]

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

# Load hex codes from file
with open(f'palettes/{pal}.hex', 'r') as file:
    hex_data = file.read()

hex_codes = hex_data.strip().split('\n')
palette = [hex_to_rgb(hex_code) for hex_code in hex_codes]

def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in palette:
        cr, cg, cb = color
        color_diff = abs(cr - r) + abs(cg - g) + abs(cb - b)
        color_diffs.append(color_diff)
    return palette[np.argmin(color_diffs)]

def create_pixel_art(image_path, output_path, pixel_size):
    img = Image.open(image_path)
    img = img.resize(
        (img.size[0]//pixel_size, img.size[1]//pixel_size),
        Image.NEAREST
    )
    img = img.convert("RGB")

    img_array = np.array(img)
    shape = img_array.shape

    for i in range(shape[0]):
        for j in range(shape[1]):
            img_array[i][j] = closest_color(img_array[i][j])

    pixel_art_img = Image.fromarray(np.uint8(img_array), 'RGB')
    pixel_art_img = pixel_art_img.resize(
        (pixel_art_img.size[0]*pixel_size, pixel_art_img.size[1]*pixel_size),
        Image.NEAREST
    )

    pixel_art_img.save(output_path, format='PNG')


start = time.time()
create_pixel_art(f"{name}", f"outputs/{pal}-{resolution}-{name}.png", resolution)
print("rendered image (res: " + str(resolution) + ") in " + str(round(time.time() - start,2)) + " seconds")