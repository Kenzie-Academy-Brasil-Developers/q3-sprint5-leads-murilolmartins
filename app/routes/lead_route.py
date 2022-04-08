from flask import Blueprint
from app.controllers import lead_controller

bp = Blueprint("leads",__name__,url_prefix="/leads")


bp.get("")(lead_controller.get_all_leads)
bp.post("")(lead_controller.post_one_lead)
bp.patch("")(lead_controller.update_one_lead)
bp.delete("")(lead_controller.delete_one)