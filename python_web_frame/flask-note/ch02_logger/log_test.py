import logging
import logging.config
from flask import Flask, current_app

"""
# log level
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# log to file
file_log = logging.FileHandler(filename="test.log", mode='w', encoding="utf-8")
logger.addHandler(file_log)

# log format
formatter = logging.Formatter("%(asctime)s-%(message)s")  # time/msg
file_log.setFormatter(formatter)

# use logging
logger.info("info")
logger.debug("debug")
logger.error("error")
logger.warning("warning")
logger.critical("critical")
"""
# read log conf
logger_conf = {
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
}


def create_app():
    app = Flask(__name__)
    # 1.set logger
    # write log to file
    handler = logging.FileHandler(filename="test.log", mode="w", encoding="utf-8")
    # set level
    handler.setLevel("DEBUG")
    # formatter
    format_ = "%(asctime)s[%(name)s][%(levelname)s] :%(levelno)s: %(message)s"
    formatter = logging.Formatter(format_)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    # 2.read conf_file
    # logging.config.dictConfig(logger_conf)
    return app


app = create_app()


@app.route("/", methods=["GET"])
def test_app():
    current_app.logger.info("info")
    current_app.logger.debug("info")
    current_app.logger.error("info")
    current_app.logger.warning("info")
    current_app.logger.critical("info")
    return "ok"


if __name__ == "__main__":
    app.run()
