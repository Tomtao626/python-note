# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    FileName: beat_task
    Github: https://github.com/Tomtao626/python-note
    Author: tp320670258@gmail.com
    Description: $
    CreateDate: 2023-04-22 00:02
    Project: python-note
    IDE: PyCharm
"""
import time
from apps import app


@app.task()
def beat_test():
	time.sleep(4)
	return "hello celery beat"
