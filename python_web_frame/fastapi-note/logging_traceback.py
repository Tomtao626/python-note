#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/26 11:24 上午
# @Author : admin
# @Software: PyCharm
# @File: logging_traceback.py

import logging
import traceback

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s-%(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')

logging.debug(u"调试")
logging.info(u"打印信息")
logging.warning(u"警告")
logging.error(u"错误")
logging.critical(u"致命错误")
