from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/list_palettes')
def list_palettes():
    folder_path = 'API/palettes/'
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return jsonify(files)

if __name__ == '__main__':
    app.run()
