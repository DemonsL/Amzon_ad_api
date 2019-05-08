# encoding: utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger


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
        sched.add_job(
            func=self.job,
            args=self.args,
            trigger=IntervalTrigger(
                start_date=self.timer,
                days=1
            ))
        sched.start()


