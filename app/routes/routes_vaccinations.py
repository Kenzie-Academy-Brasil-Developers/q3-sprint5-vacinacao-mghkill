
from flask import Blueprint
from app.controllers import controllers_vaccinations

bp = Blueprint("vaccinations", __name__, url_prefix="/vaccinations")


bp.post("")(controllers_vaccinations.create_vaccine)
bp.get("")(controllers_vaccinations.get_all_vaccine)