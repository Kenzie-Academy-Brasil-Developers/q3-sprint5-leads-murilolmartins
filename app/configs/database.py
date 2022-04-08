from flask import Flask

from environs import Env
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()




def init__app(app: Flask):

    
    env = Env()
    env.read_env()
    app.config["SQLALCHEMY_DATABASE_URI"] = env("DATABASE")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.db = db

    from app.models.lead_model import LeadModel


