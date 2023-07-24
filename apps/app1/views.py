from flask import Blueprint
from flask import current_app as app
from apps.response_helper import WebResult
from datas.models import User

app1_bp = Blueprint('my_bp', __name__, url_prefix='/my_bp')

@app1_bp.route('/my_route')
def my_route_view():
    # users = User.query.all()
    users = User.query.filter_by(username='aaa').all()
    user_data = [user.to_dict() for user in users]
    app.logger.info(f"my_route_view")
    return WebResult.list(len(user_data), user_data)
