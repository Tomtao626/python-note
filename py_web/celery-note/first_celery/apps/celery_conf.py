BROKER_URL = "redis://localhost:6379/1"
CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
CELERY_IMPORTS = (
    'apps.task1',
    'apps.task2',
    'apps.beat_task',
)
# 设置时区
CELERY_TIMEZONE = "Asia/Shanghai"
# 是否使用本地的时区
CELERY_ENABLE_UTC = False
# 重写task属性
CELERY_TASK_ANNOTATIONS = {'apps.task1.add': {'rate_limit': '10/s'}}
# 链接错误是否重试发布任务消息 默认为True
CELERY_TASK_PUBLISH_RETRY = False
# 并发的worker数量
CELERY_CONCURRENCY = 4
# 每次worker去任务队列中取的任务数量
CELERY_PREFETH_MULTIPLIRE = 5
# 每个worker执行多少次就会被删除
CELERY_MAX_TASKS_PER_CHILD = 4
# 单个任务的最大执行时间
CELERY_TASK_TIME_LIMIT = 60
# celery任务执行结果的超时时间
CELERY_TASK_RESULT_EXPIRES = 1200