from utils import Redis
from flask import Blueprint

bp = Blueprint("test_redis", __name__, url_prefix="/")


@bp.route('/testRedisWrite', methods=['GET'])
def test_redis_write():
    """
    测试redis
    """
    Redis.write("test_key", "test_value", 60)
    return "ok"


@bp.route('/testRedisRead', methods=['GET'])
def test_redis_read():
    """
    测试redis
    """
    data = Redis.read("test_key")
    return data
