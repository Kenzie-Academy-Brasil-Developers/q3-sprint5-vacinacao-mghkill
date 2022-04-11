from flask import Blueprint, Flask
from app.routes.routes_vaccinations import bp as bp_vaccinations

def init_app(app: Flask):
    app.register_blueprint(bp_vaccinations)