from flask import Flask, jsonify, request
from pix import create_pixel_art
from flask_cors import CORS
from PIL import Image
import os

app = Flask(__name__)
CORS(app)  

@app.route('/list_palettes')
def list_palettes():
    folder_path = 'API/palettes/'
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return jsonify(files)

@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.json
    base64_image = data.get('image').split(',')[1]  # Remove the 'data:image' prefix
    resolution = data.get('resolution')
    colorPalette = data.get('selectedItem')
    image = create_pixel_art(base64_image, resolution, colorPalette)
    return jsonify({'image': image})

if __name__ == '__main__':
    app.run()
