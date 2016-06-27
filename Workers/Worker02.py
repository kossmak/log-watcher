from WorkerBase import WorkerBase
import time
import random

class Worker02(WorkerBase):
    def __init__(self, info, log_queue):
        WorkerBase.__init__(self, info, log_queue)

    def run(self):
        self.send_message("begin")
        for i in range(3):
            time.sleep(2 * random.random())
            self.send_message("message #%d" % i)
        self.send_message("end")