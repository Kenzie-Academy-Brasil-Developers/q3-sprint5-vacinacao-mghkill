from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from flask import jsonify, request
from app.configs.database import db
from app.controllers import change_data
from app.models.models_vaccinations import Vaccine
from datetime import datetime as dt, timedelta as dd
from sqlalchemy.orm.session import Session



def create_vaccine():
    
    data = request.get_json()
    if len(data) < 4:
        return {"Error": "Incorrect keys"}, HTTPStatus.BAD_REQUEST

    output_data = change_data(data)
      
    try:
        if len(output_data["cpf"]) != 11:
           return {"Error": "CPF incorrect"}, HTTPStatus.BAD_REQUEST

        vaccine_value = Vaccine(**output_data)

        vaccine_value.__dict__["first_shot_date"] = dt.now()
        vaccine_value.__dict__["second_shot_date"] = dt.now() + dd(90)

        session: Session = db.session

        session.add(vaccine_value)
        session.commit()

        return jsonify(vaccine_value), HTTPStatus.CREATED

    except IntegrityError:
        return {"Error": "User already exists"}, HTTPStatus.CONFLICT
        
    except TypeError:
        return {"Error": "Incorrect keys"}, HTTPStatus.CONFLICT
        
        
        
def get_all_vaccine():
    session: Session = db.session
    
    output_vaccine: Vaccine = session.query(Vaccine).all()

    print(output_vaccine)

    return jsonify(output_vaccine), HTTPStatus.OK