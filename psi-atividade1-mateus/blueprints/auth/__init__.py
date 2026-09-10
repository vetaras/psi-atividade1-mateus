from flask import Blueprint
import routes

auth_bp = Blueprint("auth", __name__, template_folder="templates")