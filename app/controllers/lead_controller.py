import email
from http import HTTPStatus
import http
from flask import jsonify, request
from app.configs.database import db
from sqlalchemy.orm.session import Session
from app.models.lead_model import LeadModel
from sqlalchemy.orm import Query
from psycopg2.errors import UniqueViolation, CheckViolation, NotNullViolation
from sqlalchemy.exc import IntegrityError
from datetime import datetime as dt

from app.services.exceptions.lead_exceptions import LeadEmailNotFound



def get_all_leads():

    base_query : Query = db.session.query(LeadModel)

    leads = base_query.all()


    return jsonify(leads), HTTPStatus.OK

def post_one_lead():

    session : Session = db.session

    req = request.get_json()

    try:
        lead = LeadModel(**req)
        session.add(lead)
        session.commit()
    except IntegrityError as err:
        if type(err.orig) == CheckViolation:
            return {"error": "phone in a wrong format"}, HTTPStatus.UNPROCESSABLE_ENTITY
        if type(err.orig) == UniqueViolation:
            return {"error" : str(err.orig)}, HTTPStatus.CONFLICT
        return {"error": "not null violation"}, HTTPStatus.BAD_REQUEST
    except TypeError:
        return {"error": "Wrong Keys"}, HTTPStatus.BAD_REQUEST

    return jsonify(lead), HTTPStatus.CREATED

def update_one_lead():

    req = request.get_json()

    session : Session = db.session

    try:
        base_query : Query = db.session.query(LeadModel)

        lead = base_query.filter_by(email=req["email"]).first()

        if not lead:
            raise LeadEmailNotFound

        setattr(lead,"visits",lead.visits + 1)
        setattr(lead,"last_visit",str(dt.now()))

        session.commit()
    except KeyError:
        return {"error": "You must pass the email"}, HTTPStatus.BAD_REQUEST
    except LeadEmailNotFound as err:
        return {"error": err.message}, err.status_code

    return jsonify(lead), HTTPStatus.OK

def delete_one():

    req = request.get_json()

    session : Session = db.session

    try:
        base_query : Query = db.session.query(LeadModel)

        lead = base_query.filter_by(email=req["email"]).first()

        if not lead:
            raise LeadEmailNotFound

        session.delete(lead)
        session.commit()
    except KeyError:
        return {"error": "You must pass the email"}, HTTPStatus.BAD_REQUEST
    except LeadEmailNotFound as err:
        return {"error": err.message}, err.status_code
    
    return "", HTTPStatus.NO_CONTENT


