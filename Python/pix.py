from PIL import Image
import numpy as np
import time
import sys
import os

def populate_dropdown_from_folder(dropdown_var, dropdown_menu):
    # Get list of all files and folders in the specified directory
    folder_content = os.listdir("./palettes")
    
    # Update the dropdown options
    dropdown_menu['menu'].delete(0, 'end')
    for item in folder_content:
        dropdown_menu['menu'].add_command(label=item, command=lambda value=item: dropdown_var.set(value))

def check_output_folder():
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    
def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def loadPalettes(pal):
    with open(f'palettes/{pal}', 'r') as file:
        hex_data = file.read()
    hex_codes = hex_data.strip().split('\n')
    return [hex_to_rgb(hex_code) for hex_code in hex_codes]

# Find closest color
def closest_color(rgb, palette):
    r, g, b = rgb
    color_diffs = []
    for color in palette:
        cr, cg, cb = color
        color_diff = abs(cr - r) + abs(cg - g) + abs(cb - b)
        color_diffs.append(color_diff)
    return palette[np.argmin(color_diffs)]

# Resize image
def create_pixel_art(image_path, output_path, pixel_size, _palette):
    palette = loadPalettes(_palette)
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
            img_array[i][j] = closest_color(img_array[i][j], palette)

    pixel_art_img = Image.fromarray(np.uint8(img_array), 'RGB')
    pixel_art_img = pixel_art_img.resize(
        (pixel_art_img.size[0]*pixel_size, pixel_art_img.size[1]*pixel_size),
        Image.NEAREST
    )

    pixel_art_img.save(output_path, format='PNG')
