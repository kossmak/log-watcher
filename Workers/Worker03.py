from WorkerBase import WorkerBase
import time
import random

class Worker03(WorkerBase):
    def __init__(self, info, log_queue):
        WorkerBase.__init__(self, info, log_queue)

    def run(self):
        for i in xrange(3):
            self.send_message("message num ")