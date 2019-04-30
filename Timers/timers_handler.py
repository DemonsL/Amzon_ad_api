# encoding: utf-8
import datetime

class TimersHandler:

    def __init__(self, timer, client, method, params):
        self.timer = timer
        self.client = client
        self.method = method
        self.params = params

    def set_timer(self):
        flag = 0
        while True:
            now = datetime.datetime.now()
            now = now.strftime('%Y-%m-%d %H:%M')
            if now == self.timer:
                print('Starting...')
                self.method(self.client, self.params)
                print('Successful!')
                flag = 1
            else:
                if flag == 1:
                    self.timer = datetime.datetime.strptime(self.timer, '%Y-%m-%d %H:%M')
                    self.timer += datetime.timedelta(hours=8)
                    flag = 0