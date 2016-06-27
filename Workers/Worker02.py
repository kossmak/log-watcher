#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

from . import WorkerBase


class Worker02(WorkerBase):
    # def __init__(self, info, log_queue, *args, **kw):
    #     super(Worker02, self).__init__(info, log_queue, *args, **kw)
    #     pass  # пустое переопределение конструктора можно опустить

    def run(self):
        self.send_message("begin")
        for i in range(3):
            time.sleep(2 * random.random())
            self.send_message("message #%d" % i)
        self.send_message("end")
