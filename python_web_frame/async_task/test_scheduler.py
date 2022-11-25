from datetime import datetime
from tornado.ioloop import IOLoop, PeriodicCallback
from tornado.web import RequestHandler, Application, url
from apscheduler.schedulers.tornado import TornadoScheduler
from apscheduler.jobstores.redis import RedisJobStore


async def task():
	print('[APScheduler][Task]-{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))


# init
scheduler = None


# 初始化
def init_scheduler():
	global scheduler
	jobstores = {
		'default': RedisJobStore(jobs_key='cron.jobs', run_times_key='cron.runtimes', host='localhost', port=6379)
	}
	scheduler = TornadoScheduler(jobstores=jobstores)
	scheduler.start()
	scheduler.add_job(task, "interval", seconds=3, id="job1", args=())
	print("定时任务启动")


class SchedulerHandler(RequestHandler):
	def get(self, job_ids=None):
		job_id = self.get_query_argument('job_id', None)
		action = self.get_query_argument('action', None)
		if job_id:
			# 添加任务
			if 'add' == action:
				if job_id not in job_ids:
					job_ids.append(job_id)
					scheduler.add_job(task, 'interval', seconds=3, id=job_id, args=(job_id,))
					self.write('[TASK ADDED] - {}'.format(job_id))
				else:
					self.write('[TASK EXISTS] - {}'.format(job_id))
			# 删除任务
			elif 'remove' == action:
				if job_id in job_ids:
					scheduler.remove_job(job_id)
					self.write('[TASK REMOVED] - {}'.format(job_id))
				else:
					self.write('[TASK NOT FOUND] - {}'.format(job_id))
		else:
			self.write('[INVALID PARAMS] INVALID job_id or action')


if __name__ == '__main__':
	routes = [url(r"/scheduler/", SchedulerHandler)]

	init_scheduler()

	# 声明tornado对象
	application = Application(routes, debug=True)
	application.listen(8888)
	IOLoop.current().start()
