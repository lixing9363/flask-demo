from apps.app1 import app1_bp
from apps.response_helper import WebResult
from datas.models import User
from log import logger


@app1_bp.route('/my_route')
def my_route_view():
    users = User.query.all()
    user_data = [user.to_dict() for user in users]
    logger.info(user_data)
    return WebResult.list(len(user_data), user_data)
