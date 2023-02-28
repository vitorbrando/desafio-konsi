from flask import Flask
import connexion

def create_app():
    app = connexion.App(__name__, specification_dir="./")
    app.add_api("swagger.yml")
    return app