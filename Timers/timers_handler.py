# encoding: utf-8
from apscheduler.schedulers.blocking import BlockingScheduler


class TimersHandler:
    """
    定时器
    """

    def __init__(self, timer, job, args):
        self.timer = timer
        self.job = job
        self.args = args

    def excute_job(self):
        sched = BlockingScheduler()
        for arg in self.args:
            sched.add_job(self.job, 'interval', days=1, start_date=self.timer, args=arg)
        sched.start()


