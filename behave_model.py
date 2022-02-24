import threading
import behave
from behave import __main__


class BehaveModel(threading.Thread):
    @classmethod
    def set_thread_limiter(cls, limit):
        cls.thread_limiter = threading.BoundedSemaphore(int(limit))

    def __init__(self, cmd):
        super(BehaveModel, self).__init__()
        self.cmd = cmd

    def run(self):
        self.thread_limiter.acquire()
        try:
            self.thread_code()
        finally:
            self.thread_limiter.release()

    def thread_code(self):
        print('starting..!!')
        print(self.cmd)
        try:
            behave_t = behave.__main__
            self.status = behave_t.main(self.cmd)
            print(self.status)
        except Exception as e:
            self.status = 1
