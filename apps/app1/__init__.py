from flask import Blueprint

app1_bp = Blueprint('my_bp', __name__, url_prefix='/my_bp')


# 注意这里很重要
from . import views
