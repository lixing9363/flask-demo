from flask import Blueprint

app1_bp = Blueprint('my_bp', __name__, url_prefix='/my_bp')
from apps.response_helper import WebResult
from datas.models import User
from log import logger


@app1_bp.route('/my_route')
def my_route_view():
    users = User.query.all()
    user_data = [user.to_dict() for user in users]
    logger.info(f"my_route_view")
    return WebResult.list(len(user_data), user_data)
