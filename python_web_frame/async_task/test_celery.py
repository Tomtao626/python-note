import asyncio
from celery import Celery, shared_task
from datetime import datetime, timedelta
from redisbeat.scheduler import RedisScheduler

app = Celery("tornado")

app.conf["imports"] = ["celery_task"]

# 定义broker
app.conf.broker_url = "redis://localhost:6379"

# 任务结果
app.conf.result_backend = "redis://localhost:6379"

# 需要执行任务的配置
app.conf.beat_schedule = {
    "task1": {
        "task": "celery_task.async_consume",  # 执行的方法
        "schedule": timedelta(seconds=3),
        "args": ()
    },
}


async def consume():
    return 'test'


@shared_task
def async_job():
    return asyncio.run(consume())


@app.task
def sub():

    return "test"


schduler = RedisScheduler(app=app)
schduler.add(**{
        'name': 'job1',
        'task': 'test_celery.sub',
        'schedule': timedelta(seconds=3),
        'args': ()
})