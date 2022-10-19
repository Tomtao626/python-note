import os
import logging
from loguru import logger
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# logger = logging.getLogger(__name__)


logger.add("log/{time:YYYY-MM-DD HH:mm:ss}.log", format="{time:YYYY-MM-DD at HH:mm:ss}{level}{message}",
           rotation="00:01", encoding='utf-8', enqueue=True)


def log_demo():
	logger.info('info')
	sum = 0
	for i in range(1000):
		sum += i
		print(sum)


log_demo()
