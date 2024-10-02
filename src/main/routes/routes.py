from flask import Blueprint, request, jsonify

# import adapters
from src.main.adapters.request_adapter import request_adapter
# import composers
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer

user_routes_bp = Blueprint("user_routes", __name__)

@user_routes_bp.route("/user/find", methods=["GET"])
def user_find():
    http_response = request_adapter(request, user_finder_composer())
    return jsonify(http_response.body),http_response.status_code


@user_routes_bp.route("/user/register", methods=["POST"])
def user_register():
    http_response = request_adapter(request, user_register_composer())
    return jsonify(http_response.body),http_response.status_code
