# encoding: utf-8
import tornado.ioloop
from apscheduler.schedulers.tornado import TornadoScheduler
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
        sched = TornadoScheduler()
        for arg in self.args:
            sched.add_job(
                func=self.job,
                args=arg,
                trigger=IntervalTrigger(
                    start_date=self.timer,
                    days=1
                ))
        sched.start()

        try:
            tornado.ioloop.IOLoop.current().start()
        except (KeyboardInterrupt, SystemExit):
            sched.shutdown()


