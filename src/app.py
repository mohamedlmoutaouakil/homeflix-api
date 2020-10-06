from flask import Flask
import connexion

def create_app():
    # Create flask application instance
    connex_app = connexion.App(__name__, specification_dir='../openapi/')

    # Read specification.yml to configure the endpoints
    connex_app.add_api('specifications.yml')
    
    app = connex_app.app
    return app