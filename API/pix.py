from io import BytesIO
from PIL import Image
import numpy as np
import base64
    
def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def loadPalettes(pal):
    with open(f'API/palettes/{pal}', 'r') as file:
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
def create_pixel_art(b64_image, pixel_size, _palette):
    pixel_size = int(pixel_size)
    # Decode the Base64 string into an image
    try:
        base64_decoded = base64.b64decode(b64_image.split(',')[1])  # Remove the 'data:image' prefix
    except IndexError:  # Handle cases where the string might not be in 'data:image' format
        base64_decoded = base64.b64decode(b64_image)

    img = Image.open(BytesIO(base64_decoded))
    
    # Your existing logic to perform pixel art creation
    palette = loadPalettes(_palette)
    img = img.resize(
        (img.size[0] // pixel_size, img.size[1] // pixel_size),
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
        (pixel_art_img.size[0] * pixel_size, pixel_art_img.size[1] * pixel_size),
        Image.NEAREST
    )

    output_buffer = BytesIO()
    pixel_art_img.save(output_buffer, format='PNG')
    output_base64 = base64.b64encode(output_buffer.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{output_base64}"
