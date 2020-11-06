from src.media_gallery_manager import fetch_medias
from flask import Flask
import connexion
from flask_cors import CORS

def create_app():
    media_dirpath = input('Enter the path to your media directory (Example : D:\dirs\media) :')
    new_medias_count = fetch_medias(media_dirpath)
    print(str(new_medias_count) + ' new medias found.')
    # Create flask application instance
    connex_app = connexion.App(__name__, specification_dir='../openapi/')

    # Read specification.yml to configure the endpoints
    connex_app.add_api('specifications.yml')
    
    app = connex_app.app
    
    app.config['CORS_HEADERS'] = 'Content-Type'
    cors = CORS(app, resources={r"/medias": {"origins": "*"}})
    
    return app