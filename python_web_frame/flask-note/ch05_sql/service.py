from base import Service
from model import *


class ArticleAPI(Service):
    """
    文章单表接口
    """
    __model__ = Article
    service_name = 'article'
