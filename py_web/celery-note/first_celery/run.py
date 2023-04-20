# coding=utf-8
import time

from task import hello, add_task
from apps import task1, task2

if __name__ == '__main__':
    # hello.delay("tomtao626")
    # add_task.delay(22, 44)
    # hello("zhaosi")
    # task1.add.delay(9, 5)
    task2.sub.delay(9, 3)
    task1.add.apply_async(
        args=[1, 2],
        kwargs={'name': 'tomtao626'},
        task_id='1dewr34rewfewf4543dsfds',
        # countdown=7,
        # eta=time.time() + 10
        expreis=5,
        retry=True,
        shadow='tomtao-task'
    )
