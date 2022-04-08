from flask import Blueprint, Flask
from app.routes.lead_route import bp as bp_leads

bp_api = Blueprint("api",__name__)

def init_app(app: Flask):

    bp_api.register_blueprint(bp_leads)

    app.register_blueprint(bp_api)